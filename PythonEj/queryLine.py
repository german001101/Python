#!/usr/bin/env python3

#Listas con 250 cuentas

#iteración de cuentas
file = ['525562742012']

for i in file:
   print("===================================================Inicio Query==========================================================================") 
   print("var todas = ''\ndb.getCollection('services').find({'name' : 'Access Residential', 'region':'400','organizationCode':'AXTELLEGO','relatedParty.refId':{$in:[")
   print(i)
   print("]}},\n{\n\t\'relatedParty.refId\':1,\n\t\'serviceCharacteristics.value\':1,\n\t}\n\t).forEach(function(doc){\n\t\ttodas += '\\n'+doc.relatedParty[0].refId +',' +doc.serviceCharacteristics[0].value+','\n\t\tdb.getCollection('services').find({'relatedParty.refId': doc.relatedParty[0].refId, 'name':'Voice Residential'},\n\t\t{\n\t\t\t'serviceCharacteristics.value':1,\n\t\t}\n\t\t).forEach(function(doc2){\n\t\t\ttodas += doc2.serviceCharacteristics[0].value\n\t\t\t//print(doc2.relatedParty[0].refId +','+ doc2.name +','+ doc2.serviceCharacteristics[0].value+ ','+ doc.region)\n\t\t})\n\t})\n\tprint(todas)")
   print("===================================================Fin Query==========================================================================") 