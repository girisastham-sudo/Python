print("hello")
a=10
b=20
c=a+b
print(c)
a=20
c=30
print(a*c)
a=4
b=2
print(a%b)
a=10
b=5
print(a/b)
a=10
print(type(a))
a="giri"
print(type(a))
a=int(10)
b=int(20)
c=print(a+b)
a=int(input())
b=int(input())
c=a+b
print(c)
a=input("Enter your name: ")
print(a)
b=int(input("Enter your age: "))
print(b)
a=input()
b=input()
c=a+b
print(c)
print("giri")
print("hello")
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
 print("Five is greater than two!") 
else:
    print("invalid number")
    
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()