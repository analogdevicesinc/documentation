Signal Merger
=============

:doc:`Click here to return to the Mixers/Splitters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/signalmerger_054.jpg
   :align: right

The Signal Merger mixes a group of input signals and automatically decreases the signal levels in proportion to the number of inputs -- as described in the table below:

::

          ^ # Inputs  ^ Linear Gain  ^ dB gain           ^ # Inputs  ^ Linear Gain  ^ dB gain  ^
          |    2      |    1/2       |   -6              |    7      |    1/7       | -16.9    |
          |    3      |    1/3       |   -9.5            |    8      |    1/8       | -18.1    |
          |    4      |    1/4       |  -12              |    9      |    1/9       | -19.1    |
          |    5      |    1/5       |  -14              |   10      |    1/10      | -20      |
          |    6      |    1/6       |  -15.6            |   11      |    1/11      | -20.8    |

This block's algorithm can be grown up to 15 inputs.

This block helps to avoid level overages (clipping) without the need to manually adjust mix levels.
