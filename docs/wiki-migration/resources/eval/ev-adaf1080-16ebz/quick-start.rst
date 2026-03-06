AMR Current Sensing Quick Start Guide
=====================================

Features
--------

-  500A DC and AC
   \* <1mArms Noise
   \* <1% Error in Clamp Center
   \* <1% Positional Sensitivity within Clamp
   \* More than 40dB Rejection to Stray Fields
   \* Negligible Hysteresis
   \* 28mm Wire Opening

Hardware Requirement
--------------------

-  Castor Sensor Board
   \* Gemini Acquisition Board
   \* 5V Wall Adapter

.. container:: centeralign

   \ |image1|\ *Figure 1. EV-ADAF1080-16EBZ Kit -- AMR Array Based Contactless Current Sensing System*


General Description
-------------------

The Castor and Gemini boards together make up an AMR Array Based Contactless Current Sensing System. This is the quick-start guide, please refer to the AMR Current Sensing User Guide Figure 1 shows the default jumper settings that are required to operate the AMR Array Based Contactless Current Sensing System.

Quick Setup for Contactless Current Measurement
-----------------------------------------------

-  Separate the Castor board.
-  Connect the Castor board to the Gemini Board.

.. image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/ezgif.com-gif-maker.gif
   :align: center

-  Place the wire to be measured in the Castor board and reconnect the removable jaw and plastic spacers.
-  Plug in the wall adapter completely so that it is flush with the connector.
-  Press and hold the ON/OFF button for more than 1 second to power on, see Figure 2.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 2. EV-ADAF1080-16EBZ Quick Setup


.. note::

   The wireloop multiplies the effective magnetic field strength depending on the number of wire turns. For example, passing through a 1A current to a 10-turn wire loop will have an effective magnetic field strength of 10A


-  The LCD will turn on and will start displaying the measurement results, see Figure 3

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   Figure 3. EV-ADAF1080-16EBZ LCD Display


-  Pressing the ‘Null’ button at any time will null the measurement, see Figure 1.

.. image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/ezgif.com-gif-maker_1_.gif
   :align: center

| 
| =====Contactless AMR Current Measurement GUI===== The AMR Array Based Contactless Current Sensing System includes a PC Software GUI providing features that enables the customer to plot the current measurement data through graph, data logging, and have the flexibility to operate the solution in different modes.
| These features are explained in detail in this `Software User Guide <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz/sw-ug`>`__ page.

Other Information
-----------------

-  `Main Page <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz`>`__
-  `Software User Guide <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz/sw-ug`>`__
-  `Hardware User Guide <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz/hw-ug`>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/ev-adaf1080-16ebz_kit_top2a.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/castorwithwireloop.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/lcd2.png
   :width: 400px
