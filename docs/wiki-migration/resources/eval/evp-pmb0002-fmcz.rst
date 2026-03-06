ADSKPMB10-EV-FMCZ User Guide
============================

The :adi:`ADSKPMB10-EV-FMCZ` signal chain kit (Figure 1) is part of the :adi:`Precision Medium Bandwidth <en/applications/technology/precision-technology/precision-medium-bandwidth.html>` evaluation board plus series. It is a two-board solution consist of a Precision Medium Bandwidth Data Acquisition Solution on a PMOD form factor and a Fully Isolated PMOD-to-FMC interposer board.

The Precision Medium Bandwidth Data Acquisition Solution features a discrete programmable gain instrumentation amplifier (PGIA) that was built using a 30V, High Speed, Low Noise, Low Bias Current, JFET Operational Amplifier, the :adi:`ADA4627-1`, a Precision Quad Matched Resistor Network, the :adi:`LT5400`, a Low Capacitance, 4-Channel, ±15 V/+12 V iCMOS™ Multiplexer, the :adi:`ADG1209` and the internal Fully Differential Amplifier (FDA) ADC driver of the :adi:`ADAQ4003`. THE PGIA in thru front-end offers high input impedance that allows direct interface with a variety of sensors. A programmable gain is often needed to adapt the circuit to different input signal amplitudes—unipolar or bipolar and single-ended or differential with varying common-mode voltages. The PGIA works with the :adi:`ADAQ4003`, an 18-Bit, 2 MSPS, µModule Data Acquisition Solution.

The Fully Isolated PMOD-to-FMC interposer board was designed using a Low Noise, 1A, 1MHz Push-Pull DC/DC Driver with Duty Cycle Control, the :adi:`LT3999`, a Robust 3.0kVrms Digital Isolators w/ Fail-Safe for the SPI lines and PGIA gain control pins, the :adi:`ADuM152N` and the :adi:`ADuM120N`, and a Low noise and ultra-low noise LDO regulators the :adi:`ADP7105` and the :adi:`ADP150N` respectively.

| 
| \**FIGURE 1. Signal Chain Kit \*\*
| |evb_placeholder.svg|

EVALUATION SETUP
----------------

Equipment Required
~~~~~~~~~~~~~~~~~~

-  BR-071850: Isolated FMC-to-PMOD Board
-  BR-065908: PGIA+ADAQ4003 Data Acquisition Board
-  System Demonstration Platform Board : SDP-H1 (EVAL-SDP-CH1Z)
-  SYS-2722 Audio Precision or equivalent
-  SMA cables
-  XLR-SMA interposer board
-  Standard USB A to USB mini-B
-  PC or Laptop

Software Required
~~~~~~~~~~~~~~~~~

-  TO FOLLOW

Hardware Connection
~~~~~~~~~~~~~~~~~~~

| **Figure 2. Example Evaluation**
| |image1|

Hardware Description and Performance
------------------------------------

