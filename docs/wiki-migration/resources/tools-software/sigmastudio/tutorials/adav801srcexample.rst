Sample Rate Converter (SRC) example
===================================

| :doc:`Click here to return to the Tutorials page </wiki-migration/resources/tools-software/sigmastudio/tutorials>`
| Here is an example of how to use the Sample Rate Converter in the ADAV801 audio codec. The input will be an 1kHz test tone with a sample rate of 11.5kHz and the codec will output the same 1 kHz tone with a new sample rate of 44.1 kHz.

The routing inside the chip will be as follows:

-  Use the I\ :sup:`2`\ S Playback Port as input
-  Route from Playback Port to SRC at original sample rate (11.5 kHz)
-  Route from SRC to Record Port at new sample rate (44.1 kHz)
-  Use the I\ :sup:`2`\ S Record Port as output

| |SRCrouting.png|
|

.. tip::

   Please refer to the following supporting documents if any further clarification is needed throughout this example

   
   -  :adi:`ADAV801 datasheet <static/imported-files/data_sheets/ADAV801.pdf>`
   -  :adi:`Application Note AN-749 <static/imported-files/application_notes/60376866819334AN749_0.pdf>`
   


In order to achieve this routing, the Datapath Control Register 1 (0x62) register needs to be set. If you desire different routing for your own project, refer to the datasheet page listed in the following table(s).

+-----------------------------+------------------+----------------+------------------+
| Register Name               | Register Setting | Datasheet Page | Register Address |
+=============================+==================+================+==================+
| Datapath Control Register 1 | 10100xxx         | Page 45        | (0x62)           |
+-----------------------------+------------------+----------------+------------------+

Now you need to set the clocks for the desired output sampling rate, 44.1KHz in this example. Create the master clock using PLL2. You will need to modify the PLL Control Register 1 (0x74), PLL Control Register 2 (0x75), Internal Clocking Control Register 1 (0x76), and Internal Clocking Control Register (0x77).

+--------------------------------------+------------------+----------------+------------------+
| Register Name                        | Register Setting | Datasheet Page | Register Address |
+======================================+==================+================+==================+
| PLL Control Register 1               | xxxx0x0x         | page 52        | (0x74)           |
+--------------------------------------+------------------+----------------+------------------+
| PLL Control Register 2               | 110xxxxx         | page 53        | (0x75)           |
+--------------------------------------+------------------+----------------+------------------+
| Internal Clocking Control Register 1 | xxxxxx11         | page 54        | (0x76)           |
+--------------------------------------+------------------+----------------+------------------+
| Internal Clocking Control Register 2 | xxxxx00x         | page 55        | (0x77)           |
+--------------------------------------+------------------+----------------+------------------+

To assign the new clock to the sample rate converter master clock (SRC MCLK), modify the SRC and Clock Control (0x00) register.

===================== ================ ============== ================
Register Name         Register Setting Datasheet Page Register Address
===================== ================ ============== ================
SRC and Clock Control 0000xx01         page 32        (0x00)
===================== ================ ============== ================

You can use this same clock as the source for the Record Port by modifying the Record Port Control (0x06) register. It is also important to make sure that the Playback Port is in slave mode, so modifying the Playback Port Control (0x04) register is necessary.

+--------------------------------+------------------+----------------+------------------+
| Register Name                  | Register Setting | Datasheet Page | Register Address |
+================================+==================+================+==================+
| Record Port Control Register   | xx110001         | page 33        | (0x06)           |
+--------------------------------+------------------+----------------+------------------+
| Playback Port Control Register | xxx00001         | page 32        | (0x04)           |
+--------------------------------+------------------+----------------+------------------+

Make sure that the SRC output isn’t muted and has no delay.

==================== ================ ============== ================
Register Name        Register Setting Datasheet Page Register Address
==================== ================ ============== ================
Group Delay and Mute 0000000          page 34        (0x08)
==================== ================ ============== ================

Verify Functionality
--------------------

To verify that the sample rate conversion is working correctly, a 1 Khz tone with a 11.5kHz sample rate was created using SigmaStudio and an ADAU1781 evaluation board which output to the I\ :sup:`2`\ S Playback Port of an ADAV801. The sample rate was verified with an oscilloscope by placing a probe on the LRCLK of the input.

| 
| |InputFreq.png|
| To verify the correct output, a probe was placed on the LRCLK pin of the Record Port I\ :sup:`2`\ S output of the ADAV801. The signal was also analyzed to ensure the correct 1 kHz tone output.

| 
| |OutputFreq.png|
| |fft.png|
| |levels.png|

.. |SRCrouting.png| image:: https://wiki.analog.com/_media/SRCrouting.png
.. |InputFreq.png| image:: https://wiki.analog.com/_media/InputFreq.png
   :width: 600px
.. |OutputFreq.png| image:: https://wiki.analog.com/_media/OutputFreq.png
   :width: 600px
.. |fft.png| image:: https://wiki.analog.com/_media/fft.png
   :width: 600px
.. |levels.png| image:: https://wiki.analog.com/_media/levels.png
   :width: 600px
