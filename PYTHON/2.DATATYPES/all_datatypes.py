# 1. Strings
# 2. Numbers( Int, Complex, Float)
# 3. Boolean
# 4. Long
# 5. Lists
# 7. Tuples
# 8. Dictionary
import math


#STRINGS
city = "nair|obi"
print(city)
print(city.find("a"))
print(city.count("a"))
print(type(city))
print(len(city))
print(city[2])
print(city[4:])

firstName = "Debbie"
secondName = "Njenga"
print(firstName + " " + secondName)
print(city.strip())
print(city.split('|'))
print(city.capitalize())

#NUMBERS
a = 10 
b = 10.52
# c = 4 + 2i
print(a)
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a**b)
print(math.pow(a,b))
print(math.sqrt(a))
print(math.floor(b))
print(math.ceil(b))

#BOOLEAN
isWorking = True
print(isWorking)
isWorking = False
print(isWorking)