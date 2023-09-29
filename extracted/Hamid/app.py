import os
file_open = open("d:\\test.txt", "w")
file_open.write(
    "My name is Nilofar and  i am very eager to learn a new thing " "\n"  " Hamid is very good boy:")
file_open.close()
file_open = open("D:\\test.txt", "r")
content = file_open.read()
print(content)
