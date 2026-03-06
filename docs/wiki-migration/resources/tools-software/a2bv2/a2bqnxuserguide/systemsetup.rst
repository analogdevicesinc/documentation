:doc:`Click here to return to A2B QNX User Guide Homepage. </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide>`

System Setup
============

Hardware Setup
--------------

The complete hardware setup for the demo is detailed in this section. The various jumper and switch settings needed are described below.

EVAL-AD2428WD1BZ
~~~~~~~~~~~~~~~~

The Below image shows an EVAL-AD2428WD1BZ board which can be used as either an A2B master or slave node. The board has following components,

-  AD2428 A2B transceiver
-  ADAU1452 SigmaDSP Audio Processor
-  512K Self-Boot Memory (EEPROM)
-  S/PDIF Optical Connectors
-  Codec ADAU1761

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/ad2428wd1bz.png
   :align: center
   :width: 600px

Jumper Settings
^^^^^^^^^^^^^^^

Jumper settings (default) for EVAL-AD2428WD1BZ is as shown in below Table.

+---------+-----------+-----------+---------+---------+---------+---------+---------+---------+----------+----------------+----------+
| **JP1** | **JP2**   | **JP3**   | **JP4** | **JP5** | **JP6** | **JP7** | **JP8** | **JP9** | **JP10** | **JP11/12/13** | **JP14** |
+=========+===========+===========+=========+=========+=========+=========+=========+=========+==========+================+==========+
| 1-2     | 1-2 & 3-4 | 1-2 & 3-4 | 1-2     | 3-4     | 3-4     | 3-4     | 2-3     | 3-4     | 1-2      | Open           | 1-2      |
+---------+-----------+-----------+---------+---------+---------+---------+---------+---------+----------+----------------+----------+

EVAL-AD2428WB1BZ
~~~~~~~~~~~~~~~~

The below image shows an EVAL-AD2428WB1BZ board which can be used as an A2B slave node. The board has following peripherals

-  AD2428 A2B transceiver
-  SigmaDSP with codec (ADAU1761)
-  2 PDM Microphones
-  Push Button
-  EEPROM

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/wb1bz.png
   :align: center
   :width: 600px

EVAL-AD2428WC1BZ
~~~~~~~~~~~~~~~~

The below image shows an EVAL-AD2428WC1BZ board which can be used as an A2B slave node. The board has following peripherals

-  AD2428 A2B transceiver
-  4 PDM Microphones

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/wc1bz.png
   :align: center
   :width: 600px

Windows PC Software Set Up
--------------------------

The QNX SDP 7.0 and the BSP corresponding to the demo platform, i.e., BeagleBone Black can be installed via the QNX software center. The Software Center can be downloaded from `QNX Software Center <https://blackberry.qnx.com/en/products/foundation-software/qnx-software-development-platform>`__. The software center also comes with the installation of Momentics IDE.

QNX Software Development Platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launch QNX software center and click on Add Installation in the Software Center Home page. It should launch the new installation wizard as shown in below image.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/qnx_sw_setup.png
   :align: center
   :width: 600px

Follow along the instructions to complete the installation. Please note that the product must be registered in your myQNX account for it to appear in the “Available Packages” section.

Board Support Package
~~~~~~~~~~~~~~~~~~~~~

| After installing QNX Software Development Platform, the next step is to install Board Support Package for the BeagleBone Black platform from QNX software center. The list of all available BSPs for QNX 7.0 and their location is available in `QNX Website <https://blackberry.qnx.com/en/developers/board-support-packages>`__.
| Some important folder that will be used for this demo described in :doc:`A2B Demo on QNX </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/a2bdemoonqnx>` are:

| **QNX:**
| **<QNX 7.0 installation path>/target/qnx7/usr/include/hw/i2c.h:** This header file is needed to build I2C related files in the a2bapp-qnx project.
| **<QNX 7.0 installation path>/target/qnx7:** This contains the target files. This path is needed for Makefile based build.
| **<QNX 7.0 installation path>/host/win64/x86_64:** This contains the QNX host files. This path is needed for Makefile based build.

| **BeagleBone Black BSP:**
| **<BSP installation path>/images:** This contains the QNX binaries needed to boot the QNX OS
| **<BSP installation path>/prebuilt\\armle-v7\\boot\\build:** This contains the build files that need to be modified for rebuilding the image.

Board Support Package for Custom Platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a custom platform, the Board Support Package corresponding to the platform must be installed from the `QNX Website <https://blackberry.qnx.com/en/developers/board-support-packages>`__.
