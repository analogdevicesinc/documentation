.. _pluto devs usb_otg:

USB OTG
=======

The ADALM-PLUTO and ADLAM2000 support
`USB_On-The-Go <https://en.wikipedia.org/wiki/USB_On-The-Go>`__.
This allows a few different use cases for these instruments.

Running applications from USB drives
------------------------------------

The Pluto will automount any
`USB mass storage device <https://en.wikipedia.org/wiki/USB_mass_storage_device_class>`__ such as
`thumb drive <https://en.wikipedia.org/wiki/USB_flash_drive>`__ or
`Hard Drives <https://en.wikipedia.org/wiki/Hard_disk_drive#EXTERNAL>`__.
The automounter will then look for some special file names:

- ``runme[0-9].sh`` which it will run as a shell script
- ``runme[0-9]`` which it will run as a binary file.

For those interested, it will do that via the automounter script in
``/lib/mdev/automounter.sh`` which is maintained
:git-buildroot:`here <board/pluto/automounter.sh>`.

Note 1 : if you're editing the runme.sh file from windows, make sure you use
'LF' as file line ending.

Note 2 : The power supply (and USB cable quality) of the ADALM-PLUTO have an
influence on the otg storage device plug detection.

Basic Example
~~~~~~~~~~~~~

For those who just want to do something, create a ``runme0.sh`` file on a thumb
drive (FAT32 is fine) which looks like a normal unix
`shell script <https://en.wikipedia.org/wiki/Shell_script>`__.
To debug your shell script, try your commands via ssh before putting them in the script.
This example requires at least firmware v0.22.

.. code:: bash

   #!/bin/sh

   # the default directory the script runs in is /dev, so change to the drive
   cd /media/sda1/

   # create a file
   touch foobar

   # change the RX_LO to 2.4GHz
   iio_attr -a -c  ad9361-phy RX_LO frequency 2400000000

and insert the USB thumb drive in to Pluto.

The LED should stop blinking, and you have run your application. To safely
unmount the drive, you should press the button, which will cause the drive to by
sync'ed, file systems caches flushed, and properly unmount the drive.

Advanced examples
~~~~~~~~~~~~~~~~~

Send a tone
^^^^^^^^^^^

The code below sets up a tone, and plays it out via the DDS (the AD9361's test
mode). It then unmounts the drive it is running on, so you can unplug the USB
drive. All that is necessary is to boot while the uSB drive is plugged in, and
that is it. This example requires at least firmware v0.22.

.. code:: bash

   #!/bin/sh

   # the default directory the script runs in is /dev, so change to the drive
   cd /media/sda1/

   # create a file
   touch foobar.txt

   echo default-on > /sys/class/leds/led0:green/trigger >> foobar.txt

   # Set the LO up
   /usr/bin/iio_attr -a -c ad9361-phy TX_LO frequency 908460000 >> foobar.txt

   # Set the Sample frequency up, tone will appear at sampling_frequency/32
   /usr/bin/iio_attr -a -c -o ad9361-phy voltage0 sampling_frequency 32000000 >> foobar.txt

   # Turn the attenuation down
   /usr/bin/iio_attr -a -c -o ad9361-phy voltage0 hardwaregain 0

   # https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9361#bist_tone
   # Inject 0dBFS tone at Fsample/32 into TX (all channels enabled)
   /usr/bin/iio_attr -a -D ad9361-phy bist_tone "1 0 0 0" >> foobar.txt

   cd /root

   ACTION=remove_all /lib/mdev/automounter.sh

Re purposing the button
^^^^^^^^^^^^^^^^^^^^^^^

The below script will change the function of the button. Rather than unmounting
things, it pressing the button will run a script. Holding the button for longer
than 5 seconds will unmount things.

This requires a few different scripts, and modification of a configuration file.

To manage the button, pluto uses the `input event daemon <https://github.com/gandro/input-event-daemon>`__
(`doc <https://htmlpreview.github.io/?https://github.com/gandro/input-event-daemon/blob/master/docs/input-event-daemon.html>`__).
The default configuration file can be found at
:git-buildroot:`here <master:board/pluto/input-event-daemon.conf>`,
and simply calls the automounter (unmounter), when you press the button. Our
script kills that, and re-starts things with different configuration file (our
our mass storage device).
