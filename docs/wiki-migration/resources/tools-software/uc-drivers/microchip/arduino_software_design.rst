This section presents the steps for developing a chipKIT application that will run on the **Digilent Cerebot MX3cK** development board for controlling and monitoring the operation of the **ADI** part.

-  Under your **Sketchbook** directory create a folder called "Libraries"; this folder may already exist.
-  Unzip the downloaded file in the libraries folder.
-  Run the **MPIDE** environment.
-  You should see the new library under **Sketch->Import Library**, under **Contributed**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/arduino_software_design_1.png
   :align: center

-  Also you should see under **File->Examples** the demo project for the ADI library.
-  Select the ADIDriver example.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/arduino_software_design_2.png
   :align: center

-  Select the **Cerebot MX3cK** board from **Tools->Board**.
-  Select the corresponding Serial Communication Port from **Tools->Serial Port**
-  The project is ready to be uploaded on the development board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/microchip/arduino_software_design_3.png
   :align: center
