# Midterm 2016

## Question 12

Write a function named bigCount that counts how many elements in a list of numbers are greater than a threshold value and returns that count.


The function bigCount takes two parameters:
- numList, a list of numbers
- threshold, in integer

For example, the following would be correct output:

```
>>> someNums = [-5, 6, 3, 0, 7]
>>> print(bigCount(someNums, 2))
>>> 3
```


## Question 13

Write a function named getDate. The function getDate takes one parameter:
- message, a string

In addition to the parameter message, the function getDate should prompt the user for two items of input: first the month, then the day.

The function getDate should produce two kinds of output. It should
- print out the month, day and message, separated by spaces
- return a string consisting of the month and day, separated by a space 

For example, the following would be correct input and output:

```
>>> today = getDate('is a great day!')
What month is it? February
What day is it? 15
February 15 is a great day!
>>> print(today)
February 15
```




