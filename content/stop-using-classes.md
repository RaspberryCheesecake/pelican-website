Title: Stop Writing (Unecessary) Classes
Date: 2017-01-23
slug: stop-writing-classes
Category: python
tags: python, classes, talks
Summary: A look at Peter Diedrich's 'Stop Writing Classes' talk. 


I listened to a great talk recently called [Stop Using Classes](https://www.youtube.com/embed/o9pEzgHorH0?feature=player_embedded&iv_load_policy=3&autoplay=1&rel=0&start=20) by Peter Diedrich. The talk goes through some of the unhelpful ways classes can be used in Python and makes good points about readability and simplicity. Here's my mindmap of the talk.
![My mindmap of the talk]({filename}/images/stop_using_classes.jpg) 

## Game of Life
Diedrich uses as an example a neat implementation of Conway's [Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) which is beautifully straightforward and avoids the tempting trap of making a class for a Cell, a class for a Board, etc. His example is so small I've copied and annotated it here (renamed a few of the variables for extra clarity):

````
""" Example Game of Life from 'Stop Writing Classes' talk by Jack Diedrich. """
import itertools


def neighbours(point):
    x, y = point
    yield x+1, y-1
    yield x+1, y
    yield x+1, y+1
    yield x, y-1
    yield x, y+1
    yield x-1, y-1
    yield x-1, y
    yield x-1, y+1


def advance(board):
    new_state = set()  # initialises a set with a blank list inside
    friends = set(itertools.chain(*map(neighbours, board)))
    cells_we_care_about = board | friends

    for point in cells_we_care_about:
        count = sum((cell in board)
                    for cell in neighbours(point))
        if count == 3 or (count == 2 and point in board):
            new_state.add(point)

    return new_state


glider = set([(0,0), (1,0), (2,0), (0,1), (1,2)])

for i in range(1000):
    glider = advance(glider)

print glider

````

What ```friends``` does requires some unpacking. First of all, ```*map(neighbours, board)``` takes the iterable returned from ```map(neighbours, board)``` and returns it. The ```*``` is a useful way to split up the returned single thing from ```map``` into each piece and feed them separately to the ```chain()``` function as arguments. Here's an example of ```*``` in action:

````
def hallo(arg1, arg2):
     print(arg1)
     print(arg2)
     print("Hallo!!")

>>> printme = ("Yes", "Indeed")
>>> hallo(printme)
Traceback (most recent call last):
  File "/usr/lib/python3.5/code.py", line 91, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
TypeError: hallo() missing 1 required positional argument: 'arg2'
>>> hallo(*printme)
Yes
Indeed
Hallo!!
````



This ```map()``` iterable is the function ```neighbours()``` applied to every point in ```board```. So ```map(neighbours, board)``` returns sets of all the live cells' neighbours. This is used as an argument to the ```chain()``` function. What ```chain()``` does is glues groups of iterable things together into a ```chain``` object. For example:
````
>>> import itertools
>>> love = itertools.chain("123", "DEF")
>>> print love
<itertools.chain object at 0x7fe58ada5810>
>>> for item in love:
...     print item
...     
1
2
3
D
E
F
>>> sling_it_into_a_set = set(love)
>>> print sling_it_into_a_set
set(['D', 'E', 'F', 1, 2, 3])
>>>
````

So it bungs all the sets of neighbours into one single set. Because of how Python sets work, this gets rid of any duplicate points - eg points which neighbour a couple of living cells should still only be mentioned once.

```| ``` is just Python's binary OR operator - so ```cells_we_care_about``` is a set which contains all points that are in the list of live cells OR the list of their neighbours

```count``` counts neighbours for each living and dead cell. Diedrich then applies the rules for Conway's Game of Life in one line: 
* A dead cell that has 3 live neighbours becomes alive
* A live cell that has 2 live neighbours remains alive
* Every other cell dies.

## Sets are awesome
One of the reasons his implementation is so tidy and has so few lines is his great use of ```set()```, one of the built-in Python types. Sets are particularly great for this problem because they contain only unique elements - if you try to add multiples of the same element to a set you only end up with one in there. This means any duplicate points are eliminated without having to think about it. 

For more examples of how to get good use out of Python's built-ins I recommend [Built in Super Heroes](https://www.youtube.com/watch?v=lyDLAutA88s) by the excellent Dave Beazley. 

