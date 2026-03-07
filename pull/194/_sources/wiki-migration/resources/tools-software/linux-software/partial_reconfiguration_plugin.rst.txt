Partial Reconfiguration Plugin
==============================

| The Partial Reconfiguration plugin works with the `IIO Oscilloscope <https://wiki.analog.com/iio_oscilloscope>`_. You always use the latest version if possible.
| Read more about Partial Reconfiguration by following this link: :doc:`Partial Reconfiguration. </wiki-migration/resources/fpga/docs/hdl/partial>`

Screenshots / Descriptions
--------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/partial_reconfiguration_plugin.png
   :align: right
   :width: 460px

Reconfigurable Partition
~~~~~~~~~~~~~~~~~~~~~~~~

-  **Reconfiguration File:** Displays the full path of a .bin file that can be selected using the file-chooser button on the left side. The new configuration applies automatically without the need of an Apply button.

Register Access
~~~~~~~~~~~~~~~

-  **Core:** Selects a register map between the ADC and the DAC.
-  **PR_STATUS:** Status register of the Partial Reconfiguration. Read Only.
-  **PR_CONTROL:** Control register of the Partial Reconfiguration. Read/Write access.
-  **Read Button:** Reads and displays the PR_STATUS and PR_CONTROL registers.
-  **Write Button:** Writes data to PR_CONTROL register.
