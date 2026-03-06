:doc:`Click here to return to the Hardware Setup page </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup>`

:doc:`Click here to return to the Running sample Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

AD243x High Power
=================

Evaluation boards
-----------------

The AD243x high power evaluation boards used in the demos are explained in the following subsections.

EVAL-AD2435WA3LZ
~~~~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>` shows a :doc:`EVAL-AD2435WA3LZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>` board which can be used as a high power A2B main or a local powered A2B sub node. The board has following peripherals

-  AD2435 A2B transceiver
-  Stereo Audio Codec (ADAU1961) with Line I/O
-  Sigma DSP (ADAU1452) with Optical SPDIF I/O
-  512K Self-Boot Memory (EEPROM)

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/eval-ad2435wa3lz_board_new.png
   :align: center
   :width: 900px

.. container:: centeralign

   \ **Figure:** EVAL-AD2435WA3LZ board


EVAL-AD2435WJ3LZ
~~~~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>` shows :doc:`EVAL-AD2435WJ3LZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>` board which can be used as a high power bus powered A2B sub node. The board has following peripherals

-  AD2435 A2B transceiver
-  Stereo Audio Codec (ADAU1961) with Line I/O
-  Onboard Class D (FDA802S) Amplifier
-  4 Microphones
-  Onboard RGB LED

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/eval-ad2435j3lz_new.png
   :align: center
   :width: 900px

.. container:: centeralign

   \ **Figure:** EVAL-AD2435WJ3LZ board


Connections
-----------

To run the sample demo, the following setup connections are to be made.

Jumper setting
^^^^^^^^^^^^^^

Jumper settings (default) for EVAL-AD2435WA3LZ (Main) and EVAL-AD2435WJ3LZ (Sub 0 and Sub 1) are as shown in table.

.. container:: centeralign

   \ **Table:** Jumper Settings: High Power


+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| **Jumper** | **Purpose in EVAL-AD2435WA3LZ** | **Main**     |   | **Jumper** | **Purpose in EVAL-AD2435WJ3LZ** | **Sub 0** | **Sub 1** |
+============+=================================+==============+===+============+=================================+===========+===========+
| JP1        | Boot                            | x            |   | JP1        | Class D Standby                 | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP2        | /Output Source                  | 2-3          |   | JP2        | I2S/                            | 5-6       | 5-6       |
|            |                                 |              |   |            | CODEC/                          | 7-14      | 7-8       |
|            |                                 |              |   |            | TUNER/                          | 8-13      | 17-18     |
|            |                                 |              |   |            | CLASS-D                         | 19-20     | 19-20     |
|            |                                 |              |   |            |                                 | 21-22     | 21-22     |
|            |                                 |              |   |            |                                 | 23-24     | 23-24     |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP3        | Input Source                    | 2-3          |   | JP3        | PWM Select                      | 1-2       | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP4        | Clock Sel                       | 1-2          |   | JP4        | Not present                     | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP5        | Self-Discovery Mode             | 1-2          |   | JP5        | VBUS Supply                     | 2-3       | 2-3       |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP6        | ADC0/VR1                        | x            |   | JP6        |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP7        | ADC1/VR2                        | x            |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP8        | I2S Signals                     | 1-2          |   |            |                                 |           |           |
|            |                                 | 3-4          |   |            |                                 |           |           |
|            |                                 | 5-6          |   |            |                                 |           |           |
|            |                                 | 7-8          |   |            |                                 |           |           |
|            |                                 | 9-10         |   |            |                                 |           |           |
|            |                                 | 11-12        |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
|            |                                 |              |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P1         | I2C/SPI                         | x            |   | P1         | I2C/SPI                         | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P2         | SigmaStudio+                    | Connect      |   | P2         | DCOP Module Connector           | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P3         | Not present                     | x            |   | P3         | Tuner Module Connector          | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P4         | Supply In                       | Connect      |   | P4         | CH2                             | x         | Connect   |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P5         | PWR                             | Keep default |   | P5         | CH1                             | x         | Connect   |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
|            |                                 |              |   | P6         | HWMUTE                          | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P12        | Fuse                            | Keep default |   |            |                                 | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
|            |                                 |              |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+

.. _evaluation-boards-1:

Evaluation boards
~~~~~~~~~~~~~~~~~

A2B Evaluation boards shall be connected in the following order

-  :doc:`EVAL-AD2435WA3LZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>` (Main) → :doc:`EVAL-AD2435WJ3LZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>` (Sub 0) → :doc:`EVAL-AD2435WJ3LZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>` (Sub 1)
-  Connect twisted-pair wire between the “B” connector on the Main board and the “A” connector on the Sub 0 board.
-  Connect twisted-pair wire between the “B” connector on the Sub 0 board and the “A” connector on the Sub 1 board.
-  Connect 12V power supply to the power connector on Main board.

.. note::

   This connection is recommended for running the High-power sample demo using PC as host.


   |image1|

.. container:: centeralign

   \ **Figure:** A2B Eval board connections: High Power


USBi/Aardvark
~~~~~~~~~~~~~

For Aardvark, download and install the “USB Drivers – Windows” from Total Phase website.

-  Attach an USBi/Aardvark cable to the main board (SIGMA STUDIO PLUS) connector as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>`. Other end of the cable should be connected to the PC.
-  This connection is required to override the schematic for the main node SigmaDSP ADAU1452. The connection is also used to directly control A2B system when PC is used as the target processor.

**Audio In/out**

-  Connect separate audio sources (e.g., output from an iPod) to ‘Audio Line- in’ ports, shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>`, on A2B sub boards.
-  Connect separate audio sinks (e.g., headphones and speakers) to ‘Audio Line-out’ and output of Class-D amplifier ports as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>`, on A2B main and sub boards.

|Sample Audio Configuration figure|

.. container:: centeralign

   \ **Figure:** Sample Audio Configuration figure


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/img_20241009_141342.jpg
.. |Sample Audio Configuration figure| image:: https://wiki.analog.com/_media/ajaxperflookupdelay/ad2435_audio_config.png
   :width: 600px
