Title: Why Do We Do This To Ourselves?
Date: 2017-09-19
slug: why-linux
Category: open source
tags: books, open source, Ubuntu, when things go wrong
Summary: Why choose to use an open-source OS?

Hello! First of all, I'm not dead (for all three loyal followers of this blog!) I got a fantastic new job at [Cambridge Medical Robotics](www.cmedrobotics.com) as a full-time Python developer, and have consequently had rather less free time for code musings lately. It's been about five months since I first joined and I'm finally starting to emerge from the new-job haze and find my bearings again. In fact, I had time to break my laptop - and fix it again - which is what I wanted to talk about today.

# What happened?

I finally found the free time to update my laptop from Ubuntu 12.04 to the latest version of Ubuntu LTS (16.04) a weekend or so ago. I had been seeing the suggestion to update coming up for a while (... nearly a year, it turns out!) and ignoring it. But because I couldn't make a new game run with my old version of Ubuntu without installing a bunch of updates anyway, I finally decided to bite the bullet and do the full upgrade. I'd heard mixed things about how well the transition between versions went for other people, and I was also concerned about keeping my windowing appearance the way I like it, so I knew this would take a while and probably not be straightforward. I backed up my data and even made a list of the useful programs I currently have installed, in case things completely went sideways. What I was hoping not to encounter was ...

![Abandon Hope, All Ye Who Enter Here]({filename}/images/back-to-cmd-prompt.jpg)

Anyone who uses an open-source OS will be familiar with this situation. There you are, sitting in front of what was once a beautifully working machine, questioning all your choices and trying to find out how to fix whatever the problem is. The spinal reflex of Linux is the command line. It's what's left when things go wrong. As Neil Stephenson's excellent [In The Beginning Was The Command Line](http://www.mit.edu/~yandros/doc/command.txt) reminds us (although here he is actually talking about Windows vs Macs):

>"when a Windows machine got into trouble, the old command-line interface would fall down over the GUI like an asbestos fire-curtain sealing off the proscenium of a burning opera. When a Macintosh got into trouble, it would present you with a cartoon of a bomb, which was funny the first time you saw it."

#Why even choose Linux?

###My motivations
When I got my first laptop as I was about to go to University, I decided to try dual-booting with Ubuntu (it was a Windows machine originally). Mainly it was an experiment - I'd heard that there were some cool coding tools available for Linux systems and I wanted to see what it was like on the other side. I was also kind of a cocky teenager and liked the idea of using a niche, obscure system, customising my laptop in some way. And, most importantly, I had *a lot* of free time - I took a year out before going to Uni, so aside from working in a gift shop (which didn't occupy my mind that much) I was able to spend time fixing up my laptop the way I wanted. After the inevitable teething problems, I got an installation I was happy with, and enjoyed it so much I ended up just using Ubuntu as my primary system and abandoning the idea of doing dual boot. I kept my system Ubuntu all through college, and though I was sometime concerned I wouldn't be able to complete assignments with it, I was pleasantly surprised by tools such as OpenOffice, which allowed pretty seamless integration with Word, Powerpoint etc. I also had a leg-up on some of my classmates, as when I got to Uni it turned out that the machines in our department all ran Linux installations, too. So I never really had a problem there.

