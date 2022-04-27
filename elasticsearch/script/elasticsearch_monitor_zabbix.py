#!/usr/bin/env python3
#coding: utf-8
# elasticsearch zabbix监控脚本
import requests
import sys

from requests.auth import HTTPBasicAuth

ES_ENDPOINT = "http://127.0.0.1:9200"
ES_USER = ""
ES_PASSWORD = ""

class EsError(Exception):
    def __init__(self):
        self.what = 'Check error!'

    def __init__(self,des):
        self.what = des

    def __str__(self):
        return repr(self.what)

class ES_MONITOR(object):
    def __init__(self, es_server:str, user:str, password:str):
        self.es_server = es_server
        self.user = user
        self.password = password
        self.init_get_cluster()

    def url_get(self, uri:str, is_json:bool=False):
        try:
            resp = requests.get(self.es_server + uri, auth=HTTPBasicAuth(self.user, self.password))
            if is_json:
                return resp.json()
            else:
                return resp.content.decode()
        except Exception as e:
            raise EsError("es connect error")
    
    def init_get_cluster(self):
        try :
            self.cluster = self.url_get(uri="/_cluster/stats", is_json=True)
        except EsError as e :
            self.es_error = True
        else:
            self.es_error = False
        if not self.es_error: 
            self.cluster_name = self.cluster["cluster_name"]
            self.status =  self.cluster["status"]
            self.versions = self.cluster["nodes"]["versions"]
            self.nodes_total = self.cluster["_nodes"]["total"]
            self.nodes_successful = self.cluster["_nodes"]["successful"]
            self.nodes_failed = self.cluster["_nodes"]["failed"]
            self.indices_count = self.cluster["indices"]["count"]

    def get_cluster_info(self, zabbix_key:str):
        if self.es_error:
            return "es connect error"
        if zabbix_key in self.__dict__:
            return self.__dict__[zabbix_key]
        else:
            return "unknow zabbix key"


if __name__ == "__main__":
    args = sys.argv[1]
    es_monitor = ES_MONITOR(ES_ENDPOINT, ES_USER, ES_PASSWORD)
    print(es_monitor.get_cluster_info(args))
    
