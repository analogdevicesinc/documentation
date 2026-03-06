:doc:`Click here to return to the Hardware Setup page </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup>`

:doc:`Click here to return to the Running sample Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

AD2433 with SOM carrier ez-kit
==============================

Evaluation boards
-----------------

The AD243x standard power evaluation boards used in the demos are explained in the following subsections.

ADZS2433-MINI
~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` shows a :doc:`ADZS2433-MINI </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` board which can be used as a standard power A2B master. The board has following peripherals

-  AD2433 A2B transceiver
-  512K Self-Boot Memory (EEPROM)

|image1|

.. container:: centeralign

   \ **Figure:** ADZS-2433MINI


Hardware modifications
^^^^^^^^^^^^^^^^^^^^^^

The following hardware modifications are required:-

-  For all ADZS2433-MINI boards, remove R21, R18, R58, R59.
-  For all ADZS2433-MINI boards, add R17.
-  For the board with I2C address 0x68, remove R33 and add R34.
-  For the board with I2C address 0x6A, remove R34 and add R33.

Jumper settings
^^^^^^^^^^^^^^^

The jumpers on the board must be in the following positions

EVAL-AD2433WB1BZ
~~~~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` shows :doc:`EVAL-AD2433WB1BZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` board which can be used as a standard power bus powered A2B sub node. The board has following peripherals

-  AD2433 A2B transceiver
-  Stereo Audio Codec (ADAU1961) with Line I/O
-  4 Microphones

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/eval-2433wb1bz_new.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure:** EVAL-AD2433WB1BZ board


.. _jumper-settings-1:

Jumper settings
^^^^^^^^^^^^^^^

The following jumper settings are required:-

-  P1 – 1-2

EV-SC594-SOM Rev B
~~~~~~~~~~~~~~~~~~

This is same as :doc:`EV-SC594-SOM </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>`.

EV-SOMCRR-EZKIT Rev A
~~~~~~~~~~~~~~~~~~~~~

This is same as :doc:`EV-SOMCRR-EZKIT </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` .

Connections
-----------

To run the sample demo, the following setup connections are to be made.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main_connections_using_pc_host_.png
   :align: center

.. container:: centeralign

   \ **Figure:** Multi-main connections using PC(Host) and ADSP-21596 SOM carrier kit and ADZS2433MINI’s


The step described in this section are recommended to run the following configurations

-  AD2433 multi-main sample demo using ADSP-21596 platform and PC as host.

The Evaluation boards shall be connected in the following order.

-  Connect the EV-21569-SOM to the EV-SOMCRR-EZKIT.
-  Connect one of the two ADZS2433-MINI boards to J10 A2B interface of the EV-SOMCRR-EZKIT. Let this be “main node 0” with I2C address configured to be 0x68.
-  Connect other ADZS2433-MINI to J11 A2B interface of the EV-SOMCRR-EZKIT. Let this be “main node 1” with I2C address configured to be 0x6A.
-  For A2B chain 0:- ADZS2433-MINI (Main node 0) EVAL-AD2433WB1BZ (Sub node 0) EVAL-AD2433WB1BZ (Sub node 1), the connections are as follows

   -  Connect twisted-pair wire between the “B” connector on the main node 0 board and the “A” connector on the sub node 0 board.

      -  Connect twisted-pair wire between the “B” connector on the sub node 0 board and the “A” connector on the sub node 1 board.

-  For A2B chain 1:- ADZS2433-MINI (Main node 1) EVAL-AD2433WB1BZ (Sub node 2) EVAL-AD2433WB1BZ (Sub node 3), the connections are as follows

   -  Connect twisted-pair wire between the “B” connector on the main node 1 board and the “A” connector on the sub node 2 board.

      -  Connect twisted-pair wire between the “B” connector on the sub node 2 board and the “A” connector on the sub node 3 board.

-  Connect 12V power supply to the power connector of EV-SOMCRR-EZKIT.

Audio In/out for ADSP-21569 and PC as a host – multi-main
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect an audio source (e.g., output from an iPod) to ‘Audio Line- in’ port, shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>`\ (Audio Input).
-  Connect separate audio sink such as headphones to line out as shown in the :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>`.

|image2|

.. container:: centeralign

   \ **Figure:** Sample audio setup


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/adzs-ad2433mini.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/ad2433_multimain.png
   :width: 800px
