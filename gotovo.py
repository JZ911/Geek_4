#-*- coding: utf-8 -*-
import re
import csv
import os


if not os.path.exists('F:\API\GeekHub\subject_4'):
    os.mkdir('F:\API\GeekHub\subject_4')
input = open("openerp-server.txt", 'r')
output = open("result.csv", "w")
writer = csv.DictWriter(output, fieldnames = ('ID', 'Marker', 'date_and_time', 'all'))
lookfor = re.compile(r'(.*\d.-\d.-\d.*\d.:\d.:\d.).*(ERROR|WARNING|CRITICAL) (pg|\?|None) (.*)')
for line, text in enumerate(input):
    if re.findall(lookfor, text):
        row = re.findall(lookfor, text)
        writer.writerow({'ID': line, 'Marker': row[0][1], 'date_and_time': row[0][0], 'all': row[0][3]})
#print(row)

