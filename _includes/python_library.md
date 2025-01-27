A Python library is a collection of programs that do a specific task, and can be called in your program by their name. Libraries make it easy to do things that would've otherwise needed you to write out, manually, the several lines of code needed to do that thing. For example, assume you need to add two numbers. The manual, non-library way of doing so would be to write something like this:

```python
x = input('Enter a number: ')
y = input('Enter another number: ')
sum = x + y
print('Their sum is:', sum)
```

Now, imagine there's a library called `compute` that does mathematical computations, and that library has a function called `add`. If you were to use this library, your code would look something like this:

```python
x = input('Enter a number: ')
y = input('Enter another number: ')
print('Their sum is:', add(x,y))
```

This might not look like much because you save just one line of code. But, for complex things, libraries and packages take away a lot of manual work.