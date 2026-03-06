SDMP-TEMP
=========

Thermocouple
------------

SDMP-TEMP Evaluation Platform
-----------------------------

Arduino Shield
~~~~~~~~~~~~~~

mbed Board
~~~~~~~~~~

A few hardware modifications need to be made to the STNucleo board before the shield can be plugged into it. Since the shield uses D0/D1 pins for UART communication with the baseboard, these pins need to be enabled by soldering the SB62 and SB63 solder bridges shown in the picture below.


|image1|

Soldering these bridges will enable the board to shield communication via UART. However the USB connector uses the same pins, therefore we must disconnect the USB from the default serial interface. Desoldering SB14 and SB13 will disconnect achieve this.


|image2|

USB communication with the PC is required to read back data from the shield, therefore we must reroute the USB to another serial interface of the mbed board. Connect D3 to CN3-Rx and D8 to CN3-Tx (the Serial1 interface of the mbed board)


|image3|

Design Files
~~~~~~~~~~~~

.. |image1| image:: https://wiki.analog.com/_media/resources/technical-guides/img_20160630_162735.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/technical-guides/img_20160630_162744.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/technical-guides/img_20160630_163337.jpg
   :width: 600px
