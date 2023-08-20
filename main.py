

user_name = input("Enter your name: ")
age = input("Enter your age: ")
dob = input("Enter your date of birth: ")

with open("file.txt", "w") as file:
    file.write( user_name +"|"+ age + "|" +dob  )

with open("file.txt","r") as filee:
    for line in filee.readlines():
        print(line)
