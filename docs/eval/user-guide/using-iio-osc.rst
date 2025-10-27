ADI IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can connect to :ref:`iio-oscilloscope` either remotely, or locally.

Remote
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :ref:`iio-oscilloscope` application can be used to connect to another
platform that has a connected device, to configure the device and read data
from it. This application is not for performance testing, but rather
showcasing the basic features.

Please see :ref:`IIO Oscilloscope documentation <iio-oscilloscope>` for
installation steps and more details.

Build and start ``osc`` on a network-enabled Linux host.
For Windows computers, open the application from the start menu.

Once the application is launched, go to Settings > Connect > URI and type
"ip:" then the IP address of the target in the pop-up window. This IP can
be found out with a command from the previous section of this documentation.

Locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you connected an HDMI monitor to your FPGA and a mouse and a keyboard
(both on one dongle), you can navigate the ADI Kuiper Linux that is on the FPGA.

Going to the top left corner icon (the menu icon), search for IIO Oscilloscope.
Opening it will automatically connect to the setup and you can use the
application.
