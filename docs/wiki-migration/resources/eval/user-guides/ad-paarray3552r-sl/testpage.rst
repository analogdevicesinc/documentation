Power Amplifier (PA) Array Controller User Guide
================================================

**I want to...**

.. container:: round box

   
   Learn More About the Device
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


.. container:: round box

   
   Setup the Hardware for Testing
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


.. container:: round box

   
   Get Further Help
   ^^^^^^^^^^^^^^^^
   


About the Device
----------------

Overview
~~~~~~~~

|

.. container:: indent

   The optimal performance of RF power amplifiers depends on precise biasing control, which enhances factors like linearity and efficiency. GaN HEMTs have proven superior in high-frequency and high-power RF applications but require careful bias voltage timing to prevent device damage. To ensure safe and reliable operation, proper biasing sequence and protection are essential. This reference design utilizes ADI’s portfolio for control, protection, and appropriate bias sequencing of RF power amplifier arrays designed for massive MIMO and macro base-station applications. The system manages the power-up and power-down progression of power amplifier arrays while continuously monitoring the system’s crucial parameters.

   |

   .. container:: box

   |image1|

         | <fc>Figure 1. ADI PA Array System Architecture.</fc>
      |

   
   The conventional approach of powering up and powering down of GaN amplifiers involves using multiple bench power supplies and manually turning them on and off based on the specific amplifier requirements. However, this method carries a high risk of damaging the amplifier due to potential human errors and is neither time-efficient nor cost-effective. The PA Array Board reference design helps address these challenges, this innovative reference design eliminates human errors and fully automates the power-up and power-down procedure, ensuring the safe and reliable operation of GaN amplifiers.
   
   .. container:: box

   
   |image2|

         | <fc>Figure 2. ADI PA Array Controller Board. Left: Primary side; Right: Secondary side.</fc>
      |

   


Features
~~~~~~~~

-  Fault Events Protection: Undervoltage, overvoltage, overcurrent, and overtemperature
-  Fast GaN gate voltages settling time: <5 µS typical
-  Fast fault event to gate pinch-off time: <10 µS typical
-  Wide gate bias voltage range: -10 V to +10V
-  Precise power-up and down sequence of up to two GaN HEMTs-based amplifiers

Applications
~~~~~~~~~~~~

-  5G massive MIMOs
-  Macro base-stations

Pins, Connections, and Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|

