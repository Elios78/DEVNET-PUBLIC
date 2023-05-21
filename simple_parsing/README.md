# Parsing JSON/XML/YANG File

Entry
-----------------

For all type of parsing you got 1 file exemple and python code to parse

How to launch
----------

python parse"_type".py
    -   python 

Result 
-----------------

### Parsing de la partie Alcatel

*Le nom de l'equipement est : ALU1<br/>
Ip de l'equipement : 192.168.1.1<br/>
Ipv6 de l'equipement : NULL<br/>*

### Parsing de la partie Cisco

*Le nom de l'equipement est : Router1<br/>
Ip de l'equipement : 10.0.0.1<br/>
Ipv6 de l'equipement : 2000::1/3*


*Le nom de l'equipement est : Router2<br/>
Ip de l'equipement : 10.0.0.2<br/>
Ipv6 de l'equipement : 2000::2/3<br/>*

# Arborescence du projet

``` bash 
simple_parsing
    ├── JSON_PARSE
    │   ├── exemple.json
    │   └── parse_json.py
    ├── XML_PARSE
    │   ├── exemple.xml
    │   ├── parse_xml2.py
    │   └── parse_xml.py
    └── YAML_PARSE
        ├── exemple.yaml
        └── parse_yaml.py
```
