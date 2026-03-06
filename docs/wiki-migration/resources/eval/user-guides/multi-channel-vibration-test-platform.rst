USB3.0 Based Multi-Channel Vibration Test Platform For Electromechanical Sensors
================================================================================

Overview
--------

The USB 3.0 Based Multi-Channel Vibration Test Platform is a system board capable of reading data from analog (IEPE) or digital (SPI, I2C, Extended SPI) accelerometers. The analog (IEPE) inputs also contain current source switches to accommodate sensors that might need external power and individual channel offset voltage setting. Aside from sensor data reading, the board is also capable of providing a variable amplitude and frequency sinusoidal signal to an external vibration shaker as a stimulus.

FEATURES
~~~~~~~~

-  Variable Frequency Setting (0 to 50kHz)
-  Amplitude Scaling (from 0 to ~7Vpp)
-  IEPE input channel offsetting (0 to 5V)
-  Current Source Switching for IEPE sensors requiring power (4mA)
-  4-Channel simultaneous ADC Sampling.
-  Common Mode Voltage:

::

            -Mid-supply (~2.5V), 1.65V, 2.5V, 2.14V.
            -Fixed: 2.5V (default)
   * Time and Frequency Domain Display.
   * Vibration Test
   * Sine Generation (single tone, sweep)

Hardware Specification
~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel_vibration_test_specification_.png
   :align: center
   :width: 600px

Board Overview
~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel_vibration_test_platform_.png
   :align: center
   :width: 600px

-  Multi-board connectors
-  5V external supply
-  Type C port
-  Reset Switch
-  I2C/SPI connector
-  Boot option selection
-  Analog input Channel 3
-  Analog input Channel 2
-  Analog input Channel 1
-  Analog input Channel 0
-  Analog output/signal generator
-  SPI extender

--------------

GUI
---

GUI Overview
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel_vibration_gui_.png
   :align: center
   :width: 600px

GUI DAQ
~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq.png
   :align: center
   :width: 600px

GUI VIBRATION TEST WINDOW
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration.png
   :align: center
   :width: 600px

GUI SINE GENERATION WINDOW
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_sinegeneration.png
   :align: center
   :width: 600px

GUI ADXL WINDOW
~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel_vibration_test_adxl.png
   :align: center
   :width: 600px

--------------

Design Documents
----------------

For User guide, click |UGXXX| for PDF or |Getting Started wiki| for web

For more details on the hardware design, click


|CN-0582|

For more details on the API Guideline, click


|API documents|

--------------

Downloads
---------

.. admonition:: Download
   :class: download

   
   -


   
   |GUI installer.|

.. admonition:: Download
   :class: download

   
   -


   
   |Design files.|

--------------

.. |UGXXX| image:: https://wiki.analog.com/_media/insert link here
.. |Getting Started wiki| image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/getting-started
.. |CN-0582| image:: https://wiki.analog.com/_media/insert link here
.. |API documents| image:: https://wiki.analog.com/_media/insert link here
.. |GUI installer.| image:: https://wiki.analog.com/_media/insert link here
.. |Design files.| image:: https://wiki.analog.com/_media/insert link here
