groups = ("training1", "test1")
for group in groups:
    dictionaries = [] 
    for i in parse_result[:256]: 
        pathname = "im/"+ i["imagePath"]
        if os.path.exists(path):
            dictionary = {
                        "image": {
                        "pathname": pathname,
                        "shape": {
                                "r": r,
                                "c": c,
                                "channels": 3
                            }
                        },
                        "objects": []
                    }
            for j in i["shapes"]:
                category = j['label']
                (bounding_box_r, bounding_box_c)=j['points']
                minimum_r, maximum_r = bounding_box_r
                minimum_c, maximum_c = bounding_box_c
                object_dictionary = {
                        "bounding_box": {
                             "minimum": {
                                 "r": minimum_r - 1,
                                 "c": minimum_c - 1
                         },
                         "maximum": {
                                "r": maximum_r - 1,
                                "c": maximum_c - 1
                            }
                       },
                        "category": category
                    }
                dictionary["objects"].append(object_dictionary)
            dictionaries.append(dictionary)
            filename = "{}.json".format(group)
            with open(filename, "w") as stream:
                json.dump(dictionaries, stream)#dumps是将dict转化成str格式，loads是将str转化成dict格式。


        
        