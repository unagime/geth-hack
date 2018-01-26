#!/usr/bin/python

import requests
import json
import xml.etree.ElementTree
import eventlet
from pprint import pprint
eventlet.monkey_patch()
ip_addr = []
def tara(ip):
	try:
		with eventlet.Timeout(3):
			address = 'http://'+ip+':8545'
			data = {"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			r = requests.post(address, data=json.dumps(data), headers=headers, timeout=3)
			return r.text
	except: 
	  pass
def import_xml():
	e = xml.etree.ElementTree.parse('scan.xml').getroot()
	for atype in e.findall('host'):
		for xx in atype.findall('address'):
			ip_addr.append(xx.get('addr'))
def check(ip,data):
	try:
		if 'Geth' in data: 
			dosya = open('success.txt','a')
			dosya.write('\n')
			dosya.write(ip);
	except: 
	  pass
import_xml()
for ip in ip_addr:
	gelen = tara(ip)
	check(ip,gelen)
	print(ip)
#gelen = tara('127.0.0.1')
#pprint(ip_addr)
#check('127.0.0.1',gelen)
