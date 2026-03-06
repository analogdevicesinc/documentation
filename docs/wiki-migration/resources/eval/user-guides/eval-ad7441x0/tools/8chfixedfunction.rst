Multiplying IO channels in Building Controls
============================================

It's a cold winter's morning; as you step out of your car and walk towards the entry hall doors, it is clear that you are the first on-site today. As a result of advanced building automation, lights are turned on for you on arrival. The input terminal reads your credentials and allows you to enter the office. Appropriate air exchange for maintaining a healthy office environment, including the temperature and humidity, set precisely at your comfort level. All the other desks are empty and half dark when you look around, yet the workplace area has maintained perfect environmental conditions. All these parameters are regulated to meet one person's needs, the one who is currently occupying the building.

Welcome to the perfect working environment, which is not only cost-effective but also gentler towards our planet. Welcome to the office of the future, a future that is happening right now. This and more are possible using Analog Devices Software Configurable I/O parts. Software Configurable I/O has multiple end-market applications; however, the focus of this paper is on benefits that can be realised within smart building automation systems.


|image1|

.. container:: centeralign

   Figure 1: Smart and energy effective building


Software Configurable I/O for building automation
-------------------------------------------------

Analog Devices offers quad-channel software configurable I/O AD74412R suitable for building automation market. Part integrate a range of programmable functionality on every channel, including Analog Outputs, Analog Inputs, Digital Inputs and RTD and Thermocouple measurement capability. Each function is available on a single pair of screw terminals per channel, with a fixed set of external components. This flexibility allows users to design configurable modules, integrating many functions with a single hardware design.

Not all users need full configurability on a single channel. Some users require fixed-function modules supporting either Analog Output or Analog Input. With circuit modification AD74412R can be used to generate 8 channels of fixed functionality, having dramatically reduced the overall cost per channel while still offering a broad range of functionality. The AD74412R can monitor four inputs such as temperature sensor, lux sensor, switches or people count detector and also control four outputs as window blinders, airconditioning, fan or light which are commonly used elements in building automation systems.


|image2|

.. container:: centeralign

   Figure 7: AD74412R 8 channels application


The AD74412R come with in-built fault detection and diagnostics capabilities, which provide additional value to the design safety features. Some examples of fault detect features are open & short circuit detect, ADC overrange detect and SPI CRC detect, amongst others. The diagnostics features allow the user to monitor multiple internal nodes, die temperature, and some external voltages using the onboard ADC. The AD74412R is designed to be robust in harsh and noisy environments with robustness features including:

-  robust to 50 V on pin voltage,
-  Surge tested to ±1 kV (kilovolt), per the IEC61000-4-5 standard, on the input/output terminals with unshielded cables,
-  thermal on-chip protection,
-  CRC protection on SPI transactions to ensure no erroneous data transfers.

The inbuilt diagnostics and robustness features simplify the end hardware design and significantly reduce the number of external components needed resulting in space-saving and lower-cost design.

Tailor the circuit to fit your individual needs
-----------------------------------------------

This article aims to break the functionality of each AD74412R channel into 2 fixed function channels, one Analog Output and one Analog Input. This action will result in obtaining 8 channels. The proposed circuit is shown in Figure 3.


|image3|

.. container:: centeralign

   Figure 3: Proposed circuitry for using AD74412R as 8 channel part


The Analog Output channel
~~~~~~~~~~~~~~~~~~~~~~~~~

|image4|

.. container:: centeralign

   Figure 4: Analog Output Channel


Each Analog Output channel has a dedicated 13-bit DAC to support Voltage or Current output with all corresponding fault detection (Open and Short-circuit fault detection). Figure 4 highlight the Analog Output circuit connection.

The output channel performance is as specified in the AD74412R datasheet. Chip level diagnostics and the digital input comparator are available as described in the datasheet. Note that the Digital Input Comparator can only be accessed via the SENSEL pin in this configuration.

The Analog Input channel
~~~~~~~~~~~~~~~~~~~~~~~~

|image5|

.. container:: centeralign

   Figure 5: Analog Input Channel


The Analog Input channel uses the on-chip ADC. One 16-bit ADC is available to be shared across all channels. Configure the SENSEHF & SENSELF pins to monitor a voltage on the screw terminals. This offers single-ended (IP_x positive terminal & IN_x negative terminal) or differential measurements (IP_x positive terminal & DV_x negative terminal) with the measurement range from 0 to 10 V.

