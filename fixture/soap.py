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

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        username = self.app.config["webadmin"]["username"]
        password = self.app.config["webadmin"]["password"]
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl", retxml=True)
        proj_list = []
        try:
            raw = client.service.mc_projects_get_user_accessible(username, password)
            proj_list = self.read_project_list(raw)
            return proj_list
        except WebFault:
            return proj_list

    def read_project_list(self, raw):
        project_list = []
        parsed = xmltodict.parse(raw, xml_attribs=False)
        data = [dict(d) for d in parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body']
        ['ns1:mc_projects_get_user_accessibleResponse']['return']['item']]
        for el in data:
            project = Project(id=el["id"], name=el["name"])
            project_list.append(project)
        return project_list