.. container:: indent

   
   .. container:: box


   
   |image3|

         | <fc>Figure 3. Pins and test points.</fc>
      |

   
   Power Supply Connectors
   ^^^^^^^^^^^^^^^^^^^^^^^
   
   .. container:: indent

      Connecters used to supply +48 V to the entire circuitry. The PA Array Controller Board provides an option for the user to use either a barrel jack connector or a two-wire terminal.

         
         -  **P1** → Barrel connector jack. Use this port if a [x mm] barrel jack is preferred.
         -  **P2** → Two-port terminal connector. Port for supply power through non-terminated wires. Ensure proper connection to the positive and negative terminals of the power supply.
         
         |
         
         .. important::

            **Supply power to either P1 or P2 only and not at the same time**


            | Supplying power to both terminals may cause permanent damage to the device

         

   
   LED Indicators
   ^^^^^^^^^^^^^^
   
   .. container:: indent

      Four indicator LEDs to display the board's current status:

         
         -  **DS1** → Indicates a fault event on the first GaN amplifier when lit up.
         -  **DS2** → Indicates a fault event on the pre-driver and driver amplifiers when lit up.
         -  **DS3** → Indicates normal operation and good power regulation when lit up.
         -  **DS4** → Indicates a fault event on the second GaN amplifier when lit up.
         

   
   Peripheral Connectors
   ^^^^^^^^^^^^^^^^^^^^^
   
   .. container:: indent

      Connectors used for debugging, programming, and communication between the software and hardware.

         
         -  **P5** → USB UART-Serial Communication
         -  **P6** → SWD Debugger
         

   
   Reset Switches
   ^^^^^^^^^^^^^^
   
   .. container:: indent

      Hardware switches used to reset specific devices:

         
         -  **S1** → LTC7000_1 Reset
         -  **S2** → LTC7000_2 Reset
         -  **S3** → MAX32666 Microcontroller Reset
         -  **S4** → LTC7000_3 Reset
         

   
   Test Points
   ^^^^^^^^^^^
   
   .. container:: indent

      Board test points for output readouts of specific devices:

         
         .. container:: group

                     
                     .. container:: half column

                                             
                                             -  **TP3** → U1 LTC7000_1 Output, +48V
                                             -  **TP6** → U2 LTC7000_2 Output, +48V
                                             -  **TP22** → U25 LTC7000_3 Output, +48V
                                             -  **TP11** → U6 MAX17643 Output, +5.6V
                                             -  **TP15** → U10 LT3471 Positive Output, +12V
                                             -  **TP16** → U10 LT3471 Negative Output, -12V
                                             -  **TP8** → U3 ADM7172 LDO Output, +5V
                                             

                     
                     .. container:: half column

                                             
                                             -  **TP10** → U5 LT3042 LDO Output, +5V
                                             -  **TP9** → U4 LT3042 LDO Output, +5V
                                             -  **TP14** → U9 ADM7150 LDO Output, +5V
                                             -  **TP13** → U8 ADM7170 LDOOutput, +1.8V
                                             -  **TP12** → U7 ADM7170 LDO Output, +3.3V
                                             -  **TP17** → U11 ADP161 LDO Output, +1.1V
                                             

                     

         

   
   Pin Turrets and Hooks
   ^^^^^^^^^^^^^^^^^^^^^
   
   |

   .. container:: indent

      The PA Array Controller Board was designed for specific power amplifiers and is used on the RF signal chain as shown below.

         |
         
         .. container:: box

         
         |image4|

                     | <fc>Figure 4. RF Signal Chain.</fc>
            |

         
         The bias lines of these amplifiers must be connected to their desired pinouts on the reference design board. Refer to the table below for the correct pin assignments.
         
         .. container:: center

                     
                     .. container:: group

                                             
                                             .. container:: half column

                                                                                             
                                                                                             -  **5V0_802** → HMC802A VDD Pin, Hook
                                                                                             -  **EN_802** → HMC802A Enable Pin, Hook
                                                                                             -  **5V0_PDA** → ADL5611 VPOS Pin, Hook
                                                                                             -  **5V0_DA** → BTS6201U VCC Pin, Hook
                                                                                             -  **EN_DA** → BTS6201U Enable Pin, Hook
                                                                                             -  **VDC1** → A5M36TG140 LDMOS Carrier Drain Pin, Hook
                                                                                             -  **VDP1** → A5M36TG140 LDMOS Peaking Drain Pin, Hook
                                                                                             -  **VGC1** → A5M36TG140 LDMOS Carrier Gate Pin, Hook
                                                                                             -  **VGP1** → A5M36TG140 LDMOS Peaking Gate Pin, Hook
                                                                                             

                                             
                                             .. container:: half column

                                                                                             
                                                                                             -  **VDC2** → A5M36TG140 GaN Carrier Drain Pin, Turret
                                                                                             -  **VDP2** → A5M36TG140 GaN Peaking Drain Pin, Turret
                                                                                             -  **VGC2** → A5M36TG140 GaN Carrier Gate Pin, Hook
                                                                                             -  **VGP2** → A5M36TG140 GaN Peaking Gate Pin, Hook
                                                                                             -  **VD1** → GTRB384608FC-V1 GaN Main Drain Pin, Turret
                                                                                             -  **VD2** → GTRB384608FC-V1 GaN Peak Drain Pin, Turret
                                                                                             -  **VG1** → GTRB384608FC-V1 GaN Main Gate Pin, Hook
                                                                                             -  **VG2** → GTRB384608FC-V1 GaN Peak Gate Pin, Hook
                                                                                             

                                             

                     

         

   


Test Setup
----------

Before You Start
~~~~~~~~~~~~~~~~

.. container:: indent

   Note that this user guide only allows the user to test and measure the transition time of:

   
   -  AD3552R DAC settling time: From pinch-off to normal operating voltage and vice versa; and
   -  Fault detection up to DAC pinch-off voltage.
   
   |
   
   .. important::

      **Use only 10-nF capacitors as load**

      | Unintended effects to actual amplifiers may be seen as the controller has not been fully characterized

   


What You’ll Need
~~~~~~~~~~~~~~~~

