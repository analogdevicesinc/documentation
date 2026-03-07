Single Volume (shared)
======================

:doc:`Click here to return to the Volume Controls section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/volumecontrols>`

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| The Single Vol (Shared) block is a volume slider programmed with the slew algorithm. If your DSP model does not support the slew algorithm, use the Single Volume Control (it's direct-write and has the option for the algorithm with no slew). If your DSP does support the slew algorithm, use this block, because it's more powerful. The ability to Add and Grow algorithms is important, especially in applications where multiple DSP boards will be used; this volume control lets you grow a particular algorithm already selected for a DSP. | |singlevolshared1.jpg| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+

The following steps clarify the difference between an added and grown algorithm with two DSPs. Observe that there is no visible difference between a grown and added algorithm on the block itself, and the only indication of different DSP boards is wire color of block connections.

-  Drag the block into the workspace. If you have multiple DSP boards connected, It will be an empty block, as shown here.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolshared2.jpg
   :alt: singlevolshared2.jpg

-  Right-click it and select Add Algorithm > IC 1 > Single Gain xxxx (slew). (If you have only one DSP connected, you don't have to do this.)

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolshared3.jpg
   :alt: singlevolshared3.jpg

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolshared4.jpg
   :alt: singlevolshared4.jpg

-  Right-click the block border or title and select Grow Algorithm > 1. Single Gain xxxx (slew) > 1. This adds another set of input/output pins for the same DSP board and algorithm as in step 2.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolshared5.jpg
   :alt: singlevolshared5.jpg

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolshared6.jpg
   :alt: singlevolshared6.jpg

-  Right-click the block border or title and select Add Algorithm > IC 2 > Single Gain xxxx (slew) > 1. This adds another set of input/output pins, but corresponding to a different DSP board. Other blocks that you want to connect to these pins must be independent (not associated with any DSP), or they must have the same algorithm associated with the block.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolshared7.jpg
   :alt: singlevolshared7.jpg

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolshared8.jpg
   :alt: singlevolshared8.jpg

Now the top two pins are associated with the DSP under IC 1, while the bottom pin is associated with the DSP under IC 2. To wire this block to other blocks, you maintain the same DSP association; the software will not let you connect pins from one DSP to another. Observe the different-color traces for the different DSP boards below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolshared9.jpg
   :alt: singlevolshared9.jpg

.. |singlevolshared1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolshared1.jpg
