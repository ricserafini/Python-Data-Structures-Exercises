import json

number = int(input("What is you favourite number? "))

filename = 'favourite_number.json'

with open(filename, 'r+') as f:
    
    try:
        data = json.load(f)
    except:
        data = [] 
        
    data.append(number)
    f.seek(0)
    json.dump(data, f)
    print("Thanks! I will remember that!")
    
    