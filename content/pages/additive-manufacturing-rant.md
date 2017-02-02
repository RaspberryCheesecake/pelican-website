Title: Additive Manufacturing Is Not Going To Save The World (Sorry)
Date: 2017-02-01
slug: additive-manufacturing-rant
tags: additive manufacturing, 3D printing, hype, manufacturing
Summary: Let's get real about the capabilities of 3D printing technologies.

# What are we talking about here?

Additive manufacturing, popularly known as 3D printing, is a term that refers to a range of technologies. It's generally defined as repeated computer controlled deposition or binding, layer by layer, of materials to build up a product. 

The additive technologies have improved to the point where some can be used to produce final parts for end users as well as prototypes and ‘looks-like’ models. Identification of customers who benefit from the particular advantages of 3D printed products has led to an expansion of service offerings. Hearing aid shells, dental braces, shoe inserts and other low volume, complex, bespoke products are places additive manufacture has the advantage as a final production technique.

(picture of the range of processes & dates)

Additive manufacturing technologies have existed for decades, but recent development of smaller, more accessible machines has drawn media attention. The vision of a world of distributed manufacture, where the means of production sit on every desktop, is compelling. The technology has been hyped by commentators as the manufacturing tool of the future – something that will [“transform our lives”](), [“revolutionise the global economy”]() and [“change the future of industry”](). Enthusiasts advocating for the power of additive manufacturing tend to say things like

> I don’t pretend to be impartial. This is a future I believe in, and I’m one of many working to build it. 
- Chris Anderson, Makers: The New Industrial Revolution

> 3D printing will change the way things are produced more in this century than the industrial revolution did over the last 300 years... Industrial 3D printing will forever change the world as we know it. Are *you* ready? - Rick Smith, Forbes

