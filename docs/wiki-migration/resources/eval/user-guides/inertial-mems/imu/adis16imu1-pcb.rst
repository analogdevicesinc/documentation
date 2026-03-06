ADIS16IMU1/PCBZ Breakout Board Wiki-Guide
=========================================

OVERVIEW
--------

The ADIS1613x, ADIS1636x, ADIS16375, ADIS1640x, ADIS1648x and ADIS1649x IMU products all use a 24-pin, dual-row, 1mm connector for their electrical interface. The mating connector for their interface supports surface-mount solder attachment but does not support direct attachment with ribbon cables. For those who are would like to connect these IMU and gyroscope products to an existing processor board, using a ribbon cable, the :adi:`ADIS16IMU1/PCB <en/evaluation/eval-adis16imu1/eb.html#buy>` provides a simple connector translation for this purpose.

Here is a picture of the contents that come with the :adi:`ADIS16IMU1/PCB <en/evaluation/eval-adis16imu1/eb.html#buy>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb_kitpic.jpg
   :width: 300px

ORDERING
--------

To order this breakout board, please visit :adi:`the ADIS16IMU1/PCB web site (click here) <en/evaluation/eval-adis16imu1/eb.html#buy>`.

IMU/GYROSCOPE MOUNTING HOLES
----------------------------

The ADIS16IMU1/PCBZ provides several sets of mounting holes that line up with mounting holes and tabs on the following products: ADIS1613x, ADIS1636x, ADIS16375, ADIS1640x ADIS1648x and ADIS1649x products. Please see the following picture for device mounting hole locations.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu1_pcb_basicdimensions.png
   :width: 800px

NOTE: The nominal diameter of the four holes, located in each corner of this PCB, is 3.175mm.

MACHINE SCREWS IMPACT ON LOCAL MAGNETIC FIELDS
----------------------------------------------

The machine screws in the ADIS16IMU1/PCBZ kit are made out of stainless steel, which can have some moderate impact on magnetic fields, local to the IMU. For those whose application demands the best magnetometer performance offered by these IMUs, consider using plastic screws that will not impact the magnetic fields around the devices.

DUT Connection
--------------

ADIS16133, ADIS16135, ADIS1636 Mounting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the M2x0.4x16mm machine screws (provided in pink bag) for mounting these products to the ADIS16IMU1/PCBZ and set their torque for 20 inch-ounces. The yellow-highlights in the top-view picture illustrate the location of the mounting holes for these products.

.. warning::

   **WARNING:** Remove the jumper from **JP1** when using the ADIS16IMU1/PCB to evaluate these products.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb_13x.jpg
   :width: 300px

ADIS16360, ADIS16362, ADIS16364, ADIS16365, ADIS16367, ADIS16400, ADIS16405, ADIS16407 Mounting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the M2x0.4x4mm machine screws (provided in pink bag) for mounting these products to the ADIS16IMU1/PCBZ and set their torque for 20 inch-ounces. The pink-highlights in the top-view picture illustrate the location of the mounting holes for these products. For high-vibration environments, consider using more than 2 screws. :adi:`Application Note AN-1045 <static/imported-files/application_notes/AN-1045.pdf>` offers some ideas on using more than two screws to attach this package style to a system frame.

.. warning::

   **WARNING:** Remove the jumper from **JP1** when using the :adi:`ADIS16IMU1/PCBZ <en/evaluation/eval-adis16imu1/eb.html#buy>` to evaluate these products.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb_36x.jpg
   :width: 300px

ADIS16375, ADIS16480, ADIS16485, ADIS16488 Mounting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the M2x0.4mm machine screws (provided in pink bag) for mounting these products to the :adi:`ADIS16IMU1/PCBZ <en/evaluation/eval-adis16imu1/eb.html#buy>` and set their torque for 20 inch-ounces. The blue-highlights in the top-view picture illustrate the location of the mounting holes for these products.

**Mounting Holes**

The mounting holes are presently tapped for use with M2x0.4mm. While the pre-tapped holes provide convenience in the mounting process, they also constrain the mounting hole location in a manner that can result in a translational force on the electrical connector. This violates one of the "best-practice" criteria in the product datasheets and can impact key bias stability behaviors. For those who want to preserve best performance, open the diameter of these holes to 2.85mm and use a washer/nut combination on the backside of the interface board to secure the ADIS1648x to its surface.

:ez:`Click here to see learn more about "best-practices" in mounting the ADIS1648x <mems/w/documents/4440/faq-adis1648x-mounting-tips>`

Here is an example of the ADIS16IMU1/PCBZ, with an ADIS16485AMLZ mounted to it.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16488-pcb-web.jpg
   :width: 300px

Make sure that the connector pins are in alignment with J2 on the :adi:`ADIS16IMU1/PCBZ <en/evaluation/eval-adis16imu1/eb.html#buy>`, before pressing it into place.

Here is a close-up view, which shows the

.. container:: em

   correct connector alignment


.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-02b.jpg
   :width: 300px

