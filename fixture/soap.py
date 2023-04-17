# Name : soap.py
# Author : "Denisov Dmitry"
# Time : 13.04.2023
from suds.client import Client
from suds import WebFault
from model.project import Project
import xmltodict


class SoapHelper:
    def __init__(self, app):
        self.app = app
    def client_url(self):
        return Client(self.app.config["web"]["baseUrl"] + "/api/soap/mantisconnect.php?wsdl", retxml=True)
    def can_login(self, username, password):
        client = self.client_url()
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        username = self.app.config["webadmin"]["username"]
        password = self.app.config["webadmin"]["password"]
        client = self.client_url()
        proj_list = []
        try:
            raw = client.service.mc_projects_get_user_accessible(username, password)
            parsed = xmltodict.parse(raw, xml_attribs=False)
            count = self.count_item_return(parsed)
            if count is None:
                return None
            else:
                proj_list = self.read_project_list(parsed)
            return proj_list
        except WebFault:
            return proj_list

    def read_project_list(self, parsed):
        project_list = []
        data = []
        t_parse = parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body']['ns1:mc_projects_get_user_accessibleResponse']['return'][
            'item']
        if type(t_parse) == dict:
            project = Project(id=parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body'][
                'ns1:mc_projects_get_user_accessibleResponse']['return']['item']['id'],
                              name=parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body'][
                                  'ns1:mc_projects_get_user_accessibleResponse']['return']['item']['name'])
            project_list.append(project)
            return project_list
        else:
            data = [dict(d) for d in
                    parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body']['ns1:mc_projects_get_user_accessibleResponse'][
                        'return']['item']]
            count = len(data)
            i = 0
            while i < count:
                project = Project(id=data[i]["id"], name=data[i]["name"])
                project_list.append(project)
                i += 1
            return project_list

    def count_item_return(self, data):
        if data['SOAP-ENV:Envelope']['SOAP-ENV:Body']['ns1:mc_projects_get_user_accessibleResponse']['return'] is None:
            return None
        else:
            return len(
                data['SOAP-ENV:Envelope']['SOAP-ENV:Body']['ns1:mc_projects_get_user_accessibleResponse']['return'])
