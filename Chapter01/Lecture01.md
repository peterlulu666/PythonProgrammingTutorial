# Lecture 01

## List

The list item is enclosed within square bracket

The item in the list can be any type

    - number
    - string
    - list
    
List operator and function

    - x in lst
    - x not in lst
    - lst + lstB
    - lst * n
    - lst[i]
    - len(lst)
    - min(lst)
    - max(lst)
    - sum(lst)
    - use dot notation to call function
        - lst.append
        - lst.count(item)
        - lst.index(item)
        - lst.pop()
        - lst.remove(item)
        - lst.reverse(item)
        - lst.sort(item)
        - note that append(), remove(), reverse(), sort() modify list but it will not return list
        
    
List is mutable ans string is immutable

```python
number_list = [1, 2, 3]
number_list[2] = 5
print(number_list)
# The list will be [1, 2, 5]

number_str = "123"
number_str[2] = "5"
# error
```

## Tuples        

The tuple item is enclosed in parentheses        

The item in the tuple can be any type
        
    - number
    - string
    - list
    
Tuple operator and function

    - x in tple
    - x not in tple
    - tpleA + tpleB
    - tple * n
    - tple[i]
    - len(tple)
    - min(tple)
    - max(tple)
    
Tuple is immutable                

## Object and class        

In Python, every value is stored in memory as an object. Every object belongs to a class. The object's class determines what operations can be performed on it

## Python standard library        

A module must be explicitly imported into the execution environment

```python
import <module>
```        

























