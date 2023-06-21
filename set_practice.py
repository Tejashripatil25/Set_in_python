""""""
"""
1.Add a list of elements to a set | s1= {"Yellow", "Orange", "Black"},l1= ["Blue", "Green", "Red"]
EXPECTED O/P: {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
s1 = {"Yellow", "Orange", "Black"}
l1 = ["Blue", "Green", "Red"]
print(s1.union(l1))
o/p: {'Green', 'Black', 'Orange', 'Blue', 'Red', 'Yellow'}

##2 option
s1= {"Yellow", "Orange", "Black"}
l1= ["Blue", "Green", "Red"]
s1.update(l1)
print(s1) 
===========================================================================
2.Return a new set of identical items from two sets |set1 = {10, 20, 30, 40, 50} & set2 = {30, 40, 50, 60, 70} 
EXPECTED O/P:{40, 50, 30}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
o/p: {40, 50, 30}
===========================================================================
3.Get Only unique items from two sets | set1 = {10, 20, 30, 40, 50} & set2 = {30, 40, 50, 60, 70}
EXPECTED O/P: {70, 40, 10, 50, 20, 60, 30}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))
o/p: {70, 40, 10, 50, 20, 60, 30}
===========================================================================
4.Update the first set with items that don’t exist in the second set| set1 = {10, 20, 30} & set2 = {20, 40, 50}
EXPECTED O/P: set1 {10, 30}.
set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))
o/p: {10, 30}
===========================================================================
5.Remove items from the set at once | set1 = {10, 20, 30, 40, 50} EXPECTED O/P: {40, 50}
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10,20,30})
print(set1)
##2 option
set1 = {10, 20, 30, 40, 50}
set1.remove(10)
set1.remove(20)
set1.remove(30)
print(set1)
o/p: {50, 40}
===========================================================================
6.Return a set of elements present in Set A or B, but not both |
set1 = {10, 20, 30, 40, 50} & set2 = {30, 40, 50, 60, 70} EXPECTED O/P:{20, 70, 10, 60}set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))
o/p: {20, 70, 10, 60}
===========================================================================
7.Check if two sets have any elements in common. If yes, display the common elements|
 set1 = {10, 20, 30, 40, 50} & set2 = {60, 70, 80, 90, 10} 
EXPECTED O/P:Two sets have items in common   {10}
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1.intersection('Two sets have item in common',set2))
o/p: Two sets have item in common: {10}
===========================================================================
8.Update set1 by adding items from set2, except common items |set1 = {10, 20, 30, 40, 50} & set2 = {30, 40, 50, 60, 70}
 EXPECTED O/P: {70, 10, 20, 60}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))
o/p: {20, 70, 10, 60}
===========================================================================
9.Remove items from set1 that are not common to both set1 and set2 |
 set1 = {10, 20, 30, 40, 50} & set2 = {30, 40, 50, 60, 70} EXPECTED O/P:{40, 50, 30}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
o/p:{40, 50, 30}
===========================================================================
10.Does converting an object to a set maintain the object’s order? 
No,set is unordered.and background datastructure is hashtable.
===========================================================================
11.CHECK if a set a subset of another set | a = {4,5} b = {1,2,3,4,5}.
a = {4,5}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))
o/p: True
===========================================================================
12.Check if a specific value exists in a set | s = {5,7,9} check 5.
s = {5, 7, 9}
if 5 in s:
    print('True')
else:
    print('False')
o/p: True
==========================================================================
13. Add an element to a set | s = {'a','b','c'}
s = {'a','b','c'}
#s.update({'d','e', 'f'})
s1 = {'d','e','f'}
s.update(s1)
print(s)
o/p: {'f', 'a', 'c', 'd', 'e', 'b'}
==========================================================================
14.Make a copy of a set | s1 = {'a','b','c'}
s1 = {'a','b','c'}
s2 = s1.copy()
print(s2)
o/p: {'b', 'a', 'c'}
==========================================================================
15.Check if a set is a superset of another set |  a = {10,20,30} b = {10,20}
a = {10, 20, 30}
b = {10, 20}
if a.issuperset(b):
    print("True")
else:
    print("False")
o/p: True
========================================================================== 
16.Convert a set to a list | a = {4,2,3}
a = {4,2,3}
b = list(a)
print(b)
o/p: [2, 3, 4]
=========================================================================
17.How can you iterate on values in a set? | s = {'a','b','c','d','e'}
s = {'a','b','c','d','e'}
for i in s:
    print(i, end=",")
o/p: c,d,b,a,e,
==========================================================================
18.Return the length of a set | s = {'a','b','c','d','e'}
s = {'a','b','c','d','e'}
print(len(s))
o/p: 5
==========================================================================
19.Find the union of 2 sets. | s1 = {1,2,3,4,5} s2 = {4,5,6,7,8}   | EXPECTED O/P: {1, 2, 3, 4, 5, 6, 7, 8}
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.union(s2))
o/p: {1, 2, 3, 4, 5, 6, 7, 8}
==========================================================================
20. Find the elements in s1 that are not in s2 | s1 = {1,2,3,4,5} s2 = {4,5,6,7,8}
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.difference(s2))
o/p:{1, 2, 3}
===========================================================================
21.Remove an element from a set | s = {'x','y','z'}  REMOVE Z
s = {'x', 'y', 'z'}
s.discard('z')
print(s)
o/p: {'x', 'y'}
===========================================================================
22.Remove and return an unspecified element from a set | s = {'z','y','x'}
s = {'z','y','x'}
print(s.pop())
s.add('z')
print(s)
o/p: 
y
{'x', 'z'}
===========================================================================
23.Add all elements from another set to an existing set | a = {1,2,3} b = {3,4,5}| EXPECTED O/P:{1, 2, 3, 4, 5}
a = {1,2,3}
b = {3,4,5}
a.update(b)
print(a)
o/p: {1, 2, 3, 4, 5}
===========================================================================
24.Remove all elements from a set | a = {1,2,3}
a = {1,2,3}
a.clear()
print(a)
o/p: set()
===========================================================================
25.Remove an element from a set if it exists. |  a = {1,2,3}
a = {1,2,3}
#a.remove(4)
#print(a)-------KeyError: 4
a.remove(3)
print(a)----------------{1, 2}
===========================================================================
26. Can a set be accessed by index? |  (its Theory questions)
No, indexing and slicing is not supported.
===========================================================================
27.What is the difference between a set and a tuple?  | (its Theory questions)
set is mutable and datastructure is hashtable, tuple is immutable and datastructure is array
===========================================================================
28.What is the difference between a set and a frozenset? | (its Theory questions)
frozenset is immutable and set is mutable
===========================================================================
29.Python program to find the missing of s1 in s2 | s1= {1, 2, 3, 4, 5, 6}, s2={4, 5, 6, 7, 8} | expected o/p : {1,2,3}
s1= {1, 2, 3, 4, 5, 6}
s2={4, 5, 6, 7, 8}
s1.difference_update(s2)
print(s1)
o/p: {1, 2, 3}
============================================================================
30.remove last item from a given set | s1={'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}    
s1={'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
s1.remove('Blue')
print(s1)
o/p: {'Yellow', 'Green', 'Orange', 'Black', 'Red'}
===========================================================================
"""
