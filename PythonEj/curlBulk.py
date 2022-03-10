#!/usr/bin/env python3

#Listas con 250 cuentas

#iteración de cuentas
file = ['xaa.csv', 'xab.csv', 'xac.csv', 'xad.csv', 'xae.csv', 'xaf.csv', 'xag.csv', 'xah.csv', 'xai.csv', 'xaj.csv', 'xak.csv', 'xal.csv', 'xam.csv', 'xan.csv', 'xao.csv', 'xap.csv', 'xaq.csv', 'xar.csv', 'xas.csv', 'xat.csv', 'xau.csv', 'xav.csv', 'xaw.csv', 'xax.csv', 'xay.csv', 'xaz.csv', 'xba.csv', 'xbb.csv', 'xbc.csv', 'xbd.csv', 'xbe.csv', 'xbf.csv', 'xbg.csv', 'xbh.csv', 'xbi.csv', 'xbj.csv', 'xbk.csv', 'xbl.csv', 'xbm.csv', 'xbn.csv', 'xbo.csv', 'xbp.csv', 'xbq.csv', 'xbr.csv', 'xbs.csv', 'xbt.csv', 'xbu.csv', 'xbv.csv', 'xbw.csv', 'xbx.csv', 'xby.csv', 'xbz.csv', 'xca.csv', 'xcb.csv', 'xcc.csv', 'xcd.csv', 'xce.csv', 'xcf.csv', 'xcg.csv', 'xch.csv', 'xci.csv', 'xcj.csv', 'xck.csv', 'xcl.csv', 'xcm.csv', 'xcn.csv', 'xco.csv', 'xcp.csv', 'xcq.csv', 'xcr.csv', 'xcs.csv', 'xct.csv', 'xcu.csv', 'xcv.csv', 'xcw.csv', 'xcx.csv', 'xcy.csv']

for i in file:
   print("===================================================Inicio Query==========================================================================") 
   print("var todas = ''\ndb.getCollection('services').find({'name' : 'Access Residential', 'region':'400','organizationCode':'AXTELLEGO','relatedParty.refId':{$in:[")
   print(i)
   print("]}},\n{\n\t\'relatedParty.refId\':1,\n\t\'serviceCharacteristics.value\':1,\n\t}\n\t).forEach(function(doc){\n\t\ttodas += '\\n'+doc.relatedParty[0].refId +',' +doc.serviceCharacteristics[0].value+','\n\t\tdb.getCollection('services').find({'relatedParty.refId': doc.relatedParty[0].refId, 'name':'Voice Residential'},\n\t\t{\n\t\t\t'serviceCharacteristics.value':1,\n\t\t}\n\t\t).forEach(function(doc2){\n\t\t\ttodas += doc2.serviceCharacteristics[0].value\n\t\t\t//print(doc2.relatedParty[0].refId +','+ doc2.name +','+ doc2.serviceCharacteristics[0].value+ ','+ doc.region)\n\t\t})\n\t})\n\tprint(todas)")
   print("===================================================Fin Query==========================================================================") 