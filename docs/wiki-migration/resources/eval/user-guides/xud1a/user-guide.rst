ADXUD1AEBZ (XUD1A) UP/DOWN CONVERTER BOARD
==========================================

General Description
===================

The ADXUD1AEBZ evaluation board is a quad channel Up and Down converter designed for X Band general purpose use. The complete Analog Devices solution chain consist of amplifiers, LNAs, switches, mixers, integrated PLL/VCO, and power management circuitry all powered by a single +12V power supply. Frequency conversion can be accomplished using either the integrated PLL/VCO or an external LO. This evaluation board is intended to be used with an external Low Noise Amplifier and Power Amplifier to set the desired noise figure and output power of the user's signal chain.

The ADXUD1AEBZ consist of 4 channels capable of up and down conversion over a RF frequency band from 8 GHz to 12 GHz and IF frequency band from 4.2 GHz to 6.3 GHz. The RF input/outputs on the evaluation board are brought out to SMA coaxial connectors whereas the IF input/outputs are brought out to SMPM coaxial connectors specifically designated for transmit or receive. Digital control via GPIO and SPI lines are established through a PMOD connector with a compatible interposer board to allow :adi:`System Demonstration Platform (SDP-S) <SDP-S>` and FMC Mezzanine connector options. Control signals for the board are expected to be 1.8V logic with on-board level translators converting to the on-board logic level of 3.3V.


|image1|

.. container:: centeralign

   \ **Figure 1: ADXUD1AEBZ Board: Front**\


   |image2|

.. container:: centeralign

   \ **Figure 2: ADXUD1AEBZ Board: Back**\


--------------

REQUIREMENTS
============

Documents
---------

-  :adi:`HMC903LP3E Datasheet <media/en/technical-documentation/data-sheets/HMC903.pdf>`
-  :adi:`ADL8111 Datasheet <media/en/technical-documentation/data-sheets/ADL8111.pdf>`
-  :adi:`HMC8411LP2FE Datasheet <media/en/technical-documentation/data-sheets/HMC8411LP2FE.pdf>`
-  :adi:`HMC963LC4 Datasheet <media/en/technical-documentation/data-sheets/HMC963.pdf>`
-  :adi:`HMC383LC4 Datasheet <media/en/technical-documentation/data-sheets/HMC383.pdf>`
-  :adi:`HMC773ALC3B Datasheet <media/en/technical-documentation/data-sheets/HMC773ALC3B.pdf>`
-  :adi:`ADF4371 Datasheet <media/en/technical-documentation/data-sheets/ADF4371.pdf>`
-  :adi:`ADRF5020 Datasheet <media/en/technical-documentation/data-sheets/ADRF5020.pdf>`
-  :adi:`HMC652LP2E Datasheet <media/en/technical-documentation/data-sheets/hmc652lp2-hmc655lp2.pdf>`

-  ADXUD1AEBZ Rev. D Design:

   -  `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/02-065073-01-d.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/xud1a_bom.zip>`__

-  Interposer Board Rev. A Design:

   -  `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/02-067148-01-a.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/interposerbom.zip>`__

-  Interposer Board Rev. B Design:

   -  `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/02-067148-01-b.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/interposerbom-b.zip>`__

Hardware
--------

-  ADXUD1AEBZ
-  Interposer Board
-  SMA-SMA cabling to interface with the RF ports
-  SMPM-SMA cabling to interface with the IF ports
-  Digital controller and any associated hardware (:adi:`SDP-S` or PMOD)

|

.. warning::

   The SDP-S is the only SDP controller which will work with XUD1A.

   | All other SDP controllers (SDP-B, SDP-H1, SDP-K1) are **NOT** compatible.


Suggested Test Equipment
------------------------

-  20GHz RF Signal Generator (2x)
-  20GHz Spectrum Analyzer
-  20GHz Vector Network Analyzer (optional)
-  Oscilloscope (optional)
-  RF Power Meter (optional)

Software/Digital Control
------------------------

PMOD Control
~~~~~~~~~~~~

