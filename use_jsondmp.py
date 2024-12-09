import json
#print(dir(json))
with open("test_json.json","r") as fs:
    json_dict=json.load(fs)
    print(json_dict)
    print("First name is ",json_dict["myinfo"]["Firstname"])
    print("Last name is ",json_dict["myinfo"]["Lastname"])
    del json_dict["myinfo"]["Age"] # delete operation
    print("Skills are...")
    for each_skill in json_dict["myinfo"]["Technologies"]["skills"]: # read operation
        print(each_skill,end=" ")
    json_dict["myinfo"]["Firstname"]="Prashant" # update operation
    json_dict["myinfo"]["Lastname"] = "Malusare"
    json_dict["myinfo"]["Technologies"]["skills"][0] = "dockers"
    json_dict["myinfo"]["Technologies"]["skills"][1] = "kubernetes"
    json_dict["myinfo"]["Technologies"]["skills"][2] = "ansible"
    print(dir(json_dict))
    #print(type(text_string),type(json_data))

with open("test_json_copy1.json","w") as ft:
    json.dump(json_dict,ft,indent=True) # create operation
