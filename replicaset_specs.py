#!/usr/bin/env python

import json
import os

def replicaset_specs(file):
    with open(file, 'r') as f:
        jsonFile = json.load(f)
        if jsonFile:
            listOfSpecs = {}
            for item in jsonFile:
                hostname   = item['hostInfo']['system']['hostname']
                numCores   = 'numCores' + ' ' + str(item['hostInfo']['system']['numCores'])
                memSizeGB  = str(round(float(item['hostInfo']['system']['memSizeMB']) / 1024, 2)) + 'GB'
                memLimitMB = str(round(float(item['hostInfo']['system']['memLimitMB']) / 1024, 2)) + 'GB'
                osName     = item['hostInfo']['os']['name']
                osVersion  = item['hostInfo']['os']['version']
                listOfSpecs[hostname] = [numCores, memSizeGB, memLimitMB, osName, osVersion]

            for hostname in sorted(listOfSpecs, key=listOfSpecs.get):
                print(hostname,':', listOfSpecs[hostname])
        else:
            print('file', file, 'is empty')
    return

if __name__ == '__main__':
    directory = '.'
    listOfFiles = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            listOfFiles.append(os.path.join(root, name))
    for file in listOfFiles:
        if (file.find('lastPing') != -1):
            replicaset_specs(file)
