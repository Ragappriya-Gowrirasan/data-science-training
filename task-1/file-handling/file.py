# file object = open("file_name","mode")
# mode - r+ , w+ , a+

files = open("C:/Users/ragap/OneDrive/Documents/practice/demo.text","w")

# attributes - name , mode , closed , softspace

print("name of the file: ", files.name)
print("mode of file: ", files.mode)
print("file is closed: ",files.closed)

# file close 
if files.close():
    print("close the file: ",files.closed)