I used to be one of these very excited people. To a certain extent, I still am - there are some wonderful things that only additive manufacturing can achieve, and it really is transforming certain industries. For example, the hearing aid business has [undergone a silent transformation](http://ratio.se/app/uploads/2015/12/cs_3dprinting_hearingaid_262.pdf). All hearing aid shell manufacturers now offer personalised shells made by additive processes such as SLA and SLS. Dental implants aren't far behind.

(Gartner)

However, the fact is that additive manufacturing is not currently commercially viable for producing larger numbers of products. For production runs of over around 500, conventional production technologies are far more practical. Additive manufacturing is currently expensive, slow, requires more design time than commonly imagined and so far constrains production to small batches. [Gartner’s Hype Cycle](http://www.gartner.com/newsroom/id/3117917) for 3D Printing predicts that both consumer 3D printing and 3D printing in manufacturing operations will soon come out of the ‘Peak of Inflated Expectations’ and enter the ‘Trough of Disillusionment’.


#Advances so far
## At the consumer level
There have been game-changing reductions in the cost of less sophisticated machines. This has been driven by hobbyists and open-source developers such as the RepRap project led by Dr Adrian Bowyer. RepRapPro recently became a victim of its own success, closing for business in January and releasing a statement that

> "“The market for low-cost 3D printers is now so crowded and so competitive that a small specialist company like ours cannot expand. So, because we are not bankrupt and we do not have any debts to pay, we have chosen to stop now while we are ahead and to concentrate on other activities.” - RepRapPro

A message from Dr Bowyer on the RepRap.org forums explains further that
> “this great flowering of small companies (all essentially based on the RepRap Project) making commercial life difficult for each other was pretty-much what I predicted when I started the Project… But we expected it to take decades, not four years.”

A typical small desktop machine now costs in the region of hundreds of pounds. Profit margins on small desktop machines have reduced and no further large drops in price may be reasonably expected.

Desktop printers were created that will work ‘out of the box’ without the need for great additive knowledge and DIY skills. Firms like MakerBot and Ultimaker targeted those who want to access the technology but do not have the skills or time to build and maintain their own printers. However, this new generation of machines is still not reliable. MakerBot took an ‘Apple’ approach to development and have hidden the complexity of their product from users, closing the source code and preventing user modifications. Sadly, desktop printers are not yet reliable enough to be operated by unskilled users without significant risks of failure. MakerBot is now [facing a class action suit about failures of its ‘Smart Extruder’](http://makezine.com/2015/07/14/makerbot-faces-class-action-lawsuit-over-faulty-extruders/.) and has been called a [“dead company walking”](http://hackaday.com/2016/04/28/the-makerbot-obituary/) after laying off its manufacturing staff, closing its retail locations and outsourcing all production to China.

>"Anyone who has ever been to a hackerspace has seen a MakerBot printer, but that printer was broken." - Brian Benchoff, HackaDay

Whether using a pre-assembled machine or a kit made from open-source parts, what can be printed with a desktop FDM (fused deposition modelling) machine is mostly limited to plastic trinkets that “looks like I bought it in a panic at a jumble sale for 10p” as [a journalist observed](https://www.theguardian.com/lifeandstyle/2013/dec/02/christmas-presents-3d-printer-gun-gifts). A typical quote from a ‘Maker’ I interviewed at Newcastle MakerSpace was “I do spend more time trying to fix the printer than printing things”. An insightful member of the ‘Maker’ community Dominic Morrow pointed out in an interview with me,

>“In our community – the maker community and hackspace community – 3D printing isn’t about 3D printing, it’s about building a 3D printer.”

The quality of the output is considered secondary to the pleasure of tinkering with the machines.

## At the industrial level

Prototyping houses such as Shapeways, Sculpteo and iMaterialise have succeeded in popularising the larger, more professional additive technologies. They fill a niche by supplying the ability to print with expensive methods such as DMLS (Direct Metal Laser Sintering), which is not otherwise possible as an individual because the machines cost millions of pounds. However these companies don’t offer anything fundamentally new in manufacturing except for their business model. Their machines can produce higher quality results than the desktop machines and at a larger scale. But they are still slow compared to conventional processes and require skilled operation. 

Sculpteo released [a study on the batch size problem](https://www.sculpteo.com/static/0.30.0-126/download/ebooks/Sculpteo_Guide_to_Manufacturing.pdf) recently. For 5 representative parts they compared costs quoted by injection moulding companies Sinomould, Quickpart and Protomould to their own print-costing algorithm for SLS. Injection moulding is a conventonal manufacturing process which involves injecting heated plastic under pressure into a mould. Its costs include start-up costs for tooling, so this process is more expensive than additive manfuacturing at first. But as the number of parts produced increased, injection moulding catches up due to its lower cost per additional part.

(Sculpteo remote control pic)

The average break-even point was 436 units. After that, injection-moulding was less expensive per part.

>“Should the surface finish and material properties of the 3D printed part serve the needs of the desired application, then 3D printing remains an economical manufacturing method for up to 500 unit production runs (dependent on unit size)." - Sculpteo

And bear in mind that Sculpteo had every incentive to make sure this figure was as good as possible! As an additive manufacturing bureau they want to portray their technologies favourably.

Better software has also improved printing results; improvements in slicing engines, better design of support materials, semi-automatic design and placement of struts all contribute toward higher quality prints. Bedrich Benes, an academic at Purdue University, and Radomir Mĕch, from Adobe Systems worked on development of software to improve CAD files. The software can do things like increase the width of a fragile neck on a sculpture, to make sure it will print successfully. Mĕch explained to me, 

>“So there are basically two stages. One is that you can detect structural issues. And this can be found somewhere on the market. And the second thing is that you solve them. And you can solve them during the design phase, when you are creating the 3D object. [Or] you can solve them post when the object [is] created.”

‘Inspire’ software from solidThinking generates optimal organic shapes and struts, minimising material usage and maximising strength in printed objects. Their [case studies](http://www.solidthinking.com/ExploreStories.aspx?item=Stories&category=Explore) showcase the software's ability to reduce weight by 50% or more.

>""We are very satisfied with the results achieved. We have realized better designs and could fulfill all structural requirements in a shorter term." - Juan Manuel Romero, Alstom, solidThinking case study.

Although in the Alstom case study time to manufacture was shortened, this was because the iterative cycle of design optimisation was shortened – the actual additive printing process usually takes longer than conventional casting or milling. As [pointed out by ProtoLabs](https://www.protolabs.com/resources/design-tips/united-states/2015-05/): 

>“The process of melting metal one ultra thin layer at a time also isn’t terribly fast — our instruments may take a few days to build. For many parts, CNC machining remains the most economical choice.” - Protolabs, Manufacturing Design Tips.

[Plunkett Associates](http://www.plunkettassociates.co.uk/processes/direct-metal-laser-sintering-dmls.php), who deal in conventional and additive metal prototyping, explain 

> “There are limitations to be aware of, slow build speed, restriction of build volumes… support structures are required…these can be difficult to remove.”

This is reflected in the timescales – DMLS takes 2 weeks for Plunkett to turn around, sand casting just one week. Software solves important structural design problems unique to additive manufacturing, but does not enable any radical improvements in speed.

#The Limits
##Speed
Time taken to create an object is proportional to the number of printed layers. This is a more powerful effect than x and y movements in additive technologies. Whether it is a swipe and refresh stroke to lay fresh powder down, the movement of an object in a resin bath or the motion of an FDM extruder, z motion is crucial. As Joseph DeSimone says [“There are some mushrooms that grow faster than 3D printed parts.”](https://www.ted.com/talks/joe_desimone_what_if_3d_printing_was_25x_faster). To print parts quickly, they must be thin, with few layers - the 2D+ approach.

Some like Rob Winker of Stratays will argue that this [doesn’t matter much](http://www.stratasys.com/~/media/Main/Secure/White-Papers/WP_FDM_TruthAboutSpeed.pdf?la=en) if you are accustomed to leaving the printer running overnight. However, this approach fundamentally limits additive manufacturing to batch production.

Print head speed and acceleration restricts the speed at which the printer can produce each layer. This is a somewhat artificial limit – one can imagine a printer where the head(s) are stationary and a belt is swept underneath at high speed. In DMLS and SLA (selective laser sintering) the problem turns into a raster scanning one – how fast a laser may sweep across a bed of powder or a tank of resin while laying out a pattern. 

Fundamental speed restrictions are dictated by the physical properties of print materials that must melt and solidify. Take the example of depositing ABS using a heated extruder nozzle. [An elegant study](http://www.extrudable.me/2013/04/18/exploring-extrusion-variability-and-limits/) by Stuart Oliver determined the speed limits on PLA for the Ultimaker extruder to be around 8 – 10 mm3/sec for a 0.4mm diameter nozzle. After that point 

>“the constant excessive push of plastic into the hot end raises the pressure in the molten plastic, making it more likely that the molten plastic, unable to escape the way it is supposed to go, will instead find its way back up … and form a jam”.

This is not only a plastics issue. Currently, “steel powder is quite slow” and “expensive equipment (is) needed for essential post-processing” according to the textbook 'Developments in Rapid Casting'.

##Expense
There is a fundamental disconnect between price of hobbyist desktop equipment and the price of professional machines. No hobbyist could to afford to buy, run or maintain a metal sintering machine. Print bureaux give more access to the technology, but at a high price of £25 typically for a small metal part. Regardless of machine, there is little economy of scale in additive manufacture. If an increase in production volumes is needed, manufacturers naturally turn to conventional processes. [“Generally the material is expensive to buy, and the process is slow”](https://www.3dprint-uk.co.uk/management-of-expectations/) advises print service bureau 3D Print UK.

There has been enlightening [comparison](http://gizmodo.com/why-3d-printing-is-overhyped-i-should-know-i-do-it-fo-508176750) of desktop 3D printers to the bread making machine fad of the 90s – appealing as a novel concept, but not about to replace conventional methods due to cost and inconvenience.

Cost of materials is very high, typically around £35/kg for high quality plastic filaments, and ten times that or more for resins and powders. Some of these materials will inevitably be wasted due to swipe and refresh mechanism operations, support material printing and resin exposure to light. This raises product costs further.

>“Sadly for every request we have for a full sized Daft Punk helmet, there’s an equal number of disappointed Daft Punk fans out there, when they find out how much it will cost to build” - Nick Allen, Why 3D Printing is Overhyped.

Compare this to the <£1 - £10/kg raw material prices when purchasing even high quality engineering plastics in bulk and the enduring appeal of conventional methods becomes clear.

##Materials
In general, chemistry must be precisely understood and controlled – particularly as it relates to surface wetting since this controls the height and resolution of layers and interlayer bonding in droplet based printing. High wetting tends to give thinner layers with a stronger bond.

 Material properties and changes in the environment also affect print quality. Humidity, ambient temperature, storage of reels all affect plastic prints. Excess humidity causes water absorbent filaments such as nylon to noticeably swell and PLA filament to become more brittle and degrade. 

New materials have been used in additive manufacturing. The range now includes ceramics, elastomers, composites and waxes. These materials do not deliver any changes to the speed of manufacture however, and each material has its own unique challenges in printing.

##Maintenance and reliability 
OEE refers to Overall Equipment Effectiveness which measures the percentage of time equipment is used for production. “World class” OEE for machining centres and other non-continuous processes is commonly defined as 85%. Continuous processes can achieve [90% OEE or greater](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=5412049&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D5412049). Additive manufacturing tends to fall far beneath this, though it is difficult to gather exact data due to the secrecy of the main players. The machines are most suited to custom production runs and small order quantities, which brings down OEE metrics. Due to these restrictions, few final parts are made using additive techniques. Wohlers’ surveys indicate less than a quarter of additive sales are of functional parts. Their data from 2011 indicates around 13% of sales are direct part production. Additive production is still dominated by research and prototyping.