The ADC is available with the 50/60Hz rejection filter (20 SPS) or without 50/60Hz rejection (4.8 kSPS). Once the ADC is enabled to measure 4 channels, its sampling speed is divided by 4, which results in ≈ 1.2 kSPS for the channel, with a fast conversion rate enabled.

The input channel performance is as specified in the AD74412R datasheet. Chip level diagnostics are available as described in the datasheet. Each enabled diagnostic counts as a separate measurement channel and ADC conversion time should be calculated according to the datasheet instructions.

The Digital Input comparator is available on the SENSELF pin if required.

To support the measurement of sourcing or sinking current, the circuit would need to be adjusted to provide a current path. A 100 Ω resistor and a current source/sink path with a 30 mA limit would be sufficient.

Practical example with configuration details
--------------------------------------------

Figure 6 shows the hardware configuration that allows a single channel of the AD74412R to be used to provide a 4 - 20 mA Current Output on one pair of terminals named OP_x and ON_x. The second pair of terminals named IP_x and IN_x provides 0 - 10 V voltage input.


|image6|

.. container:: centeralign

   Figure 6: Hardware configuration for Analog Input and Analog Output channels


Table 1 shows the sequence of register writes required to configure the device for Current Output and Voltage Input, as described.

Table 1: Example of the channel configuration sequence

+------+----------------+--------------+-------+------------------------------------------------------------------------------------------------------+--------------------------+
| Step | Register       | Bit/Bitfield | Value | Value Description                                                                                    | Note                     |
+======+================+==============+=======+======================================================================================================+==========================+
| 1.   | CH_FUNC_SETUPx | CH_FUNC      | 0010  | Current output                                                                                       | Configure main function  |
+------+----------------+--------------+-------+------------------------------------------------------------------------------------------------------+--------------------------+
| 2.   | DAC_CODEx      | DAC_CODE     | x     | Set to meet application needs                                                                        | Set output current       |
+------+----------------+--------------+-------+------------------------------------------------------------------------------------------------------+--------------------------+
| 3.   | ADC_CONFIGx    | RANGE        | 000   | 0 V to 10 V range. Typically used to measure the voltage across the I/OP_x to I/ON_x screw terminals | Configure ADC range      |
+------+----------------+--------------+-------+------------------------------------------------------------------------------------------------------+--------------------------+
|      | ADC_CONFIGx    | ADC_MUX      | 00    | Voltage between the I/OP_x screw terminals and the AGND_SENSE pin                                    | Choosing ADC inputs      |
+------+----------------+--------------+-------+------------------------------------------------------------------------------------------------------+--------------------------+
|      | ADC_CONFIGx    | EN_50_60_HZ  | 00    | Enables the 50 Hz or 60 Hz rejection, resulting in a sampling rate of 20 SPS.                        | Set sampling rate of ADC |
+------+----------------+--------------+-------+------------------------------------------------------------------------------------------------------+--------------------------+

In this configuration 4 – 20 mA current loop is provided by a 13-bit precision DAC, this should ideally result in a 3 µA resolution. Open circuit faults can be detected and will generate an interrupt on the ALERT pin. Voltage Input is enabled and measured by the internal 16-bit ADC, with 50 Hz and 60 Hz rejection filter enabled, resulting in a 20 SPS conversion rate. This conversion rate is suitable for precision measurements. If 50/60 Hz rejection is not required, the filter can be disabled to achieve faster conversion times.

|

.. note::

   \ **Configuration:**

   | It is recommended to follow the sequence as described in Table 1. Configure the CH_FUNC register first, to avoid overwriting the ADC settings.


One Digital Input comparator is available for each channel, it can be used either at Analog Output or Analog Input channel, but not both at once. Digital Input comparator is available through SENSEL or SENSELF pin.

Proven concept
--------------

Software Configurable I/O have been mostly focused on full software configurability, however, this article has shown, that there is the possibility of using it tailored to your needs. For cost-sensitive applications where Analog I/O is required, the AD74412R can be used creatively away from its standard recommended configuration. Use the AD74412R to provide 8 cost competitive, robust channels (4 input and 4 output), with a wide range of integrated fault detection capabilities. With Software Configurable I/O countless configurations and possibilities lay ahead.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7441x0/tools/smartbuilding.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7441x0/tools/ad74412_splitchan8-copy_of_8_chan_connection-complete.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7441x0/tools/ad74412_splitchan8-general_one.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7441x0/tools/ad74412_splitchan8-ao_part.png
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7441x0/tools/ad74412_splitchan8-ai_part.png
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7441x0/tools/ad74412_splitchan8-ao_current_-_ai_voltage.png
   :width: 800px
