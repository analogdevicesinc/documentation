JESD204B Status Utility
=======================

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/jesd_status.png
   :align: center
   :width: 600px

The jesd_status utility is in some sense similar to the :doc:`JESD204B Eye Scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>` application. It currently doesn't support EYE SCAN, but can show all the link and lane status information, similar to the :doc:`JESD204B Eye Scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`, while being much more lightweight and doesn't require a graphical desktop environment. It can be started from a serial root console or from a SSH terminal.

It interfaces with the :doc:`JESD204 Interface Framework </wiki-migration/resources/fpga/peripherals/jesd204>`:

-  :doc:`JESD204B Transmit Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`
-  :doc:`JESD204B Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`
-  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

And reads the status information of all devices from SYSFS, aggregates and processes them and finally pretty prints it to the terminal in a continuous fashion. A single key event will terminate the application.

-  :doc:`JESD204 Status Registers </wiki-migration/resources/fpga/peripherals/jesd204/tutorial/linux>`

.. tip::

   In case this utility is not available on your platform you may run following command below to extract similar information:

   
   ::
   
      root@analog:/# grep "" /sys/bus/platform/drivers/axi-jesd204*/*/status /sys/bus/platform/drivers/axi-jesd204*/*/lane* /sys/bus/platform/drivers/axi-jesd204*/*/encoder
   


+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| What                                               | Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+====================================================+=====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| Link is [enabled|disabled]                         | Link state indicator. In case link state is disabled, that either means the link was never enabled or that an error occurred and the FSM rolled back and disabled the link. In the jesd204-fsm case this can be prevented by using the ``jesd204-ignore-errors;`` devicetree property when placed in the jesd204-fsm jesd204-top-device node.                                                                                                                                                                   |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link status                                        | Depending on the encoding JESD204B/C 8B10B/64B66B there can be different values ``RESET``, ``WAIT``, ``CGS``, ``ILAS``, etc., ``DATA`` Please see link layer documentation for the state machine: :doc:`JESD204B/C Link Receive Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>` \\ :doc:`JESD204B/C Link Transmit Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>` In general ``DATA`` is the desired state indicating proper operation.                                             |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SYNC is [asserted|deasserted] (8B10B only)         | State of the external ``SYNC`` signal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SYSREF captured: [Yes|No] (Subclass 1 only)        | Yes indicates that a ``SYSREF`` pulse was captured.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SYSREF alignment error: [Yes|No] (Subclass 1 only) | Yes indicates that a ``SYSREF`` event has been observed which was unaligned, in regards to the ``LMFC/LEMC`` period, to a previously recorded ``SYSREF`` event.                                                                                                                                                                                                                                                                                                                                                 |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lane rate                                          | The ``SERDES`` lane rate / bit clock.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [LMFC|LEMC] rate                                   | Frequency of the internal local multiframe clocks (``LMFC``)/ local-multiblock-clock (``LEMC``).                                                                                                                                                                                                                                                                                                                                                                                                                |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lane rate / [40|66]                                | Is equal to the desired ``Link Clock`` frequency.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reported Link Clock                                | Is the ``Link Clock`` frequency which is reported by the common clock framework. If this rate is different from the desired ``Link Clock`` frequency, there is likely a problem. For example the clock provider wasn’t able to set the desired value.                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Measured Link Clock                                | Is the measured ``Link Clock``, using a frequency counter inside the Link Layer Peripheral. For proper operation desired, reported and measured frequency must match.                                                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Desired Device Clock                               | In case this value is different from the Desired ``Link Clock``, this indicates Dual Clock Operation required by the Gearbox. Please see Gearbox/Dual Clock Operation in the Link Layer Peripheral documentation: :doc:`JESD204B/C Link Receive Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>` \\ :doc:`JESD204B/C Link Transmit Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>` The ``Device Clock`` is typically generated by the clock provider which also provides ``SYSREF``. |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reported Device Clock                              | Is the ``Device Clock`` frequency which is reported by the common clock framework. If this rate is different from the desired ``Device Clock`` frequency, there is likely a problem. For example the clock provider wasn’t able to set the desired value.                                                                                                                                                                                                                                                                                           |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Measured Device Clock                              | Is the measured ``Device Clock``, using a frequency counter inside the Link Layer Peripheral. For proper operation desired, reported and measured frequency must match.                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Source
------

`jesd-eye-scan-gtk application <https://github.com/analogdevicesinc/jesd-eye-scan-gtk>`__

Related device drivers
~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`JESD204 Linux Drivers </wiki-migration/resources/fpga/peripherals/jesd204/tutorial/linux>`

Running the software
~~~~~~~~~~~~~~~~~~~~

The software is started from the command line (it's better to do this as root):

::

   Usage: jesd_status [-s] [-p PATH] 
       -s     Simple mode no boxes and frames (useful for serial terminals)
       -p     Allows setting a different directory root. Default is /. 
              This is useful when running the tool remote

Running local
^^^^^^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any root shell prompt running on the target

   
   ::
   
      root@analog:~# **jesd_status**
   


Running local via a simple terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/jesd_status_simple.png
   :align: center
   :width: 600px

Depending on the terminal used colors might be unsupported and boxes, frames might not be properly displayed. The ``-s`` option allows to disable boxes, while setting the ``TERM`` variable will fix the display.

.. container:: box bggreen

   
   .. note::

      This specifies any root shell prompt running on the target

   
   ::
   
      root@analog:~# **TERM=vt100 jesd_status -s**
   

