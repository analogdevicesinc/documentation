For data transmission to IIO client, VirtualCOM Or UART serial communication is used. SDP-K1 by default uses the VCOM serial interface for higher speed data transmission.

SDP-K1 is powered through USB connections from the computer. SDP-K1 acts as a Serial device when connected to PC, which creates a COM Port to connect to IIO Oscilloscope GUI running on windows-os. The COM port assigned to a device can be seen through the device manager for windows-based OS.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_assigned_com_port.png
   :align: center
   :width: 600px

SDP-K1 can support high speed VirtualCOM port USB interface, so by default VCOM is configured as default interface in the firmware. The interface can be set to UART by defining macro “USE_PHY_COM_PORT” in the app_config.h file.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_phy_and_virtual_com.png
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_vir_com_port.png
   :align: center
   :width: 600px

*<fc #ff0000>*Note: Actual COM port number for your device may not be the same as shown above. Therefore, always check your SDP-K1 serial COM port number before connecting to IIO client.</fc>*
