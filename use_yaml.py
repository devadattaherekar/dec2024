import yaml

with open("test_yaml.yml","r") as fs:
    data_dict=yaml.load(fs,Loader=yaml.FullLoader)
    data_dict["myinfo"]["Firstname"] = "nitin"
    data_dict["myinfo"]["Lastname"] = "lokhande"
    data_dict["myinfo"]["Technologies"]["skills"][0] = "perl"
    data_dict["myinfo"]["Technologies"]["skills"][1] = "ruby"
    data_dict["myinfo"]["Technologies"]["skills"][2] = "php"
    print(data_dict)

with open("modify_yaml.yml","w") as ft:
    yaml.dump(data_dict,ft)
