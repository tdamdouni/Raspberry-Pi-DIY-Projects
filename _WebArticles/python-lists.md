# Python Lists

_Captured: 2017-05-10 at 23:51 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/python/python-list)_

This tutorial will teach you everything you might want to know about lists in Python 3. It will assume that you've got a Raspberry Pi running Raspbian, and that you're set up with a monitor, mouse and keyboard.

## Following along with this guide

If you want to follow the examples and code snippets in this guide, you'll need to fire up Python 3 in interactive mode. You can do this in one of two ways;

![Starting Python IDE](https://learn.pimoroni.com/static/repos/learn/python/starting-python-ide.jpg)

> _At your Raspberry Pi desktop, click the Menu, then Programming and finally "Python 3", a new window will pop up which you can type Python code into_

  * If you're looking at your Pi's terminal, a black screen with only text, just type "python3" and hit enter.

When you see Python code below prefixed with `>>>` these are snippets that I'm typing straight into the Python interactive shell, you cam use it to play with these examples and see what else you can do.

![Python shell in action](https://learn.pimoroni.com/static/repos/learn/python/python-shell.jpg)

## Introduction

In Python, a list is an easy concept to understand; it's just a series of usually related, similar things, in a specific order. If you understand the reasons why you'd use a list written down on paper, then you should already understand where you might want to use one in Python.

![List introduction](https://learn.pimoroni.com/static/repos/learn/python/list-intro.jpg)

> _There are several important things to understand about lists before you start using them:_

  * They can contain anything- numbers, text, objects, classes, functions, etc
  * The things they contain should almost always be of the same type to avoid confusion
  * List items have a numeric key, think of a list as being numbered: 0, 1, 2, 3.. etc
  * List items have an order, usally the order you added them in, and can be sorted into different orders
  * In a list, the first item is at 0. Counting from 0 can be confusing at first, but it makes more sense to a computer.

We're going to cover a few basic Python list topics to let you get the most out of this useful tool, this tutorial will have the Raspberry Pi in mind and so most of the suggestions are to benefit your Raspberry Pi adventures.

  1. Creating lists
  2. Adding items to lists
  3. Accessing lists
  4. Iterating through lists
  5. Sorting lists
  6. Changing items in lists
  7. The magical world of "list comprehensions"

## Creating Lists

Python has a couple of ways to create lists which behave differently:
    
    
    my_list = ['a', 'b', 'c']
    
    # Or...
    
    my_list = list("abc")
    

The normal syntax for creating a list consists of square brackets containing every item you want in your list separated by commas.

Both of these methods can be used to create an empty list:
    
    
    my_list = []
    my_other_list = list()
    

However, the correct way to create a new, empty list is:
    
    
    my_list = []
    

Why? Well, the `list()` function attempts to convert whatever you pass it into a list. This means Python has to spend time looking up the `list` function and figuring out what you're passing to it- even if you pass nothing! A simple `[]` in Python doesn't involve a function lookup and is a tiny bit faster! More important, however, it's much, much neater. Good programming practises often involve a lot of neatness!

### Why use Python's `list()` at all?

It comes in handy occasionally. If you pass it a string, the result is a list which contains each letter in that string:
    
    
    >>> list("abc")
    ['a', 'b', 'c']
    

If you pass it a tuple `("like", "this")` it will turn that tuple into a list:
    
    
    >>> list(("like", "this"))
    ["like", "this"]
    

If you pass it a range it will give you a list. Try typing just a range, and see what you get:
    
    
    >>> range(0,4)
    range(0, 4)
    

... well, that's... uh... not helpful! ... but wait:
    
    
    >>> list(range(0,4))
    [0, 1, 2, 3]
    

Magic!

The `list()` function can be very handy for peering into lazy things like ranges, which don't provide all of their values unless you ask nicely.

However, apart from experimenting in Interactive Python there's little practical use for `list()` and the many things it'll accept. If you're creating an empty list then using `[]` is slightly faster and a lot tidier!

### Strings are list-y too!

A string in Python behaves a little like a list, observe:
    
    
    >>> "hello"[0] # Don't forget, the first item is always at index 0
    'h'
    >>> "hello"[2]
    'l'
    

or perhaps:
    
    
    >>> for letter in "hello":
    ...     print(letter)
    ...
    h
    e
    l
    l
    o
    

## Adding Items to Lists

Imagine you've got a "To do" list, and you realise an extra task has slipped your mind. You're doing to want to add it to the end of your list. The same applies in Python, which has us covered with the `append` method:
    
    
    >>> my_list = ['Do the dishes', 'Tidy up']
    >>> print(my_list)
    ['Do the dishes', 'Tidy up']
    >>> my_list.append('Walk the dog')
    >>> print(my_list)
    ['Do the dishes', 'Tidy up', 'Walk the dog']
    

You can also _add_ items to your list with the `+` operator:
    
    
    >>> my_list += ['Feed the cat']
    >>> print(my_list)
    ['Do the dishes', 'Tidy up', 'Walk the dog', 'Feed the cat']
    

Or, if you've just discovered a list of tasks between the sofa cusions and want to remember to do those too, even add whole lists together:
    
    
    >>> my_list += ['Find the TV remote', 'Mow the lawn']
    >>> print(my_list)
    ['Do the dishes', 'Tidy up', 'Walk the dog', 'Feed the cat', 'Find the TV remote', 'Mow the lawn']
    

## Accessing Lists

Whew, that's a lot of tasks! Making a list of things is all well and go, but if we don't go through and do our tasks in some way or another it'll be a waste of time.

Python lists have a specific order, usually the order in which you created them. Each item is given an index from 0 onwards depending upon this order, and we can use those indexes to access lists.
    
    
    >>> my_list = ['Do the dishes', 'Tidy up', 'Walk the dog', 'Feed the cat', 'Find the TV remote', 'Mow the lawn']
    >>> my_list[0]
    'Do the dishes'
    >>> my_list[2]
    'Walk the dog'
    

When you do this, your list stays the same. It's the pen and paper equivalent of glancing at a specific item and checking what it says.

What if we want to access our list one item at a time, do the task and remove it from the list? This is the pen and paper equivilent of striking out each item in our list. We can do it with the `pop()` method. "pop" will pop off and return the very last item of your list, resulting in your list being one item shorter.
    
    
    >>> my_list = ['Do the dishes', 'Tidy up', 'Walk the dog', 'Feed the cat', 'Find the TV remote', 'Mow the lawn']
    >>> my_list.pop()
    'Mow the lawn'
    >>> my_list
    ['Do the dishes', 'Tidy up', 'Walk the dog', 'Feed the cat', 'Find the TV remote']
    

Every time we access an list using this method, we throw the last item away, so our list is now:
    
    
    ['Do the dishes', 'Tidy up', 'Walk the dog', 'Feed the cat', 'Find the TV remote']
    

![List pop](https://learn.pimoroni.com/static/repos/learn/python/list-start.jpg)

> _This is useful if you want to work through a queue of things in order and don't need to worry about them again. But what if you want to work from the top down? Easy:_
    
    
    >>> my_list = ['Do the dishes', 'Tidy up', 'Walk the dog', 'Feed the cat', 'Find the TV remote']
    >>> my_list.pop(0)
    'Do the dishes'
    

When you give `pop()` a number, it will pop that specific item from your list. Since lists are numbered from 0 onwards, you `pop(0)` to get the first item. This will work for any list index, right up until that index can no longer be found in your list:
    
    
    >>> my_list = ['Do the dishes', 'Tidy up', 'Walk the dog', 'Feed the cat', 'Find the TV remote']
    >>> my_list.pop(1)
    'Tidy up'
    >>> my_list
    ['Do the dishes', 'Walk the dog', 'Feed the cat', 'Find the TV remote']
    

![List pop](https://learn.pimoroni.com/static/repos/learn/python/list-crossed-out.jpg)

> _Now the previous list item at position 1 ( the second item in the list ) has been removed, and 'Walk the dog' has replaced position 1._
    
    
    >>> my_list.pop(1)
    'Walk the dog'
    >>> my_list
    ['Do the dishes', 'Feed the cat', 'Find the TV remote']
    

If we kept going, we'd eventually run out of items at position 1. Python will produce an `IndexError` to let you know you're trying to access a list item that doesn't exist:
    
    
    >>> my_list.pop(1)
    'Feed the cat'
    >>> my_list.pop(1)
    'Find the TV remote'
    >>> my_list.pop(1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: pop index out of range
    

## Iterating Through Lists

While you can access items from a list one at a time, this would lead to really, really long-winded code. If you had two things in your list it might look like this:
    
    
    >>> my_list = ['Do the dishes', 'Feed the cat']
    
    >>> list_item = my_list.pop()
    >>> print(list_item)
    'Do the dishes'
    
    >>> list_item = my_list.pop()
    >>> print(list_item)
    'Feed the cat'
    

Now... imagine what might happen if you tried this for 200 items, or 2000! Fortunately Python has a solution to this in the form of iteration:
    
    
    >>> my_list = ['Do the dishes', 'Feed the cat']
    >>> for list_item in my_list:
    ...     print(list_item)
    ...
    'Do the dishes'
    'Feed the cat'
    

In this example it doesn't matter if your list is two, twenty, or two billion items long; the code will still be exactly the same length.

If you want to go backwards through your list, you can reverse it with `reversed`:
    
    
    >>> my_list = ['Do the dishes', 'Feed the cat']
    >>> for list_item in reversed(my_list):
    ...     print(list_item)
    ...
    'Feed the cat'
    'Do the dishes'
    

If you need the index of each list item as you step through, you must "enumerate" your list like this:
    
    
    >>> my_list = ['Do the dishes', 'Feed the cat']
    >>> for index, list_item in enumerate(my_list):
    ...     print(index, list_item)
    ...
    (0, 'Do the dishes')
    (1, 'Feed the cat')
    

And you can combine reversing and enumerating:
    
    
    >>> my_list = ['Do the dishes', 'Feed the cat']
    >>> for index, list_item in enumerate(reversed(my_list)):
    ...     print(index, list_item)
    ...
    (0, 'Feed the cat')
    (1, 'Do the dishes')
    

Notice that the items in the list have switched places, but their indexes have not. A list will always be indexed from 0 to N, no matter how many times you sort or reverse it.

## Sorting Lists

Sooner or later, you're going to want to sort a list. Perhaps your list of tasks have a priority, or you want to do them in alphabetical order. Either way, every Python list has a `sort` method which likes to sort things by alphabetic order:
    
    
    >>> my_list = ['z', 'e', 'b', 'r', 'a']
    >>> my_list.sort()
    >>> my_list
    ['a', 'b', 'e', 'r', 'z']
    

Or by numeric order:
    
    
    >>> my_list = [11, 5, 10, 1]
    >>> my_list.sort()
    >>> my_list
    [1, 5, 10, 11]
    

Or by anything you like:
    
    
    >>> my_list = [(10, 'Do the dishes'), (2, 'Walk the dog'), (4, 'Feed the cat')]
    >>> my_list.sort(key=lambda task: task[0])
    >>> my_list
    [(2, 'Walk the dog'), (4, 'Feed the cat'), (10, 'Do the dishes')]
    

In the above example, we've used Tuples to pair a priority with each task. Now we can pass a special function, called a key function, to sort which uses that priority as the sort order. If you've not seen `lambda` before don't worry, this is juat a quick example!

If you want to sort something in reverse order, you can specify `reverse=True` like so:
    
    
    >>> my_list = [11, 5, 10, 1]
    >>> my_list.sort(reverse=True)
    >>> my_list
    [11, 10, 5, 1]
    

## Changing Lists

Suppose we wanted to specify exactly what 'Do the dishes' means, just in case we rope someone else into doing our chores. Let's change that item on our list to be more specific:
    
    
    >>> my_list = ['Do the dishes', 'Feed the cat']
    >>> my_list[0] = 'Load the dishwasher, turn it on'
    >>> print(my_list)
    ['Load the dishwasher, turn it on', 'Feed the cat']
    

That's better. By accessing the first item on the list ( which is always at position zero ) and assigning it a new value we've updated our list with a more descriptive task.

Sometimes we want to change one or more items in a list. Let's say we wanted to assign each chore to a different person, right now we'll just use "me" since nobody has volunteered to help us. Let's modify our list to add " ( me )" to the end of every chore:
    
    
    >>> my_list = ['Do the dishes', 'Feed the cat']
    >>> for index, list_item in enumerate(my_list):
    ...     my_list[ list_item ] += " ( me )"
    ...
    >>> print(my_list)
    ['Do the dishes ( me )', 'Feed the cat ( me )']
    

This works, but it's a slightly inelegant way of updating lists. This is where things get a little scary. Python has a clever function called `map` which take a list, and a function and runs that function against every item in the list.

First, let's make a function for assigning tasks to people:
    
    
    >>> def assign_task(task):
    ...     return task + " ( me )"
    ...
    

Now, let's use it on our list:
    
    
    >>> my_list = ['Do the dishes', 'Feed the cat']
    >>> my_list = map(assign_task, my_list)
    >>> print(my_list)
    ['Do the dishes ( me )', 'Feed the cat ( me )']
    

Magic! The `map` function has done the looping for us, stepping through and calling `assign_task` for each item in our list.

## The magical world of "list comprehensions"

If the idea of `map` hasn't put you off, Python has some fantastical and powerful features in the guise of list comprehensions.

List comprehensions allow you to describe lists of things in a very condensed way which would be natural to mathmeticians used to describing sets. Unfortunately, most of us aren't mathmaticians so the concept of comprehensions can look a little confusing at first.

Let's start with our task assignment challenge from above and try to do a `map` using list comprehension:
    
    
    >>> my_list = [task + ' ( me )' for task in ['Do the dishes', 'Feed the cat']]
    >>> print(my_list)
    ['Do the dishes ( me )', 'Feed the cat ( me )']
    

![Map using list comprehension](https://learn.pimoroni.com/static/repos/learn/python/map-using-list-comprehension.jpg)

> _Whoa! What happened there? Python has understood that for each task in our list, we want to add ourselves as the dooer and save the result as a new list._
    
    
    task + ' ( me )'
    

Is where we're adding ourselves to the end of each task. Perplexingly, this appears _before_ the for loop this time but Python understands that we're trying to say: "Add ' (me)' to each task in my list".

The second half instructs Python to step through the list:
    
    
    for task in ['Do the dishes', 'Feed the cat']
    

And, finally, to make the list comprehension actually function it's got to be wrapped in `[]` or Python won't be able to figure out what we're trying to do.

If we wanted to do this to our original list, we could:
    
    
    >>> my_list = ['Do the dishes', 'Tidy up', 'Walk the dog', 'Feed the cat', 'Find the TV remote', 'Mow the lawn']
    >>> print( [task + ' ( me )' for task in my_list] )
    ['Do the dishes ( me )', 'Tidy up ( me )', 'Walk the dog ( me )', 'Feed the cat ( me )', 'Find the TV remote ( me )', 'Mow the lawn ( me )']
    

List comprehensions are also great for mathmatical madness, say you wanted the square of every number from 0 to 99:
    
    
    >>> [x * x for x in range(0, 100)]
    [0, 1, 4, 9, 16, 25 ...
    

And what if we wanted a list of all 10,000 possible 4-digit pin combinations:
    
    
    >>> [str(a) + str(b) + str(c) + str(d) for a in range(0,10) for b in range(0,10) for c in range(0,10) for d in range(0,10)]
    ['0000', '0001', '0002', '0003' ... '9999']
    

Bonkers, of course, but it's a good example of how we can generate a great big list of possibly meaningful things with just one line of code.

# Putting it all together

You should now have a better understanding of Python lists, now you should put it into practise! Create yourself a task list in Interactive Python, `append` a few tasks onto it, sort it, `pop` your first task off and... well... get to work!

Need something for this project? You can use the links below to add products to your [Pimoroni Shop](http://shop.pimoroni.com/) basket for easy checkout.

Want to checkout or change something? Click here to [view your cart](http://shop.pimoroni.com/cart).

## Phil Howard

Phil is Pimoroni's software guru, instantly recognisable by his somewhat pirate-themed moustache growing attempts. Usually found buried neck deep in Python libraries, he's also been known to escape on occasion and turn out crazy new products. If you need a helping hand, he's a prolific Twitter user and rampages around the forums like a T-Rex. Ask him if you need help with Pimoroni's software libraries, or Propeller HAT.
