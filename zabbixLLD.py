#!/usr/bin/env python3
# zabbix低级别自动发现(lov level discovery)传入监控key，返回json
import json


class ZabbixDiscovery(object):
    def __init__(self, keys):
        self.data={
            "data":[]
        }
        for key in keys:
            context = {"{#NAME}":key}
            self.data["data"].append(context)
    def discovery(self):
        print(json.dumps(self.data))

if __name__ == "__main__":
    keys = ("keys1", "keys2")
    z = ZabbixDiscovery(keys)
    z.discovery()