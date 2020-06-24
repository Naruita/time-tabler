#!usr/bin/python
# -*- coding: utf-8 -*-

# File managing
import json

''' This program is a testing program for the processing of the time difference between each of the stamps.'''


with open('schedule.txt', 'r') as f:
    content = f.read()
    content = json.loads(content)
print(content)