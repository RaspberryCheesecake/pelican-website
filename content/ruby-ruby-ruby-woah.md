Title: First Steps Exploring Ruby
Date: 02-02-2017
slug: first-ruby
tags: Ruby, Understanding Computation, CPSG


Last night I went to the first of the [Cambridge Programmers' Study Group](https://www.meetup.com/Cambridge-Programmers-Study-Group/) new sessions - we're starting to work through the book ['Understanding Computation: From Simple Machines to Impossible Programs'](http://computationbook.com/) by Tom Stuart. The book uses practical exercises in Ruby to explain a bunch of theoretical computer science stuff, working up to cellular automata, Turing machines and the lambda calculus (exciting!). As Stuart's blurb explains, the book is aimed at

> An audience of working programmers without assuming any academic background.

So, people like me.  It sounded like exactly the sort of thing I should be learning, since I don't have a Computer Science background.

One small problem - very few of us in the group actually knew any Ruby! So we spent this session trying to teach ourselves using the examples in the first chapter. It was fun trying to pick up a new language in the company of other people - a lot more companionable than noodling around on your own, and easier to find out cute things about the language because if one person discovered something cool, they shared it with the group. This post will be about some of my first impressions of Ruby.

##Getting Ruby set up

For those like myself who prefer more instructions than 'download Ruby online!' here's how I did it in the end:
```` $ sudo apt-get install ruby-full ``` which on my Ubuntu system downloaded Ruby 2.3, which was just fine for my needs. If you use Windows or Mac I'm told the [instructions on the Ruby-lang website](https://www.ruby-lang.org/en/documentation/installation/) are quite helpful and up-to-date. I first tried using the default terminal, irb, which you call from the command line

````
user@device:~$ irb
irb(main):001:0> 1+2
=> 3
````
This works fine for the first few exercises, but I couldn't get auto-indentation to work, important for writing multi-line programs! I tried tinkering around with adding a ```.irbrc``` file with ```require 'irb/completion'``` as recommended in the comments of the main ```irb.rb``` file (which I found in ```/usr/lib/ruby/2.3.0```). This didn't help - perhaps I put the config file in the wrong place? I ended up just using a slightly different terminal, pry, which was recommended by a colleague at the Meetup. It does auto-indentation and colour-coding too, which was very helpful! I don't think I'll be going back to irb. To install that, I just did ```$ gem install pry``` (gem is Ruby's package manager). To start using it, just type ```pry``` in the command line. 

##Ruby is like Python

Ruby is similar to Python in a lot of ways - this almost hindered me as I kept getting confused between Python and Ruby syntax. It felt like trying to learn Spanish when I already knew some French - confusingly close but distinct. I think ultimately this is helpful (I was mentally translating some things to Python to understand them, and that worked quite well) but to start with it was rather confusing.

Some similarities: ```yield``` sort of works the same


    :::fancy
    >> def do_thrice
    *   yield
    *   yield
    *   yield
    * end
    => :do_thrice
    >> do_thrice { puts "Hello world!" }
    Hello world!
    Hello world!
    Hello world!
    => nil

And the string formatting works [rather like Python 3.6's new f-strings](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings). So for instance, in Ruby ```"#{x*2} and also #{y+1}"``` gives you a string that calculates & inserts those values.

The ```*``` operator works in similar ways to unpack elements of an iterable - for instance, you can do fun things like:

    :::fancy
    >> a, *b, c = [1, 2, 3, 4]
    => [1, 2, 3, 4]
    >> b
    => [2, 3]


##Ruby is not like Python
####Objects! Objects everywhere!
[(Almost) everything is an object in Ruby](http://rubylearning.com/blog/2010/09/27/almost-everything-is-an-object-and-everything-is-almost-an-object/), and it made me realise how I usually write Python in a fairly un-Object Oriented style. I generally avoid writing classes if I can help it ([especially classes which only contain two methods, one of which is __init__](https://www.youtube.com/watch?v=o9pEzgHorH0) but this isn't really possible in Ruby. I suppose it's good for my soul - having a language that forces you into object-oriented thinking must make you confront what that really means. That's why there are these little ```=> nil``` statements scattered around my code examples, by the way - irb and pry always shows you what object your statements evaluate to, and often that's ```nil```, which is the object representing nothing - the 'empty' object, if you're mathematically minded.

I guess I'm going to have to go read those books on Design Patterns after all...

####It's super-terse
If Python cares a lot about preventing programmers having to type unecessary characters (goodbye ```;``` I didn't miss you) then Ruby cares even more. There are a lot of things you can do in one line. Here's a good one:

    :::fancy
    >> (1..10).select { |num| num.even? }
    => [2, 4, 6, 8, 10]

This creates a ```range``` which spans the numbers 1 to 10, then looks at all the numbers in that range and, if they are even, adds them to a list and returns the list. Phew!

At times, this can be confusing - for instance, there's no need to write explicit ```return``` statements if you don't want to. By default, Ruby returns the evaluation of the last statement in the body of a method. For instance,

    :::fancy
    >> def what_do_i_return
    *   "A"
    *   "B"
    *   "or C?"
    * end  
    => :what_do_i_return
    >> what_do_i_return
    => "or C?"

You *can* write explicit return statements, but you don't have to. And the way to get a function to evaluate to [sort-of-nothing](http://stackoverflow.com/questions/5267412/can-ruby-return-nothing) is to explicitly return nil (of course!). This returning-by-default is confusing at first, but it seems to fit with the rest of Ruby's style.

####'nil' isn't *really* nothing
You can put ```nil``` into things, which is hella confusing. For instance, suppose you have an array, you can add nil elements to it:

    :::fancy
    >> my_array = ["a", "b", "c"]
    => ["a", "b", "c"]
    >> my_array[4]
    => nil
    >> my_array.push("d")
    => ["a", "b", "c", "d"]
    >> my_array.push(nil)
    => ["a", "b", "c", "d", nil]
    >> my_array[10] = "surprising behaviour"
    => "surprising behaviour"
    >> my_array
    => ["a", "b", "c", "d", nil, nil, nil, nil, nil, nil, "surprising behaviour"]

Assigning to an element beyond the length of the array inserts nils until it reaches that element index (which didn't exist before!) and then it bungs in the thing you assigned. Intriguing!

##Some gripes
#### 'Monkey patching'

Monkey patching is *dangerous*. It's the way Ruby programmers refer to the ability to dynamically modify classes 'live' - at any time. You can even do this with Ruby's built-in classes, like String. At first glance it sounds really cool - you can just go define a new class method whenever you like! For instance

    :::fancy
    >>class String
    *    def shouty
    *        upcase + "!!!"
    *    end
    * end

adds a new 'shouty' method to strings. So now any string can use .shouty, just as if it were a built-in method

    :::fancy
    >> "hello".shouty
    => "HELLO!!!"

But here's the thing - monkey patching can break things really easily - **and Ruby won't warn you about it!** One of the guys sitting next to me at the meet-up managed to break his irb's Array class by redefining some of its built-in methods. Especially if you're new to Ruby and don't know all the built-in class names, it's really easy to *accidentally* monkey patch your way into disaster. It seems like a really powerful feature, but I'm not happy with how it seems to work. Perhaps with a nice Ruby IDE that reminds you about all the classes you have on-the-go, it's easier to avoid horrible mistakes?

####CONSTANTS - why even bother?
'Constants' are sort-of a thing in Ruby. If you define a variable with CAPITAL LETTERS, the Ruby interpreter will give you a warning. But it won't do anything about the warning - it'll still change the 'constant' value, and just complain about it. Here's an example:

    :::fancy
    >> CONST = "Don't change me please"
    => "Don't change me please"
    >> CONST = "I changed you anyways!!"
    (pry):224: warning: already initialized constant CONST
    (pry):223: warning: previous definition of CONST was here
    => "I changed you anyways!!"

What's the *point* of having this feature? Can we perhaps write larger programs that will catch this warning and not change the constant (well, and change it back, since we warn but change things anyway)? [Basically not at all](http://stackoverflow.com/questions/660737/can-you-ask-ruby-to-treat-warnings-as-errors), apparently! I'm happy to be enlightened by some Ruby-god but as far as I can tell, this feature does nothing except confuse people used to programming in languages where constants exist and are, well, constant.

#Overall Impressions
I found that during the session I fluctuated between delight ("what a nice way to do that!") and terror/annoyance as things behaved in unexpected ways. It has some peculiarities that particularly stand out to me in comparison with Python, and some features that are just adorably cute. I've been noodling around with it on and off all day today, and still enjoying getting to know it. Overall I'd say it's been fun! I can't say that I'm dying to use it as my new scripting language, but I'll certainly be pleased to become better acquainted as we work our way through the Computation book.

####PS
Thanks again to [RedGate](http://www.red-gate.com/) for hosting the session and feeding pizza to 20+ hungry programmers!


        
