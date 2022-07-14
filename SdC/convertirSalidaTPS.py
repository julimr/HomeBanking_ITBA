import json

from Classic import Classic
from Gold import Gold
from Black import Black


def convertToDict(file):

    with open(file) as json_file: 
        data = json.load(json_file) 
        
    return data