.. container:: indent

   
   .. container:: indent

         
         .. container:: center box

                     
                     +------------------------------------------------------------------+--------------+
                     | **Item Name**                                                    | **Quantity** |
                     +------------------------------------------------------------------+--------------+
                     | ADI PA Array Controller Board with Firmware v0.0.10112023 [BETA] | 1            |
                     +------------------------------------------------------------------+--------------+
                     | MAX32625-PICO                                                    | 1            |
                     +------------------------------------------------------------------+--------------+
                     | IDC10 Cable                                                      | 1            |
                     +------------------------------------------------------------------+--------------+
                     | +30 to +60 V Programmable Power Supply                           | 1            |
                     +------------------------------------------------------------------+--------------+
                     | Micro-USB to USB Cables                                          | 2            |
                     +------------------------------------------------------------------+--------------+
                     | 4-Channel Oscilloscope                                           | 1            |
                     +------------------------------------------------------------------+--------------+
                     | Oscilloscope Probe                                               | 4            |
                     +------------------------------------------------------------------+--------------+
                     | 10-nF Capacitors as Loads                                        | 6            |
                     +------------------------------------------------------------------+--------------+
                     | Windows PC with 2 free USB-A ports                               | 1            |
                     +------------------------------------------------------------------+--------------+
                     | ADI PA Array Control GUI Executable                              | 1            |
                     +------------------------------------------------------------------+--------------+

                     | <fc>Table 1. Evaluation Requirements.</fc>
            |

General Test Setup
~~~~~~~~~~~~~~~~~~

.. container:: indent

   
   Firmware
   ^^^^^^^^
   
   .. container:: indent

      The controller board comes preloaded with Firmware v0.0.10112023 [BETA], no initial setup is necessary. Should a re-upload is required, please see, Firmware Download and Re-Uploading.

   
   Software
   ^^^^^^^^
   
   .. container:: indent

      **System Requirements**

         
         -  Windows 10 OS or later
         -  Microsoft .Net Framework 4.6.2
         -  1920 by 1080 or greater screen resolution, recommended
         -  Keyboard and mouse
         -  Optional internet connectivity to access online resources
         
      Ensure computer meets system requirements and then run the ADI PA Array Control GUI executable included in the package. Installation is not necessary.

   
   Hardware
   ^^^^^^^^
   
   |
   
   .. container:: indent

         
         .. container:: box


         
         |image5|

                     | <fc>Figure 5. Hardware Connections Diagram.</fc>
            |

         

   
   -  Connect the 10-pin SWD debug (IDC10) cable to port P6 of the PA Array Board and then connect the other end of the SWD debug cable to the MAX32625 Pico.
   -  Use the micro-USB to USB-A cable and connect the MAX32625 Pico to your computer. This connection allows the user to upload firmware to the board.
   -  Connect the other micro-USB to USB-A cable to port P5 of the PA Array Board. This connection enables the USB-UART communication between the hardware and the graphical user interface on the host computer.
   -  Open your Windows computer, click the Start icon, start typing "This PC", and then press Enter key. In the new window that opens, look for the DAPLINK drive. If you see this then the drivers are complete and correct. If you do not see this drive, please refer to, What to do when DAPLINK does not show.
   
   .. container:: box

         
         | [diagram]
         | <fc>Figure 6. DAPLINK Drive on This PC.</fc>
      |

   
   -  Ensure that power supply output is **off** and then:
   
      -  Connect a barrel jack to P1 of the PA Array Board and the power supply; OR
   
         -  Connect negative and positive wires to port P2 of the PA Array Board and the power supply.
   
   .. important::

         
         | **Supply power to either P1 or P2 only and not at the same time**
      | Supplying power to both terminals may cause permanent damage to the device

   
   -  Connect probes to the oscilloscope.
   


Measurements
------------

