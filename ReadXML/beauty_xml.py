import xml.dom.minidom
import sys

xml = xml.dom.minidom.parse(sys.argv[1]) # or xml.dom.minidom.parseString(xml_string)
beauty_xml = xml.toprettyxml()
print beauty_xml
