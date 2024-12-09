import json

#print(dir(json))
with open("test_json.json","r") as fs:
    text_string=fs.read()
    json_dict=json.loads(text_string)
    print(json_dict)
    print("First name is ",json_dict["myinfo"]["Firstname"])
    print("Last name is ",json_dict["myinfo"]["Lastname"])
    print("Skills are...")
    for each_skill in json_dict["myinfo"]["Technologies"]["skills"]:
        print(each_skill,end=" ")
    json_dict["myinfo"]["Firstname"]="Prashant"
    json_dict["myinfo"]["Lastname"] = "Malusare"
    json_dict["myinfo"]["Technologies"]["skills"][0] = "dockers"
    json_dict["myinfo"]["Technologies"]["skills"][1] = "kubernetes"
    json_dict["myinfo"]["Technologies"]["skills"][2] = "ansible"
    print(dir(json_dict))
    #print(type(text_string),type(json_data))

with open("test_json_copy1.json","w") as ft:
    text_string=json.dumps(json_dict,indent=True)
    ft.write(text_string)
