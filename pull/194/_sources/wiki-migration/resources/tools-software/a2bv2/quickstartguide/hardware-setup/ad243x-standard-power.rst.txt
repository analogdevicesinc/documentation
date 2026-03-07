:doc:`Click here to return to the Hardware Setup page </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup>`

AD243x standard Power
=====================

Evaluation boards
-----------------

The AD243x standard power evaluation boards used in the demos are explained in the following subsections.

EVAL-AD2433WA1BZ
~~~~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` shows a :doc:`EVAL-AD2433WA1BZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` board which can be used as a standard power A2B main or a local powered A2B sub node. The board has following peripherals

-  AD2433 A2B transceiver
-  Stereo Audio Codec (ADAU1961) with Line I/O
-  Sigma DSP (ADAU1452) with Optical SPDIF I/O
-  512K Self-Boot Memory (EEPROM)

|image1|

.. container:: centeralign

   \ **Figure:** EVAL-AD2433WA1BZ board


EVAL-AD2433WB1BZ
~~~~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` shows :doc:`EVAL-AD2433WB1BZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` board which can be used as a standard power bus powered A2B sub node. The board has following peripherals

-  AD2433 A2B transceiver
-  Stereo Audio Codec (ADAU1961) with Line I/O
-  4 Microphones

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/eval-2433wb1bz_new.png
   :align: center
   :width: 500px

.. container:: centeralign

   \ **Figure:** EVAL-AD2433WB1BZ board


Connections
-----------

To run the sample demo, the following setup connections are to be made.

Jumper setting
~~~~~~~~~~~~~~

Jumper settings (default) for EVAL-AD2433WA1BZ (Main) and EVAL-AD2433WB1BZ (Sub 0 and Sub 1) are as shown in Table.

.. container:: centeralign

   \ **Table:** Jumper Settings: Standard Power


+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| **Jumper** | **Purpose in EVAL-AD2433WA1BZ** | **Main**     |   | **Jumper** | **Purpose in EVAL-AD2433WB1BZ** | **Sub 0** | **Sub 1** |
+============+=================================+==============+===+============+=================================+===========+===========+
| JP1        | USBi Sel                        | 1-2          |   | JP1        | DRX0                            | 1-2       | 1-2       |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP2        | Boot                            | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP3        | DRX0                            | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP4        | DRX1                            | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP5        | Clock Sel                       | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP6        | PWM Select                      | X            |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP7        | Self-Discovery                  | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
|            |                                 |              |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P1         | I2C/SPI                         | Keep default |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P2         | SigmaStudio+                    | Connect      |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P3         | PWR                             | Connect      |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P4         | +12V                            | Keep default |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P5         | IOVDD                           | 2-3          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P7         | I2S Connector                   | Keep default |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+

.. _evaluation-boards-1:

Evaluation boards
~~~~~~~~~~~~~~~~~

A2B Evaluation boards shall be connected in the following order

-  :doc:`EVAL-AD2433WA1BZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` (Main) → :doc:`EVAL-AD2433WB1BZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` (Sub 0) → :doc:`EVAL-AD2433WB1BZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` (Sub 1)
-  Connect twisted-pair wire between the “B” connector on the Main board and the “A” connector on the Sub 0 board.
-  Connect twisted-pair wire between the “B” connector on the Sub 0 board and the “A” connector on the Sub 1 board.
-  Connect 12V power supply to the power connector on Main board.

.. note::

   This connection is recommended for running the standard power sample demo using PC as host.


   |image2|

.. container:: centeralign

   \ **Figure:** A2B Eval board connections: Standard Power


Audio In/out
~~~~~~~~~~~~

-  Connect separate audio sources (e.g., output from an iPod) to ‘Audio Line- in’ ports, on A2B subordinate boards.
-  Connect separate audio sinks (e.g., headphones and speakers) to ‘Audio Line-out’ on A2B main and subordinate boards.

Sample configuration
^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/sample_a2b_demo_configuration_1.png
   :alt: Figure: Sample demo configuration
   :align: center
   :width: 400px

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/eval-ad2433wa1bz.png
   :width: 1080px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433_setup.png
   :width: 1000px
