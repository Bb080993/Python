#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#will return 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#will create an error message bc the Number_of_days... function has not been defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#will return 5. Will not return 10 bc once you hit the first return you exit the function


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#will return 5. will not print 10 bc after you hit the first return, you exit the function, and print is below the return in the code


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#will print 5 when function is called, but then will not print anything for x because nothing was returns
# After trying, I guess it will specifically print none for x because the function doesn't have a return


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#will print 3 and 5, then none again because there was no return
#we specifically got 3, 5 and a typeError after running

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#I think it will print the return "25" because it changed the numbers 2 and 5 into strings, and adding string numbers together smooshes them together instead of actually performing the math


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#will print 100, then return 10 to be printed outside the function


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#first statement prints 7
#second statement prints 14
# third statement prints 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#will return 8 to the print statement and then print 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#statement above function prints b as define(500)
#first statement below prints the b we see outside the function (500)
#second statement prints the b we see inside the function (300)
#third statement prints the b outside the function again (500)


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#statement above prints b as defined (500)
#statement below function prints b as defined(500)
#function call prints b(300) inside function AND returns that b to the function call, but then that function has no print, so we dont see it on the console
#last statement prints the b from above function (500)


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#500, 500, 300, 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#1,3, 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#1,3,5,10