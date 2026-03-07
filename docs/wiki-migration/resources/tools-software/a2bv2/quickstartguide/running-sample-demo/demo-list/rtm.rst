:doc:`Click here to return to the Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

:doc:`Clik here to return to Running sample demo, PC as Host </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host>`

:doc:`Click here to return to Running sample Demo: Target as Host </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/target>`

Running Remote Tuner Module Sample Demo
=======================================

This section briefs the procedure to run the advanced demo using remote tuner module. BF527 acts as host processor. In this case the host processor controls the discovery and programming of A2B nodes in the system. The remote tuner module is connected to A2B slave node. The system block diagram for this is as shown in Figure

Additional requirement
----------------------

-  Tuner module – TDA7707EB
-  Antenna assembly
-  Flat ribbon cable for Tuner – DCOP connection.

Jumper setting
~~~~~~~~~~~~~~

+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| **Jumper** | **Purpose in EVAL-AD2433WA1BZ** | **Master**   |   | **Jumper** | **Purpose in EVAL-AD2435WA3LZ** | **Slave 0** | **Purpose in EVAL-AD2435WJ3LZ** | **Slave 1** |
+============+=================================+==============+===+============+=================================+=============+=================================+=============+
| JP1        | USBi Sel                        | 1-2          |   | JP1        | Boot                            | x           | Class D Standby                 | x           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| JP2        | BOOT                            | 1-2          |   | JP2        | Output Source                   | 2-3         | I2S/                            | 9-10        |
|            |                                 |              |   |            |                                 |             | CODEC/                          | 15-16       |
|            |                                 |              |   |            |                                 |             | TUNER/                          | 17-18       |
|            |                                 |              |   |            |                                 |             | CLASS-D                         | 19-20       |
|            |                                 |              |   |            |                                 |             |                                 | 21-22       |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| JP3        | DRX0                            | 1-2          |   | JP3        | Input Source                    | 2-3         | PWM Sel                         | x           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| JP4        | DRX1                            | 1-2          |   | JP4        | Clk Sel                         | 1-2         |                                 |             |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| JP5        | CLK Sel                         | 1-2          |   | JP5        | Self Discovery Mode             | 1-2         | VBUS Supply                     | 2-3         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| JP6        | PWM Sel                         | x            |   | JP6        | ADC0/VR1                        | x           |                                 |             |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| JP7        | Self Disc.                      | 1-2          |   | JP7        | ADC2/VR2                        | x           |                                 |             |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
|            |                                 |              |   | JP8        | I2S Signals                     | 1-2         |                                 |             |
|            |                                 |              |   |            |                                 | 3-4         |                                 |             |
|            |                                 |              |   |            |                                 | 5-6         |                                 |             |
|            |                                 |              |   |            |                                 | 7-8         |                                 |             |
|            |                                 |              |   |            |                                 | 9-10        |                                 |             |
|            |                                 |              |   |            |                                 | 11-12       |                                 |             |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| P1         | I2C/SPI                         | keep default |   | P1         | I2C/SPI                         | x           | I2C/SPI                         | x           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| P2         | SigmaStudio Connect             | connect      |   | P2         | SigmaStudio                     | Connect     | DCOP Module Connector           | Connect     |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| P3         | PWR                             | connect      |   | P3         |                                 |             | Tuner Module Connector Connect  | Connect     |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
| P4         |                                 | Keep default |   | P4         | Supply in                       | Connect     | CH2                             | Connect     |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
|            |                                 |              |   | P5         |                                 |             | CH1                             | Connect     |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+
|            |                                 |              |   | P6         |                                 |             | HWMUTE                          | x           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-------------+---------------------------------+-------------+

A2B Cross-Over Cable
^^^^^^^^^^^^^^^^^^^^

This demo requires a connection to made between EVAL-AD2433WA1BZ board (which has DuraClick connector) to EVAL-AD2435WA3LZ board (which has H-DAC connector). For this purpose, users are required to have an A2B cross-over cable as in below figure. Please contact your ADI or your local FAE’s for the cross-over cable.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ **Figure:** A2B Cross-Over Cable


A2B Demo system Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~

After completing all the connections, the A2B system should look as shown in Figure


|image2|

.. container:: centeralign

   \ **Figure:** RTM demo system in PC as Host


   |image3|

.. container:: centeralign

   \ **Figure:** RTM demo system: Tuner connection close up


Running sample demo: PC as host
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  The SigmaStudio+ schematic for this demo can be found at .\\Schematics\\PC\\A2BSchematics\\adi_a2b_3NodeRTMDemoConfig.dspproj. Refer the figure RTM demo system in PC as Host for connection and this project can be run as such.

Running sample demo: BF as host
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    *The SigmaStudio+ schematic for this demo can be found at "C:\Analog Devices\ADI_A2B-SSPlus_Software-Relx.y.z\Schematics\PC\adi_a2b_3NodeRTMDemoConfig.ssprj". The demo application already uses the exported BCF from this schematic.
   * The demo project is in /Target/examples/advancedapp/remoteTuner folder. This can be used for downloading using CCES- similar to BF project in [[/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/bf-as-host|running sample demo with BF as host]]

   |image4|

.. container:: centeralign

   \ **Figure:** RTM demo system in target as host


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/a2b_crossover_cable.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/rtm_ss.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/rtm_module_setup.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/rtm_bf.jpg
   :width: 600px
