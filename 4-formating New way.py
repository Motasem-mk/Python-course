n = "Motasem"
a = 40
s = "Python"
r = 14

print("My name is {:s} i'm {:d} i'm{} devlopper,my rank {:f}".format(n,a,s,r))
print("My name is {:s} i'm {:d} i'm{} devlopper,my rank {:.2f}".format(n,a,s,r))
print("My name is {:.3s} i'm {:d} i'm{} devlopper,my rank {:.1f}".format(n,a,s,r))

money = 459987324567
print("my bank account balance is {} ".format(money))
print("my bank account balance is {:,d} ".format(money))

one = 1
two = 2
three = 3
four="four"
print("n{}, n{},  n{}".format(one,two,three))
print(" n{1} , str {3:.3s}  n{2:.2f} , n{0}".format(one,two,three,four))

name = "Motasem"
age = 40
skills = ["Python","Hive","Hadoop"]

print(f"my name is {name} , i'm {age} and my skills are : {skills}")
sk=",".join(skills)
print(f"my name is {name} , i'm {age} and my skills are : {sk}")

 