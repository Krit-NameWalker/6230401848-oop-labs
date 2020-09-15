import json

with open ("hobbies.json", "r") as json_file:
    read = json.load(json_file)
    hobbie = ", ".join(read["hobbies"])
    print(read["firstName"], "has hobbies as", hobbie)