# 1. Strings
# 2. Numbers( Int, Complex, Float)
# 3. Boolean
# 4. Lists
# 5. Tuples
# 6. Dictionary
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

# #LISTS

myList = [1,2,3,"book","pencil","spoon"]
list2 = ["laptop","sweets",6,"normal"]

myList.append("danger")
myList.pop()
myList.remove("book")
myList.pop(4)
myList.sort()
myList.reverse()

print(len(myList))
myList.insert(2, "stationary")
myList.extend(list2)

print(myList)



# # #TUPLES

myTuple = (1,2,3,4,5,3,"money")
print(myTuple)
print(myTuple[3])
print(myTuple.count(3))

#DICTIONARY

myDict = {
    "name" : "Victor",
    "city" : "Kiambu",
    "hobby" : "Music",
    "fruit" : "pineapples"
}
dict2 = {
    "sex" : "Male"
}
print(myDict.update(dict2))
print(myDict["city"])
myDict["city"] = "Nairobi"
del myDict["fruit"]
print(myDict)

print(myDict.get("hobby"))
print(myDict.clear())
print(len(myDict))

seq = ("name", "sex", "age")
dict = dict.fromkeys(seq)
print(dict)
dict = dict.fromkeys(seq, 10)
print(dict)

day_number = int(input("Enter a number: "))

def week(day_number):
    days_of_the_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days_of_the_week.get(day_number, "Invalid Day Number")

print(week(day_number))