filename = 'learning_python.txt' 

with open(filename) as file_object:
    content = file_object.read()
    content = content.replace('Python', 'C')
    
print(content)


with open(filename) as file_object:
    for content in file_object:
        print(content.rstrip())
        
print('')

with open(filename) as file_object:
    lines = file_object.readlines()
    
    for line in lines:
        print(line.rstrip())