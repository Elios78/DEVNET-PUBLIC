import yaml

from pprint import pprint


def read_yaml_file():
    f = open("exemple.yaml", "r+")
    yaml_file = f.read()
    yaml_object = yaml.load(yaml_file)
    return yaml_object


def read_yaml_object(yaml_object):
    # Parse Manuel de la partie Alcatel
    # pprint(yaml_object)
    print(
        "\n----------------- Parsing de la partie Alcatel -----------------\n"
    )
    print(
        "Le nom de l'equipement est : " + yaml_object["device:Alcatel"]["name"]
    )
    print(
        "Ip de l'equipement :"
        + yaml_object["device:Alcatel"]["configuration:network"]["ip"]
    )
    print(
        "Ipv6 de l'equipement :"
        + yaml_object["device:Alcatel"]["configuration:network"]["ipv6"]
    )

    # Parse Automatique des objets XML
    print(
        "\n----------------- Parsing de la partie Cisco  -----------------\n"
    )
    for device in yaml_object["device:Cisco"]:
        print("Le nom de l'equipement est : " + device["name"])
        print("Ip de l'equipement :" + device["configuration:network"]["ip"])
        print(
            "Ipv6 de l'equipement :" + device["configuration:network"]["ipv6"]
        )
        print("\n")


read_yaml_object(read_yaml_file())
