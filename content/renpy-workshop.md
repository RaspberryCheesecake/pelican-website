Title: Telling Stories With Python And Ren'Py
Date: 16-09-2019
slug: renpy
tags: Workshop, Ren'Py, Interactive Fiction
Summary: A Workshop I Gave At PyCon UK

This is a write-up of a workshop I've given at [CamPUG](https://www.meetup.com/CamPUG/events/263945805/) and [PyCon UK 2019](https://2019.pyconuk.org/). It was a lot of fun to deliver, and my participants came away with their own mini-games written in Ren'Py. I was impressed by the range of creative stories, everything from getting lost in Cardiff, storming Area 51, coaxing a grumpy cat, visiting a music festival, going to space, defeating animated fleas, visiting every pub in Cambridge, a child's guide to the Divine Right of Kings, interactive graffiti and more!

I hope this post will be useful as a reference for workshop participants and those who couldn't make it along.

## What is Interactive Fiction?

You might be familiar with the concept of interactive fiction from "Choose Your Own Adventure" books. 

Ever since computers came on the scene there has been interactive fiction here, too. [Zork](http://textadventures.co.uk/games/view/5zyoqrsugeopel3ffhz_vq/zork), one of the earliest examples, is a dungeon-crawling game where the player explores The Great Underground Empire by typing text commands.

Using later tools like [Parchment](https://github.com/curiousdannii/parchment) and [Twine](https://twinery.org/wiki/start) people are still creating these text-based interactive fiction games. A text-based game I've enjoyed recently is [Moonlit Tower](http://iplayif.com/?story=http%3A%2F%2Fwww.ifarchive.org%2Fif-archive%2Fgames%2Fcompetition2002%2Fzcode%2Fmoonlit%2FMoonlit.z5) by sci-fi author Yoon Ha Lee.

Visual Novels are a genre of interactive fiction that combines pictures and text as a storytelling tool. They originated in Japan and many famous examples such as *Fate/Stay Night* and *Symphonic Rain* are Japanese. These games are often romance or relationship-themed, each path perhaps leading to a relationship with a different character.

## Ren'Py

![Ren'Py Icon]({filename}/images/renpy-icon.png)

[Ren'Py](https://renpy.org) is a visual novel creation engine written in Python. It has its own syntax and style, but also allows you to embed pure Python for more complex gameplay mechanics.

It is cross-platform and works on Mac, Linux and Windows. All that you need alongside it is a simple text editor that can convert tabs to spaces, such as gedit.

## What can you do in Ren'Py?

#### Label Jump For Branching Stories
![Road Not Taken Screenshot]({filename}/images/road_not_taken.png)

I would humbly suggest my own game [The Road Not Taken](https://github.com/RaspberryCheesecake/RoadNotTaken) as a useful introduction to the `label` / `jump` mechanic. Take a look in the `script.rpy` file to follow how the game works. It demonstrates how menus work in the game and how you can use them to move to different choices, similar to a GOTO statement. It also includes an example of embedding music within gameplay to add a mood to a scene. Feel free to copy and modify it as a basis for your own games.

#### Custom GUI
![Hotel Shower Knob Screenshot]({filename}/images/Hotel_Shower_Knob_gameplay.png)

[Hotel Shower Knob](https://yossarianiii.itch.io/ho), a game where you have to puzzle out an unfamiliar hotel bathroom to take a shower, is a good example of a custom GUI. Inside `options.rpy` the creator replaced the usual cursor with a custom image of a hand:

```
## The mouse clicker thingy.

define config.mouse = { 'default' : [ ('cursor.png', 66, 95)] }
```

This makes for a unique visual experience. As the hand is Creative-Commons licenced, you could use it in your own games, too!

#### Embedded Python
![Two Worlds Screenshot]({filename}/images/two-worlds-screenshot.png)


Because Ren'Py is written in Python (2.7, if you're interested) it's easy to embed Python statements within it to acheive more complex effects such as creating mini-games. There are two ways to do this - prefixing single lines with `$` or using an indented block with the `python:` statement. I used `python: ` statements within Ren'Py to create `Card` objects for my game [Two Worlds](https://github.com/RaspberryCheesecake/TwoWorldsGame/blob/master/game/script.rpy#L22).

The key thing to notice is the definition of the `Card` class:

```
# Define the card objects used to play the games with
init:
    python:

        flowers = ["card-front-land-flower%d.png" % i for i in range(1, 3)]

        class Card(object):
            def __init__(self):
                self.face_up = False
                self.selected = False
                self.number = 0
                self.coords = [0, 0]
                self.back = "card-back-land.png"
                self.front = flowers[0]
                self.paired = False

            @property
            def coord_text(self):
                return "{}, {}".format(self.coords[0], self.coords[1])
```

This happens during the `init:` block, before the game starts, so it is available from the beginning. I subsequently used this in the `sea_game.rpy` and `land_game.rpy` files using the `ui.interact()` statement and `action If` to connect it with Ren'Py responses to on-screen clicks.

#### Persistent Data
Another useful trick is the ability to store persistent data between plays of the game. 

![Example From Long Live The Queen]({filename}/images/llq-ss3.jpg)
*An example from Long Live The Queen*

This allows more satisfying gameplay such as unlocking new routes after a complete playthrough, and keeping track of player stats like Strength or Skill. Anything that can be `pickled` is suitable for this treatment. A simple example:

```
if persistent.secret_unlocked:
        scene secret_room
        e "I see you've played before!"
```

To unlock this path the user must hit a piece of code that sets `$persistent.secret_unlocked = True`

`persistent` is a special keyword in Ren'Py, so you shouldn't use it for anything else. Unlike other variables, if you haven't yet initialised it when you reach the if statement Ren'Py won't complain.



## Useful sources of free images and sounds for your games

There are various community projects to collect images and sound to use in games with Creative Commons or similar licences.

I've found [px here](www.pxhere.com) a useful collection of images, particularly photos.

I used [Fraqtive](https://fraqtive.mimec.org/) to create the card images and backgrounds for Two Worlds.

Useful sound sources include [Free Music Archive](http://freemusicarchive.org) and for sound effects, [Free Sound](https://freesound.org/)


## Example games written in Ren'Py

[Benthic Love](https://joffeorama.itch.io/benthic-love) – Michaela Joffe, Sonya Hallett

[Hotel Shower Knob](https://yossarianiii.itch.io/ho) – Yoss III

[Death And Burial Of Poor Cock Robin](https://lernakow.itch.io/dabopcr) – Lernakow

[Long Live The Queen](https://www.hanakogames.com/llq.shtml) – Hanako Games

And check out the [NaNoRenO](https://itch.io/jam/nanoreno-2019) game jam each year during the month of March – or better still, take part!
