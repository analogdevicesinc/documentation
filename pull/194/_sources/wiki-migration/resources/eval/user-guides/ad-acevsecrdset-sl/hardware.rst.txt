AD-ACEVSECRDSET-SL Hardware User Guide
======================================

Introduction
------------

The :adi:`AD-ACEVSECRDSET-SL` design incorporates the :adi:`ADE9113` 3-Channel, Isolated, Sigma Delta (Σ-Δ) ADC and the :adi:`MAX32655` low-power, Arm Cortex-M4 processor with FPU-Based microcontroller and Bluetooth 5.2 allowing the implementation of type 2 EVSE charging cables. The :adi:`ADE9113` has two voltage measurement channels and a current measurement one used to implement the safety functions in the firmware. The integrated isolation makes the connection with the :adi:`MAX32655` straightforward. The communication between the two components is implemented over SPI.

The control pilot (CP) signal needed for implementing the communication between the EVSE and EV is generated using the :adi:`MAX32655` and the :adi:`ADA4523-1` Low Noise, Zero Drift Op Amp.

The system is powered from the single phase 230V AC input. An isolated AC-DC SMPS is used to deliver 12V to the board and the :adi:`MAX20457` high-efficiency dual synchronous buck converters for automotive applications are used to step down the voltage to 5V and 3.3V providing power to the isolated side of the board. The :adi:`LT8330` used in the inverting configuration generates the 12V negative voltage needed for the low side of the CP signal.

The :adi:`MAX32655` exposes all the necessary debug and programming features enabling a complete software development experience. The Bluetooth 5.2 LE radio with the available fully open-source Bluetooth 5.2 stack makes it easy to develop an interaction method between the user and the board. Four user buttons and 4 LEDs are also provided to complete the user interface. Serial communication (RS-232) is used for sending debug messages during testing or development.

The :adi:`ADT75` 12-Bit digital temperature sensor monitors the temperature of the device and sends it to the MCU unit for implementing overtemperature protection.

The main components used in the design are highlighted in the following figures.

Revision A
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/02_ad_bct2ade9113_sl_top_components.png
   :align: center
   :width: 800px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/03_ad_acevsecrdset_sl_bottom_components_v3.png
   :align: center
   :width: 800px

Revision D
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/ad-acevsecrdset-sl_board_with_components-top_rev_d.png
   :align: center
   :width: 800px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/ad-acevsecrdset-sl_board_with_components-bottom_rev_d.png
   :align: center
   :width: 800px

Setting up the board
--------------------

In order to power up the board the "*grid connector*" must be connected to a single phase 230V AC line. A 3-wire cable rated at 16A is the minimum acceptable. The output can be connected to an EVSE test adapter, a type 2 cable (and EV) or it can be left disconnected for the first-time power up or for programming. The prog/debug connector which is a 10-pin ARM Cortex debug connector must be connected to a programmer e.g. :adi:`MAX32625PICO` MAXDAP DAPLink programmer based on the :adi:`MAX32625` through a cable in case a firmware update is available. The MAXDAP can be also used to read the debug messages during the development stage. The messages are sent via RS-232. The UART device ID is 0 with the following settings (57600 8N1). In the following figure the messages received on a computer connected to the board through the MAXDAP with the debug print option being active are presented.

.. _revision-a-1:

Revision A
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/debug_message_self_test.png
   :align: center
   :width: 400px

.. _revision-d-1:

Revision D
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/rev_d_debug_1.png
   :align: center
   :width: 400px

After the self-test finishes a charging session can be initiated by the EV or the device connected to the "*EV connector*". The following image presents the debug messages received during a charging session.

.. _revision-a-2:

Revision A
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/debug_message_charging_session.png
   :align: center
   :width: 400px

.. _revision-d-2:

Revision D
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/rev_d_debug2.png
   :align: center
   :width: 400px

User interface
~~~~~~~~~~~~~~

Three programable push buttons, one MCU reset button and four LEDs are available for user interface.


|image1|

The buttons and LEDs are connected to the MCU as indicated in the above image. The LEDs are used to display the current state of the EVSE or the type of error in case that one has been detected. |image2| \*during state C if the LED blinks fast then the current is set at 16A, if it blinks slow it is limited to 10A

Test points
~~~~~~~~~~~

For evaluation and debugging purpose, test points are provided at every important point on the PCB. The names of the test points are printed on the silkscreen.

