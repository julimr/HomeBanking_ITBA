import json

def convertToDict(file):

    with open(file) as json_file: 
        data = json.load(json_file) 
        
    return data
