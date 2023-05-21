import xmltodict
from pprint import pprint


def read_xml_file():
    f = open("exemple.xml", "r+")
    xml_file = f.read()
    xml_object = xmltodict.parse(xml_file)
    return xml_object


def read_xml_object(xml_object):
    # Parse Manuel de la partie Alcatel
    # pprint(xml_object)
    print(
        "\n----------------- Parsing de la partie Alcatel -----------------\n"
    )
    print(
        "Le nom de l'equipement est : "
        + xml_object["device"]["type"][0]["name"]["@name"]
    )
    print(
        "Ip de l'equipement :"
        + xml_object["device"]["type"][0]["name"]["configuration"]["ip"]
    )
    print(
        "Ipv6 de l'equipement :"
        + xml_object["device"]["type"][0]["name"]["configuration"]["ipv6"]
    )

    # Parse Automatique des objets XML
    print(
        "\n----------------- Parsing de la partie Cisco  -----------------\n"
    )
    for device in xml_object["device"]["type"][1]["name"]:
        print("Le nom de l'equipement est : " + device["@name"])
        print("Ip de l'equipement :" + device["configuration"]["ip"])
        print("Ipv6 de l'equipement :" + device["configuration"]["ipv6"])
        print("\n")


read_xml_object(read_xml_file())
