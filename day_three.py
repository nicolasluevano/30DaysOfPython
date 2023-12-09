age = 100
height = 5.7
complex_num = 3 + 4j

base = int(input("Enter base:"))
height = int(input("Enter height:"))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

side_a = int(input("Enter side a:"))
side_b = int(input("Enter side b:"))
side_c = int(input("Enter side c:"))
perimeter = side_a + side_b + side_c
print(f'The perimeter of the triangle is {perimeter}')

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter_rectangle = 2 * (length + width)

radius = int(input("Enter radius"))
pi = 3.14
area_of_circle = pi * radius * radius
circumference_of_circle = 2 * pi * radius

y = (2 * x) -2
slope = (y2 - y1) / (x2 - x1)
y_intercept = y1 - (slope * x1)

m = (y2 - y1) / (x2 - x1)
slope = -1 / m
euclidean_distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

st1 = 'python'
st2 = 'dragon'
print(len(st1) != len(st2))

if 'on' in st1 and st2:
    print('on is present in both')

jargon = 'I hope this course is not full of jargon'

if 'jargon' in jargon:
    print('jargon is present in jargon')

if 'on' not in st1 or st2:
    print('on is not present in both')

python_length = len('python')
python_float = float(python_length)
print(str(python_float))

#how to check if number is even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f'{num} is an even number')

if type('10') == type(10):
    print('equal')
else:   
    print('not equal')

if int('9.8') == 10:
    print('equal')
else:
    print('not equal')

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
weekly_earning = hours * rate
print(f'Your weekly earning is ${weekly_earning}')

years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f'You have lived for {seconds} seconds')

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')


