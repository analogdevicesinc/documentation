ADRV9009/ADRV9008 Advanced Plugin
=================================

The ADRV9009/ADRV9008 Advanced plugin works with the `IIO Oscilloscope <https://wiki.analog.com/iio_oscilloscope>`__. You always use the latest version if possible. Changing any field will immediately write changes which have been made to the ADRV9009 settings to the driver, but not to the HW unless the Save Settings button is pressed.

The ADRV9009 Advanced Plugin allows testing of different device driver initialization options and values. In contrast to the controls on the `ADRV9009/ADRV9008 Main Plugin <https://wiki.analog.com/adrv9009_plugin>`__ – the controls here are not part of the main driver API.

In the No-OS driver the values directly correspond to members of the (taliseInit_t) talInit init structure. For the ADRV9009 Linux Device Driver each control corresponds to a specific devicetree property. Since the ADRV9009 Linux driver uses the Analog Devices provided API driver. Ultimately also for the Linux driver maps any settings back to the taliseInit_t init structure. It's therefore recommended to consult the **ADRV9009 User Guide** for more information about the options provided here.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/taliseInit_t.png
   :alt: taliseInit_t structure
   :align: center
   :width: 500px

See more details about :doc:`ADRV9009/ADRV9008 Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009-customization>`.

In order for the settings made on these plugin to take affect, the Save Settings button must be pressed. It should be noted that the driver then reinitialized the ADRV9009 from reset, which will rerun all calibrations and this may take several seconds to complete.

.. tip::

   \ **TIP:** After you customized the driver for your application needs you can read back all values from the Linux debugfs:

   
   .. container:: box bggreen

         
         .. note::

            This specifies any shell prompt running on the target

         
         ::
         
            root@analog:/sys/bus/iio/devices/iio:device3# **cd /sys/kernel/debug/iio/iio\:device3**
            root@analog:/sys/kernel/debug/iio/iio:device3# **grep "" * | sed "s/:/ = </g"

            | awk '{print $0">;"}'**
            adi,arm-gpio-config-en-tx-tracking-cals-enable = <0>;
            adi,arm-gpio-config-en-tx-tracking-cals-gpio-pin-sel = <0>;
            adi,arm-gpio-config-en-tx-tracking-cals-polarity = <0>;
            adi,arm-gpio-config-orx1-tx-sel0-pin-enable = <0>;
            adi,arm-gpio-config-orx1-tx-sel0-pin-gpio-pin-sel = <0>;
            adi,arm-gpio-config-orx1-tx-sel0-pin-polarity = <0>;
            adi,arm-gpio-config-orx1-tx-sel1-pin-enable = <0>;
            adi,arm-gpio-config-orx1-tx-sel1-pin-gpio-pin-sel = <0>;
            adi,arm-gpio-config-orx1-tx-sel1-pin-polarity = <0>;
            adi,arm-gpio-config-orx2-tx-sel0-pin-enable = <0>;
            adi,arm-gpio-config-orx2-tx-sel0-pin-gpio-pin-sel = <0>;
            adi,arm-gpio-config-orx2-tx-sel0-pin-polarity = <0>;
            adi,arm-gpio-config-orx2-tx-sel1-pin-enable = <0>;
            adi,arm-gpio-config-orx2-tx-sel1-pin-gpio-pin-sel = <0>;
            adi,arm-gpio-config-orx2-tx-sel1-pin-polarity = <0>;
            adi,aux-dac-enables = <0>;
            adi,aux-dac-resolution0 = <0>;
            adi,aux-dac-resolution1 = <0>;
         
            [ -- snip -- ]
         

   
   Simply update the values here: :doc:`ADRV9009 Devicetree Initialization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`
   
   For the No-OS driver the mapping can be found here: :doc:`ADRV9009 Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009-customization>`
   
   |

| ===== Screenshots / Descriptions =====

Clock Settings
--------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_1.png
   :alt: BIST
   :align: center
   :width: 600px

Calibrations
------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_2.png
   :alt: BIST
   :align: center
   :width: 600px

TX Settings
-----------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_3.png
   :alt: BIST
   :align: center
   :width: 600px

RX Settings
-----------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_4.png
   :alt: BIST
   :align: center
   :width: 600px

Observation RX Settings
-----------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_5.png
   :alt: BIST
   :align: center
   :width: 600px

Frequency Hopping Mode Setup
----------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_6.png
   :alt: BIST
   :align: center
   :width: 600px

PA Protection Settings
----------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_7.png
   :alt: BIST
   :align: center
   :width: 600px

Gain Settings
-------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_8.png
   :alt: BIST
   :align: center
   :width: 600px

AGC Settings
------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_9.png
   :alt: BIST
   :align: center
   :width: 600px

ARM GPIO Settings
-----------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_10.png
   :alt: BIST
   :align: center
   :width: 600px

AUX DAC Settings
----------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_11.png
   :alt: BIST
   :align: center
   :width: 600px

JESD204B Settings
-----------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_12.png
   :alt: BIST
   :align: center
   :width: 600px

JESD204B Framer Settings
------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_13.png
   :alt: BIST
   :align: center
   :width: 600px

JESD204B Deframer Settings
--------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_14.png
   :alt: BIST
   :align: center
   :width: 600px

BIST
----

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_ADV_PLUGIN_15.png
   :alt: BIST
   :align: center
   :width: 600px

BIST stands for Build-In Self-Test. Selections on this Tab take immediately effect and therefore don’t require the Save Settings Button. Functionality exposed here is only meant to inject test patterns/data than can be used to validate the Digital Interface or functionality of the device.

There are three major facilities.

BIST TX NCO Tone
~~~~~~~~~~~~~~~~

User selectable tone with frequency in kHz, that can be injected into the TX path.

BIST PRBS
~~~~~~~~~

Patterns and Pseudorandom Binary Sequence (PRBS) that can be injected into the RX path.
