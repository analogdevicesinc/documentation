Auto Configuration of Network
=============================

A complete A2B network can be configured using the information stored in a memory device that is directly connected to the Host processor via I2C. Such memory device shall use device address 0x50 (7-bit) and accessible directly to the Host processor over I2C. Upon boot, the host processor can read this information to automatically configure the complete A2B network i.e., main and sub-node A2B Transceivers, network and sub-node peripheral devices without any prior knowledge of the network.

.. note::

   The Auto configuration of Network .dat file can also be exported using Thrift Automation. For more information, refer to “\ :doc:`Export A2B Auto Configuration Files Using Thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.”


Storing Network Configuration
-----------------------------

In SigmaStudio+, one can store the network configuration information into a memory device by saving the Schematic into an EEPROM connected to ECU. This can be done by right clicking the master node. It also can be access from the project window.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ **Figure:** Saving Schematic to EEPROM


Also, there is a provision to export the information into an XML/ Dat file as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`. These files can be input to custom EEPROM programming utilities, specifically .dat file can be converted to hex/.s37 format for ease of flashing.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   \ **Figure:** Schematic Dump as XML


Loading Network Configuration
-----------------------------

Alternatively, network wide configuration can be sourced to target software from .dat file via the local file system. Refer :doc:`adi_a2b_busconfig.dat </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>` section for more details. (.dat file from EEPROM window and adi_a2b_busconfig.dat file is essentially same)

The Stream information of A2B network is exported to binary file/EEPROM if ‘Include Stream info to dat file’ checkbox is enabled. Stream Information of A2B network is stored in the EEPROM/binary file as shown below.

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   \ **Figure:** A2B Network Stream Information Schematic for EEPROM/DAT File


In EEPROM/Binary file 6th byte (EEPROM Byte Address is 0x05) indicates that the Stream information is exported if the value is 0x01. Addresses mentioned in the Stream Information :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>` are just for representation and they are not the actual address. Stream information address would be defined by the value at 0x18 (MSB) and 0x19 (LSB) in EEPROM/Binary (DAT) File.

For optimized discovery flow, configure the A2B stack to program the peripherals in multiple jobs instead of serial peripheral processing. This can be done by setting the macro ‘A2B_CONSECUTIVE_PERIPHERAL_CFGBLOCKS’ to a non-zero value in case of EEPROM usage.

Custom Node Information
-----------------------

The Custom Node Information is stored in .DAT in the format specified in below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`.

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   \ **Figure:** A2B Network Custom Node Information for EEPROM/DAT File


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/save_schematic_eeprom.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/schematic_dump_as_xml.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/a2b_network_stream_information_schematic_for_eeprom_dat_file.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/l5updated.png
