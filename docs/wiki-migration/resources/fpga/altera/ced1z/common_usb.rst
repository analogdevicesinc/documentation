The USB Blaster is used to program the FPGA on the CED1Z board and also for data exchange between the system and a PC. To install the driver plug the Terasic USB Blaster into one of the PCs USB ports. Your Windows PC will find the new hardware and try to install the driver.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image007.png
   :alt: image007.png
   :align: center
   :width: 350px

Since Windows cannot locate the driver for the device the automatic installation will fail and the driver has to be installed manually. In the *Device Manager* right click on the **USB-Blaster** device and select **Update Driver Software**.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image009.png
   :alt: image009.png
   :align: center
   :width: 700px

In the next dialog box select the option **Browse my computer for driver software**. A new dialog will open where it is possible to point to the driver’s location. Set the location to **altera\\11.0\\quartus\\drivers\\usb-blaster** and press **Next**.

|image011.png|\ |image013.png|


.. tip::

   If Windows presents you with a message that the drivers have not passed Windows Logo testing, please click “\ **Install this driver software anyway**\ ”. Upon installation completion a message will be displayed to inform that the installation is finished.


|image017.png|\ |image016.jpg|

.. |image011.png| image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image011.png
   :width: 400px
.. |image013.png| image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image013.png
   :width: 400px
.. |image017.png| image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image017.png
   :width: 400px
.. |image016.jpg| image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image016.jpg
   :width: 400px
