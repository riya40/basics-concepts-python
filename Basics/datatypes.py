# data types -
a = 10
b = 2.0
c = 9 + 8j
d = 'Vizag'

print("the numeric datatypes are", type(a), type(b), type(c), type(d))

# sequence type
# list - group of elements;
l = [10, 20, 30.123, 15, 20, 'xyz']
print(l)
print(type(l))
print(l.append(45))
print(l)
print(l.insert(2, 34))
print(l)
print(l.pop())

# tuple - group of fixed elements
t = (10, 20, 30.12, 15, 20, 'abc')
print(t)
print(t[0])
print(t[1:5])

# string - group of characters
string = 'priya'
print(string)
string = 'priya' + "riya" + "priyanka"
print(string)
print(string[0])
print(string[-1])
print(string * 4)
print(string + "5")
print(string + string[5])
print(string[5:7])

# set - group of unique elements
set1 = {10, 20, 30, 12, 20, 'abc'}
set2 = {23, 34, 54, 12}
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))


# Boolean Datatype
print(type(True))
#print(type(true))

d = {'priya': 20, 'anu': 29, 'srinu': 43}
print(d)
print(d.get(2))
print(d['anu'])
d['priya'] = 'priyanka'
print(d)
print(d.keys())
