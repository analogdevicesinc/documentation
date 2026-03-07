RMS Table
=========

:doc:`Click here to return to the Level Detectors/Lookup Tables page </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/rmstable_004.jpg
   :align: right

The RMS Table takes an input signal and outputs the interpolated mapped value of the signal, relative to the table, depending on the calculated rms input. The block uses rms average values and maps them to the user-selectable table values, employing linear interpolation in between table values.

Three parameters are available through the edit boxes / control arrows:

+---------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RMS TC (dB/s) | |image4| | Controls the time constant (TC) used for calculating the rms value. This determines how rapidly the gain will adapt to changes in the input level; this is also called the attack time.      |
+---------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)     | |image5| | Controls the time the rms average holds its current output setting before it detects a lower value and starts ramping down.                                                                  |
+---------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay (dB/s)  | |image6| | Controls the rate at which the output signal returns to a lower detected level. Decay is responsible for releasing the signal at a given rate. This is also referred to as the release time. |
+---------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Press Show Table to view and edit the table values. The calculated signal RMS values are mapped to an index in the table. The maximum table resolution is approximately 96 dB with indices spaced 3 dB apart (as shown in the example below).

=========== =================== ==============================
Table Index Detected Value (dB) Mapped Values (user-specified)
=========== =================== ==============================
1           -90                 0.01
2           -87                 0.01
3           -84                 0.01
4           -81                 0.02
5           -78                 0.02
6           -75                 0.02
7           -72                 0.02
8           -69                 0.03
9           -66                 0.03
10          -63                 0.04
11          -60                 0.04
12          -57                 0.05
13          -54                 0.06
14          -51                 0.07
15          -48                 0.08
16          -45                 0.09
17          -42                 0.10
18          -39                 0.12
19          -36                 0.13
20          -33                 0.15
21          -30                 0.18
22          -27                 0.21
23          -24                 0.24
24          -21                 0.28
25          -18                 0.32
26          -15                 0.37
27          -12                 0.42
28          -9                  0.49
29          -6                  0.57
30          -3                  0.65
31          0                   0.75
32          3                   0.87
33          6                   1.01
=========== =================== ==============================

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/rmstable_005.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/rmstable_006.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/rmstable_007.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/rmstable_005.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/rmstable_006.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/rmstable_007.jpg
