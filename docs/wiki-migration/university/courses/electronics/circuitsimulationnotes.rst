Circuit Simulation Notes
========================

A common tool (computer aided design or CAD / electronic design automation or EDA software) for the electronic circuit designer is circuit simulation software. Although most often called simply a *simulator*, it is a software application that typically may include many functions beyond electrical circuit simulation, including schematic capture, printed circuit board layout, and bill of materials generation.

Most circuit simulator software grew out of a public domain program called SPICE (Simulation Program with Integrated Circuit Emphasis) developed at UC Berkeley\ :sup:`[1]` in the 1970s. The original SPICE program operated in a batch mode and was text based. That is, the user created a text file which described the circuit using a special circuit netlist syntax. This file also included simulation directives which told the software what type of simulation is to be performed. The SPICE program read the input file, performed the appropriate analyses, and produced a text output file that contained the results. Graphs of output functions were drawn using text characters in a low resolution fashion. It may not have been very user friendly, but it was functional.

Over time EDA companies began adding graphical "back-ends" that could produce better looking graphs and plots of the simulation results. A next obvious step was to add a graphical interface for building the circuit (GUI). This had the dual benefit of both describing the circuit for the simulation engine (generating the SPICE netlist) and allowing for the production of publication quality schematic diagrams. Some of the early popular graphical versions included PSpice and ElectronicsWorkbench (EW being the precursor to Multisim).

Eventually, functionality to create printed circuit board layouts from the schematics was added, along with supporting features such as electrical and design rule checking and Bill of Materials (BOM, basically a components list).

More recent features include instrumentation simulation. That is, simulations of real world commercial measurement devices may be used as part of the circuit simulation. In this way, a sort of "virtual lab bench" may be created. Some packages, such as Fritzing\ :sup:`[2]`, also include physical imagery of devices and proto-boards. With this feature, the circuit being designed will look very similar to the actual circuit sitting on your lab bench. That is, if a transistor is used in the simulation, it will look like a real transistor instead of the standard schematic symbol. While this may initially appear to be very useful, especially for beginners, in practical terms it sometimes slows down the design process by making the schematic less clear and more cluttered to the user.

Circuit simulation tools are available in both the public domain and commercially. Commercial simulation packages can cost up to several thousand dollars. Fortunately, an introductory or Student version of many programs is available, in many cases for free. The accompanying schematic files provided for use with the example electronics labs were created using a software package called SIMetrix\ :sup:`[3]`. It is distributed by SIMetrix Technologies Ltd. SIMetrix/SIMPLIS Intro is Free. You may use it with the following conditions, to simulate SIMetrix circuits up to 140 nodes, for any purpose, commercial or non-commercial, for as long as you like - there are no time limits.

The included Lab schematic material (see links below) was created using version 7.1 of the SIMetrix software. Other versions of the software will be similar although there may be some differences in the appearance and functionality.

The archive files contain folders with one or more example schematics for use with each Lab Activity. A few extra device model files are also included in the archive that do not generally come bundled with the software. These can be added to the model library by dragging and dropping them onto the SIMetrix main window. The provided schematic files are also compatible with the Analog Devices supplied ADsimPE\ :sup:`[4]` simulator which is based on SIMetrix.

There is also an archive file that contains schematic files with examples for the lab activities that are compatible with the LTspice\ :sup:`[5]` simulation software.

It is recommended that the free introductory version of SIMetrix (or ADsimPE) be installed on the students' personal computer or laptop early in the class. Basic tutorials are included with the software which can be used to become familiar with the software. Simulation Pre-Lab activities will help reinforce the experience gained with the hands-on lab work.

**Electronics I lab simulation schematic files with ADsimPE:** :git-education_tools:`m2k/adisimpe/electronics-lab-i`

**Electronics II lab simulation schematic files with ADsimPE:** :git-education_tools:`m2k/adisimpe/electronics-lab-ii`

**Electronics lab simulation schematic files with LTspice:** :git-education_tools:`electronics-lab-ltspice <m2k/ltspice>`

| **Mini-Tutorial on analog circuit simulation:**
| http://www.analog.com/static/imported-files/tutorials/MT-099.pdf

[1] L. W. Nagel, "SPICE2: A Computer Program to Simulate Semiconductor Circuits," May 1975, UCB/ERL M75/520, Univ. of California, Berkeley, CA, 94720.

Software Links:
---------------

[3] **SIMetrix/SIMPLIS Intro**. SIMetrix/SIMPLIS Intro is a free version of the program with no license or copying restrictions. Virtually all features are enabled but a circuit size limit applies. The limits for the Intro versions are generous enough for them to be used for real work.

http://www.simetrix.co.uk/site/index.html

| [4] **ADIsimPE:**
| \* Extensive library of ADI IC models and application schematics.
| \* Full schematics capture and editing capabilities with easy waveform viewing and analysis.
| \* SPICE mode SIMetrix simulation ideal for op-amps, references, Linear Regulators, and more.
| \* SIMPLIS mode simulation optimized for switching power supplies, PLLs, and more.
| \* Integration capability with ADIsimPower design tools.
| \* Supported by EngineerZone.

http://www.analog.com/en/content/adisimpe/fca.html

[5] **LTspice** is a freeware computer software implementing a SPICE simulator of electronic circuits, produced by semiconductor manufacturer Linear Technology, now part of Analog Devices.

http://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html

[2] **Fritzing** is an open-source hardware initiative that makes electronics accessible as a creative material for anyone.

http://fritzing.org/home/

| Another public domain circuit simulation software package:
| **Qucs - Quite Universal Circuit Simulator.**

Qucs is an integrated circuit simulator with the ability to setup a circuit with a graphical user interface (GUI) and simulate the large-signal, small-signal and noise behavior of the circuit. After the simulation has finished the simulation results can be viewed on a presentation page or window.

http://qucs.sourceforge.net/index.html

**Back to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`
