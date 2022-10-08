from zeep import Client
import xml.etree.ElementTree as ET

client = Client(wsdl='http://localhost:8000/?wsdl')
countries = ET.Element('countires')
country = ET.SubElement(countries, 'country')
country.text = input("Enter country shortcut: ")
xml_send = ET.tostring(countries)

print("XML sent: {}".format(xml_send))
print("Server answered: {}".format(client.service.getCountry(xml_send)))