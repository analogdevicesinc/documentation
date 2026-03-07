AD5758 + ADP1031 Eight Channel Analog Output Module
===================================================

Using the Demo Board
--------------------

|

.. important::

   Before proceeding, please ensure you have the DEMO_AD5758-AO8Z Demo software installed on your PC or Laptop and that the latest version of the firmware has been uploaded to the board. Instructions on how to complete these steps can be found earlier in this guide in the `Software Details <https://wiki.analog.com/software>`_ section.


   |image1|

| Figure 1 - DEMO-AD5758-AO8Z Setup

Connecting the Board
~~~~~~~~~~~~~~~~~~~~

-  Remove Jumpers P4 & P5
-  Connect the power supplies as show in Figure 1. The field power supply should be capable of supplying at least 300 mA @ 24 V. The system supply needs to only supply about 20 mA (max) @ 24 V
-  Alternatively, if only one power supply is available, then P4 & P5 jumpers can be left in place and a single field supply used.

.. warning::

   If either P4 and/or P5 jumpers are inserted, then there will be no isolation between the system domain and the field power domain.


-  Connect a USB cable from your PC or laptop to the USB port on the demo board.
-  Start the DEMO-AD5758-AO8Z GUI Software and select the correct COM port, then click [**Connect**]
   <WRAP>\ |image2|\ </WRAP>

-  The GUI display should resemble the following image. <WRAP>\ |image3|\ </WRAP>

DPC ON vs. DPC OFF Demonstration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Quiescent Current should be approximately:-

   -  I\ :sub:`FIELD` = 26 mA ± 5 mA
   -   I\ :sub:`SYSTEM` = 3 mA ± 1 mA

-  Connect a 1 Ω resistors to each of eight channel headers (CH0 to CH7].

.. note::

   Resistor values between 0 Ω and 1 kΩ can be used. However, lower values provide a more challenging load and demonstrate the DPC mode power savings better.


-  Turn on Channel 0 by clicking the **DPC OFF** radio button. This turns on the channel but leaves DPC mode disabled by fixing the output of the DPC buck (and thus the power supply to the buffer) to 23.3 V<WRAP>\ |image4|\ </WRAP>

-  Set Desired Output to 20 mA and click **Apply to all**. This will set the remaining channels to the same state as channel 0. i.e. 20 mA output, DPC OFF. <WRAP>\ |image5|\ </WRAP>

Observe that VDPC+ is fixed at 23.3 V even though the buffer output is at 0 V.
-  I\ :sub:`FIELD` should now be around 207 mA ± 10 mA (~5 W). I\ :sub:`SYSTEM` should be relatively unchanged.
-  Click the **Status** button of any channel to see a graph of the internal die temperature rise of the :adi:`AD5758`. Notice how the temperature rises rapidly when DPC is disabled.
   <WRAP>\ |image6|\ </WRAP>

.. note::

   When DPC mode is turned **off**, the DPC buck is programmed to output a fixed voltage of 23.3 V. Because the load resistance is low (1 Ω), there is a large voltage drop across the :adi:`AD5758` output buffer. There is 23.3V X 20mA = 466mW of power dissipated in the output buffer plus an additional 47 mW dissipation in the DPC buck regulator

   (466 mW X (1-η)). Which translates to 513 mW of dissipation per channel in the module.


-  Now select CH0 **DPC ON**
   <WRAP>\ |image7|\ </WRAP>

-  Click "**Apply to all**".
   <WRAP>\ |image8|\ </WRAP>

Notice how VDPC+ is now at its minimum value of approximately 4.95 V and the die temperature begins to drop rapidly as DPC power saving take effect.
   <WRAP>\ |image9|\ </WRAP>

.. note::

   When DPC mode is turned **on**, a high efficiency (η = 0.9) buck converter reduces the supply to the buffer to 2.5 V above the required output voltage or 4.95 V - whichever is higher, so there is now a small voltage drop of only 4.95 V across the :adi:`AD5758` output buffer\ :sup:`1`. This translates to 4.95V X 20mA = 99mW plus 99 mW X (1 - η) = 10 mW of heat dissipation in the output buffer of the :adi:`AD5758`. This is a power saving of 404 mW per channel.

   :sup:`<fc #ff0000>1</fc>` <fc #ff0000>If VIOUT > 2.5 V, then the the DPC buck tracks the output to maintain a fixed 2.5 V headroom.</fc>


-  I\ :sub:`FIELD` should now be around 72 mA ± 5 mA (~ 1.7 W). I\ :sub:`SYSTEM` should be unchanged.

Related Resources
~~~~~~~~~~~~~~~~~

-  :adi:`AD5758`: Single-Channel, 16-Bit Current and Voltage Output DAC with Dynamic Power Control and HART Connectivit
-  :adi:`adp1031`: Three-Channel, Isolated Micropower Management Unit with Seven Digital Isolators
-  Video: `ADI: Doubling Channel Density of Industrial Output Modules <https://www.youtube.com/watch?v=3jvZrx5-yEY>`_
-  Video `Analog Devices: AD5758 DAC for EMC/EMI Robustness <https://www.youtube.com/watch?v=QbfdilQjfNY>`_

--------------

Navigation
~~~~~~~~~~

`Top <https://wiki.analog.com/../ad5758_adp1031>`_ \| `Previous(Software Details) <https://wiki.analog.com/software>`_ \| `Next (Legal terms and conditions) <https://wiki.analog.com/legal_terms_and_conditions>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/demo-ad5758-ao8z/artboard_1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/demo-ad5758-ao8z/com-connect.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/guii/full-panel-power_up-state.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/gui/dpc_off-0ma.png
   :width: 250px
.. |image5| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/gui/apply-to-all-dpc_off-20ma.png
   :width: 250px
.. |image6| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/gui/die-temperature_rise_off-to-dpc_off.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/demo-ad5758-ao8z/13-08-2019_14-17-26.png
   :width: 250px
.. |image8| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/13-08-2019_14-26-28.png
   :width: 250px
.. |image9| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/gui/die-temperature_fall_dpc_off-to-dpc_on-very-long.png
   :width: 250px