This picture provides an example of the an

.. container:: em

   incorrect connector alignment


. Note that this view is on the EVAL-ADISZ board, not the :adi:`ADIS16IMU1/PCBZ <en/evaluation/eval-adis16imu1/eb.html#buy>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-03.jpg
   :width: 300px

ADIS16490, ADIS16495, ADIS16497 Mounting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

STEP #1
^^^^^^^

Using the silk screen as a guideline for where to start (silk variation may result in some misalignment with the ADIS1649x's package edge), set the ADIS1649x on the :adi:`ADIS16IMU1/PCBZ <en/evaluation/eval-adis16imu1/eb.html#buy>`. Make sure that the ADIS1649x's connector aligns with J2 on the :adi:`ADIS16IMU1/PCBZ <en/evaluation/eval-adis16imu1/eb.html#buy>` before pressing it in (Step #2)

|image1| |image2| |image3|

STEP #2
^^^^^^^

Verify the alignment with J2 and then gently press the ADIS1649x into J2. Here is a picture of what this looks like, when the ADIS1649x has proper insertion alignment into J2.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_003c.jpg
   :width: 430px

Here are two examples of

.. container:: em

   incorrect


insertion alignment.

|image4| |image5|

STEP #3
^^^^^^^

Secure the ADIS1649x to the :adi:`ADIS16IMU1/PCBZ <en/evaluation/eval-adis16imu1/eb.html#buy>` using M2 hardware (machine screws, washers and nuts). Note that early versions of the :adi:`ADIS16IMU1/PCBZ <en/evaluation/eval-adis16imu1/eb.html#buy>` include tapped holes that would support M2x0.4mm machine screws. Variation in hole location in standard PCB processing made it difficult to support this process economically, so newer boards have holes that have a diameter of 2.85mm. For best performance, use the same torque for all four machine screws (20 inch-ounces used in ADIS1649x qualification).

STEP #4
^^^^^^^

Secure the 16-pin, 1mm ribbon cable to J1 and use that to connect to an embedded processor board or to the evaluation system (:adi:`eval-adis2`). The following two pictures illustrate

.. container:: em

   correct


insertion alignment between the ribbon cable and J1.

|image6| |image7|

The following two pictures illustrate

.. container:: em

   incorrect


insertion alignment between the ribbon cable and J1.

|image8| |image9| |image10|

STEP #5
^^^^^^^

When connecting the other end of the ribbon cable to an embedded processor board, take note of the pin 1 location for J1, using the following picture:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_004c.jpg
   :width: 430px

JP1 Settings by DUT Model
-------------------------

JP1 controls the power supply to the VDDRTC function on the ADIS16375 and all parts in the ADIS1648x family, including the ADIS16485 and ADIS16488A. For all other products, do not install JP1.

Please use the following table to determine how to use JP1 on the ADIS16IMU1/PCBZ.

================ ==============
DUT MODEL NUMBER JP1 INSTALLED?
================ ==============
ADIS16133        NO
ADIS16135        NO
ADIS16136        NO
ADIS16137        NO
ADIS16360        NO
ADIS16362        NO
ADIS16364        NO
ADIS16365        NO
ADIS16367        NO
ADIS16400        NO
ADIS16405        NO
ADIS16407        NO
ADIS16375        YES
ADIS16480        YES
ADIS16485        YES
ADIS16488        YES
ADIS16488A       YES
ADIS16490        NO
ADIS16495        NO
ADIS16497        NO
================ ==============

CONNECTING TO THE EVAL-ADIS2
----------------------------

This can also connect to J1 on the EVAL-ADIS2

|image11| |image12|

INTERFACE CONNECTOR
-------------------

J1 is the electrical connector that provides direct access to power, ground and critical digital I/O pins on the devices. It is a 16-pin, dual-row, 2-mm pitch connector.

Pin Assignments
~~~~~~~~~~~~~~~

Here are the pin assignments for J1, which is the connector that will interface with an embedded processor board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb-j1-connector.png
   :width: 200px

Ribbon Cable Options
~~~~~~~~~~~~~~~~~~~~

Check out the `TCSD series <https://www.samtec.com/products/tcsd>`__ from `Samtec <https://www.samtec.com>`__, to purchase ribbon cable assemblies, which will mate to J1, on the :adi:`\|ADIS16IMU1/PCB <EVAL-adis16imu1>` and the :adi:`EVAL-ADIS2`.

ELECTRICAL SCHEMATIC
--------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb-schematic.png
   :width: 400px

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_002c.jpg
   :width: 270px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_000c.jpg
   :width: 240px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_001c.jpg
   :width: 310px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_003ac.jpg
   :width: 430px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_003bc.jpg
   :width: 410px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_005c.jpg
   :width: 420px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_006c.jpg
   :width: 360px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_007c.jpg
   :width: 290px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_008c.jpg
   :width: 270px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_wikiguide_bb_009c.jpg
   :width: 270px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_imu1_web_00.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis2_imu1_web_01.png
   :width: 400px