Scope images
~~~~~~~~~~~~

CP signal values corelated to the EVSE states
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CP signal is presented for each state (A, B, C, D and diode error) in the following images, measured at two different points on the board. The first image for each case represents the value measured at the CP test point highlighted in the following image and the second one at the CP_READ test point corresponding to the MCU ADC input.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/19_ad_bct2ade9113_sl_cp_test_points.png
   :align: center
   :width: 400px

The values of the CP signal must be in the limits indicated in the next table for each state.

+---------+----------------+-------------------+------------------+---------------------------+-------------------------------------------------+
| State   | CP signal type | CP high value [V] | CP low Value [V] | Equivalent resistance [Ω] | EV status                                       |
+---------+----------------+-------------------+------------------+---------------------------+-------------------------------------------------+
| State A | PWM/DC         | 12 [11;13]        | -                | -                         | Not connected                                   |
+---------+----------------+-------------------+------------------+---------------------------+-------------------------------------------------+
| State B | PWM/DC         | 9 [8;10]          | -12              | 2740                      | Connected                                       |
+---------+----------------+-------------------+------------------+---------------------------+-------------------------------------------------+
| State C | PWM/DC         | 6 [5;7]           | -12              | 882                       | Charging, does not require charging ventilation |
+---------+----------------+-------------------+------------------+---------------------------+-------------------------------------------------+
| State D | PWM/DC         | 3 [2;4]           | -12              | 246                       | Charging, ventilation required                  |
+---------+----------------+-------------------+------------------+---------------------------+-------------------------------------------------+
| State E | DC             | 0 [-1;1]          | 0                | -                         | Fault in control circuit                        |
+---------+----------------+-------------------+------------------+---------------------------+-------------------------------------------------+
| State F | DC             | -                 | -12              | -                         | Unknown fault                                   |
+---------+----------------+-------------------+------------------+---------------------------+-------------------------------------------------+

State A (EVSE IDLE) CP tespoint: |image3| CP_READ tespoint


|image4|

State B (EV connected) CP testpoint |image5| CP_READ testpoint


|image6|

State C (charging requested) CP testpoint |image7| CP_READ testpoint


|image8|

State D (charging with ventilation requested) CP testpoint |image9| CP_READ testpoint


|image10|

State diode error (EV diode missing) CP testpoint |image11| CP_READ testpoint


|image12|

Testing the EVSE
^^^^^^^^^^^^^^^^

Two measurements are presented following a complete run of the state machine from power-up to charging and EV disconnected. The tests are done using the following test bench setup.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/20_ad_bct2ade9113_sl_test_bench.jpg
   :align: center
   :width: 800px

Normal working conditions with highlight on the EVSE-EV states. |image13| RCD AC error detected during a charging session in state C (charging without ventilation).


|image14|

Setup of the EVSE with the type 2 cable connected on the EV side.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/21_ad_bct2ade9113_sl_test_bench_type2_cable.jpg
   :align: center
   :width: 800px

--------------

.. tip::

   **If you want to go back to the SOFTWARE SETUP, click here:** :doc:`AD-ACEVSECRDSET-SL Software User Guide </wiki-migration/resources/eval/user-guides/ad-acevsecrdset-sl/software>`


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/user_interface.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/leds_revd.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/09_ad_bct2ade9113_sl_cp_statea.jpg
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/10_ad_bct2ade9113_sl_cp_statea_adcin.jpg
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/12_ad_bct2ade9113_sl_cp_stateb.jpg
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/11_ad_bct2ade9113_sl_cp_stateb_adcin.jpg
   :width: 800px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/14_ad_bct2ade9113_sl_cp_statec.jpg
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/13_ad_bct2ade9113_sl_cp_statec_adcin.jpg
   :width: 800px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/16_ad_bct2ade9113_sl_cp_stated.jpg
   :width: 800px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/15_ad_bct2ade9113_sl_cp_stated_adcin.jpg
   :width: 800px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/18_ad_bct2ade9113_sl_cp_state_b_diode_error.jpg
   :width: 800px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/17_ad_bct2ade9113_sl_cp_state_b_diode_error_adcin.jpg
   :width: 800px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/06_ad_bct2ade9113_charging_scenario.jpg
   :width: 800px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/07_ad_bct2ade9113_rcd_error_scenario.jpg
   :width: 800px
