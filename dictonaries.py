import json

#initialize a dictionary
dictionary = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}

#update a dictionary
dictionary.update({"Sarah": 9})

## loop over key
for key in dictionary.keys():
    print(key + " " + str(dictionary[key]))

## loop over key and values
for (key, value) in dictionary.items():
    print(key + " " + str(value))

##covert dict to json
print(json.dumps(dictionary))

##convert json to dict
x = '{ "name":"John", "age":30, "city":"New York"}'
xdictionary = json.loads(x)
print(xdictionary)
