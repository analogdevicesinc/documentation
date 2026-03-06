AD936X Advanced Plugin
======================

The AD936X Advanced plugin (formerly known as the FMComms2/3/4/5 Advanced Plugin) works with the `IIO Oscilloscope <https://wiki.analog.com/iio_oscilloscope>`__. You always use the latest version if possible. Changing any field will immediately write changes which have been made to the AD936X settings to the hardware, and then read it back to make sure the setting is valid. If you want to set something that the GUI changes to a different number, that either means that GUI is rounding (sorry), or the hardware (either the AD9361 or the FPGA fabric) does not support that mode/precision.

If you want to go play with ``/sys/bus/iio/devices/....`` and manipulate the devices behind the back of the GUI, it's still possible to see the settings by clicking the "refresh" button at the bottom of the GUI.

The AD936X Advanced Plugin allows testing of different device driver initialization options and values. In contrast to the controls on the `AD936X Main Plugin <https://wiki.analog.com/fmcomms2_plugin>`__ – the controls here are not part of the main driver API.

In the No-OS driver the values correspond to members of the setup/init structure. For the AD9361 Linux Device Driver each control corresponds to a specific devicetree property.

See more details about :doc:`AD9361 Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361-customization>`.

.. tip::

   \ **TIP:** After you customized the driver for your application needs you can read back all values from the Linux debugfs:

   
   .. container:: box bggreen

         
         .. note::

            This specifies any shell prompt running on the target

         
         ::
         
            root@linaro-ubuntu-desktop:~# **cd /sys/kernel/debug/iio/iio\:device1/**
            root@linaro-ubuntu-desktop:/sys/kernel/debug/iio/iio:device1# **grep "" * | sed "s/:/ = </g"

            | awk '{print $0">;"}'**
            adi,2rx-2tx-mode-enable = <1>;
            adi,agc-adc-large-overload-exceed-counter = <10>;
         
            [ -- snip -- ]
         

   
   Simply update the values here: :doc:`AD9361 Devicetree Initialization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   
   For the No-OS driver the mapping can be found here: :doc:`AD9361 Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361-customization>`
   
   |

Screenshots / Descriptions
--------------------------

MAIN
~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms234_advanced_plugin_main.png
   :alt: MAIN
   :align: center
   :width: 500px

With the Clockout setting, you can control the signal on the Output Clock (``CLK_OUT`` pin). This pin can be configured to output either a buffered version of the external input clock (the digital controlled crystal oscillator (DCXO)) or a divided down (÷2, ÷3, ÷4, ÷8, ÷16, ÷32, ÷64) version of the internal ADC sample clock (ADC_CLK).

Gain Control
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms234_advanced_plugin_gain1.png
   :alt: GAIN MGC, Slow Attack AGC
   :align: center
   :width: 500px

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms234_advanced_plugin_gain2.png
   :alt: GAIN Fast Attack AGC
   :align: center
   :width: 500px

RSSI
~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms234_advanced_plugin_rssi.png
   :alt: RSSI
   :align: center
   :width: 500px

External LNA
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms234_advanced_plugin_elna.png
   :alt: eLNA
   :align: center
   :width: 500px

TX Monitor
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms234_advanced_plugin_tx_monitor.png
   :alt: TX Monitor
   :align: center
   :width: 500px

Axillary IO (ADC, DAC, Control IO, Temp Sensor)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms234_advanced_plugin_auxio.png
   :alt: AuxIO
   :align: center
   :width: 500px

MISC
~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms234_advanced_plugin_misc.png
   :alt: MISC
   :align: center
   :width: 500px

BIST
~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms234_advanced_plugin_bist.png
   :alt: BIST
   :align: center
   :width: 500px

BIST stands for Build-In Self-Test. Selections on this Tab take immediately effect and therefore don’t require the Save Settings Button. Functionality exposed here is only meant to inject test patterns/data than can be used to validate the Digital Interface or functionality of the device.

There are three major facilities. The top most drop down selection box allows you to specify the injection point.

BIST Tone
^^^^^^^^^

User selectable tone (with frequency and level selection), that can either injected into the RX or TX path. There are some check boxes below that allow you to MASK off certain channels. A masked channel (box check) is not driving any data. (This feature can be useful to determine the I,Q Rx1, Rx2 channel to data mapping)

BIST PRBS
^^^^^^^^^

Pseudorandom Binary Sequence (PRBS) that can either injected into the RX or TX path.

BIST Loopback
^^^^^^^^^^^^^

Allows either to digitally loopback TX data into the RX path or vice versa.

-  Digital TX -> Digital RX loopback : The loopback happens inside the AD9361/4 close to the internal digital interface block. The entire RF section is bypassed. This can be used to validate (monitor on RX) the digital samples/symbols sent to the device.
-  RF RX -> RF TX loopback : The loopback happens in the ADI provided HDL core. The Transmitter will transmit anything that the receiver receives. The entire RF chain is active (Sample rates, RF bandwidth and FIR settings will all effect the transmission.
