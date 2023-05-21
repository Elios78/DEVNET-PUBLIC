import json


def read_json_file():
    f = open("exemple.json", "r+")
    json_file = f.read()
    json_object = json.loads(json_file)
    # print (json_object) -> Pour afficher le fichier JSON
    return json_object


def read_json_object(json_object):
    # Parse Manuel de la partie Alcatel
    print(
        "\n----------------- Parsing de la partie Alcatel -----------------\n"
    )
    print("Le nom de l'equipement est : " + json_object["Alcatel"][0]["name"])
    print(
        "Ip de l'equipement : "
        + json_object["Alcatel"][0]["configuration"][0]["ip"]
    )
    print(
        "Ipv6 de l'equipement : "
        + json_object["Alcatel"][0]["configuration"][0]["ipv6"]
    )

    # Parse Automatique des objets JSON
    print(
        "\n----------------- Parsing de la partie Cisco  -----------------\n"
    )
    Cisco_device = json_object["Cisco"]
    for device in Cisco_device:
        print("Le nom de l'equipement est : " + device["name"])
        print("Ip de l'equipement : " + device["configuration"][0]["ip"])
        print("Ipv6 de l'equipement : " + device["configuration"][0]["ipv6"])
        print("\n")


read_json_object(read_json_file())
