#!/usr/bin/env python

from datetime import datetime, date
import json
import sys

def snapshot_time(file):
    with open(file, 'r') as f:
        myDict      = {}
        myList = json.load(f)
        for item in myList:
            epoch_time         = item['nextSnapshot']['$timestamp']['t']
            replicaSet         = (item['rsId'])
            myDict[replicaSet] = datetime.fromtimestamp(epoch_time)

    for replicaSet in sorted(myDict, key=myDict.get):
        print(myDict[replicaSet], replicaSet)

if __name__ == '__main__':

    try:
        if len(sys.argv) == 2:
            file = sys.argv[1:2]
            snapshot_time(file[0])
        else:
            print('Usage: %s backupJobs.json' % sys.argv[0])
            sys.exit(1)
    except IOError:
        print('No such file or directory: %s' % sys.argv[1])
        sys.exit(1)
    except ValueError:
        print('Expected file backupJobs.json')
        sys.exit(1)