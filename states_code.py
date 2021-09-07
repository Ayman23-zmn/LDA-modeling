import json

# Important note - load() method loads file into a python object. loads()method loads a string 
#                - dump() method converts the python object into a json file. dumps() method converts data into json string

## (1) make a function that loads json files into python object  
with open('vs codes\Json file reading\Datasets\states.json') as f:
     data = json.load(f)

## (2)prints out different keys
for state in data['states']:
    print(state['name'],state['abbreviation'])  

## (3) delete keys that are not required and write this python object into a json file
for state in data['states']:
    del state['area_codes']

#(4) this creates a new json file to the directory you wanna save 
with open('C:/Users/USER/Desktop/vs codes/Json file reading/Datasets/new_states.json','w') as f:
    json.dump(data,f,indent=2)
    




