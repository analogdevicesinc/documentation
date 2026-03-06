AD-FMCMOTCON1-EBZ IIO User Guide
================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



IIO OSC
-------

ADI IIO oscilloscope is used for monitoring and controlling the AD-FMCMOTCON1-EBZ board, when using Linux operating system.

There are two main tabs that are to be used: **Capture** and **Motor Control**.

Capture
~~~~~~~

The Capture tab is used for monitoring the system.

Current monitoring
^^^^^^^^^^^^^^^^^^

On the AD-FMCMOTCON1-EBZ system, there are two sets of ADCs for monitoring the current to the motor:

The first AD7401A based measuring system is part of the controller board. The signal is pre amplified on the Low Voltage Drive board. The amplification factor is controlled by the GPO0 and GPO1 pins

-  in_voltage0 corresponds to IA
-  in_voltage1 corresponds to IB
-  in_voltage2 corresponds to IT
-  in_voltage3 corresponds to VBUS

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/mc_adc1_sc.png
   :alt: Current measurement using the control board ADCs
   :width: 600px

The second AD7401A measuring system is part of the Low Voltage Drive board. The signal is not preamplified in this case

-  in_voltage0 corresponds to IA
-  in_voltage1 corresponds to IB
-  in_voltage2 corresponds to IT
-  in_voltage3 is always 0

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/mc_adc2_sc.png
   :alt: Current measurement using the drivel board ADCs
   :width: 600px

Speed monitoring
^^^^^^^^^^^^^^^^

| This IP monitors the speed, and display the number of counts ( in 10ns units) between two motor commutations. In order to display the speed in RPM, the data should be processed by checking the 1/x option and multiply by 25.000.000
| |Speed measurement|

FOC Controller monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^

This IP allows monitoring of the following signals from the :doc:`MathWorks FOC IP </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/matlab_models>`:

-  voltage_0 - Phase A voltage
-  voltage_1 - Phase B voltage
-  voltage_2 - Phase A current
-  voltage_3 - Phase B current
-  voltage_4 - Rotor mechanical position
-  voltage_5 - Rotor velocity
-  voltage_6 - d current
-  voltage_7 - q current

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/mc_full_sc.png
   :alt: FOC monitoring
   :width: 600px

Control
~~~~~~~

Manual Control
^^^^^^^^^^^^^^

| This controller allows the control of the motor in manual mode by directly specifying the fill factor of the PWM signal applied used to control the 3 phase inverter. The motor is driven using a 6 step comutation algorithm.
| |Manual Control|

+-----------------+--------------------------------------------------------------------------------+
| Control         | Description                                                                    |
+=================+================================================================================+
| Run             | Starts the motor                                                               |
+-----------------+--------------------------------------------------------------------------------+
| Delta           | Selects between driving the motor using a Star-like sequence or Delta sequence |
+-----------------+--------------------------------------------------------------------------------+
| Direction       | Selects between clockwise and counterclockwise rotation directions             |
+-----------------+--------------------------------------------------------------------------------+
| Controller Type | Selects between the Manual PWM drive or the MathWorks FOC Controller           |
+-----------------+--------------------------------------------------------------------------------+
| PWM             | In Manual mode, the PWM can be set between 50% - 100%                          |
+-----------------+--------------------------------------------------------------------------------+

Matlab Controller
^^^^^^^^^^^^^^^^^

This selects the :doc:`MathWorks FOC IP </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/matlab_models>`. From the IIO Scope the only available is to Start/Stop the motor, while the operation of the IP core is controlled through the *foc_script.sh* script located under */usr/local/bin*. The script executes the following steps:

-  Set the FOC controller in open loop mode and wait for the user to start the motor by clicking the Run checkbox in IIO scope
-  Calibrate the encoder readings to remove the offset between the motor's actual electrical position and the position read from the encoder
-  Set the motor's reference speed
-  Start the FOC controller in closed loop mode

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/mc_foc_ctrl.png
   :alt: Matlab Controller
   :width: 500px

.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#none#../
   :alt: Overview#none

.. |Speed measurement| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/mc_speed_sc.png
   :width: 600px
.. |Manual Control| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/mc_manual_ctrl.png
   :width: 400px
