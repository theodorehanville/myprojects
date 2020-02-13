import json
from difflib import get_close_matches
#loading the json file into a variable called data that becomes a python dictionary
data = json.load(open('076 data.json','r'))


#defining the function
def dictionary (wor):
    l1 =[]
    if wor in data.keys():
        wor = str(wor.lower())
        print('\n')
        print(wor + ':')
        i = 0
        for k in data[wor]:
            length = len(data[wor]) +1
            num_1 = list(range(length))
            num = num_1[1:]
            r = str(num[i]) + '. ' + data[wor][i]
            l1.append(r)
            i = i +1
    elif len(get_close_matches(wor,data.keys(),n = 5,cutoff = 0.7))>0:
        l1.append('Did you mean:')
        for m in get_close_matches(wor,data.keys(),n = 5,cutoff = 0.7):
            l1.append(m)
    else:
        l1 =['Word does not exist in dictionary']

    return (l1)
