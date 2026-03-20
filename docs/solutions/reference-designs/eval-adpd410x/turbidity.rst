-----------------------------------------------------------------------------------------------------------------------------====== EVAL-ADPD410X-ARDZ Turbidity Measurement Demo ====== The :adi:`EVAL-ADPD410x-ARDZ` allows users to take advantage of the flexibility of the :adi:`ADPD4100` and :adi:`ADPD4101` as multimodal sensor front ends to a wide range of applications. One example of a specialized application is the :adi:`CN0409`, a reference design for turbidity measurement. This demonstration shows how to measure turbidity using a similar method, but using the :adi:`EVAL-ADPD410x-ARDZ`.

General Description/Overview
============================

The International Organization for Standardization (ISO) developed a design standard known as ISO 7027 Water Quality—Determination of Turbidity, which is best known for its requirement of a monochromatic light source. Most instruments that comply with this standard use an 860 nm LED light source and a primary detector at an angle of 90°. Additional detection angles are allowed, such as a detector at an angle of 180°, to increase the range of measurable turbidity levels.

The demo uses a network of 860 nm infrared emitters and silicon PIN photodiodes
to achieve a water turbidity measurement system. The system can measure low to
high water turbidity levels ranging from 0 FTU to 1000 FTU.

Demo Requirements
=================

The following is a list of items needed to replicate this demo:

-  :adi:`EVAL-ADPD410x-ARDZ`
-  :adi:`EVAL-ADICUP3029` with firmware (see Firmware Setup)
-  Host computer with PyADI-IIO and relevant dependencies installed (See :doc:`EVAL-ADPD410X-ARDZ Python Example </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`)
-  `Type 1FLP Disposable Macro Cuvettes UV Plastic (Lightpath: 10 mm) <https://www.fireflysci.com/disposable-fluorescence-cells/type-1flp-disposable-macro-cuvettes-lightpath-10 mm>`_
-  `QED-123 Infrared LED <https://www.digikey.com/en/products/detail/on-semiconductor/QED123/187398>`_
-  2 x `QSD123 Infrared Photo Transistor <https://www.digikey.com/en/products/detail/onsemi/QSD123/187443>`_
-  2 x `18-pin Single Row Female Headers <https://www.digikey.com/en/products/detail/samtec-inc/SSQ-118-03-F-S/6692999>`_
-  4 x `6-pin Single Row Female Headers <https://www.digikey.ph/en/products/detail/samtec-inc/SSQ-106-03-F-S/6678741>`_
-  6 x Female-to-Female Jumper Headers for Connection
-  (**Optional**) Samples with known turbidity concentration

Setting up the EVAL-ADPD410X-ARDZ
=================================

| Configure the onboard jumper header and solder jumper connections, as shown below.
| |image1|

========== ======================= =========
**Header** **Setting**             **Image**
========== ======================= =========
P10        No connection

|image2|

JP1        Shorted Pin 2 and Pin 3

|image3|

IOSEL      Shorted Pin 1 and 2

|image4|

========== ======================= =========

Set the following :adi:`EVAL-ADICUP3029` switches according to their configuration on the table below.

========== =====================
**Switch** \**Configuration**
========== =====================
UART (S2)  USB
POWER (S5) WALL/USB
========== =====================

| Connect the :adi:`EVAL-ADPD410x-ARDZ` to the :adi:`EVAL-ADICUP3029` using the headers, as shown below.
| |image5|

Firmware Setup
==============

Connect the :adi:`EVAL-ADICUP3029` to the PC using the micro USB to USB cable. Drag and drop the appropriate .hex file from the list below to the Daplink Drive. (See :doc:`-firmware-setup </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`)

