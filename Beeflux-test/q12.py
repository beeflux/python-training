"""
Q12.

Write a program to create a flie name bee.txt write “hello bee to it”

write another program to read the contents of bee.txt in uppercase.
"""

with open("bee.txt", "w") as file:
    #simply open the file and write the text
    file.write("hello bee to it")
    file.close()

with open("bee.txt","r") as file:
    #simple open the file and read data from the text
    print(file.read())
    file.close()