#!/usr/bin/env python3
import zabbixLLD
import subprocess
import sys
import json

with open('process.json', 'r') as f:
    config = json.load(f) 

monitor_key = config["process"]

if len(sys.argv) == 1 :
    print(sys.argv[0] + " [discovery|getcode]")
    sys.exit()
action = sys.argv[1]
if action == "discovery":
    z = zabbixLLD.ZabbixDiscovery(monitor_key)
    z.discovery()
elif action == "getcode":
    process_name = sys.argv[2]
    (status, output) = subprocess.getstatusoutput("ps auxf|grep %s |grep -v grep |grep -v %s|wc -l" % (process_name, sys.argv[0]))
    if output == "":
        print(0)
    else:
        print(output)
else:
    print(sys.argv[0] + " [discovery|getcode]")
    sys.exit()
