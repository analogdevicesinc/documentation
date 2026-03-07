RapidNet IP Slave Mode Userguide
================================

RapidNet IP software protocol supports two modes- master mode and slave mode.

Master mode
-----------

The RapidNet module is used as primary MCU for application purposes and also used to communicate using RapidNet IP.

.. important::

   Even though the module software is open to customers, the RapidNet IP protocol stack is still a black box.


   |image1|

Slave mode
----------

The RapidNet module is used as a comms pipe by a different MCU which is primarily uised for application purposes. The application's MCU (apps MCU) is expected to use certain APIs over UART in order to communicate over RapidNet IP.


|image2|

UART interface
~~~~~~~~~~~~~~

The rfmodule project provided with the RapidNet software package is the default firmware to be programmed to the RapidNet module. It provides several configurable UART parameters such as baudrate, parity, data, stop bits, etc.

.. note::

   By default, the rfmodule firmware supports a baudrate of 460800, data of 8 bits, 1 stop bit, and no parity


Apps MCU program flow
~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/slave_mode_app_flow.png
   :align: center
   :width: 400px

Configuration APIs
^^^^^^^^^^^^^^^^^^

RF Module stack parameter configurations and stack initialization can be controlled from Apps MCU through RFM commands. Some basic configuration commands are-

-  RFMODULE_SET_PARAMS_REQ- used to set RF module parameters such as network PANID, TX power, datarate.
-  RFMODULE_SET_KEY_REQ- used to set the network key for the node.
-  RFMODULE_CONFIG_NETWORK_REQ- used to set the network parameters such as node type (LBR/LN /AP), mode (master/slave), etc.
-  RFMODULE_START_NETWORK_REQ- This command starts the network for RF modules configured as 6AP and 6LN i.e the nodes will search for a gateway (LBR) to join.

.. important::

   The RapidNet module needs to be reconfigured on reset when last used in slave mode.


Slave mode APIs
^^^^^^^^^^^^^^^

These APIs allow the RapidNet module to be used as a comms pipe by the Apps MCU. Some basic APIs are-

-  RFMODULE_SEND_REQ- used to transmit data to the gateway
-  RFMODULE_DATA_IND- used to indicate to apps MCU that data has been received from the gateway
-  RFMODULE_GOTO_SLEEP_REQ- used to put the RF Module into sleep mode.
-  RFMODULE_WAKEUP_CONF- used to indicate to the apps MCU that the module wakeup was successful. Apps MCU wakes the module by providing an external interrupt via SYS-WAKE3 on the RapidNet module.

.. note::

   Host MCU should put the RapidNet module to sleep whenever there are no packets to be sent.


Packet format
^^^^^^^^^^^^^

|image3|

.. note::

   The full list of configuration/slave mode APIs with details of command ID, data and expected response can be found in the RapidNet API guide.


Example - CONFIGURING THE RF MODULE PARAMETERS
""""""""""""""""""""""""""""""""""""""""""""""

The device PAN ID, PHY data rate, and transmit power can be set using a single command as shown below

-  PAN ID: 0x3344
-  PHY data rate: 50 Kbps
-  Transmit power: 12 dBm

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/sm_example_1.png
   :align: center

Example - SENDING DATA REQUEST COMMAND
""""""""""""""""""""""""""""""""""""""

The format and parameters to send data request command to the RF Module to start device as RapidNet IP node is shown below.


|image4|

Sample Slave mode application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A sample slave mode application is provided in the RapidNet software package, it uses the ADuCM3029 as it’s Apps MCU and the source code can be found in the path- \\RapidNet-IP-Rel1.1.2\\Tools\\sample_host_apps\\

Sample application flow
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/slave_mode_sample_app_flow.png
   :align: center

Application summary
^^^^^^^^^^^^^^^^^^^

-  The sample application sets the network parameters of the connected RapidNet module, configures it to be a node (LN) in slave mode and starts network using commands mentioned in the configuration APIs section.
-  It then puts the node to sleep and toggles the GPIO acting as external wakeup after a set interval.
-  It transmits a packet of data (1KB) to the gateway and waits to receive an acknowledgement. If acknowledgement is not received within a set interval, the packet is retransmitted.
-  Steps 2 and 3 repeat indefinetly

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/master_mode_block_diagram.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/slave_mode_block_diagram.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/sm_packet_format.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/sm_example_2.png