GaN Power-Up Voltage Settling Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: indent

   Measure the settling time of the DAC across the GaN gate pins, VGC2, VGP2, VG1, and VG2:

   
   -  Ensure the hardware has been correctly setup. See, General Test Setup.
   -  Connect a 10-nF capacitive load across each of the GaN gate pins and ground: VGC2, VGP2, VG1, VG2.
   -  Connect the positive and negative terminals of the oscilloscope probes in parallel with each of the capacitor pins and ground.
   -  Configure the oscilloscope. Recommended settings are:
   
      -  Trigger value → -3 V, rising edge
      -  Time scale factor → 1 µS/div
      -  Amplitude scale factor → 2 V/div
   
   -  Refer to Figure x for the complete test setup.
   -  Set the power supply to +48 V and turn on output.
   -  Upon board boot-up, the default voltages on the GaN gate pins should be at its pinch-off voltage of -5 V.
   -  On the GUI, set carrier and peak gates to the operating voltages by typing on the input boxes or moving the sliders to the indicated levels and then pressing the Set button:
   
      -  **GaN1 Carrier Gate Voltage** (VGC2) → -2 V
      -  **GaN1 Peak Gate Voltage** (VGP2) → -2.6 V
      -  **GaN2 Carrier Gate Voltage** (VG1) → -2.75 V
      -  **GaN2 Peak Gate Voltage** (VG2) → -2.75 V
   
   .. container:: box

         
         | [diagram]
         | <fc>Figure 7. ADI PA Array Control GUI for Setting GaN Voltages.</fc>
      |

   
   -  The readouts on the UI should show the gate voltages changing from pinch-off to operating voltage.
   -  The transition should also be visible from the oscilloscope display. Refer to expected oscilloscope outputs below.
   
   .. container:: group

         
         .. container:: half column

                     
                     .. container:: box

                                             
                                             | |image6|
                                             | <fc>Figure 8. VGC2 Voltage Time Response.</fc>
                        |

                     
                     .. container:: box


                     
                     |image7|

                                             | <fc>Figure 9. VGP2 Voltage Time Response.</fc>
                        |

                     

         
         .. container:: half column

                     
                     .. container:: box


                     
                     |image8|

                                             | <fc>Figure 10. VG1 Voltage Time Response.</fc>
                        |

                     
                     .. container:: box


                     
                     |image9|

                                             | <fc>Figure 11. VG2 Voltage Time Response.</fc>
                        |

                     

         

   


LDMOS Power-Up Voltage Settling Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|

.. container:: indent

   Measuring the DAC voltage transition across the LDMOS gate pins, VGC1, and VGP1:

   
   .. important::

      **Complete all preceding steps before continuing to this section**

      | Lorem ipsum dolor sit amet

   
   -  Connect a 10-nF capacitive load across each of the LDMOS gate pins (VGC1, VGP1) and ground.
   -  Connect the positive and negative terminals of the oscilloscope probes in parallel with each of the capacitor pins and ground.
   -  Adjust oscilloscope settings:
   
      -  Trigger value → +1 V on rising edge
   
   -  On the GUI, set carrier and peak gates to the operating voltages by typing on the input boxes or moving the sliders to the indicated levels and then pressing the Set button:
   
      -  **LDMOS Carrier Gate Voltage** (VGC1) → +3.8 V
      -  **LDMOS Peak Gate Voltage** (VGP1) → +1.9 V
   
   .. container:: box

         
         | [diagram]
         | <fc>Figure 12. ADI PA Array Control GUI for Setting LDMOS Voltages.</fc>
      |

   
   -  The readouts on the UI should show the gate voltages changing from pinch-off to operating voltage.
   -  The transition should also be visible from the oscilloscope display. Refer to expected oscilloscope outputs below.
   
   .. container:: group

         
         .. container:: half column

                     
                     .. container:: box

                                             
                                             | |image10|
                                             | <fc>Figure 13. VGC1 Voltage Time Response.</fc>
                        |

                     

         
         .. container:: half column

                     
                     .. container:: box


                     
                     |image11|

                                             | <fc>Figure 14. VGP1 Voltage Time Response.</fc>
                        |

                     

         

   


GaN and LDMOS Power-Down Settling Times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|

