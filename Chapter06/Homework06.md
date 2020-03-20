# CS 100 2017F Homework 06

## Problem 1.

This problem provides practice using a while True loop.
 
Write a function named `twoWords` that gets and returns two words from a user. The first word is of a specified length, and the second word begins with a specified letter.

The function `twoWords` takes two parameters:

    1. an integer, `length`, that is the length of the first word and
    2. a character, `firstLetter`, that is the first letter of the second word. The second word may begin with either an upper or lower case instance of `firstLetter`.

The function `twoWords` should return the two words in a list.

Use a `while` True loop and a `break` statement in the implementation of `twoWords`.

The following is an example of the execution of `twoWords`:

```
print(twoWords(4, 'B'))
A 4-letter word please two
A 4-letter word please one
A 4-letter word please four
A word beginning with B please apple
A word beginning with B please pear
A word beginning with B please banana
['four', 'banana']
```

## Problem 2.

Write a function named `twoWordsV2` that has the same specification as Problem 1, but implement it using `while` and not using `break`. (Hint: provide a different boolean condition for `while`.)

Since only the implementation has changed, and not the specification, for a given input the output should be identical to the output in Problem 1.

Problem 3.
Do problem 5.29 in the textbook. (This problem is the same in editions 1 and 2.)

Problem 4.
Do problem 5.33 in the textbook. (This problem is the same in editions 1 and 2.)

Problem 5.
Write a function named `enterNewPassword`. This function takes no parameters. It prompts the user to enter a password until the entered password has 8-15 characters, including at least one digit. Tell the user whenever a password fails one or both of these tests

