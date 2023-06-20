filename = str(input("What is the Filename?: "))
name = input("What is your first name?: ")
address = input("What is your address?: ")
number = input("What is your phone number?: ")

with open(filename, 'w') as file_object:
  file_object.write(name + ", ")
  file_object.write(address + ", ")
  file_object.write(number)

with open(filename) as file_object:
  contents = file_object.read()

print(contents)
