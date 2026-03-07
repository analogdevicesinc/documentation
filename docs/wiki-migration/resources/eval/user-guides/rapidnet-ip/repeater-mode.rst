RapidNet IP Repeater Userguide
==============================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/1.png
   :width: 400px

RapidNet IP device types
------------------------

RapidNet modules can be configures as a-

-  Host/6LoWPAN border router (6LBR) – device used by the gateway to start and manage RapidNet network.
-  Mote/6LoWPAN node (6LN) – device acting as end nodes sending/receiving data to/from the gateway.
-  Repeater/ Access point (6AP) - device used to improve the signal range and strength of a RapidNet network.

This guide describes the steps to configure and use a RapidNet module as a repeater.

Configuration APIs
------------------

RF Module stack parameter configurations and stack initialization is a one-time configuration that needs to be performed via configuration APIs over UART. The basic configuration APIs are-

-  RFMODULE_SET_PARAMS_REQ- used to set RF module parameters such as network PANID, TX power, datarate.
-  RFMODULE_SET_KEY_REQ- used to set the network key for the node.
-  RFMODULE_CONFIG_NETWORK_REQ- used to set the module configuration such as node type (6LBR/6LN/6AP), mode (master/slave), etc.
-  RFMODULE_START_NETWORK_REQ- This command starts the network for RF modules configured as 6AP and 6LN i.e the nodes will search for a gateway (6LBR) to join.

Repeater flow
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/ap_app_flow.png
   :align: center
   :width: 400px

Packet format
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/sm_packet_format.png

deviceServer APIs
-----------------

Once a module has been configured as a repeater, it joins the RapidNet network and can be used by nodes outside the range of the gateway to join the network. The deviceServer provides gateway applications certain APIs relevant to access points-

-  DS_ADD_LN_PREFERRED_PARENT_REQ – used to force a node to prefer a certain access point to join the network.
-  DS_GET_AP_LIST_REQ - used to get the list of joined APs

.. important::

   
   -  Note that DS_ADD_LN_PREFERRED_PARENT_REQ needs to be sent before a node joins the network.
   -  Please see the :doc:`RapidNet IP DeviceServer Userguide </wiki-migration/resources/eval/user-guides/rapidnet-ip/deviceserver-userguide>` for more information on using the deviceServer and it's APIs.
   -  The full list of configuration/deviceServer APIs with details of command ID, data and expected response can be found in the RapidNet API guide.
   

