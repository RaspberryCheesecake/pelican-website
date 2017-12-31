Title: The Knowledge in the Code
Date: 31-12-2017
slug: legacy-code
tags: legacy code, cruft, refactoring
Summary: Legacy code is valuable

My colleagues and I were discussing legacy code the other day. Someone gave the pretty common opinion that, if there was time, they would of course completely re-write all the legacy code they came across, from scratch. But, since this is not an ideal world and time is limited, they would settle for refactoring what they could. It got me thinking about how my own attitude toward legacy code has changed over time, and why that is.

##Indiana Jones and the Lost Code

I spent one summer at university working on a classic legacy code problem. A scientist had written a large piece of Fortran 95 to simulate a manufacturing process for my employers. He had long since retired and there was no way to contact him to ask about his work. As an intern I was asked to add a little bit of extra functionality. They were still using the code and found it reliable, but wanted to add a feature. I felt like an archaeologist, dusting off terse variable names and cryptic comments, trying to understand not only this code but the complex processes it was simulating, too. It was very difficult to get anywhere.

![Uncovering the secret of the Lost Code]({filename}/images/indy-uncovers-artifact.jpg)
*I wonder if I can replace this function without adding test coverage?*

My initial reaction - rewrite it! I think most programmers share this instinct. My idea was to tear it down completely and rebuild it, preferrably in a different, more modern language. Then, I felt, I could add the features that were needed. But my manager was adamantly against this. As a summer intern, I would leave soon anyway. If I rewrote the code in another language, where was the benefit to the company? From their perspective, they already had a tool that worked fine. They just needed someone to understand what they already had and improve it a bit. At the time I was frustrated by this. I would tell others the tale with a wistful air - "If only I had had the time to rewrite it properly" I would think, "it would have been so much better". But would it have?

##Why Rewrite Code?

I've come across a few different reasons for re-writing code completely. None of them really convince me of their merits anymore.

- **To write it in a new language.**

The new language is considered to be 'better' - it has features you want, or the old language is considered passe. Fortran 95 certainly wasn't the best language to be writing new code in anymore! For one thing, there was a severe restriction on variable and routine name lengths - in order to maintain backward compatibility with earlier versions of the language, none of the variables was over 6 characters in length, which didn't aid readability. But most cases aren't as clear-cut as this - I think most people wouldn't choose to re-write a large C program in Rust even if they think Rust is a superior language in some respects.

- **For understanding.**
 
No-one can figure out how the old code works, so we have the idea to learn by doing and completely rewrite it. It's certainly "easier to write code than read it." This is even true of one's own code - returning to something I wrote six months ago, I realised to my regret I left insufficient comments and good names behind - so I had to learn how to understand my own code again, refactoring some of the names once I had worked out what I was doing. But by the same token, if you re-write others' code, there's no guarantee it will be any more readable to the next person - even to yourself, later on. Taking more time to read and understand what the existing code is doing may end up being more valuable. Perhaps one of the problems with this approach is that programmers feel guilty for spending some of their work time 'just reading' other people's code. It doesn't feel like a productive activity in the same way as re-writing. Reading old code just produces understanding in your mind, no tangible output.

- **You don't trust the people who wrote the code.**

