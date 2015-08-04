import xml.etree.ElementTree as ET

tree = ET.parse('simple-soap.xml')
root = tree.findall('.//{http://lalala.org/}GetResult')

# Single row iterate. For example : ID column value
"""
for row in tree.findall('.//{http://schemas.datacontract.org/SomeFormat}ID'):
	print row.text
"""

# Multiple row iterate.
for row in root[0]:
	print "ID = ",row[0].text,", Date ",row[1].text,", Divsion ",row[2].text,", Product ",row[3].text,", Model_Alias ",row[4].text,", Mobile No ",row[5].text,", Sales ",row[6].text
