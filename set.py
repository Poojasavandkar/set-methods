# #set:- is one of the 4 built-in data types in python used to stored collection of element enclosed in curley braces, it is mutable 
# # duplicates are not allowed, unordered, indexing slicing are not possible, item assignment not possible
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Sets cannot have two items with the same value.
#Set items can be of any data type:String, int and boolean data types:examples

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}


# #empty set
# p=set()
# print(type(p))

# p={11,22,33,44,55,66}
# print(p)

# #access element by loops 

# p={11,22,33,44,55}

# for i in p:
#     print(i)

# for i in range(len(p)):
#     print(i,p[i])  # 'set' object is not subscriptable

#method of set 
# 
#add()- add a element in set

# p={11,22,33,44,55}
# print(p.add(111))
# print(p)


# p={11,22,33,44,55}
# p=(p.add(39))
# print(p)

# P={"bacillis", "gols", "butki", "chimni", "chakuli"}
# P.add("chutku")
# print=(P)

#clear:-removes the element of set
chotu={"bacillis", "gols", "butki", "chimni", "chakuli"}
chotu.clear()
print(chotu) 

#add:- add  element to set

bacteria={"bacillus", "escherichia","staphalococci", "listeris"}
bacteria.add("vibrio")
print(bacteria)

#copy:- returns a copy of set

bacteria={"bacillus", "escherichia","staphalococci", "listeris"}
x=bacteria.copy()
print(x)


#difference:-Returns a set containing the difference between two or more sets

x={"bacteria","virus","fungi", "algae"}
y={"yuki", "nobi","dori","algae"}
z=x.difference(y)
print(z)

x={"bacteria","virus","fungi", "algae"}
y={"yuki", "nobi","dori","algae"}
z=y.difference(x)
print(z)


#difference update:-Removes the items in this set that are also included in another, specified set

x={"bacteris","virus", "fundgi", "algae"}
y={"yuki", "nobi", "dori", "algae"}
x.difference_update(y)
print(x)  #outout x={"bacteris","virus", "fundgi"}


x={"bacteris","virus", "fundgi", "algae"}
y={"yuki", "nobi", "dori", "algae"}
y.difference_update(x)
print(y)   #output  {"yuki", "nobi", "dori", "algae"}


#discard:-removes the perticular atom in list

virus={"corona", "rabirs", "influenza", "hepatatis"}
virus.discard("hepatatis")
print(virus)  #output  {"corona", "rabirs", "influenza"}


#intresection"-Returns a set, that is the intersection of two or more sets
x={"cherry","melon","banana", "apple"}
y={"coconut", "badam","banana","apricot"}
z=x.intersection(y)
print(z)      #output banana


#intersection.update:-Removes the items in this set that are not present in other, specified set(s

x={1,2,3,4}
y={5,7,8,9,1}
x.intersection_update(y)
print(x)     #output 1


#pop:- removes an element from set

fruit={"pooji", "apple","banana"}
fruit.pop()
print(fruit)


fruit={"pooji", "cherry","banana", "melon"}
fruit.pop()
print(fruit)

#remove:-remove am specified element

peoples={"chhaya", "surekha","muskan","pooja","ranjana"}
peoples.remove("ranjana")
print(peoples) #output {"chhaya", "surekha","muskan","pooja"}

peoples.remove("muskan")
print(peoples) #output {"chhaya", "surekha","pooja"}

#union:-Return a set containing the union of sets

x={11,22,33,44,55,}
y={11,66,77,88,99,11}
z=x.union(y)
print(z) # output  {33, 66, 99, 11, 44, 77, 22, 55, 88}


#update :- Update the set with another set, or any other iterable
x={"bella", "edward", "jackson", "bili"}
y={"isbella","jenney","bili"}
x.update(y)
print(x)    #output {'bella', 'jenney', 'edward', 'jackson', 'bili', 'isbella'}


























