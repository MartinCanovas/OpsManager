#!/usr/bin/env python

import json
import os

def replicaset_specs(file):
    with open(file, 'r') as f:
        jsonFile = json.load(f)
        if jsonFile:
            listOfSpecs = {}
            for item in jsonFile[:1]:
                hostname  = item['hostInfo']['system']['hostname']
                numCores  = 'numCores' + ' ' + str(item['hostInfo']['system']['numCores'])
                memLimitGB = str(round(float(item['hostInfo']['system']['memLimitMB']) / 1024, 2)) + 'GB'
                memSizeGB = str(round(float(item['hostInfo']['system']['memSizeMB']) / 1024, 2)) + 'GB'
                osName    = item['hostInfo']['os']['name']
                osVersion = item['hostInfo']['os']['version']
                listOfSpecs[hostname] = [numCores, memSizeGB, memLimitGB, osName, osVersion]
        else:
            print('file', file, 'is empty')
            return

    for hostname in sorted(listOfSpecs, key=listOfSpecs.get):
        print(hostname,':', listOfSpecs[hostname])
        return

if __name__ == '__main__':
    directory = '.'
    listOfFiles = []
    for path, subdirs, files in os.walk(directory):
        for name in [os.path.join(path, name) for name in files]:
            if (name.find('lastPings.json') != -1):
                replicaset_specs(name)
