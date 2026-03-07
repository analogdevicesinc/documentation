Single Slew External Volume
===========================

:doc:`Click here to return to the Volume Controls section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/volumecontrols>`

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
| The Single Slew External Volume permits external control of an audio stream's signal level. The control signal can come from another algorithm within SigmaStudio; or, a microcontroller can apply changes by manipulating a DC Cell connected to the control pin. | |singleslewexternalvolume.jpg| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+

The slew function applies changes the signal level incrementally over a short period of time, eliminating pops or clicks from step changes at the control input.

Connect an input audio signal to the green pin and a control signal to the orange, external control pin. The text field allows you to specify the slew-rate time constant between 1 and 23 (Note this is a larger range than available for the Adjustable Volume Control block).

When only a few audio channels need to be slewed, the SW Slew algorithms may use fewer DSP cycles. This is due to the overhead of setting up the HW Slew accelerator. When there are many channels involved, the HW Slew option will be more efficient. The threshold depends on the DSP; cycles can be compared using SigmaStudio's Compiler Output window.

| 
| This table relates Slew settings to time constants (in ms) and convergence rates (in dB/s):

====== ====== =============
Slew # T (ms) Decay in dB/s
====== ====== =============
2      0.05   173720
3      0.10   86860
4      0.30   28953
5      0.60   14477
6      1.30   6682
7      2.60   3341
8      5.30   1639
9      10.60  819
10     21.30  408
11     43.0   204
12     85.0   102
13     171    51
14     341    26
15     680    13
16     1364   6.4
17     2730   3.2
18     5460   1.6
19     10860  0.8
====== ====== =============

| 
| You can both Grow Algorithm (add additional inputs and outputs) and Add Algorithms (Add additional control input pins and associated inputs and outputs) to this block; both functions are accessible from the block's right-click menu. Refer to Single Vol (Shared) for detailed discussion or adding and growing.

.. |singleslewexternalvolume.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singleslewexternalvolume.jpg