#Common fears
### But what if there are bugs and I don't know how to fix them? I'm not some l33t hacker!
Returning to [In The Beginning Was The Command Line](http://www.mit.edu/~yandros/doc/command.txt), which really is a stupendous essay, we find a wisdom about bugs which definitely still holds out. Whatever OS you are running will not be perfect. There will be problems from time to time, and you will try to learn how to fix those problems. Neal Stephenson compares the OS situation to a crossroads with different competing auto-dealerships. Customers come there and 90% go straight to the station-wagon dealership (Windows).

>The group giving away the free tanks only survives because it is staffed by volunteers, who are lined up at the edge of the street with bullhorns, trying to draw customers' attention to this incredible situation. A typical conversation goes something like this:

>**Hacker with bullhorn**: "Save your money! Accept one of our free tanks! It is invulnerable, and can drive across rocks and swamps at ninety miles an hour while getting a hundred miles to the gallon!"

>**Prospective station wagon buyer**: "I know what you say is true... but ... er... I don't know how to maintain a tank!"

>**Bullhorn**: "You don't know how to maintain a station wagon either!"

>**Buyer**: "But this dealership has mechanics on staff. If something goes wrong with my station wagon, I can take a day off work, bring it here, and pay them to work in it while I sit in the waiting room for hours, listening to elevator music."

>**Bullhorn**: "But if you accept one of our free tanks we will send volunteers to your house to fix it for free while you sleep!"

>**Buyer**: "Stay away from my house, you freak!"'

With an open-source OS like any of the Linux flavours, hundreds of people will be able to help you, and a solution will probably already exist online. StackOverflow and other such repositories of knowledge are great, as are reading the manuals and docs for specific tools you want to use. Whereas proprietary OS vendors are naturally interested in 
a) Convincing consumers that there are no problems with their product (particularly security problems!)
b) Convincing shareholders that their product is commercial (not 'giving anything away for free') and worth paying money for

### I don't think I can keep up with the skills you need to run an OS like that
Not going to lie, this can be a barrier. If you're like me and don't enjoy change, the process of continually needing to update and patch your open-source OS can be scary. You ask yourself - what if it doesn't work next time? You think about how you already voided the warranty on your machine by installing this *crazy free OS* and you question whether you'll be able to fix it. 

To this I have several suggestions:
- Use an OS which has widespread adoption and is known to be easier to maintain, such as Ubuntu. I began with Ubuntu and continue to stick with it despite some gripes, because the canonical system does make it so easy to install the patches and updates you need to keep rollin'. Plus, the version system means you can go several years without needing to do a major upgrade.

- Cultivate technically minded friends who can advise if things go very wrong. This can be online or off - Ubuntu has a warm community of volunteers who staff the forums and are generally very helpful and kind to newbies. If you're a student there is often at least one l33t sysadmin in your department who Knows The Ways of Linux and they are generally happy to help - perhaps in trade for chocolate! Depending on where you work your colleagues may be able to help out, too. Linux users tend to be evangelists who want to assist others to enjoy using the systems they do.

