#!/usr/bin/env python3

"""
Requests Proficiency Assignment
Tasks:
- send a GET request to Flask API to JSON endpoint
- take the returned JSON and normalize it (chose YAML)
"""

# import requests
import requests
# import the pprint module: 
from pprint import pprint
# import yaml
import yaml

# capture the URL endpoint 
json_url = "http://127.0.0.1:3000/all"

# request the data from the server and convert to json
response = requests.get(json_url).json()

# convert new python dict to yaml string
yamlresponse = yaml.dump(response, sort_keys=False)

pprint(yamlresponse)