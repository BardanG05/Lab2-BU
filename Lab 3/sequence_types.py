my_list = ["hello", 20, 20.5, "chicken", 25.0]
print(len(my_list))
my_list.append(96)
print(my_list)

my_list.insert(0, "First")
print(my_list)
my_list.remove(25.0)
print(my_list)
print(len(my_list))
print(my_list[0])
my_list[1] = 21
print(type(my_list))

my_tuple = tuple(my_list)
print(type(my_tuple))
print(my_tuple[0])
#tuple value cannot be channged my_tuple[0] = 3 

another_tuple = (5, 6.6, "Me")

joined_tuple = my_tuple + another_tuple
print(joined_tuple)

my_list = list(joined_tuple)
print(type(my_list))

my_set = set(my_list)
print(len(my_set))
my_set.add("water")
print(my_set)

my_set.add(20)
print(my_set)

another_set = {1, 2, 3, "Me"}
new_set = my_set & another_set 
print(new_set)

# & returns the common items in the sets 

car_details = {"car_make":"Tesla",
               "model":"Cyber Truck",
               "weight":"11,000 lbs",
               "est_range": "340 miles"
               }

print(car_details)
Company = car_details["car_make"]
print(car_details)
print(Company)
car_details["colour"] = "Grey"
print(car_details)
del car_details["colour"]
print(car_details)

# 1. Tuples, list
# 2. Dictionaries
# 3. Using & between sets  
