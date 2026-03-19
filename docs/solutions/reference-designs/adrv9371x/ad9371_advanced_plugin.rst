AD9371/AD9375 Advanced Plugin
=============================

The AD9371/AD9375 Advanced plugin works with the `IIO Oscilloscope <https://wiki.analog.com/iio_oscilloscope>`_. You always use the latest version if possible. Changing any field will immediately write changes which have been made to the AD9371 settings to the driver, but not to the HW unless the Save Settings button is pressed.

The AD9371 Advanced Plugin allows testing of different device driver initialization options and values. In contrast to the controls on the `AD9371/AD9375 Main Plugin <https://wiki.analog.com/ad9371_plugin>`_ – the controls here are not part of the main driver API.

In the No-OS driver the values directly correspond to members of the (mykonosDevice_t) mykDevice init structure. For the AD9371 Linux Device Driver each control corresponds to a specific devicetree property. Since the AD9371 Linux driver uses the Analog Devices provided API driver. Ultimately also for the Linux driver maps any settings back to the mykDevice init structure. It's therefore recommended to consult the **AD9371 User Guide** for more information about the options provided here.

.. image:: images/mykonosdevice_t.png
   :alt: mykonosDevice_t structure
   :align: center
   :width: 500

See more details about :doc:`AD9371/AD9375 Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9371-customization>`.

In order for the settings made on these plugin to take affect, the Save Settings
button must be pressed. It should be noted that the driver then reinitialized
the AD9371 from reset, which will rerun all calibrations and this may take
several seconds to complete.

.. tip::

   \ TIP: After you customized the driver for your application needs you can
   read back all values from the Linux debugfs:

   
   .. container:: box bggreen

      This specifies any shell prompt running on the target

         
         ::
         
            root@analog:/sys/bus/iio/devices/iio:device3# cd /sys/kernel/debug/iio/iio\:device3
            root@analog:/sys/kernel/debug/iio/iio:device3# grep "" * | sed "s/:/ = </g" | awk '{print $0">;"}'
            adi,clocks-clk-pll-hs-div = <4>;
            adi,clocks-clk-pll-vco-div = <2>;
            adi,clocks-clk-pll-vco-freq_khz = <9830400>;
            adi,clocks-device-clock_khz = <122880>;
            adi,default-initial-calibrations-mask = <32255>;
            adi,gpio-3v3-oe-mask = <0>;
            adi,gpio-3v3-src-ctrl11_8 = <3>;
            adi,gpio-3v3-src-ctrl3_0 = <3>;
            adi,gpio-3v3-src-ctrl7_4 = <3>;
            adi,gpio-oe-mask = <0>;
            adi,gpio-src-ctrl11_8 = <0>;
            adi,gpio-src-ctrl15_12 = <0>;
            adi,gpio-src-ctrl18_16 = <0>;
            adi,gpio-src-ctrl3_0 = <0>;
            adi,gpio-src-ctrl7_4 = <0>;
         
         
            [ -- snip -- ]
         

   
   Simply update the values here: :doc:`AD9371 Devicetree Initialization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9371>`
   
   For the No-OS driver the mapping can be found here: :doc:`AD9371 Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9371-customization>`
   

Screenshots / Descriptions
--------------------------

Clock Settings
~~~~~~~~~~~~~~

.. image:: images/myk_clk.png
   :alt: BIST
   :align: center
   :width: 600

Calibrations
~~~~~~~~~~~~

.. image:: images/myk_cal.png
   :alt: BIST
   :align: center
   :width: 600

TX Settings
~~~~~~~~~~~

.. image:: images/myk_tx.png
   :alt: BIST
   :align: center
   :width: 600

RX Settings
~~~~~~~~~~~

.. image:: images/myk_rx.png
   :alt: BIST
   :align: center
   :width: 600

Observation RX Settings
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/myk_obs.png
   :alt: BIST
   :align: center
   :width: 600

Gain Settings
~~~~~~~~~~~~~

.. image:: images/myk_gain.png
   :alt: BIST
   :align: center
   :width: 600

AGC Settings
~~~~~~~~~~~~

.. image:: images/myk_agc.png
   :alt: BIST
   :align: center
   :width: 600

ARM GPIO Settings
~~~~~~~~~~~~~~~~~

.. image:: images/myk_arm_gpio.png
   :alt: BIST
   :align: center
   :width: 600

GPIO Settings
~~~~~~~~~~~~~

.. image:: images/myk_gpio.png
   :alt: BIST
   :align: center
   :width: 600

AUX DAC Settings
~~~~~~~~~~~~~~~~

.. image:: images/myk_aux_dac.png
   :alt: BIST
   :align: center
   :width: 600

JESD204B Framer Settings
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/myk_framer.png
   :alt: BIST
   :align: center
   :width: 600

JESD204B Deframer Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/myk_deframer.png
   :alt: BIST
   :align: center
   :width: 600

BIST
~~~~

.. image:: images/myk_bist.png
   :alt: BIST
   :align: center
   :width: 600

BIST stands for Build-In Self-Test. Selections on this Tab take immediately
effect and therefore don’t require the Save Settings Button. Functionality
exposed here is only meant to inject test patterns/data than can be used to
validate the Digital Interface or functionality of the device.

There are three major facilities.

BIST Tone
^^^^^^^^^

User selectable tone with frequency in kHz, that can be injected into the TX
path.

BIST PRBS
^^^^^^^^^

Pseudorandom Binary Sequence (PRBS) that can either injected into the RX or TX
path.

BIST Loopback
^^^^^^^^^^^^^

Allows to digitally loopback TX data into the RX path.

DPD Setup (AD9375 only)
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/myk_dpd.png
   :alt: BIST
   :align: center
   :width: 600

CLGC Setup (AD9375 only)
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/myk_clgc.png
   :alt: BIST
   :align: center
   :width: 600

VSWR Setup (AD9375 only)
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/myk_vswr.png
   :alt: BIST
   :align: center
   :width: 600
