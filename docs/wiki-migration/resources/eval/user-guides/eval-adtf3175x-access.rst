Accessing the ADTF-3175x
========================

This section discusses how to access the command line interface (CLI) of the ADTF-3175x. Doing so gives the user access to Linux.

Out of the box, the user can write to the file system. However, any written data will be lost on reboot or power cycle of the device. The device can be setup such that changes to the file system survive reboots and power cycles. The following discussed how this can be done.

When operating the ADTF-3175x with a read/write partition it is highly recommended that Linux be shutdown prior to disconnecting power, not doing so may result in a corrupted file system. Issue the following command in the CLI to power down the system:

.. important::

   \ **sudo systemctl poweroff**\


**Disclaimer:** <fc #ff0000>It is rather easy to stop the proper functioning of the ADTF-3175x via an errant Linux command. The user is responsible for the state of the device once they start using the CLI. If the ADTF-3175x does stop functioning it is trivial to re-flash the stock micro-SD card image from the installation package.</fc>

Making the SD Card Writable
---------------------------

The image for the micro-SD card is shipped with the Linux partition as read only. It is possible to make the Linux partition read-write.

Once again, not the introduction at the top of this page.

The micro-SD card image has two partitions:

-  Windows FAT
-  Linux ext4

When the micro-SD card is inserted into a Windows machines the FAT partition will become available. For example:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/adtf3175x-rw-fat-partition.png
   :width: 400px

Case 1: You computer does *not* encrypt files on external storage devices.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open the FAT partition that is available once the camera is connected
-  Open extlinux.conf file in the extlinux folder with notepad
-  Replace all **ro** with **rw** as shown below

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/readwrite_modify.png
   :align: center

Case 2: You computer encrypts files on external storage devices.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your organization encrypts file transfers to external drives, it is recommended to use a personal pc to run this step. Once the change is made it is permanent and the user can go back to their work PC.

If using a personal PC is not an option, mapping the windows partition as a network drive could allow the user to bypass encryption (Although your mileage may vary)

-  Go to the partition properties and click on 'Advanced Sharing'

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/properties_share.png
   :align: center

-  Check 'Share this folder' and create a name for the drive

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/advanced_sharing.png
   :align: center

-  In the properties folder copy the Network Path, and paste in File Explorer to open the drive

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/get-network-path.png
   :align: center

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/file-exp.png
   :align: center

-  Modify the extlinux.conf file as mentioned in Case 1

Connecting to the ADTF-3175x
----------------------------

Connecting to the ADTF-3175x is accomplished via a USB-Serial link via micro-USB cable. Referring to the below, the micro-USB port is shown in the red circle.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/adtf3175x-micro-usb.jpg
   :width: 300px

We use PuTTY for a terminal. PuTTY can be downloaded from `here (PuTTY download) <https://www.putty.org/>`__.

Before running PuTTY we need to discover the COM port of the device.

-  Plug the USB-C cable into the NXP to power up the device.
-  Without the micro-USB cable connected to the ADTF-3175x device,
-  Open 'Device Manager' on Windows. If you do not know how, please see the `here <https://www.howtogeek.com/697936/5-ways-to-open-device-manager-on-windows-10/>`__.
-  In the 'Device Manger' window, find 'Port (COM & LPT)', then expand the selection.
-  Now plug in the micro-USB cable back into the ADTF-3175x.
-  When booting is complete you should see a new COM port, note this COM port for use in PuTTY.

For example, in the case shown in the image below, the COM port is COM7.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/adtf3175x-device-manager-com-port.png
   :width: 1200px

Onto PuTTY:

-  Open PuTTY
-  You will see the 'Putty Configuration' window.
-  In the 'Session' category: Select the 'Connection type' as 'Serial'; set the 'Serial line' to the value observed in the 'Device Manager'; set the 'Speed' to 115200; finally click 'Open'.
-  PuTTY should open a terminal window at the login prompt of the ADTF-3175x.

Example of configuring PuTTY:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/adtf3175x-putty-configuration.png
   :width: 400px

Example of opening PuTTY (note, you may need to press 'enter' to see the login prompt):

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/adtf3175x-putty-open.png
   :width: 400px

Logging into the ADTF-3175x
---------------------------

User name: analog Password: analog

Example of logging into the console of the ADTF-3175x via PuTTY.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/adtf3175x-console-login.png
   :width: 400px

Setting up Wifi
---------------

The ADTF-3175x device has Wifi support. Through the Wifi connection it is possible to connect to a router then to the Internet. Having Wifi

Setting up Wifi is as easy on the ADTF-3175x as it would be on any Ubuntu device.

-  wpa_passphrase *<SSIDOfYourNetwork>* *<Password>* \| sudo tee /etc/wpa_supplicant/wpa_supplicant-wlan0.conf
-  sudo systemctl enable wpa_supplicant@wlan0
-  sudo reboot

However, there is a script for doing this:

-  cd ~/Workspace/Tools
-  ./adi-enable-wifi.sh *<SSIDOfYourNetwork>* *<Password>*

Using Ethernet
--------------

For Ethernet a special cable is required: `Ethernet Calbe <https://www.digikey.com/en/products/detail/harting/33480147826005/14556497?utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_High%20ROAS%20Categories&utm_term=&utm_content=&gad_source=1&gclid=Cj0KCQiA2eKtBhDcARIsAEGTG42oZjojdGeKNfvpwGK2jDzSHm63GUJM7dJPYx7M9Nad7B_VOsofZVYaAg4REALw_wcB>`__

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/tof-adtf3175d-ethernet.png
   :width: 200px
