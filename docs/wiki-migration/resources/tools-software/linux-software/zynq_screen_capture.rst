Taking Screenshots on the Xilinx Zynq or Altera SoC
===================================================

Screenshot is an image taken by a computer to capture the visible items on the monitor or any other output devices. Normally, people want to do this to capture a screen for placement in this wiki. There are several ways of taking screenshots in Linux. We will cover few tools that are used for taking screenshots.

There are two steps do getting screen shots on the wiki.

-  take the screen shot
-  load it on the wiki

Taking Screenshots
------------------

Use Print Screen
~~~~~~~~~~~~~~~~

This is the most common method to take screenshots. Pressing the "Print Screen" key on the keyboard will take the screenshot of the “Entire Visible Screen”. On many keyboards, the "Print Screen" button will only be active if you hold down the "Function" button.

When we want to take a particular window, we can use "Alt+Print Screen". Alt+PrintScreen will take only the particular window which is currently active.

Use gnome-screenshot
~~~~~~~~~~~~~~~~~~~~

Transferring to wiki
--------------------

Edit the wiki directly on the Zynq
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  open firefox,
-  goto ``wiki.analog.com``,
-  log in,
-  upload things through the media manager

Ethernet
~~~~~~~~

-  save or move your pictures to the /media folder
-  this folder is shared as a windows share
-  from your windows PC, open the share and copy the files

USB
~~~

-  If you have a USB hub, and have a spare USB slot, plug in a USB drive
-  mount it
-  save or move your pictures to the USB drive (where ever you mounted it).

SD Card
~~~~~~~

-  save the pictures into the ``BOOT`` partition
-  turn off the Zynq
-  eject the SD card, and plug it into your PC
-  copy files from the SD Card
