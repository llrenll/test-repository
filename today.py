
'''
ef say_something():
    print("hi")

say_something()
print(type(say_something))
fu = say_something()
fu

def morning():
    print("morning")

morning()
print(type(morning))
tu = morning
tu

def my_calc(a, b):
    return a-b


result = my_calc(5, 1)
print(result)

def my_order(fruit = 'banana', drink = 'tee'):
    print("fruit = " + fruit)
    print('drink = ' + drink)
    print("--------------------------------")

my_order()
my_order('orange', 'coffee')
my_order(drink='coffee',)

#参照渡し
def my_calc(x,l = []):
    l.append(x)
    return l

result = my_calc(100)
print(result)
result2 = my_calc(50)
print(result2)


l = []
result = my_calc(100, l)
print(result)
ll = []
result2 = my_calc(50, ll)
print(result2)



def say_something(*args):
    for arg in args:
        print(arg)
    print("-----------------------")


say_something('Hi', 'kondo')
say_something('Hi', 'kondo', 'Hellow')


def menu(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
    print("-----------------------")

menu(entree = 'beef', drink = 'coffee')
d = {
    "entree":"beef",
    "drink":"ice coffee",
    "dessert": "ice"
}
menu(**d)


def f():

    global animal
    animal = "doc"
    print("f" + animal)


f()
print("global:" + animal)
print(locals())



l = [1,2,3]
i =1

try:
    print(l[i])
except:
    print("No!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

print("end")


import sys

print(sys.argv)

'''

from termcolor import colored

print('test')
print(colored('test', 'red'))
print(help(colored))