#We learned different datatypes, int, str, float, and boolean
#fetching datatypes using type method
x = 50
print(x)
print("the value for x is", type(x))
h = 165.75
print(h)
print("the value for h is", type(h))
is_student_present = True
print(is_student_present)
print("the value for is_student_present is", type(is_student_present))
city = "Toronto"
print(city)
print("the value for city is", type(city))

#typeconversions
x = float(x)
print("the float value of x is", x)
h = int(h)
print("the integer value of h is", h)
z = 10
z = str(z)
print("the string value of z is", z)
#c = int(city)
#print("the integer value of c is", c)

#reversingstring - stringname[startindex:endingindex:-1]
string1 = "hello"
s1 = string1[::-1]
print("the reverse string for hello is", s1)