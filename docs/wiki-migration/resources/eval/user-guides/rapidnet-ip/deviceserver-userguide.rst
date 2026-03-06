RapidNet IP DeviceServer Userguide
==================================

DeviceServer
------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/gateway.png
   :align: center
   :width: 400px

::

                          RapidNet IP gateway bloack diagram

RapidNet IP allows gateway applications to communicate with the network through the deviceServer.

Starting the deviceServer
~~~~~~~~~~~~~~~~~~~~~~~~~

Required files - deviceServer executable and deviceServer_config.ini

-  Windows- The required files can be found in \\RapidNet-IP-Rel1.1.2\\Tools\\RapidNet-IP-Demo_App\\config
-  Linux (Raspberry Pi) - The required files can be found in \\RapidNet-IP-Rel1.1.2\\Manager\\deviceServer\\RaspberryPi

Steps-

-  Create a folder named "config" in the same directory as the deviceServer executable
-  Place deviceServer_config.ini in the "config" folder
-  Run the deviceServer executable via command prompt/terminal

.. note::

   Instructions to run the deviceServer-

   
   Windows
   
   -  Open a command prompt in the same directory as deviceServer.exe
   -  Type "deviceServer.exe" in the commandline and press the Enter key.
   
   Linux
   
   -  Open a terminal window in the same directory as deviceServer
   -  Type the following commands and press the Enter key after each-
   
      -  sudo chmod 555 deviceServer
   
         -  sudo ./deviceServer –v
   


Configuring the deviceServer/LBR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The deviceServer_config.ini file defines the runtime configuration for the deviceServer/LBR, such as-

-  LBR communication parameters such as COM port, baud rate
-  RapidNet network parameters such as PAN ID, ISM band, datarate
-  Debug preferences

Message queues
~~~~~~~~~~~~~~

The gateway application is required to send and receive packets via message queues provided by the host operating system. The message queue names used by the deviceServer are defined in deviceServer_config.ini –

-  ds_rxq_name=/rfm_host_app_rxq #Message queue used by deviceServer to receive messages from app.
-  ds_txq_name=/rfm_host_app_txq #Message queue used by deviceServer to transmit messages to app.

.. important::

   Ensure that message queuing is enabled in the operating system being used

   
   -  It may be enabled by default for linux systems
   -  It is disabled by default for windows systems. Please find instructions on how to enable it on page 6 of the Sensor integration guide (available in the path \\RapidNet-IP-Rel1.1.2\\Docs)
   


Gateway application
-------------------

Gateway application flow
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/gw_app_flow.png
   :align: center
   :width: 400px

deviceServer APIs
~~~~~~~~~~~~~~~~~

The RapidNet API guide provides a list of APIs to be used by gateway applications by exchanging request/response packets with the deviceServer. Some important APIs are-

-  DS_UPDATE_LN_DATA_REQ – send data to one or multiple nodes in the network.
-  DS_ADD_LN_PREFERRED_PARENT_REQ – set the preferred parent node for one or more nodes in the network.
-  DS_GET_REGISTERED_LN_LIST_REQ - get the list of registered Motes
-  DS_LBR_NWK_READY_IND – indication given by the deviceServer when the network has been started successfully
-  DS_LN_REG_IND – indication given by the deviceServer when a node registers with the network
-  DS_LN_APP_DATA_IND – indication given by the deviceServer when application data is received from a node

Packet format
^^^^^^^^^^^^^

|image1| Where,

-  MID – request/confirmation message ID
-  ML – message length in bytes (including ML and MID)
-  Message data – message data based on MID

The full list of APIs with details of MID, message data and expected response can be found in the RapidNet API guide.

Example - Requesting current state of a node from the deviceServer
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

-  The DS_GET_LN_STATE_REQ API is used to request the current state of a node.
-  Send a DS_GET_LN_STATE_REQ to the deviceServer by writing the packet from below figure into the RX message queue of the deviceServer (ds_rxq_name)
-  After performing necessary operations, the deviceServer responds with a DS_GET_LN_STATE_CONF which should be read from the TX message queue of the deviceServer (ds_txq_name)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/ds_example_pf_1.png
   :align: center
   :width: 400px

::

                                               Example DS_GET_LN_STATE_REQ packet

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/ds_example_pf_2.png
   :align: center
   :width: 400px

::

                                               Example DS_GET_LN_STATE_CONF packet

Example applications
~~~~~~~~~~~~~~~~~~~~

Example applications are provided for the linux operating system in the RapidNet software package, they can be found in the path- \\RapidNet-IP-Rel1.1.2\\Manager\\application\\appsOnLinux\\

Example1
^^^^^^^^

Example application uses the DS_ADD_LN_LIST_REQ, DS_ADD_AP_LIST_REQ and DS_ADD_LN_PREFERRED_PARENT_REQ commands to add a list of LNs, APs and set the preferred parents for the list of LNs. It then uses the DS_UPDATE_LN_DATA_REQ command to send data to the list of nodes periodically.

Example2_OTA_FU
^^^^^^^^^^^^^^^

Example application uses the DS_OTA_FU_FOR_LN_REQ API to update the firmware for a hardcoded list of end nodes.

Example3_actions_commands
^^^^^^^^^^^^^^^^^^^^^^^^^

Example application provides code snippets to test various APIs such as-

-  DS_SET_LBR_CHANNEL_HOPPING_MASK_REQ
-  DS_OTA_SET_LN_PARAMS_REQ
-  DS_SET_LBR_RTC_TIME_REQ
-  DS_GET_LBR_RTC_TIME_REQ
-  DS_GET_LBR_PARAMS_REQ
-  DS_GET_REGISTERED_LN_LIST_REQ
-  DS_SET_LBR_FACTORY_DEFAULT_REQ
-  DS_RESET_LBR_REQ
-  DS_GET_AP_LIST_REQ
-  DS_OTA_GET_LN_PARAMS_REQ
-  DS_OTA_RESET_LN_REQ
-  DS_GET_LN_STATE_REQ
-  DS_GET_LN_STATS_REQ
-  DS_GET_LN_FW_VERSION_REQ

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/ds_packet_format.png
   :width: 400px
