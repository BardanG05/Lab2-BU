t = 15
e = 5

something = t < e

type_something = type(something)
print(f"Result = {something} and its data type is {type_something}")


unit_name = "Level 4 programming"
print("This unit is", unit_name)

print("The 1st character is:", unit_name[0]) 
print("The 4th character is:", unit_name[3]) 
print("The 8th character is:", unit_name[7])

greeting_string= "Welcome to Programming unit! This is a level 4 unit :)"
print(greeting_string)
print("The 1st character is:", greeting_string[0])
print("The 5th character is:", greeting_string[4])

print("These are the first 5 characters:", greeting_string[0:5])
print("This is the last character:", greeting_string[-1])
print("These are the last 4 characters:", greeting_string[-4:])

a =11
print(type(a)) 
a = 11.0 
print(type(a))
a = "11"
print(type(a))
a = "11" + "11"
print(type(a))
a = "a"
print(type(a))
a = True 
print(type(a))
a = "False" 
print(type(a))

a = 14.99
print(int(a))


x = "I am awake at 1:49 AM right now"
y = 12
z = 9.99

print(type(x))
print(type(y))
print(type(z))

result = y + z
print(result)
print(type(result))

result = y + int(z)
print(result)
print(type(result))

result = z + float(y)
print(result)
print(type(result))

print(type(str(z)))

result = x + str(y) + str(z)
print(result)
print(type(result))

#Cannot add x + y as u cannot add a string with an  integer or float

my_var = 1


