ADIS16210/PCBZ USER GUIDE
=========================

The ADIS16210/PCBZ is a "breakout board," which provides (1) ADIS16210CMLZ and (1) interface PCB to simplify the process of "prototyping" during the early stages of system design and evaluation.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16210_pcbz_wiki_00.png
   :width: 300px

ADIS16210CMLZ
-------------

The ADIS16210CMLZ is a fully-integrated/calibrated, digital tilt sensor, which provides a serial peripheral interface (SPI) for all digital communications. It provides a flexible connector interface, with a with 15-lead, cable edge interface. which minimizes board space, but does not support standard ribbon cable connections.

INTERFACE PCB
-------------

The interface PCB provides access to the ADIS16210CMLZ, using a dual-row, 16-pin connector, which supports standard ribbon cable systems and hand-soldering connection techniques. The interface PCB also provides two sets of mounting holes: one set of holes for attaching the ADIS16210CMLZ to the interface PCB and another set of holes for mounting the interface board to the system’s frame. The first set of holes line up with the ADIS16210CMLZ's mounting holes and are pre-tapped for use with M2x0.4mm machine screws. The second set of holes are support M2 machine screws and line up with M2x0.4mm, pre-tapped holes on the EVAL-ADIS evaluation system board.

Mechanical Drawing
~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16210_pcbz_wiki_02.png
   :width: 600px

Electrical Schematic
~~~~~~~~~~~~~~~~~~~~

Please see the following graphic for the Interface PCB's electrical schematic:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16210_pcbz_wiki_01.png
   :width: 600px

INTERFACE CONNECTOR PIN ASSIGNMENTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

J1 is the electrical connector that provides direct access to power, ground and critical digital I/O pins on the devices. It is a 16-pin, dual-row, 2-mm pitch connector that support 1mm ribbon cable systems. Here is the pin assignments for J1:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb-j1-connector.png
   :width: 200px

NOTE: The ADIS16210CMLZ does not support DIO3 and DIO4, so pins 15 and 16 are not connected.

Check out the following link for ideas on how to make or purchase 16-pin, 1mm ribbon cables that can mate to the ADIS16210/PCBZ.

:ez:`Acquiring 1mm ribbon cables <docs/DOC-2523>`

PHYSICAL SETUP
--------------

Installing the ADIS16210CMLZ onto the Interface board requires two steps:

1. Insert the end of the flex cable (ADIS16210CMLZ) into J2 on the interface board. Check out the video attachment at this link for a demonstration.

:ez:`Click here to see connector seating demonstration <docs/DOC-2672>`

2. Secure the ADIS16210CMLZ base to the Interface PCB, using four M2x0.4mm machine screws

3. Connect J1 to the application processor, using a 16-pin ribbon cable.

USE WITH THE EVAL-ADIS SYSTEM
-----------------------------

Click on the following link to access instructions for using the ADIS16210/PCBZ with the EVAL-ADIS evaluation system:

`ADIS16210 Evaluation on a PC <https://wiki.analog.com/adis16210>`__
