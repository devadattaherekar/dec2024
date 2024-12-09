import json

with open("json_ex.json","r") as fp:
    data_dict=json.load(fp)
    print(data_dict)
    print(data_dict["menu"]["items"])
    print(data_dict["menu"]["items"][3]['id'])
    del data_dict["menu"]["items"][2]
    del data_dict["menu"]["items"][5]
    del data_dict["menu"]["items"][8]
    del data_dict["menu"]["items"][-3]
    print(data_dict)
    for each_dict in data_dict["menu"]["items"]:
        if any(each_dict['id']):
            print(each_dict['id'])
