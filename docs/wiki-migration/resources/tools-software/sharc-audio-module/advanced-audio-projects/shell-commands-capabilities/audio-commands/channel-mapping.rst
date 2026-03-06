Overview
========

This section describes hardware channel mappings for src and dst offsets that are inputs to route shell command.

--------------

src/dst offsets for SC589 Mini
------------------------------

| |image1|
| *SC589-Mini Audio Line In/Out Connectors*

| Below is the table for src offset and the corresponding audio output.
| A route is added from codec for dst offset as 0, for 1 channel and with 0dB attenuation on SC589-mini.
| route <idx> codec <SRC Offset> codec 0 1 0

==================== =============
**Codec SRC Offset** **Mapped to**
0                    LINE IN
1                    LINE IN
==================== =============

| Below is the table for dst offset and the corresponding audio output (L/R).
| A route is added for codec for any src offset, 1 channel and 0dB attenuation on SOMCRR EZKIT Rev-A.
| route <idx> codec <src offset> codec <dst offset> 1 0

==================== ======================
**Codec DST Offset** **Audio audible from**
0                    Left
1                    Right
==================== ======================

--------------

src/dst offsets for SC598 SOMCRR EZKIT Rev-A
--------------------------------------------

| |image2|
| *SOMCRR-EZKIT Rev-A Audio In/Out Connectors*

| Below is the table for src offset and the corresponding channel mapping.
| A route is added as shown for input and output as codec audio for dst offset as 0, for 1 channel and with 0dB on SC598 SOMCRR EZKIT Rev-A.
| route <idx> codec <SRC Offset> codec 0 1 0
| Carrier board ADC inputs need to be enabled with this shell command - adc enable

==================== ======= ==============================
**Codec SRC Offset** **adc** **Starting channel mapped to**
0                    enable  AN1
1                    enable  AN2
2                    enable  AN3
3                    enable  AN4
==================== ======= ==============================

| Below is the table for dst offset and the corresponding channel mapping.
| A route is added for spdif audio input, src offset as 0, codec as stream destination, 1 channel and 0dB attenuation on SOMCRR EZKIT Rev-A.
| route <idx> spdif 0 codec <dst offset> 1 0
| adc <enable/disable>
| DNC - do not care

==================== ============= ==============================
**Codec DST Offset** \*\* adc \*\* **Starting channel mapped to**
0                    DNC           DAC1
1                    DNC           DAC2
2                    DNC           DAC3
3                    DNC           DAC4
4                    DNC           DAC5
5                    DNC           DAC6
6                    DNC           DAC7
7                    DNC           DAC8
8                    disable       DAC9
9                    disable       DAC10
10                   disable       DAC11
11                   disable       DAC12
==================== ============= ==============================

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/audio-commands/sc589-mini-channel-mapping.jpg
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/audio-commands/somcrr-ezkit-aud-in-out-updated.png
   :width: 400px
