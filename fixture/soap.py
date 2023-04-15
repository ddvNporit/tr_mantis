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
        try:
            raw_data = client.service.mc_projects_get_user_accessible(username, password)
            project_list = self.parse_project_list(raw_data)
            return project_list
        except WebFault as err:
            print(f"Error {err}")
            return []

    def parse_project_list(self, raw_data):
        project_list = []
        parsed = xmltodict.parse(raw_data, xml_attribs=False)
        data = [dict(d) for d in parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body']
        ['ns1:mc_projects_get_user_accessibleResponse']['return']['item']]
        for p in data:
            project = Project(id=p["id"], name=p["name"])
            project_list.append(project)
        return project_list
