num1 = 42 #primitive data type,number, specifically integer
num2 = 2.3 #primitive data type,number, specifically float
boolean = True #primitive data type, boolean
string = 'Hello World' #primitive data type, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#dictionary
fruit = ('blueberry', 'strawberry', 'banana')
#tuple
print(type(fruit))
#will print the type of variable, which is a tuple
print(pizza_toppings[1])
#will print pizza topping at index 1, which is the string "Sausage"
pizza_toppings.append('Mushrooms')
#will add the string "Mushrooms" to the pizza_toppings list at the end
print(person['name'])
#will print from the dictionary the value to the key "name", which is "John"
person['name'] = 'George'
#will change the value of the "name" in the dictionary to "George"
person['eye_color'] = 'blue'
#adds a new key value pair to the end of the dictionary
print(fruit[2])
#will print the fruit in tuple at index2, which is "banana"

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#condition with if and else, will check if a variable num1> integer 45

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#will check length of a string in a conditional with 3 different outputs depending on the length

for x in range(5):
    print(x)
# for loop printing each variable from 0-4
for x in range(2,5):
    print(x)
#for loop printing each variable from range 2 to 5
for x in range(2,10,3):
    print(x)
#for loop printing each variable from 2-10 incrementing by 3 each loop
x = 0
while(x < 5):
    print(x)
    x += 1
#while loop printing the variable x until it reaches 5, adding 1 to x each time

pizza_toppings.pop()
#remove the last item on the pizza_toppings list
pizza_toppings.pop(1)
#remove the item at index 1 on the pizza_toppings list

print(person)
#prints the person dictionary
person.pop('eye_color')
#removes the "eye_color" key value pair that we had added previously
print(person)
#will print the entire person dictionary now without the "eye_color"

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#for loop, with conditional statement, will break the loop when we reach "olives" or the end, skips over pepperoni

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#function that uses for loop. Loops through the range 0-9 (10 times total), will print "Hello" each loop

print_hello_ten_times()
#calls function above

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
#for loop inside a function passing in the argument 4 into the range. Will print "Hello" from indexes 0-3, a total of 4 times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
#function that if an argument is passed in, will loop through that number and print "Hello" that many times, or if not argument is passed in, will use the parameter x=10


"""
Bonus section
multiline comment
"""

""" print(num3)
- NameError: name <variable name> is not defined
 num3 = 72"""

""" fruit[0] = 'cranberry'
- TypeError: 'tuple' object does not support item assignment"""

"""print(person['favorite_team']
- KeyError: 'favorite_team' """

""" print(pizza_toppings[7])
- IndexError: list index out of range"""

"""   print(boolean)
- IndentationError: unexpected indent"""

""" fruit.append('raspberry')
- AttributeError: 'tuple' object has no attribute 'append'"""

"""fruit.pop(1)
- AttributeError: 'tuple' object has no attribute 'pop'"""