-  Two 14-pin PMOD cables (`Example <https://www.digikey.com/en/products/detail/assmann-wsw-components/H3AKH-1406G/998997>`__)
-  Example PMOD digital controllers:

   -  `Raspberry Pi <https://www.raspberrypi.org/>`__
   -  FPGA demonstration board
   -  `Arduino <https://www.arduino.cc/>`__
   -  `FTDI <https://www.ftdichip.com/>`__

SDP Control
~~~~~~~~~~~

-  `SDP Drivers <http://swdownloads.analog.com/ACE/SDP/SDPDrivers.exe>`__
-  `Basic SDP-S Test Program Rev A <https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/sdp_xud1a.zip>`__
-  `Basic SDP-S Test Program Rev B <https://wiki.analog.com/_media/{{ /resources/eval/user-guides/xud1a/sdps_xud1a_r1.zip>`__

.. note::

   Windows 10 might try to block the example Test Program, you'll have to explicitly allow it in your security settings


-  :adi:`SDP-S controller board <sdp-s>`

Software
~~~~~~~~

-  :git-pyadi-iio>`__ interface for LibIIO

   -  `ADF4371 wrapper <https::`PyADI-IIO </github.com/pyadi-iio?master/adi/adf4371.py>`
   -  `ADF4371 Documentation <https://analogdevicesinc.github.io/pyadi-iio/devices/adi.adf4371.html>`__

::

    *[[https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/xud_ctrl.zip|Standalone Python Application using SDP-S Controller]]

--------------

Board Design
============

The ADXUD1AEBZ evaluation board has 4 SMA RFIO connectors for the RF Input/Output and 8 SMPM RFIO connectors for the IF Input/Output. The 8 SMPM connectors have 4 RX IF channels and 4 TX IF channels. There is 1 SMA connector available to supply an external LO signal. The board is configured for an external LO by default. A capacitor can be rotated to disable the external LO port and access the internal PLL/VCO (ADF4371). The PLL/VCO can be programmed via SPI to allow an on-board LO signal.

One 12V DC barrel jack is provided to apply the required 12V power supply with on-board power management circuitry to converter to the necessary power rails.

One 14 PIN PMOD connector is provided to apply GPIO/SPI digital control lines.

Power Supply
------------

The ADXUD1AEBZ board must be powered from the included power supply with a voltage level of 12V. There is an on-board power management tree which generates the required voltage rails for all of the associated parts.

RF/IF Signal Chain
------------------

The ADXUD1AEBZ has 4 RF input/output SMA connectors and 4 TX IF inputs and 4 RX IF outputs via SMPM connectors. Each RF channel is bandpass filtered and tied to two :adi:`ADRF5020` switches with independent :adi:`HMC903 <hmc903lp3e>` amplifiers for TX and RX. Up/down conversion is accomplished using the :adi:`HMC773A <hmc773alc3b>` with the option to drive the LO either externally via the J4 SMA connector or internally with the :adi:`adf4371`. The RX IF channel is amplified by the :adi:`ADL8111` and :adi:`hmc8411` whereas the TX IF channel is internally bypassed by the :adi:`ADL8111`.


|image3|

.. container:: centeralign

   \ **Figure 3: ADXUD1AEBZ Block Diagram**\


LO Signal Chain
---------------

The LO signal is amplified by :adi:`HMC963 <hmc963lc4>` and :adi:`HMC383 <hmc383lc4>` amplifiers and divided across all channels to provide a common LO signal. The user can decide between an internal PLL or external LO. The internal PLL is the :adi:`adf4371` with an option for an external reference via J3 connector or an on-board VCXO reference. An external LO source can be injected via the J4 SMA connector. When using an external LO, the recommended input power to J4 is +5 dBm.

By default, the board populates C165 for an external LO source with C61 not installed. The user can remove C165 and re-install on the C61 pad to enabled use of the ADF4371. When using the onboard ADF4371, the default reference is the onboard VCXO with C372 installed and C373 not installed. The user can remove C372 and re-install on the C373 pad to enabled use of the external reference port J3.