'Not Invented Here' syndrome. Especially since [many programmers have poor code reading skills](http://gamedevwithoutacause.com/?p=1329) it's difficult to relax and trust unknown programmers. We can't easily just grok their code and be reassured that it's solid - so fear creeps in and the idea of a complete re-write or making our own version from scratch seems more appealing. If your instinct is not to trust the unknown, it becomes even harder:

>"You can’t look down on someone when you read their code. If you don’t respect the person writing the code, you won’t be able to apply the energy needed to understand it." - Keiichi Yano [@CaptivNation](https://twitter.com/CaptivNation)

In the Python world this has mostly been overcome when dealing with third-party modules - for some reason, if you can pip install a library function to do what you want, there isn't the same need to question and look under the hood in mistrust at *how* it does what it does. The module is generally treated as a black box, whose documentation is all you need to work with it. Perhaps this trust has been built up in the Python community over time and isn't readily extendable to other domains - it's certainly a large factor in the appeal of Python as a language.

- **It's ugly**

And finally the real reason, the one we feel deep-down in our bones: the old code *looks* bad - it's flaky, it doesn't have any test coverage, the relationship between the parts looks crazy. When you read it, you sometimes want to laugh out loud - it's a big hot mess. There is a strong temptation to start again from scratch out of an aesthetic instinct for perfection.

##Why Keep Code?

- **Commercial concerns**

Joel Spolsky of Joel on Software fame has called rewriting source code from scratch ["the single worst strategic mistake that any software company can make"](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/). Spolsky uses the example of Netscape 6.0 to demonstrate why as a corporate strategy, complete re-writes are almost never a good idea. They tend take longer than anticipated (because people are bad at working out how long it will take), and burn time and resources for no appreciable reward until the very end when the new code is ready - by which time, a competitor has probably caught up to you and eaten your lunch. There are almost no commercial examples where a complete re-write turned out to be a good idea. Sometimes as a programmer you need to 'zoom out' and take a more general view of your company's trajectory, and how time spent on re-writes and refactoring fits into it.

Of course, companies also need to take care not to pressure their programmers into behaving in this negative way. If you're rewarded based on new code output or some other metric that doesn't take into account the increase in understanding from reading others' code, it can be hard to fight the instinct to re-write code more than you should. Managers should try to grow their programmers' understanding of the existing codebase and allow time for them to read code as an activity of value in itself. Taking a leaf from [Peopleware](https://raspberrycheesecake.github.io/peopleware.html) and accepting that 'human resources' are individuals who are not interchangeable and who contain valuable institutional knowledge should help here.

- **Code learns**

As Joel also points out, 'hairy' legacy code functions embody years of bug fixes and reactions to specific situations. But not only that. Legacy code often embodies knowledge about a process, knowledge that is very difficult to recapture. The writers might have left the company, or been run over by a bus! Re-writing doesn't recapture all the nuances of the understanding embedded in the old codebase, and can leave important institutional knowledge behind. This knowledge might not be documented in any other way. I've lost count of the times an old comment or variable name has led me in a valuable direction to a deeper understanding of changes to our hardware, for example. This sort of thing would be lost, throwing the baby out with the bathwater, if the code had been completely re-written by someone who didn't keep the old comments they didn't understand.

- **Refactoring can give the best of both worlds**

It can be difficult to get the balance right between too many re-writes on the one hand and leaving flawed, buggy existing code alone on the other. My own experience at [CMR](www.cmedrobotics.com) has definitely taught me the value of keeping and improving on an existing codebase. Through resisting the temptation to stop and completely re-write parts of the Python codebase, we have come further and faster than we could have done otherwise, and managed to still continue improving as we go along. Refactoring is sometimes used as a synonymn for re-writing, but it's actually a different approach. Refactoring values existing code and makes the base assumption that it is valuable and should be preserved. By adding tests, old code can be refactored with the confidence that bugs won't be introduced. Tweaking variable names and adding explanatory comments is generally harmless and can be very valuable. In this way, incrementally refactoring old code can give excellent results, in less time than a complete rewrite. [Your Code as a Crime Scene](https://pragprog.com/book/atcrime/your-code-as-a-crime-scene) explains how making improvements to the code can and should be done in a targeted way, rather than by hunches. By focusing on areas with the highest cyclomatic complexity and churn, we direct our energy where it produces the most valuable results. This means the majority of the existing legacy code can be left alone, while still significantly improving the functionality and test coverage.

##A Book Recommendation

In the course of my research for this post I came across [Code Reading](https://www.spinellis.gr/codereading/), a book about precisely the discipline reading legacy code in order to maintain it and add features. This looks to be a great primer on a neglected skill for programmers. I plan to read it myself and leave a review here in the New Year.
