ADIS16IMU2/PCBZ Breakout Board Wiki-Guide
=========================================

GENERAL DESCRIPTION
-------------------

The ADIS16IMU2/PCBZ is a breakout board that provides the ability to connect with the following products, using a standard ribbon cable (16-pin, 1mm pitch): :adi:`ADIS16334`, :adi:`ADIS16362`, :adi:`ADIS16364`, :adi:`ADIS16365`, :adi:`ADIS16367`, :adi:`ADIS16405`, :adi:`ADIS16407`, :adi:`ADIS16445`. This breakout board simplifies connection to an embedded processor system, early in the development cycle and also connects this products to the :adi:`EVAL-ADIS-FX3` or EVAL-ADIS2 (obsolete) evaluation systems.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wiki_pcb_00.jpg
   :width: 200px

SETUP WITH ADIS1633X/44X IMUS
-----------------------------

Connecting the IMU (ADIS16334, ADIS16445 or ADIS16448), ADIS1644X/FLEX and ADIS16IMU2 together is a very simple two-step process. Please note that the pin numbers markings on the ADIS1644X/FLEX were incorrect in early manufacturing lots. Please ignore the pin number markings on the ADIS1644X/FLEX and use the following instructions to guide the connection process.

Step 1: ADIS16xxx (IMU) to ADIS1644X/FLEX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following diagram illustrates the two different connectors on ADIS1644X/FLEX, along with their connections:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wiki_adis1644x_flex_02.png
   :width: 500px

The following diagram shows the IMU's interface connector, which the ADIS1644X/FLEX connects with:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wiki_adis16448.png
   :width: 500px

The following table shows the correct insertion, along with the three most common incorrect ways to insert the flex onto the IMU's interface connector

======== ==============
TOP VIEW CONNECTOR VIEW
======== ==============
|image1| |image2|
|image3| |image4|
|image5| |image6|
|image7| |image8|
======== ==============

Step 2: ADIS1644X/FLEX to ADIS16IMU2/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADIS1644X/FLEX has 20 pins, while J2 on the ADIS16IMU2/PCBZ has 24-pins. Connect the flex to pins 1 through 20 on J2. Pin numbers 1, 2, 23 and 24 are clearly identified on the silk screen, which is associated with J2 on the ADIS16IMU2/PCBZ. The following pictures illustrate the correct insertion alignment for this connection

======== ========= =========
|image9| |image10| |image11|
======== ========= =========

Here is an example of what this will look like, after finishing these steps:


|image12|

SETUP WITH ADIS1636x/40X IMUs
-----------------------------

Connecting any of the ADIS1636x or ADIS1640x IMU products is very simple, as J2 mates perfectly with the interface connect on these products. Click on any of the images to below for larger views.

========= =========
|image13| |image14|  
========= =========

========= =========
|image15| |image16|
========= =========

For more information on proper handling of the ADIS1636x and ADIS1640x packages, please consult :adi:`AN-1045 <media/en/technical-documentation/application-notes/AN-1045.pdf>`

KEY PHYSICAL DIMENSIONS
-----------------------

Please see the following diagram for dimensions of all key physical attributes:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_pcb_dimensions.png
   :width: 300px

INTERFACE CONNECTOR
-------------------

J1 is the electrical connector that provides direct access to power, ground and critical digital I/O pins on the devices. It is a 16-pin, dual-row, 2-mm pitch connector that support 1mm ribbon cable systems.

Pin Assignments
^^^^^^^^^^^^^^^

Here is the pin assignments for J1, which is the connector that will interface with an embedded processor board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb-j1-connector.png
   :width: 200px

Ribbon Cable Options
^^^^^^^^^^^^^^^^^^^^

Check out the following link for ideas on how to make or purchase 16-pin, 1mm ribbon cables that can mate to the ADIS16IMU2/PCBZ.

:ez:`Acquiring 1mm ribbon cables <docs/DOC-2523>`

ELECTRICAL SCHEMATIC
--------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb-schematic.png
   :width: 400px

SUPPORT
-------

If you have any questions in using this evaluation tool, please visit the Inertial MEMS Community, inside of the :ez:`Inertial MEMS Sesnor Community <community/mems>` EngineerZone. If you are unable to find an answer to your question through the search tools in this forum, please feel free to post a new question. As always, the quality of detail in the original request will relate to the quality of the support that forum can provide. We thank you for your business and look forward to seeing what you create with this technology!

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis16448_to_flex_01.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis16448_to_flex_05.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis16448_to_flex_02.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis16448_to_flex_06.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis16448_to_flex_03.png
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis16448_to_flex_07.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis16448_to_flex_04.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis16448_to_flex_08.png
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wiki_install_insertion_00.jpg
   :width: 230px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wiki_install_insertion_01.jpg
   :width: 320px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wiki_install_insertion_02.jpg
   :width: 300px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wiki_functional_00.jpg
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis1640x_install_00.png
   :width: 360px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis1640x_install_01.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis1640x_install_02.png
   :width: 440px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu2_wikiguide_adis1640x_install_04.png
   :width: 400px