- Comfort yourself by thinking of the various [high](https://en.wikipedia.org/wiki/EternalBlue) [profile](https://arstechnica.com/information-technology/2017/03/new-wikileaks-dump-the-cia-built-thunderbolt-exploit-implants-to-target-macs/) [problems](https://smbloris.com/) with commercial OSes - at least you are not suffering with that!

- Believe in yourself and your ability to fix things if they go wrong. I can't state this enough! Running my own installation of Ubuntu really helped in giving me the confidence I needed to get into coding and eventually, to get a full-time programming job. You don't have to be an IT professional to run Linux though - people from many walks of life do it for different reasons. One of my friends is a historian who uses Ubuntu to make cross-referenced notes more easily!

- You don't have to commit to running an open-source OS full-time to give it a whirl and see if it's for you. These days you can fairly easily try booting Ubuntu or Debian [from a memory stick](https://askubuntu.com/questions/261985/how-do-i-try-ubuntu-from-a-usb-stick). Using a [Rasperry Pi](https://www.raspberrypi.org/) will also give you a taste of Linux for a fairly small investment if you already have a separate screen and keyboard. And of course, [dual-booting](https://askubuntu.com/questions/666631/how-can-i-dual-boot-windows-10-and-ubuntu-on-a-uefi-hp-notebook) is getting easier to do - meaning you still have a full working installation of Windows alongside your Linux OS should you need or want.

##Why continue with it?
For me in particular, it's important to know I have the ultimate control over my machine. As a programmer this is particularly important, since it is the tool of my trade - it's where I go to think and play. But I think the importance of control is true for everyone, if you think about what you use a laptop for. These days your computer contains your life - your bank statements, your music, photos, books, your email history, everything you've touched online. With a commercial OS, you have to admit that you are not the person who ultimately gets to decide what uses your machine can be put to. Whereas with an open-source OS, you call the shots. 

Some concrete examples are in order.

###I know that I will always fully own my digital books and music. I'm also confident I can make my own content through remixing the work of others, without being prevented from exercising my creativity.

I am a strong believer in the harmfulness of Digital Rights Management. Ultimately in order to enforce this notion (that these things do not 'belong' to you) someone else has to control your means to access them. Lawrence Lessig is far more eloquent than I can be about why it is harmful to lock off access to these things, so I would direct those interested in finding out more to [his work](http://www.free-culture.cc/freecontent/) which is, naturally, freely available online. I agree with him that the division between 'creator' and 'consumer' is artificial, and ultimately, harmful. I want to pay creators a fair prices for ebooks and music I enjoy, and in return to be freely able to use those purchases whatever way I see fit, just as I would a physical book or a vinyl record - to lend it to a friend, reshape or remix it. One of my hobbies is [vidding](https://fanlore.org/wiki/Vidding). This is considered copyright violation of the video and music sources I use, and treated variously depending on my source material - sometimes fond indulgence, sometimes takedown notices and harsh threats. I am confident my OS will never prevent me from making my art, and that no-one else will get to decide what is acceptable for me to work on.

###I can control my security and privacy and can be fairly confident that no-one is using my machine against my wishes.
####*"I just received an e-mail from my daughter, who is very upset, saying, 'Mom, I have my laptop open in my room all the time, even when I'm changing."*

This is a big one. People may have heard of the laptops in Philadelphia that [spied on schoolchildren](https://en.wikipedia.org/wiki/Robbins_v._Lower_Merion_School_District) and took tens of thousands of pictures of students, teachers and their families at home. The pictures were shared among staff and some were used to discipline students. One student was [called into the Principal's office and accused of drug abuse](https://www.pcmag.com/article2/0,2817,2367209,00.asp) after being secretly photographed eating pill-shaped Mike and Ike candy in his bedroom by his open laptop, for instance.

>"[T]here is absolutely no way that the District Tech people are going to monitor students at home.... If we were going to monitor student use at home, we would have stated so. Think about it—why would we do that? There is no purpose. We are not a police state.... There is no way that I would approve or advocate for the monitoring of students at home. I suggest you take a breath and relax."  Principal DiMedio in an email to a concerned student intern, 2008

>"Among all of the webcam photographs recovered in the investigation there are a number of photographs of males without shirts, and other content that the individuals appearing in the photographs might consider to be of a similarly personal nature." [Report of Independent Investigation Regarding Remote Monitoring of Student Laptop Computers by the Lower Merion School District, 2010](https://web.archive.org/web/20100602042403/http://www.lmsd.org/documents/news/100503_ballard_spahr_report.pdf)

During the case, some argued this was fine, because the children didn't really own their laptops - they were issued to them by the school and the families had signed a consent form about the use of "TheftTrack" software. But the same argument can be made for any piece of proprietary software. Do you really read all of those EULAs before you click 'agreed'? If you use the iTunes music store for instance, you'll remember [being forced to download a U2 album you weren't interested in and being unable to delete it](https://www.wired.com/?p=1563271). You might also remember the irony of [Amazon remotely deleting ebook copies of George Orwell's 1984 from people's Kindles](http://www.nytimes.com/2009/07/18/technology/companies/18amazon.html). What does your 'ownership' of a piece of proprietary software really mean, when the true owners are the company who created and retain ultimate control over it? Those companies do not necessarily have our best interests at heart. 

This is an even bigger issue for those living in repressive regimes which seek to prevent free access to knowledge - Tor and other open-source anonymisation tools and open-source OSs are [incredibly valuable](https://www.torproject.org/about/torusers.html.en) to journalists, union organisers, and those working for the cause of human rights and free speech around the globe. The point of open-source tools such as Tor is that anyone is able use them completely freely, even those who the creators [rightly despise](https://blog.torproject.org/tor-project-defends-human-rights-racists-oppose).

###I know that I can completely understand the tools I use, if I take the time to do so. I can even contribute to making those tools better for everyone.

This is a big one as a software developer, but also as someone who enjoys creating works of art. It's liberating to know that, even though I don't understand a great deal of the software I use, I *can* learn to understand it, and if it goes wrong, I can learn to fix it. The source and config files for Linux are not locked away or hidden. They are just text files that are freely editable - I can eternally change, customise (and definitely break!) my machine if I want. I don't have to stick with the settings that someone else thought would be best for people like me - I can alter how my machine works freely so that it works the way I want. This is particularly great for [accessbility features](https://www.washington.edu/accessit/print.html?ID=1015) such as screen magnification, audio readers and the ability to navigate without a mouse. The Ubuntu community is definitely ahead of MacOS in accessibility, and Windows to an extent as well.

###Warm fuzzies

It's quite nebulous but I do enjoy the sensation of being part of a community committed to helping one another and to continual learning. It's also just fun to feel like I've taken the red pill and decided to understand more about how my machine really works! The thrill of having 'insider knowledge' and feeling a little bit like a hacker, that motivated my teenage self to go and install Linux, never entirely went away for me. Of course, there are sometimes feelings of being a fraud or not knowing enough. But the good outweighs the bad for me. As with other computer-related pursuits, I swing between two states:

![Two states of every programmer]({filename}/images/two-states-of-every-programmer-i-am-god-i-have-no-idea-what-im-doing.jpg)
And I wouldn't have it any other way.


So there you have it. Reasons why I continue to use a Linux OS, despite the sometimes-frustration.


#Postscript: what was The Fix?

There's almost no point telling you about what fixed my particular problem, since [googling for your specific problem](http://lmgtfy.com/?q=ubuntu+12.04) will be far more effective. I've forgotten myself most of the details of what I did. However, if you're really curious, I do keep a notebook for these things (it's a nice way to learn a bit more for next time) so according to my notes, here is what I ended up doing:

- Pressed 'Shift' as my laptop booted up to access kernel selection and selected my previous happy kernel 3.13 to get into cmd prompt mode.
- Had a look around using the command line tools at my disposal - this was no hardship since on Ubuntu you can do everything with the command line - it just took me a little while to look up some of the commands. `sudo lshw -C Network` showed me that network access was disabled - no good if I was going to try installing updates from the internet. `sudo service network-manager restart` did the trick and got that going again.
- At first I thought I had a problem with where I was pointing at repositories, so I checked that `/etc/apt/sources.list` had the sources that a bit of googling led gave me a list of what to expect for 16.04. They were actually fine.
- I ran a `sudo apt-get upgrade` and `autoclean` which seemed to fix some of the errors, but I still saw a message saying `dpkg broken`.
- Finally, I found out the fix on this [handy bug report](https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/1389320) - looking in `etc/init.d/virtuoso-nepomuk` showed me that my file there did indeed miss out a `### END INIT INFO` at the end of its block. Using a command-line text editor (since I'm not a l33t Emacs or vim hacker, I just used nano) I fixed that and saved the file. After that, `sudo-apt-get update` worked. Following a restart, I had a GUI again!
- After that it was actually relatively simple to get the Gnome interface I know and love back (I really despise the Unity GUI, but that's another post).

That might sound overwhelming - and at the time there were moments of frustration for sure! It took me a few hours, spaced over several days. But I never doubted during this process that my OS problem could be fixed, and that I could be the one to fix it. It helped greatly that I have a tablet, so I was able to go on the internet during the crisis look up suggestions and solutions. These days, smartphones mean most people aren't trapped offline in a situation like this, and can find advice and help.