.. note::

   An external LO source is recommended for performance based measurements. The on-board ADF4371 is provided for convenience to allow stand-alone operation of the hardware for a wide range of operational frequencies. A bandpass filter should be inserted in the ADF4371 PLL output path depending on the final frequency plan to reject the harmonic content generated by the ADF4371 internal multipliers.


Digital Control
---------------

PMOD Pinout
^^^^^^^^^^^

The digital input signals are intended to be 1.8V logic while the :adi:`ADRF5020`, :adi:`ADL8111`, and :adi:`ADF4371` digital control inputs require logic levels of 3.3V. Level translators and digital logic circuitry have been included between the PMOD connector and aforementioned components.


|image4|

.. container:: centeralign

   \ **Figure 4: ADXUD1AEBZ PMOD Pinout**\


Interposer Board
^^^^^^^^^^^^^^^^

The Interposer board allows the option to control the ADXUD1AEBZ via :adi:`System Demonstration Platform (SDP-S) <SDP-S>` and FPGA via FMC Mezzanine connector. Note the Interposer board PMOD connector is pin compatible with the ADXUD1AEBZ PMOD connector and can be connected directly to XUD1A.


|image5|

.. container:: centeralign

   \ **Figure 5: ADXUD1AEBZ Interposer Pinout with SDP-S Connector**\


Control Logic
^^^^^^^^^^^^^

The PMOD inputs are fed to a buffer and logic network for simplified board control and quick switching time.


|image6|

.. container:: centeralign

   \ **Figure 6: ADXUD1AEBZ Control Block Diagram**\


======= ============ ===== ===== ===== ===== ============
Channel Mode         TXRX0 TXRX1 TXRX2 TXRX3 Rx Gain Mode
======= ============ ===== ===== ===== ===== ============
A       TX           1     -     -     -     0
:::     RX Low Gain  0     -     -     -     0
:::     RX High Gain 0     -     -     -     1
B       TX           -     1     -     -     0
:::     RX Low Gain  -     0     -     -     0
:::     RX High Gain -     0     -     -     1
C       TX           -     -     1     -     0
:::     RX Low Gain  -     -     0     -     0
:::     RX High Gain -     -     0     -     1
D       TX           -     -     -     1     0
:::     RX Low Gain  -     -     -     0     0
:::     RX High Gain -     -     -     0     1
======= ============ ===== ===== ===== ===== ============

.. container:: centeralign

   \ **Table 1: ADXUD1AEBZ RF Control Logic**\


============== ==============
ADF4371 Output PLL_OUTPUT_SEL
============== ==============
8 - 16 GHz     1
16 - 32 GHz    0
============== ==============

.. container:: centeralign

   \ **Table 2: ADXUD1AEBZ ADF4371 Control Logic**\


Evaluation
==========

Software Control
----------------

There are two methods to control the XUD1A board using the interposer board. Either over the FMC connector using the ZCU102 FPGA or over the SDP connector using a SDP-S controller. Limited functionality is available using the SDP-s controller, but a user has the basic ability to program the state of XUD1A (TX, RX Low Gain, RX High Gain) using the SPD-S controller.

Standalone Python Application
-----------------------------

Download the application from the `Software <https://wiki.analog.com/>`__ section. Extract the file contents to your desired PC drive. It is recommended to save the folder to your root drive for simplicity. Using your preferred command terminal, change the directory to the desired state folder (e.g. >> cd C:/XUD1A_ctrl/TX). Execute the application through the terminal window.

Support
-------

For additional questions or support, please visit the Engineering Zone forum at :ez:`ADEF`.

:doc:`ADXUD1AEBZ Homepage </wiki-migration/resources/eval/user-guides/xud1a>`

:doc:`X Band Development Platform </wiki-migration/resources/eval/user-guides/x-band-platform>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/eval-adxud1aebz_top-web.gif
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/eval-adxud1aebz_bottom.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/xud1a_revd_blockdiagram.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/xud1a_pmod.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/xud1a_sdps.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/xud1a/xud1a_controlblockdiagram.png
   :width: 600px
