###Created 11/02/18
#######NPPES get some data for demo
import requests
import json
import pprint
#for key, value in data.iteritems():
    #print key, value
class ThisClass:
	r = requests.get("https://npiregistry.cms.hhs.gov/api/?&city=Baltimore&state=MD&skip=1000&pretty=on")
	data = json.loads(r.text)
	#print("data type(): ",type(data))
	pp = pprint.PrettyPrinter(indent=1)
	#pp.pprint(data)
	#print("print keys: ",  data.keys())
	#print("keys type: ", type(data.keys()))
	
	print("##############for item in data['results'][0]['addresses'][0]:")	
	for item in data['results'][0]['addresses'][0]:
		print("type(item): ",type(item))	
		print("item: ",item)
		#this thing prints the dictionary keys as strings, but you can't get the 
		#address_1 value or telephone_number value, for example
	
	
	dataset = data['results']
	
	print("##############for item in dataset:")
	print("#########dataset = data['results']")	
	for items in dataset:
		for x in items:
			try:
				iterator = iter(items[x])
			except TypeError:
				print("items is not iterable.")
			else:
				for y in items[x]:
					try:
						print("y type: ",type(y[0]))
						print("y = ")
						pp.pprint(y[0])
					except Exception:
						print("y type: ",type(y[0]))
						print("can't pretty print y")
						print("y = ",y[0])
								
# type(item):  <class 'dict'>
# item:  {'addresses': [{'address_1': '5205 EAST DR', 'address_2': '', 'address_pu
# rpose': 'LOCATION', 'address_type': 'DOM', 'city': 'BALTIMORE', 'country_code':
# 'US', 'country_name': 'United States', 'postal_code': '212272403', 'state': 'MD'
# , 'telephone_number': '410-247-5333'}, {'address_1': '5205 EAST DR', 'address_2'
# : '', 'address_purpose': 'MAILING', 'address_type': 'DOM', 'city': 'BALTIMORE',
# 'country_code': 'US', 'country_name': 'United States', 'postal_code': '212272403
# ', 'state': 'MD', 'telephone_number': '410-247-5333'}], 'basic': {'credential':
# 'DPM', 'enumeration_date': '2005-10-09', 'first_name': 'NEIL', 'gender': 'M', 'l
# ast_name': 'SCHEFFLER', 'last_updated': '2007-07-08', 'middle_name': 'M', 'name'
# : 'SCHEFFLER NEIL', 'name_prefix': 'DR.', 'sole_proprietor': 'NO', 'status': 'A'
# }, 'created_epoch': 1128816000, 'enumeration_type': 'NPI-1', 'identifiers': [],
# 'last_updated_epoch': 1183852800, 'number': 1295723880, 'other_names': [], 'taxo
# nomies': [{'code': '213E00000X', 'desc': 'Podiatrist', 'license': '000319', 'pri
# mary': True, 'state': 'MD'}]}
