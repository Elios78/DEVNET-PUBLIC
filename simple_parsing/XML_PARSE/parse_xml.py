import xml.etree.ElementTree as ET


def read_xml_file():
    xml_object = ET.parse("exemple.xml").getroot()
    return xml_object


def read_xml_object(xml_object):
    # Parse Manuel de la partie Alcatel
    print(
        "\n----------------- Parsing de la partie Alcatel -----------------\n"
    )
    print("Le nom de l'equipement est : " + xml_object[0][0].get("name"))
    print("Ip de l'equipement :" + xml_object[0][0][0][0].text)
    print("Ipv6 de l'equipement :" + xml_object[0][0][0][1].text)

    # Parse Automatique des objets XML
    print(
        "\n----------------- Parsing de la partie Cisco  -----------------\n"
    )
    for device in xml_object.findall(".//*[@name='Cisco']/name"):
        print("Le nom de l'equipement est : " + device.get("name"))
        print("Ip de l'equipement :" + device[0][0].text)
        print("Ipv6 de l'equipement :" + device[0][1].text)
        print("\n")


read_xml_object(read_xml_file())
