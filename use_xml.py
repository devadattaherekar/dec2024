import xmltodict

with open("test_xml.xml","r") as fp:
    str_data=fp.read()
    dict_data=xmltodict.parse(str_data)
    print(dict_data)
    print(dict_data['root']['myinfo']['Firstname'])
    dict_data['root']['myinfo']['Firstname']="sunny"
    dict_data['root']['myinfo']['Lastname'] = "chavan"
    del dict_data['root']['myinfo']['Technologies']['skills'][1]
    dict_data['root']['myinfo']['Technologies']['skills'][1]="shell scripting"

with open("modifytest_xml.xml","w") as ft:
    str_data=xmltodict.unparse(dict_data,pretty=True)
    ft.write(str_data)