.. container:: indent

   All the gate pins are should be in the normal operating voltage state.

   
   .. important::

      **Complete all preceding steps before continuing to this section**

      | Lorem ipsum dolor sit amet

   
   Measuring the voltage transition from normal operating to pinch-off voltage:
   
   -  Connect all 4 channels of the oscilloscope probes in parallel with all the capacitor pins and ground.
   -  Configure the oscilloscope. Recommended settings are:
   
      -  Trigger value → -3 V, falling edge
   
   -  Set the gate voltages to their pinch-off voltages:
   
      -  **LDMOS Carrier Gate Voltage** (VGC1) → 0 V
      -  **LDMOS Peak Gate Voltage** (VGP1) → 0 V
      -  **GaN1 Carrier Gate Voltage** (VGC2) → -5 V
      -  **GaN1 Peak Gate Voltage** (VGP2) → -5 V
      -  **GaN2 Carrier Gate Voltage** (VG1) → -5 V
      -  **GaN2 Peak Gate Voltage** (VG2) → -5 V
   
   .. container:: box

         
         | [diagram]
         | <fc>Figure 15. ADI PA Array Control GUI for Setting GaN and LDMOS Voltages.</fc>
      |

   
   -  Press the set button to reflect the changes. The result should be the same as the image below.
   
   .. container:: group

         
         .. container:: half column

                     
                     .. container:: box

                                             
                                             | |image12|
                                             | <fc>Figure 16. VGC2 Voltage Time Response.</fc>
                        |

                     
                     .. container:: box


                     
                     |image13|

                                             | <fc>Figure 17. VGP2 Voltage Time Response.</fc>
                        |

                     
                     .. container:: box


                     
                     |image14|

                                             | <fc>Figure 18. VG1 Voltage Time Response.</fc>
                        |

                     

         
         .. container:: half column

                     
                     .. container:: box


                     
                     |image15|

                                             | <fc>Figure 19. VG2 Voltage Time Response.</fc>
                        |

                     
                     .. container:: box


                     
                     |image16|

                                             | <fc>Figure 20. VGC1 Voltage Time Response.</fc>
                        |

                     
                     .. container:: box


                     
                     |image17|

                                             | <fc>Figure 21. VGP1 Voltage Time Response.</fc>
                        |

                     

         

   
   .. tip::

      **Faster settling time can be achieved by using smaller capacitance**


      | The relationship between speed and oscillation ripple is inversely proportional. Faster settling time can be achieved at the expense of a much cleaner oscillation and vice versa.

   


Fault Detection Response Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|

.. container:: indent

   Fault detection is important because lorem ipsum dolor sit amet consectetuer. The fault detection response time is the time it takes from when the fault is detected until the DAC outputs the gate pinch-off voltage. When LTC7000 detects a fault event, a signal to the MCU in approximately 1 microsecond. This value will then be added to the system power-down measurement and the time it takes for the MCU to process the fault flag up to the DAC command.

   |
   
   .. container:: box

   
   |image18|

         | <fc>Figure 22. LTC7000 → MCU GPIO Fault Flag Time.</fc>
      |

   
   Inducing an overvoltage fault:
   
   -  Place the positive terminal of the oscilloscope probe into the provided wire as shown in the image below. Then connect the negative terminal of the oscilloscope probe to the GND of the board.
   
   .. container:: box

         
         | [diagram]
         | <fc>Figure 23. Fault Detection Response Time Measurement Setup.</fc>
      |

   
   -  Set the required oscilloscope settings:
   
      -  **Trigger value** → +1 V
      -  **Time scale factor** → 1 µS/div
      -  **Amplitude scale factor** → 1 V/div
   
   -  Increase the voltage from the external power supply from +48V to +56V. This will cause a fault event since the preset threshold for an overvoltage is +55V.
   -  The oscilloscope will display a similar time response as shown below.
   
   .. container:: box

         
         | [diagram]
         | <fc>Figure 24. Lorem ipsum dolor sit amet.</fc>
      |

   
   -  On the GUI, it will notify the user that a fault event occurred and show a warning message as in the image below.
   -  Also, the GUI is capable of logging and displaying the fault event time and on which device it occurs.
   
   .. container:: box

         
         | [diagram]
         | <fc>Figure 25. GUI Fault Message and Logs.</fc>
      |

   
   -  The overall time from LTC7000 fault detection up to the DAC pinch-off voltage is shown on the Fault Event Time Summary below.
   


DAC Settling Time
~~~~~~~~~~~~~~~~~

.. container:: indent

   As per the customer's request, we are able to test and measure the DAC settling time from these specified voltage levels

   
   -  **Pinch-off Voltage** → -7 V
   -  **Operating Voltage** → -1.2 V
   
   Do note that the firmware loaded on the board doesn't include these measurements. We can send a separate firmware if necessary.

   
   | The DAC output voltage settling time from -7V pinch-off to -1.2V is 2.31 µS. See the image below.
   |

   .. container:: group

         
         .. container:: half column

                     
                     .. container:: box


                     
                     |image19|

                                             | <fc>Figure 26. -7 V to -1.2 V DAC Settling Time.</fc>
                        |

                     

         
         .. container:: half column

                     
                     .. container:: box


                     
                     |image20|

                                             | <fc>Figure 27. -1.2V to -7V DAC Settling Time.</fc>
                        |

                     

         

   


