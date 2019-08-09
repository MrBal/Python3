import json,os
def add(x,y):
    a = {x : y}
    with open('personal.json') as jsonfile:
        parsed=json.load(jsonfile)
    parsed.update(a)
    with open('personal.json','w') as jsonfile:
        json.dump(parsed,jsonfile)
def show(x):
    with open('personal.json') as jsonfile:
        parsed = json.load(jsonfile)
    print(parsed[x])
while True:
    a = input("\n1-Add\n2-Show\n3-List\n---->")
    if int(a)==1:
        x = input("Add key = \n")
        y = input("Add value = \n")
        add(x,y)
        continue
        pass
    elif int(a)==2:
        x = input("Search Key = \n")
        show(x)
        continue
        pass
    elif int(a)==3:
        with open('personal.json') as jsonfile:
            parsed = json.load(jsonfile)
        print (json.dumps(parsed, indent=2, sort_keys=True))
        continue
        pass
    else:
        print("Input Error\n")
        continue
        pass
