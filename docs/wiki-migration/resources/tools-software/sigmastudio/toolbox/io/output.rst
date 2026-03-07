Output
======

| :doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudio/toolbox/io>`

--------------

| The Output block routes signals to the hardwares physical outputs. Each block is linked to a single output channel.
| |outputpic1.png|
| Using the drop-down list, select the output channel to associate with a particular block.

Observe that as you drag more output blocks to your schematic, the number of output channels available in the drop-down list decreases because each output can only be associate with a single output block at a time.

If you have multiple DSP processors in a design, specify which processor to associate with the output block by right-clicking the block and selecting Add Algorithm > IC # > *DSP Type* from the menu.

| The hardware outputs for a particular processor are limited. While designing you can see the number of outputs that are still available from the HWOutputs item of the :doc:`Resources window </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/workspacewindows>`.
| |outputpic2.png|

Relationship Between Hardware Outputs and SigmaStudio Output Channels
---------------------------------------------------------------------

The relationship between an output cell in SigmaStudio and the physical output pin on the chip can vary in some cases depending on register settings.

AD1940/AD1941
~~~~~~~~~~~~~

+----------------------------+-----------------------------------------+-----------------------------------+
| SigmaStudio Output Channel | Hardware Output in 2 Channel (I2S) Mode | Hardware Output in TDM Mode       |
+============================+=========================================+===================================+
| 0                          | Left channel on SDATA_OUT0              | First TDM channel on SDATA_OUT0   |
+----------------------------+-----------------------------------------+-----------------------------------+
| 1                          | Right channel on SDATA_OUT0             | Second TDM channel on SDATA_OUT0  |
+----------------------------+-----------------------------------------+-----------------------------------+
| 2                          | Left channel on SDATA_OUT1              | Third TDM channel on SDATA_OUT0   |
+----------------------------+-----------------------------------------+-----------------------------------+
| 3                          | Right channel on SDATA_OUT1             | Fourth TDM channel on SDATA_OUT0  |
+----------------------------+-----------------------------------------+-----------------------------------+
| 4                          | Left channel on SDATA_OUT2              | Fifth TDM channel on SDATA_OUT0   |
+----------------------------+-----------------------------------------+-----------------------------------+
| 5                          | Right channel on SDATA_OUT2             | Sixth TDM channel on SDATA_OUT0   |
+----------------------------+-----------------------------------------+-----------------------------------+
| 6                          | Left channel on SDATA_OUT3              | Seventh TDM channel on SDATA_OUT0 |
+----------------------------+-----------------------------------------+-----------------------------------+
| 7                          | Right channel on SDATA_OUT3             | Eighth TDM channel on SDATA_OUT0  |
+----------------------------+-----------------------------------------+-----------------------------------+
| 8                          | Left channel on SDATA_OUT4              | First TDM channel on SDATA_OUT4   |
+----------------------------+-----------------------------------------+-----------------------------------+
| 9                          | Right channel on SDATA_OUT4             | Second TDM channel on SDATA_OUT4  |
+----------------------------+-----------------------------------------+-----------------------------------+
| 10                         | Left channel on SDATA_OUT5              | Third TDM channel on SDATA_OUT4   |
+----------------------------+-----------------------------------------+-----------------------------------+
| 11                         | Right channel on SDATA_OUT5             | Fourth TDM channel on SDATA_OUT4  |
+----------------------------+-----------------------------------------+-----------------------------------+
| 12                         | Left channel on SDATA_OUT6              | Fifth TDM channel on SDATA_OUT4   |
+----------------------------+-----------------------------------------+-----------------------------------+
| 13                         | Right channel on SDATA_OUT6             | Sixth TDM channel on SDATA_OUT4   |
+----------------------------+-----------------------------------------+-----------------------------------+
| 14                         | Left channel on SDATA_OUT7              | Seventh TDM channel on SDATA_OUT4 |
+----------------------------+-----------------------------------------+-----------------------------------+
| 15                         | Right channel on SDATA_OUT7             | Eighth TDM channel on SDATA_OUT4  |
+----------------------------+-----------------------------------------+-----------------------------------+

ADAU1701/ADAU1702/ADAU1401/ADAU1401A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------+-----------------------------------------+-----------------------------------+
| SigmaStudio Output Channel | Hardware Output in 2 Channel (I2S) Mode | Hardware Output in TDM Mode       |
+============================+=========================================+===================================+
| DAC0                       | DAC_OUT0                                | N/A                               |
+----------------------------+-----------------------------------------+-----------------------------------+
| DAC1                       | DAC_OUT1                                | N/A                               |
+----------------------------+-----------------------------------------+-----------------------------------+
| DAC2                       | DAC_OUT2                                | N/A                               |
+----------------------------+-----------------------------------------+-----------------------------------+
| DAC3                       | DAC_OUT3                                | N/A                               |
+----------------------------+-----------------------------------------+-----------------------------------+
| DIG0                       | Left channel on SDATA_OUT0              | First TDM channel on SDATA_OUT0   |
+----------------------------+-----------------------------------------+-----------------------------------+
| DIG1                       | Right channel on SDATA_OUT0             | Second TDM channel on SDATA_OUT0  |
+----------------------------+-----------------------------------------+-----------------------------------+
| DIG2                       | Left channel on SDATA_OUT1              | Third TDM channel on SDATA_OUT0   |
+----------------------------+-----------------------------------------+-----------------------------------+
| DIG3                       | Right channel on SDATA_OUT1             | Fourth TDM channel on SDATA_OUT0  |
+----------------------------+-----------------------------------------+-----------------------------------+
| DIG4                       | Left channel on SDATA_OUT2              | Fifth TDM channel on SDATA_OUT0   |
+----------------------------+-----------------------------------------+-----------------------------------+
| DIG5                       | Right channel on SDATA_OUT2             | Sixth TDM channel on SDATA_OUT0   |
+----------------------------+-----------------------------------------+-----------------------------------+
| DIG6                       | Left channel on SDATA_OUT3              | Seventh TDM channel on SDATA_OUT0 |
+----------------------------+-----------------------------------------+-----------------------------------+
| DIG7                       | Right channel on SDATA_OUT3             | Eighth TDM channel on SDATA_OUT0  |
+----------------------------+-----------------------------------------+-----------------------------------+

ADAU1442/ADAU1445/ADAU1446
~~~~~~~~~~~~~~~~~~~~~~~~~~

The routing between pin and SigmaStudio channel is dependent on the individual channel settings of each serial port. Refer to the :adi:`datasheet <static/imported-files/data_sheets/ADAU1442_1445_1446.pdf>` for more information.

ADAU1761
~~~~~~~~

+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| SigmaStudio Output Channel | Hardware Output in 2 Channel (I2S) Mode | Hardware Output in TDM4 Mode    | Hardware Output in TDM8 Mode     |
+============================+=========================================+=================================+==================================+
| DAC0                       | Left DAC Output                         | Left DAC Output                 | Left DAC Output                  |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| DAC1                       | Right DAC Output                        | Right DAC Output                | Right DAC Output                 |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| DIG0                       | Left channel on ADC_SDATA               | First TDM channel on ADC_SDATA  | First TDM channel on ADC_SDATA   |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| DIG1                       | Right channel on ADC_SDATA              | Third TDM channel on ADC_SDATA  | Fifth TDM channel on ADC_SDATA   |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| DIG2                       | N/A                                     | Second TDM channel on ADC_SDATA | Second TDM channel on ADC_SDATA  |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| DIG3                       | N/A                                     | Fourth TDM channel on ADC_SDATA | Sixth TDM channel on ADC_SDATA   |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| DIG4                       | N/A                                     | N/A                             | Third TDM channel on ADC_SDATA   |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| DIG5                       | N/A                                     | N/A                             | Seventh TDM channel on ADC_SDATA |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| DIG6                       | N/A                                     | N/A                             | Fourth TDM channel on ADC_SDATA  |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+
| DIG7                       | N/A                                     | N/A                             | Eighth TDM channel on ADC_SDATA  |
+----------------------------+-----------------------------------------+---------------------------------+----------------------------------+

ADAU1761 in I2S (2 channel) Output Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/adau1761_output_routing_004.jpg
   :align: center

ADAU1761 in TDM4 (4 channel) Output Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/adau1761_output_routing_005.jpg
   :align: center

ADAU1761 in TDM8 (8 channel) Output Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/adau1761_output_routing_006.jpg
   :align: center

ADAU1781
~~~~~~~~

+----------------------------+-----------------------------------------+----------------------------------+
| SigmaStudio Output Channel | Hardware Output in 2 Channel (I2S) Mode | Hardware Output in TDM Mode      |
+============================+=========================================+==================================+
| DAC0                       | Left DAC Output                         | N/A                              |
+----------------------------+-----------------------------------------+----------------------------------+
| DAC1                       | Right DAC Output                        | N/A                              |
+----------------------------+-----------------------------------------+----------------------------------+
| DIG0                       | Left channel on ADC_SDATA               | First TDM channel on ADC_SDATA   |
+----------------------------+-----------------------------------------+----------------------------------+
| DIG1                       | Right channel on ADC_SDATA              | Second TDM channel on ADC_SDATA  |
+----------------------------+-----------------------------------------+----------------------------------+
| DIG2                       | N/A                                     | Third TDM channel on ADC_SDATA   |
+----------------------------+-----------------------------------------+----------------------------------+
| DIG3                       | N/A                                     | Fourth TDM channel on ADC_SDATA  |
+----------------------------+-----------------------------------------+----------------------------------+
| DIG4                       | N/A                                     | Fifth TDM channel on ADC_SDATA   |
+----------------------------+-----------------------------------------+----------------------------------+
| DIG5                       | N/A                                     | Sixth TDM channel on ADC_SDATA   |
+----------------------------+-----------------------------------------+----------------------------------+
| DIG6                       | N/A                                     | Seventh TDM channel on ADC_SDATA |
+----------------------------+-----------------------------------------+----------------------------------+
| DIG7                       | N/A                                     | Eighth TDM channel on ADC_SDATA  |
+----------------------------+-----------------------------------------+----------------------------------+

--------------

AD1953 Output
-------------

.. warning::

   The AD1953 is not recommended for new designs. Information is included here for reference only.


| The AD1953 has the DACs built into the DSP core, so you must choose an interpolation filter for the output. To use Output blocks with the AD1953 you will need to add an algorithm. As shown below, right-click the block to select which interpolating filter you would like to implement in the DSP core.
| |outputpic3.png|

Next, designate the channel on the block to be left, right, or sub. Only one block can write to the same output channel.

Following are descriptions of the interpolation filters:

**Write to DAC No Interp**

Writes to the DAC registers with no interpolation. Useful for subwoofer outputs, where it does not matter that distortion above 2kHz rises (output slewing) and HF response suffers (sinc(x) droop).

**Interpolator 8x 27dB**

27dB DAC interpolation filter. Response flat to 20kHz with a 48kHz sample rate. Stopband starts at 40kHz ??TKTK, so images of frequencies above 8 kHz will not be attenuated strongly. Lowest-quality, but very low MIPS: uses 37 instructions.

**Interpolator 8x 70dB**

Highest-quality interpolation filter: flat to 20kHz with a 44.1kHz sample rate. Uses 80 instructions.

**Interpolator 8x 50dB @48kHz**

50dB interpolation filter. Flat to 20kHz with a 48kHz sample rate; uses 53 instructions.

ADAU145x Output
---------------

Input Pins
~~~~~~~~~~

+--------------+-----------------------------+-------------------------------------------+
| Name         | Format                      | Function Description                      |
|              | [int/dec] - [control/audio] |                                           |
+==============+=============================+===========================================+
| Pin 0: Input | dec- audio                  | The data to be written to output register |
+--------------+-----------------------------+-------------------------------------------+

Grow Algorithm
~~~~~~~~~~~~~~

This output module supports growth upto 16 channels. The output algorithm will be optimized to reduce MIPS when the grown output channels are consecutive and the starting index is a multiple of 4.

.. _relationship-between-hardware-outputs-and-sigmastudio-output-channels-1:

Relationship Between Hardware Outputs and SigmaStudio Output Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The relationship between an output cell in SigmaStudio and the physical output pin on the chip can vary in some cases depending on register settings. Refer to *Serial Audio Outputs from DSP Core* section in the :adi:`datasheet <media/en/technical-documentation/data-sheets/ADAU1452_1451_1450.pdf>` for more infor mation on the same.

.. |outputpic1.png| image:: https://wiki.analog.com/_media/outputpic1.png
.. |outputpic2.png| image:: https://wiki.analog.com/_media/outputpic2.png
.. |outputpic3.png| image:: https://wiki.analog.com/_media/outputpic3.png
