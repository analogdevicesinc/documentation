Single Volume Control
=====================

:doc:`Click here to return to the Volume Controls section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/volumecontrols>`

+--------------------------------------------------------------------------------------------------------------------------+----------------------------+
| The Single Volume Control block is a GUI-controlled volume slider. It allows access to both slew and no-slew algorithms. | |singlevolumecontrol1.jpg| |
+--------------------------------------------------------------------------------------------------------------------------+----------------------------+

Right-click the block border or title to Add algorithms, which adds pins controlled by the slider. Each pin can be associated with a different algorithm (slew or no slew) under control of this slider. Pay attention when selecting multiple algorithms. There is no visible indication on the block of whether each pin corresponds to a slew or no slew algorithm. The :doc:`User Comment </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign/usercomment>` feature can help you keep track of which pins correspond to which algorithm.

The right-click menu also allows selection of different slew modes.


|image1|

The slider control's min/max value and step size can be customized. To modify the slider's settings, right-click on the control which will display the control pop-up window (shown below).

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolumecontrol2.jpg
   :alt: singlevolumecontrol2.jpg
   :align: center

Adjusting the Volume Control from a Microcontroller
===================================================

The following assumes you have a working microcontroller platform, with SigmaDSP interface code based on :doc:`Interfacing SigmaDSP Processors with a Microcontroller </wiki-migration/resources/tools-software/sigmastudio/tutorials/microcontroller>`.

The SigmaStudio GUI allows users to choose a gain value in dB. However, within SigmaDSP processors, the volume control value is stored as a linear gain. SigmaStudio automatically performs this conversion. In a system with a controller, the controller should convert a user's dB entry to linear.

The linear scale factor is stored in decimal format (8.24 or 5.23).

Reading Volume Values from the SigmaDSP
---------------------------------------

.. code:: cpp

   double read_volume_control(int controlAddress) {
    double linear_gain = SIGMA_READ_REGISTER_FLOAT(controlAddress);
    return 20 * log10(linear_gain);
   }

Example Usage:

.. code:: cpp

   // Print the current volume in dB; adjust MOD_SWVOL1_ALG0_TARGET_ADDR to match your volume control
   Serial.println(read_volume_control(MOD_SWVOL1_ALG0_TARGET_ADDR));

Writing Volume Values to the SigmaDSP
-------------------------------------

.. code:: cpp

   void write_volume_control(int controlAddress, double dBGain) {
    double linearGain = pow(10, dBGain / 20);
    SIGMA_WRITE_REGISTER_FLOAT(controlAddress, linearGain);
   }

Example Usage:

.. code:: cpp

   // Set the current volume of the control to -30 dB
   write_volume_control(MOD_SWVOL1_ALG0_TARGET_ADDR, -30);

.. |singlevolumecontrol1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolumecontrol1.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/singlevolumecontrol_slew.png
   :width: 400px
