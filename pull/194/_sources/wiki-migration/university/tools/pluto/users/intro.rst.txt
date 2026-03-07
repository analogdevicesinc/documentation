Introduction to the ADALM-PLUTO
===============================

.. image:: https://wiki.analog.com/_media/university/tools/pluto/pluto_on_desk.png
   :align: right
   :width: 300px

To use the :adi:`ADALM-PLUTO` Active Learning Module, you have:

-  2 RF `SMA connectors <https://en.wikipedia.org/wiki/SMA_connector>`_  [1]_ to connect to instrumentation or an antennas

   -  Transmit (labeled 'Tx')
   -  Receive (labeled 'Rx')
   -  300 MHz - 3.8 GHz
   -  200 kHz - 20 MHz channel bandwidth

-  USB for your host connectivity (used to stream data)

   -  USB 2 (480 Mbits/second)
   -  libiio USB device for communicating to the RF device
   -  Network device

      -  Remote Network Driver Interface Specification (`RNDIS <https://en.wikipedia.org/wiki/RNDIS>`_)
      -  This will enumerate with the ``192.168.2.1`` IP address by default.

   -  USB serial device

      -  provides access to the Linux console on the Pluto device via USB Communication Device Class Abstract Control Model (`USB CDC ACM <https://en.wikipedia.org/wiki/USB_communications_device_class>`_) specification

   -  Mass storage device

      -  this will appear to the host as a disk, where you can find links for software uploads, and the serial number of the device.

-  External power

   -  It was a possibility during the design of Pluto that the design could have consumed more than 5 unit loads for `USB 2 <https://en.wikipedia.org/wiki/USB#Power>`_ (500mA), and a "backup" power connector was added to mitigate this. This should not be necessary for nominal use, (we haven't needed it yet) but if you find the device is power cycling, or your host reports problems, please let us know, we have not seen this.
   -  An external adapter (like `this one from Adafruit <https://www.adafruit.com/products/1995?gclid=CjwKEAjwjqO_BRDribyJpc_mzHgSJABdnsFWlRs2FrqbAVZt9erVQDN6LakvKxmYjiLjTHKe_7ZqVxoCPu3w_wcB>`_).
   -  We know the "Power" icon is the "on/off" icon, if you think that is confusing - please let us know.

.. [1]
   SubMiniature version A
