import xml.etree.ElementTree as ET
tree = ET.parse('soap.xml')    

#print tree.find('.//{http://tempuri.org/wsSalesQuotation/Service1}LoginResult').text
#print tree.find('.//{http://www.example.org/stock}Price').text
for p in tree.findall('.//{http://tempuri.org/wsSalesQuotation/Service1}LoginResult'):
	print p.text