.. admonition:: Download
   :class: download

   
   Pre-built hex files can be found here:
   
   -  `EVAL-ADPD4100-ARDZ .Hex File (ADuCM3029_demo_adpd410x_spi_waterquality.hex) <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_adpd410x_spi_waterquality.hex>`_
   -  `EVAL-ADPD4101-ARDZ .Hex File (ADuCM3029_demo_adpd410x_i2c_waterquality.hex) <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_adpd410x_i2c_waterquality.hex>`_
   
   The latest source code can be found here:
   
   -  :git-EVAL-ADICUP3029:`EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_adpd410x <projects/ADuCM3029_demo_adpd410x>`
   

DIY Test Board Setup
====================

To set up the optical path, use the prototype board that comes in the box with the :adi:`EVAL-ADPD410x-ARDZ` as a base. The connection diagram for the QED123 LED and the two QSD123 is shown below:

.. image:: images/turbidity-connectiondiagram.png
   :width: 600

-  To connect to the :adi:`EVAL-ADPD410x-ARDZ`, solder the two 18-pin single row female headers at the bottom sides of the prototype board.
-  Solder the four 6-pin female headers enclosing a 5 x 5 pad space as a DIY cuvette holder.
-  Solder the LEDs and photodiodes at 3 adjacent sides of the cuvette holder and directed inward. A photo of a completed test board setup mounted on the :adi:`EVAL-ADPD410X-ARDZ` and the :adi:`EVAL-ADICUP3029` is shown below using Female-to-Female headers for connection.

.. image:: images/img_20220720_150406.jpg
   :width: 600

You can place a sample placed in a cuvette to the square space at the center, as
shown below.

.. image:: images/img_20220722_130556.jpg
   :width: 600

Software Setup
==============

This demo uses a PyADI-IIO example script. See :doc:`Software Setup </solutions/reference-designs/eval-adpd410x/eval-adpd410x>` for the complete installation instructions from libiio to pyadi-iio.

-  Connect the :adi:`EVAL-ADPD410x-ARDZ` to the :adi:`EVAL-ADICUP3029`.
-  Connect the :adi:`EVAL-ADICUP3029` to the PC using the micro USB cable and note the serial port from the Device Manager as in :doc:`Connection </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.
-  Open command prompt or terminal and navigate through the examples folder inside the downloaded or cloned *pyadi-iio* directory.
-  Run the example script using the command. ``...\pyadi-iio\examples>python adpd410x_demo.py``
-  The script will ask for a serial port. Input the noted serial port and press Enter. In cases when the board is not found, press the reset button (S1) on the :adi:`EVAL-ADPD410x-ARDZ` and input the noted serial port again.

|image6|

-  When the board is detected, you will be asked to specify the demo application
   to use. Since this setup is only applicable for turbidity measurements, enter
   3.

|image7|

-  A plot will appear showing the measured and computed turbidity in FTU. You
   have the option to save a copy of the displayed waveform at any point in time
   using the matplotlib controls at the top. Remove the cuvette and replace the
   sample with a different turbidity to observe the measurement change.
   **Low Turbidity Sample**

   |image8|

   **High Turbidity Sample**

   |image9|

.. important::

   The measurements obtained have not been tested and verified with the actual
   turbidity measurement, and is not expected to be accurate. The demo showcases
   a proof-of-concept DIY setup for turbidity measurement, which users can tweak
   and improve upon.

.. important::

   The demo script uses the same approximation used in `Linear Approximation using 3-Point Calibration <https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0503/turbidity>`_.

Reference Links
===============

-  :doc:`Hardware User Guide </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`

.. |image1| image:: images/fl_adpd410x_jumperconn.jpg
   :width: 400
.. |image2| image:: images/p10_empty.png
   :width: 200
.. |image3| image:: images/jp1_5v.png
   :width: 200
.. |image4| image:: images/iosel_shunt.png
   :width: 200
.. |image5| image:: images/arduinoconnection.jpg
   :width: 400
.. |image6| image:: images/pyadiiio_example2_comport.png
   :width: 400
.. |image7| image:: images/demo_selectapplication.png
   :width: 400
.. |image8| image:: images/screenshot_2022-07-22_133951.png
   :width: 400
.. |image9| image:: images/screenshot_2022-07-22_133731.png
   :width: 400
