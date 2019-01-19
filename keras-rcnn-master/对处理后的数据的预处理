from pathlib import Path
import json

analysis_root_dir = "C:/Users/zhuhuiling/Desktop/total/1_1_son"
path = Path(analysis_root_dir)
all_json_file = list(path.glob('**/*.json'))
parse_result = []
for json_file in all_json_file:
    # 获取所在目录的名称
    service_name = json_file.parent.stem
    with json_file.open() as f:
        json_result = json.load(f)
    parse_result.append(json_result) 

r, c = 224, 224   
groups = ("training", "test")
for group in groups:
    dictionaries = []


for i in parse_result:
    for group in groups:
        dictionaries = []
        for _ in range(256):
            pathname =  i["imagePath"]
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
            category = i['shapes'][0]['label']
#           (bounding_box_r, bounding_box_c) =  i['shapes'][2]#需要修改
#           minimum_r, maximum_r = bounding_box_r
#           minimum_c, maximum_c = bounding_box_c
            object_dictionary = {
#                       "bounding_box": {
#                            "minimum": {
#                                "r": minimum_r - 1,
#                                "c": minimum_c - 1
#                        },
#                        "maximum": {
#                                "r": maximum_r - 1,
#                                "c": maximum_c - 1
#                        }
#                    },
                        "category": category
                }
            dictionary["objects"].append(object_dictionary)
            dictionaries.append(dictionary)
        filename = "{}.json".format(group)

        with open(filename, "w") as stream:
            json.dump(dictionaries, stream)#dumps是将dict转化成str格式，loads是将str转化成dict格式。


        