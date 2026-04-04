# learning file Operations

# although we can hard code the arguments but for now lets take as inputs
file_path = input("file path enter kar bhai: ")
key = input("key where change is required: ")
value = input("what should be the updated value: ")

# ab likhenge main function to read and write a particular file ...
def update_config(file_path,key,value) :
    with open(file_path,"r") as file:
     lines = file.readlines()
     key_part = key.strip()
     value_part = value.strip()
     # after storing the content of file in lines(variable) now update the value of key provided 
    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
                file.write(f"{key_part} = {value_part}\n")
            else:
                file.write(line)
# bhai indentations bhot preshan krti hai yrr but finally function ends here ... lets call the function with proper args 

update_config(file_path, key, value)
