Preface Electronics I and II:
=============================

Preface:
--------

Broad interest in electronics started in the early 1900s with the introduction of radio communication and later broadcasting. Interest peaked in the 1940s, 50s, 60s, with the invention of solid state devices, the transistor radio, the launch of NASA, and the educational push in math and science to win the space race. One well known example is that interest in electronics as a hobby in the 1970s led to the creation of the personal computer.

Although they are extremely computer literate, today's engineering students frequently enter college without the same level of hands-on "tinkering" with hardware that prior generations exhibited. Gone are the days when students entering college were ham radio operators, played with Erector sets and had tinkered extensively with electronic kits or simply taken things apart. As a result, students have less "gut intuition" than prior generations possessed when entering the job market.

Today, while students are computer-savvy, they exhibit a diminished attention span, and have multiple demands on their time. Educational research has shown that humans retain as little as 10% of what they hear someone else tell them, but retain as much as 90% of what they learn by doing.

Typically authors of academic text books wanted their works to be considered the definitive reference for electrical engineering students and working engineers. This motivation leads to books containing considerably more material in much greater detail than could be realistically covered in a one semester Introduction to Electronics course. This introductory Electronics I text is limited to the scope of teaching undergraduate EE students and is not intended to replace that all inclusive reference book on the art and science of Electronics. Other authors have produced excellent examples of such texts. Much of the more in depth subject matter, such as reference texts and professional journals, is now available electronically over the internet.

In this text we attempt to pull out and condense the amount of material and level of detail to an amount that can realistically be presented in the course of 20 or so 2 hour lectures and 10 2 hour Lab sessions. Additional "advanced topics" are included in various chapters which can be inserted as desired. Electronics as, currently practiced, is largely a combination of some basic physical laws, rules of thumb and a large bag of tricks. For these reasons we have omitted entirely the usual in depth and detailed discussion of solid state physics, complicated network theory, and S-parameters. The treatment in this text is largely non-mathematical with strong encouragement of circuit brainstorming and mental estimation of circuit behavior and performance.

This book, through the extensive inclusion of laboratory activities, is an attempt at reviving the tinkering mentality that made electronics a popular career in the past, by making electronics concepts more accessible and giving practical knowledge, as well as providing underlying technical information for the reader. Where possible the text and labs provide side bar links to more in depth background information for the more curious readers to explore.

Traditional introductory text books on Electronics are often filled with detailed mathematical formulas which are used to explain the behavior of the electronic devices and circuits. It is certainly important to understand the underlying fundamentals, but it can be tedious and time consuming for the reader to calculate every detail of a circuit. This is often a distraction and frustration for someone trying to learn about electronics and can cause them to lose interest in the topic. The philosophy of this book is to let a circuit simulator, such as one or the other of the freely available versions of SPICE, do the heavy lifting beyond the basic math. The simulator can do it more accurately and faster than the reader. A simulation can tell the you within seconds if you are on the right track and how well the circuit performs. The instant feedback provided by the simulation can teach more about the circuit than simple words and diagrams on a page.

To further reinforce this philosophy this book makes extensive use of the more hands on concepts originally developed at Rensselear within the Mobile Studio project and desktop hardware and software. Laboratory activities are integrated with the lecture materials where the reader will learn and retain much more by actually building and analyzing real circuits, letting the low cost and compact individually owned hardware provide the "answers" instead of a book or the instructor. Lab experimentation provides a sense of where things deviate from theory, offering the opportunity to explore non-ideal conditions; while also giving the reader a chance to play with hardware and gain the experience that helps them support their subsequent design courses.

Hands-on, intellectually engaging studio course delivery was a revolutionary idea that has improved the quality of education at Rensselaer over the past several years and has since been adopted, in various forms, by many other universities. Yet even with more engaging studio environments, student learning is still impeded by space constraints, insufficient time for laboratory activities (particularly to do the in-depth probing that leads to an intuitive feel for system design) and poorly designed equipment that takes up a great deal of space. Furthermore, the equipment sets can't be brought home for individual study, thus limiting the time for hands-on exploration that students need to grasp the "big ideas" in engineering.

This text does not provide much in the way of historical background to the Electronic principles or concepts presented here. Those readers interested in such background are encouraged to search out the history of Electronics.

A few words on freely available SPICE like simulator software platforms. Qucs (Quite Universal Circuit Simulator) is a circuit simulator with graphical user interface. The software aims to support all kinds of circuit simulation types, e.g. DC, AC, S-parameter, Transient, Noise and Harmonic Balance analysis. Pure digital simulations are also supported.

A popular standalone version of Spice is Ngspice, a mixed-level/mixed-signal circuit simulator. Its code is based on three open source software packages: Spice3f5, Cider1b1 and Xspice. This package does not generally include Schematic Capture in the bundle. A front end software tool such as the Electric VLSI Design System or TinyCAD is needed to create simulation netlists for the circuit.

There are certain other "freely available" (but not open source) simulation tools. In addition to the example Labs which accompany this book, we provide example schematic files compatible with the SIMetrix simulation environment. The free Intro version of SIMetrix is distributed by SIMetrix Technologies Ltd. Analog Devices offers the ADsimPE simulator which is based on SIMetrix. The included Lab schematic material was created using version 7.1 of the Intro SIMetrix software and should be compatible with ADsimPE.

The Student version of PSpice, provided by Cadence, is also commonly used in Universities and is the choice of many instructors. In this book we do not provide ready made schematics for any of these non-open source tools.

Software Links:
---------------

**SIMetrix/SIMPLIS Intro**. SIMetrix/SIMPLIS Intro is a free version of the program with no license or copying restrictions. Virtually all features are enabled but a circuit size limit applies. The limits for the Intro versions are generous enough for them to be used for real work.

http://www.simetrix.co.uk/site/index.html

| **ADIsimPE:**
| \* Extensive library of ADI IC models and application schematics.
| \* Full schematics capture and editing capabilities with easy waveform viewing and analysis.
| \* SPICE mode SIMetrix simulation ideal for op-amps, references, Linear Regulators, and more.
| \* SIMPLIS mode simulation optimized for switching power supplies, PLLs, and more.
| \* Integration capability with ADIsimPower design tools.
| \* Supported by EngineerZone.

http://www.analog.com/en/content/adisimpe/fca.html

**Fritzing** is an open-source hardware initiative that makes electronics accessible as a creative material for anyone.

http://fritzing.org/home/

Other public domain circuit simulation or schematic entry software packages:

**Qucs - Quite Universal Circuit Simulator.**

Qucs is an integrated circuit simulator with the ability to setup a circuit with a graphical user interface (GUI) and simulate the large-signal, small-signal and noise behavior of the circuit. After the simulation has finished the simulation results can be viewed on a presentation page or window.

http://qucs.sourceforge.net/index.html

| NgSpice (Circuit Simulation)
| http://ngspice.sourceforge.net/

| Electric VLSI Design System (Schematic Capture / net listing)
| http://www.staticfreesoft.com/index.html

| TinyCAD (Schematic Capture / net listing)
| http://sourceforge.net/apps/mediawiki/tinycad/index.php?title=Main_Page

| Cadence/ OrCAD PSpice 9.1 Student version: (Schematic Capture / net listing / circuit simulation)

Acknowledgements:
~~~~~~~~~~~~~~~~~

Nearly all of the schematic figures in this book were generated using Analog Devices internal software. Most of the simulation plots were generated using Qucs.

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-1>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
