.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/app_interface.png
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/evb_connection_diagram.png
   :align: center
   :width: 400px

IIO oscilloscope is used as client application running on Windows-os, which is ADI developed GUI for ADC data visualization and device debug. The interface used for communicating client application with firmware application (IIO device) is UART (Note: SDP-K1 can also support high speed VirtualCOM port @1Mbps or higher speed for faster data transmission). The firmware application communicates with IIO device using ADI No-OS drivers and platform drivers low level software layers. SDP-K1 is used as controller board, on which IIO firmware application runs and using above software libraries, the IIO firmware communicates with IIO device.

.. image:: https://wiki.analog.com/_media/section>/resources/tools-software/product-support-software/mbed_support_board_message#Getting Started&showfooter=nofooter
   :alt: section>/resources/tools-software/product-support-software/mbed_support_board_message#Getting Started&showfooter=nofooter