Enabling Continuos Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: indent

   
   -  Step
   -  Step
   -  Step
   


Lab Results
-----------

.. container:: center box

   
   +--------+-------------------------------+-------------+-------------+------------+---------------+
   | **Pin  | **Description**               | **Pinch-off | **Operating | **Power-up | \**Power-down |
   | Name** |                               | Voltage**   | Voltage**   | Time**     | Time \*\*     |
   +--------+-------------------------------+-------------+-------------+------------+---------------+
   | VGC1   | A5M36TG140 LDMOS Carrier Gate | 0 V         | +3.8 V      | 2.09 µS    | 2.25 µS       |
   +--------+-------------------------------+-------------+-------------+------------+---------------+
   | VGP1   | A5M36TG140 LDMOS Peaking Gate | 0 V         | +1.9 V      | 1.65 µS    | 2.01 µS       |
   +--------+-------------------------------+-------------+-------------+------------+---------------+
   | VGC2   | A5M36TG140 GaN Carrier Gate   | -5 V        | -2 V        | 1.95 µS    | 2.05 µS       |
   +--------+-------------------------------+-------------+-------------+------------+---------------+
   | VGP2   | A5M36TG140 GaN Peaking Gate   | -5 V        | -2.6 V      | 1.73 µS    | 1.95 µS       |
   +--------+-------------------------------+-------------+-------------+------------+---------------+
   | VG1    | GTRB384608FC-V1 GaN Main Gate | -5 V        | -2.75 V     | 1.81 µS    | 2.00 µS       |
   +--------+-------------------------------+-------------+-------------+------------+---------------+
   | VG2    | GTRB384608FC-V1 GaN Peak Gate | -5 V        | -2.75 V     | 1.81 µS    | 2.00 µS       |
   +--------+-------------------------------+-------------+-------------+------------+---------------+

   | <fc>Table X. Gate Voltages Timing Response Summary.</fc>
   |

System Power Up and System Power Down
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: indent

   The below table shows the summary of our time response test for each DAC's. As shown below, we achieved the <5 µS time requirement.


-  **Power-up Time** → from pinch-off voltage to operating voltage.
-  **Power-down Time** → from operating voltage to pinch-off voltage.

Fault Event Time Response
~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: indent

   The below table shows the summary of our time response test when a fault occurs. As shown below, we achieved the <10 µS time requirement.

   
   The total time from fault detection up to the gate pinch-off is given by:
   
   -  Total time = Fault flag (µS) + MCU processing time (µS) + RF switch time (µS) + highest power down time between VGC2, VGP2,VG1,VG2 (µS) + highest power down time between VGC1, VGP1
   -  Total time = 1.0898 µS + 3.7078 µS + 0.3 µS + 2.05 µS + 2.25 µS
   -  Total time = 9.4 µS
   
   | **Fault Flag Time** → Time it takes for the MCU to recognize that there is a fault signal coming from the LTC7000.
   | **MCU Processing Time** → Total time for MCU to process the fault flag signal up to commanding the DAC.
   | **RF switch Time** → Total time for the RF switch to turn-off.
   | **Power-down Time** → DAC output from operating voltage to pinch-off.
   | **Total Time** → Time from fault detection to Vgg pinch-off.
   |


Resources
---------

Software Manual
~~~~~~~~~~~~~~~

.. container:: indent

   Parts of the UI (new page)


Firmware Download and Reuploading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Further Help
~~~~~~~~~~~~

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/block_diagram.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/side-by-side.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/tps.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/8t8r_signal_chain.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/connection.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vgc2_pwr_up_time.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vgp2_pwr_up_time.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vg1_vg2_pwr_up_time.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vg1_vg2_pwr_up_time.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vgc1_pwr_up_time.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vgp1_pwr_up_time.png
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vgc2_pwr_dwn_time.png
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vgp2_pwr_dwn_time.png
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vg1_vg2_pwr_dwn_time.png
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vg1_vg2_pwr_dwn_time.png
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vgc1_pwr_dwn_time.png
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/vgp1_pwr_dwn_time.png
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/flag_time.png
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/7vto-1.2v.png
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/1.2vto-7v.png
