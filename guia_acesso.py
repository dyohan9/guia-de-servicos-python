import requests, json

__version__ = '0.0.2'
__author__ = 'Daniel Yohan <dyohan9@gmail.com>'

class Services:
    def __init__(self, id, type):
        if type == "services":
            self.__content = json.loads(requests.get('http://www.servicos.al.gov.br/api/v1/services/%s.json' % id).content)
        elif type == "units":
            self.__content = json.loads(requests.get('http://www.servicos.al.gov.br/api/v1/units/%s.json' % id).content)

    def __del__(self):
        self.__content = None

    def getContent(self):
        return self.__content

    def getName(self):
        return self.__content["name"]

    def getDescription(self):
        return self.__content["description"]

    def getApplicants(self):
        return self.__content["applicants"][0]["type"]

    def getSteps(self):
        return self.__content["steps"]

    def getUnitID(self):
        return self.__content["unit_ids"]

class UnitID:
    def __init__(self, id, type):
        self.content = Services(id, type).getContent()

    def __del__(self):
        self.__content = None

    def getContent(self):
        return self.getContent()

    def getUnitName(self):
        return self.content["name"]

    def getURL(self):
        return self.content["url"]



