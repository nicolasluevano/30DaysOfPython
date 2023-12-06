# Day 2: 30 Days of python programming

first_name = 'Nicolas'
last_name = 'Luevano'
full_name = 'Nicolas Luevano'
country = 'USA'
city = 'Los Angeles'
age = 100
year = 2100
is_married = False
is_true = True
is_light_on = False
variable_one, variable_two = 'multiple variables on one line', 2

# Check the data type of all your variables using type() built-in function
fnt = type(first_name)
lnt = type(last_name)
fnt = type(full_name)
ct = type(country)
ctyt = type(city)
aget = type(age)
yrt = type(year)
mrdt = type(is_married)
ist = type(is_true)
lgtht = type(is_light_on)
onet = type(variable_one)
twot = type(variable_two)

# Using the len() built-in function, find the length of your first name
len(first_name)

# Compare the length of your first name and your last name
first_name_length = len(first_name)
last_name_length = len(last_name)
print(f'first name has {first_name_length} characters and last name has {last_name_length}')

num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = pow(num_one, num_two)

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area_of_circle = 3.14 * (pow(radius, 2))
circum_of_circle = 2 * 3.14 * radius

# Take radius as user input and calculate the area.
user_radius = int(input("Radius: "))
area_of_circ = 3.14 * (pow(user_radius, 2))

user_first_name = input("First Name: ")
user_last_name = input("Last Name: ")
user_country = input("Country: ")
user_age = int(input("Age: "))















