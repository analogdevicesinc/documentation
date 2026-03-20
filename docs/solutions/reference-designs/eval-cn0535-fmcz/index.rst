.. _cn0535-eval: 

EVAL-CN0535-FMCZ
================

High Performance, Alias Free Measurement Platform for Flexible Data Acquisition System

.. image:: images/EVAL-CN0535-FMCZANGLE-web.png
   :align: center
   :width: 400

.. image:: images/block_diagram.jpg
   :align: center

Overview
--------

The :adi:`EVAL-CN0535-FMCZ` is a data acquisition (DAQ) system that measures real world 
physical phenomenon such as temperature, force, acceleration, or vibration, 
converting measurements into digital values for data processing, storage, 
or transmission to a remote location. A typical DAQ system is comprised of a sensor, 
analog filtering and signal conditioning circuitry, an analog-to-digital converter
(ADC), and digital controller. Components for a DAQ solution are selected on a
per application basis. Some DAQ systems are designed to minimize the overall
system DC error from sensor, with fast settling filters for control-loop or
multiplexed applications. Others are designed to provide superior AC
performance, with low distortion and flat frequency response.

Features
~~~~~~~~

- Alias free Measurement System
- Optimized for AC and DC Performance
- Wide Analog Input (+/-12V)
- FMC Compatible Form Factor

Applications
~~~~~~~~~~~~

- Control loop or multiplexed applications
- AC and DC application

.. admonition:: Getting Started

   The :adi:`CN0535` can be used for a wide range of applications, 
   and the following demos are meant to show examples of the flexibility of the board. 
   To get started with setup, configuration, and example use cases, 
   please proceed to the provided demo page.

   - :ref:`CN0535 and the SDP-K1 <cn0535-sdp-k1>`

Hardware Setup
--------------

Equipment Required
~~~~~~~~~~~~~~~~~~

-  CN0535 Circuit Evaluation Board (EVAL-CN0535-FMCZ)
-  System Demonstration Platform Board (EVAL-SDP-CH1Z)
-  AP2700 Signal Source or Equivalent

Hardware Connection
~~~~~~~~~~~~~~~~~~~

.. image:: images/hardware_setup.jpg
   :align: center

To begin using the evaluation board, take the following steps:

1. Ensure the EVAL-SDP-CH1Z system demonstration platform board is disconnected from the PC. 
   Install the :adi:`AD7768-1 Evaluation Board Software </media/en/evaluation-boards-kits/evaluation-software/ad7768-1-evaluation-software.zip>`. 
   Restart the PC after the software installation is complete.

2. Connect the EVAL-SDP-CH1Z system demonstration platform board to the
   EVAL-CN0535-FMCZ reference design board. The J4 connector of the
   EVAL-SDP-CH1Z system demonstration platform board connects to the receiving
   socket P1 on the EVAL-CN0535-FMCZ.

   |image1|

3. Ensure the evaluation boards are securely connected together by tightening
   the mounting screws.

4. Connect the 12 V DC power supply to the EVAL-SDP-CH1Z system demonstration
   platform board, then connect the provided USB cable from the board to the PC.
   If prompted, allow the operating system to automatically search for and
   install the EVAL-SDP-CH1Z drivers.

5. Launch the AD7768-1 evaluation board software from the Analog Devices folder
   in the Programs menu.

6. Connect the differential input source to the SMB connectors (J3 and J4).
   P7 can also be used for a wired source.

   |image2|

7. In the AD7768-1 evaluation software, click the Sample button.

   Below are the measured values for a 5.9 Vp-p sine input from an AP2700 signal
   source.

   FFT Tab

   |image3|

   Waveform Tab

   |image4|

System Gain Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Select the gain by configuring the switch (S2) on the EVAL-CN0535-FMCZ board.
Table 1 shows the system gain and the corresponding input voltage ranges.

|image5|

ADC Driver (ADA4945-1) Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the ADC driver mode by configuring the switch (S2) on the
EVAL-CN0535-FMCZ board.

|image6|

Software GUI Setup
------------------

GUI Main Window
~~~~~~~~~~~~~~~

.. image:: images/gui_main.jpg
   :align: center
   :width: 600

The main window of the GUI allows the user to configure the following settings
on the ADC

1. Buffer Control: This allows the user to configure the internal ADC input and
   reference buffers

   .. image:: images/buffer.jpg
      :align: center
      :width: 400

2. Digital Filter Control: This allows the user to select the digital filter
   setting of the ADC

   .. image:: images/filter.jpg
      :align: center
      :width: 400

3. MCLK DIV: This allows the user to configure the MCLK divider setting on the
   ADC

   |image7|

4. Power Mode: This sets the power mode setting on the ADC. the user can select
   from Fast, Median and Low power mode setting.

   |image8|

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download
   
   :adi:`EVAL-CN0535-FMCZ Design & Integration Files <cn0535-designsupport>`
   
   -  Schematics
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   
Additional Information and Useful Links
---------------------------------------

-  :adi:`CN0535 Circuit Note Page <CN0535>`
-  :adi:`CN0535 Design Support Package <CN0535-DesignSupport>`
-  :adi:`AD7768-1 Product Page <AD7768-1>`
-  :adi:`LTC6373 Product Page <LTC6373>`
-  :adi:`ADA4945-1 Product Page <ADA4945-1>`
-  :adi:`ADR444 Product Page <ADR444>`
-  :adi:`AD8628 Product Page <AD8628>`
-  :adi:`LT3095 Product Page <LT3095>`
-  :adi:`ADP2300 Product Page <ADP2300>`
-  :adi:`ADP7182 Product Page <ADP7182>`

Software Projects and Platforms
-------------------------------

-  :ref:`CN0535 + SDP-K1 <cn0535-sdp-k1>`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, 
   view the latest videos, and more when you register your hardware. 
   `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-CN0535-FMCZ?&v=RevD>`_ 
   to receive all these great benefits and more!

Warning
-------

.. esd-warning::

Help and support
----------------

Please go to :ez:`Help and Support <help-and-support>` page.

.. toctree::
   :hidden:

   sdp-k1

.. |image1| image:: images/cn0535_sdp_connection.jpg
   :width: 400
.. |image2| image:: images/input_port.jpg
   :width: 400
.. |image3| image:: images/fft.jpg
   :width: 400
.. |image4| image:: images/time_domain.jpg
   :width: 400
.. |image5| image:: images/system_gain_config.jpg
.. |image6| image:: images/adc_driver_config.jpg
.. |image7| image:: images/mclk.jpg
   :width: 400
.. |image8| image:: images/pwrmd.jpg
   :width: 400
