# -*- coding: utf-8 -*-

# DESCRIPTION
# This small script will turn the Ukrainian small business taxpayers CSV database
# into a much more accessible Sqlite3 format. Feel free to change whatever.
# N.B. I know there are other ways to do this. I just find this more convenient.

# Instructions:
# 1. Download the database file (should be available at http://data.gov.ua/passport/5fc89a6f-55b8-4ec6-95d6-38a0fdc31be1)
#  what you need is "Відомості щодо юридичних осіб".
# 2. Extract the zip file. You should have a file called UO.csv or something like that.
# 3. Now we need to fix the encoding mess.
# - On a Linux PC (on Windows use iconv.exe) do this:
# iconv -f CP1251 -t UTF-8 UO.csv > uo-utf.csv
# This will save a utf-8 encoded copy of the file.
# Just in case, more info is available here: http://stackoverflow.com/questions/15422753/iconv-convert-from-cp1252-to-utf-8

from peewee import *
from playhouse.csv_loader import load_csv

db = SqliteDatabase('payers.db')

fields = [CharField(null=True), CharField(null=True), IntegerField(null=True), CharField(null=True), CharField(null=True), CharField(null=True), CharField(null=True)]
field_names = ['name', 'short_name', 'taxpayer_code', 'address', 'director_name', 'major_activity', 'status']

print 'This script takes a while (like 10-15 min maybe?), so please, be patient.'
print "You can watch the payers.db file - if it's size changes, then all is going well and you just need to wait."

data = load_csv(db, 'uoutf.csv', fields=fields, field_names=field_names, has_header=True, delimiter=';')

print ''
print 'Done!'