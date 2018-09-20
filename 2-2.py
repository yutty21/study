#!/usr/bin/env python

import re
import sys
import time

def t1():
    start = time.clock()
    count = 0
    for line in sys.stdin:
        line = line.strip()
        pattern = re.compile("(?:\"device_id\":\")([^\"]+)")
        search = pattern.search(line)
        if search:
            count += 1
            #print search.groups()[0]
    end = time.process_time.clock()
    print ("The count is: %d" %(count))
    print ("The cost time is: %f" %(end - start))

t1()