Precision Medium Bandwidth Data Acquisition Solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| This Data Acquisition Solution has 4 gain option as shown in Figure 3. The gain of the signal chain can be control by changing the logic levels of the ADG1209 A0 and A1 pins.
| **Figure 3. System Gain and Input Range**
| |image2|
| Shown in below Figure 4 the Dynamic Range VS Gain Performance of the data acquisition solution.
| **Figure 4. Dynamic Range VS Gain**
| |image3|
| Shown in below Figure 5 the Signal-to-Noise Ratio (SNR VS Frequency VS Gain Performance of the data acquisition solution.
| **Figure 5. SNR VS Frequency VS Gain**
| |image4|
| Shown in below Figure 6 the Total Harmonic Distortion (THD) VS Frequency VS Gain Performance of the data acquisition solution.
| **Figure 6. THD VS Frequency VS Gain**
| |image5|
| **POWER SUPPLIES**
| ==== Fully Isolated PMOD-to-FMC Interposer Board ==== The Fully Isolated PMOD-to-FMC interposer board was designed using a Low Noise, 1A, 1MHz Push-Pull DC/DC Driver with Duty Cycle Control, the :adi:`LT3999`, a Robust 3.0kVrms Digital Isolators w/ Fail-Safe for the SPI lines and PGIA gain control pins, the :adi:`ADuM152N` and the :adi:`ADuM120N`, and a Low noise and ultra low noise LDO regulators the :adi:`ADP7105` and the :adi:`ADP150N` respectively.
| The Board was designed to cater multiple VIO voltage levels. The has 3 options on the FMC VIO side and by default the VIO is connected or set by FMC's VADJ pin. 3.3V and 1.8V is also available incase other VIO voltage level is needed as shown in Figure 7 below. **Figure 7. FMC side VIO Options**
| |image6|
| On the PMOD side, the use has an option to connect the VCC pin of the PMOD Data Acquisition device directly to LT3999's push-pull transformer output or provide a regulated 3.3V output using the ADP7105. By default, the PMOD VCC is power directly from the LT3999's push-pull transformer output as shown is Figure 8 below. **Figure 7. PMOD VCC Options**
| |image7|
| ===== Software GUI Setup =====
| TBD

Navigating the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  In the Evaluation Software Select the Configure Tab.


|image8|

-  Click Normal Mode to enable Turbo Mode.
-  Select Gain=1 in the Gain Control window.
-  Manually type 2000 in Throughput window.
-  Set Samples to 1048576.
-  Click Read Register button and verify settings that the TURBO mode LED lit up green.
-  Select the FFT Tab.
-  Turn on AP signal generator.
-  Click the Single Capture button.
-  Check SNR/THD against values on Table 3.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   
   `adskpmb10-ev-fmcz_design\_&_integration_files <https://wiki.analog.com/adskpmb10-ev-fmcz_design_&_integration_files>`__
   
   -  Schematics
   -  `Precision Medium Bandwidth Data Acquisition Board <https://wiki.analog.com/_media/resources/eval/user-guides/adskpmb02-ev-fmcz/02-065908-01-b.pdf>`__
   -  `Fully Isolated PMOD-to_FMC Board <https://wiki.analog.com/_media/resources/eval/user-guides/adskpmb02-ev-fmcz/02-071850-01-b.pdf>`__
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


Troubleshooting
---------------

| 
| TBD

Additional Information and Useful Links
---------------------------------------

-  :adi:`Precision Medium Bandwidth Platforms <en/applications/technology/precision-technology/precision-medium-bandwidth.html>`
-  :adi:`ADAQ4003 Product Page <ADAQ4003>`
-  :adi:`ADA4627-1 Product Page <ADA4627-1>`
-  :adi:`ADG1209Product Page <ADG1209>`
-  :adi:`LT5400 Product Page <LT5400>`
-  :adi:`LT3999Product Page <LT3999>`
-  :adi:`ADuM152NProduct Page <ADuM152N>`
-  :adi:`ADuM120NProduct Page <ADuM120N>`
-  :adi:`ADP7105Product Page <ADP7105>`
-  :adi:`ADP150 Product Page <ADP150>`

Software Projects and Platforms
-------------------------------

-  ADSKPMB10-EV-FMCZ Evaluation Software
-  ADSKPMB10-EV-FMCZ Evaluation Software using Zedboard

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-CN0535-FMCZ?&v=RevD>`__ to receive all these great benefits and more!


*End of Document*

.. |evb_placeholder.svg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adskpmb02-ev-fmcz/evb_placeholder.svg
   :width: 600px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adskpmb02-ev-fmcz/evaluationsetup.svg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/user-guides/adskpmb02-ev-fmcz/gain_inputrange.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adskpmb02-ev-fmcz/dr.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adskpmb02-ev-fmcz/snr_vs_frequency_vs_gain.svg
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adskpmb02-ev-fmcz/thd_vs_frequency_vs_gain.svg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adskpmb02-ev-fmcz/fmc_vio.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adskpmb02-ev-fmcz/pmod_vcc.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/01_landing_page.png
