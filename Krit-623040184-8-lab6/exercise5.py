import json

py_obj = {
    "firstName": "Jane",
    "lastName": "Doe",
     "hobbies": ["running", "sky diving", "singing"]
}

with open ("hobbies.json", "w") as json_file:
    (json.dump(py_obj, json_file))

with open ("hobbies.json", "r") as json_file:
    print(json.load(json_file))
