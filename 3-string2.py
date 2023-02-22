a="i love python"
print(a.index("p"))
print(a.index("y",3,12))
#print(a.index("h",0,4))

print(a.find("h",0,4))

b="Motasem"
print(b.rjust(10))
print(b.rjust(10,"*"))
print(b.ljust(10))
print(b.ljust(10,"*"))


print(b[3])

c = "I love Python  hive and hadoop"
print(c.split())
d = ''' i love python 
and hadoop 
and hive 
'''
print(d.splitlines())
e = 'I love python\nHadoop\nand hive'
print(e.splitlines())
print("*"*60)
f = "i love\tpython\tand hadoop\tand hive"
print(f.expandtabs())
print(f.expandtabs(10))
print("*"*60)
one = "I Have A 5G Mobile Phone"
two = "I Have A 5g Mobile Phone"
print(one.istitle())
print(two.istitle())
print("*"*60)

three=" "
four = ""
print(three.isspace())
print(four.isspace())
print("*"*60)

five = "i love python"
six = "i love pYthon"

print(five.islower())
print(six.islower())
print("*"*60)
seven = "I LOVE PYTHON"
eight = "I LOVE PyTHON"
print(seven.isupper())
print(eight.isupper())
print("*"*60)
nine = "Motasem1983_1"
ten="motasem_mk@"
eleven = "MOtasem--mk"
twilve = "1motasm"
print(nine.isidentifier())
print(ten.isidentifier())
print(eleven.isidentifier())
print(twilve.isidentifier())
print("*"*60)

x="assjbljdfg"
y="qwerrt123"
print(x.isalpha())
print(y.isalpha())
print(x.isalnum())
print(y.isalnum())
print("*"*60)

z="@#"
print(z.isalnum())

#--------------------------------
#replace value , new value , count

first = "I love python and hive and hadoop and kafka "

print(first.replace("and",","))
print(first.replace("and",",",2))
print("*"*60)

#join (iterable ), to convert list or tuple into a string  the opposite of split 
second = ["i","love","python","and","HIve"]

print(" ".join(second))
print("-".join(second))
print(",".join(second))
print(type(" ".join(second)))