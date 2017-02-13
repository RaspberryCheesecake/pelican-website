Title: Monkey Patching Reprise
Date: 13-02-2017
slug: monkey-patching
Tags: Ruby, Python

It turns out that things aren't as simple as they seemed in my last post. A couple of people have pointed out to me that Python can indeed do monkey patching - so what's the difference between this and Ruby? Am I just making a fuss over nothing? First of all, to some proper definitions.

#What Even Is Monkey Patching?
It's also known as guerilla (/gorilla) patching, hot-fixing, and more recently, 'duck-punching'.

>**Geoffrey**: Now, you went to PyCon a couple months ago. And it’s well-known that in the Python world, they frown on monkey-patching. Do you think they would think more positively of duck-punching?

>**Adam**: No, I think they will continue to look down on us, no matter how awesome and hilarious we become.

>**Voice In Background**: Isn’t that the truth.

>**Geoffrey**: I also have Patrick Ewing. Is this a good idea, and will it catch on?

>**Patrick Ewing**: Well, I was just totally sold by Adam, the idea being that if it walks like a duck and talks like a duck, it’s a duck, right? So if this duck is not giving you the noise that you want, you’ve got to just punch that duck until it returns what you expect.

>[Transcript from Geoffrey Grosenbach podcast](https://web.archive.org/web/20120114085702/http://podcast.rubyonrails.org/programs/1/episodes/railsconf-2007) at RailsConf2007

Monkey patching can mean some subtly different things:

* Changing a class's methods at runtime
* Changing a class's methods at runtime *and making all the instances of that class change after the fact*

As pointed out in [this thread on StackOverFlow](http://stackoverflow.com/questions/192649/can-you-monkey-patch-methods-on-core-types-in-python) by Dan Lenski, both variants are indeed possible with Python. Here's an example:


````
class Widget:
    def __init__(self):
       pass
    def who_am_i(self):
       print("I'm a widget")

>>> my_widget = Widget()
>>> my_widget
<Widget object at 0x7f6b5aa52e80>
>>> my_widget.who_am_i()
I'm a widget
>>> def teapot(self):
...     print("I'm a little teapot")
...
>>> Widget.who_am_i = teapot
>>> my_widget.who_am_i()
I'm a little teapot
>>> new_widget = Widget()
>>> new_widget.who_am_i()
I'm a little teapot

````

And Python doesn't warn you either! So perhaps I was unfairly harsh to Ruby? Not quite.

#One *Important* Difference
*Unlike* with Ruby, we can't monkeypatch the basic built-in classes, such as ```int```, ```float``` or ```str```. This is because they are defined in C extension modules which are immutable. These modules are shared between multiple interpreters and made immutable for efficiency (and safety)'s sake. So when you try to change the behaviour of the built-ins, you can't -

````
def own_up(self, a_string):
    return a_string.length()*"!"

>>>my_string = "Hello, World!"
>>> my_string.upper()
'HELLO, WORLD!'
>>> str.upper = own_up
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can't set attributes of built-in/extension type 'str'
````

To do something which approximates the effects of monkeypatching a built-in we have to subclass, like so - this example lets us write a custom instance of the str.upper() method by inheriting from str.

````
class CustomString(str):
    def upper(self):
        desired_value = "!" * len(self)
        return CustomString(desired_value)

>>> custom = CustomString("hello world")
>>> custom
'hello world'
>>> custom.upper()
'!!!!!!!!!!!'
````

Ta-da! I still maintain that this is saner behaviour than Ruby.

(Sidenote - Remember, for str and any class based on it, Python strings are immutable - when we call methods on a string, we just get a new return value that we have to assign to some other string object to store.)

#If Python and Ruby do it in similar ways, is Monkey Patching even All That Bad, then?
Yes! I still maintain that monkey patching is dangerous and shouldn't be used often. I think it says something positive about Python that it's not something you need to know intimately in order to program competently in the language, and indeed most Python programmers I know feel a bit iffy about it. It's a little off-putting (to say the least) to realise how much of a way of life it is for Ruby programmers.

But don't just take my word for it - have a read of this [insightful blog post](http://www.virtuouscode.com/2008/02/23/why-monkeypatching-is-destroying-ruby/) by Avdi Grimm, an experienced Rubyist worried about the impact of thoughtless 'hip' monkey patching - a choice quote:

> Where I work, we are already seeing subtle, difficult-to-debug problems crop up as the result of monkey patching in plugins.  Patches interact in unpredictable, combinatoric ways.  And by their nature, bugs caused by monkey patches  are more difficult to track down than those introduced by more traditional classes and methods.  As just one example: on one project, it was a known caveat that we could not rely on class inheritable attributes as provided by ActiveSupport.  No one knew why.

A fun (scary) read.

#Temporary Monkey Patching in Python for testing
As I was looking around at this stuff, I discovered there are a couple of libraries, [```unittest.mock.patch```](https://docs.python.org/3/library/unittest.mock.html#patch) and [```pytest monkeypatch```](http://docs.pytest.org/en/latest/monkeypatch.html) designed to allow *temporary* monkeypatching for testing - when the function or statement using it exits, the patch disappears. I can see how useful it would be to set up mocks in this controlled way, rather than having to worry about it affecting all of your tests. It was deemed so handy that ```mock``` is now part of the standard library in Python3. Time to investigate further!

