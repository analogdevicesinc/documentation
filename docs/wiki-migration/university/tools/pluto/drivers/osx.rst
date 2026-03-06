Mac OS X Drivers
================

Serial
------

.. container:: box

   
   ::
   
      adi-mm:tests analogdevices$ **ls -l /dev/tty.* **
      crw-rw-rw-  1 root  wheel   17,   0 Nov  7 15:13 /dev/tty.Bluetooth-Incoming-Port
      crw-rw-rw-  1 root  wheel   17,   2 Nov  7 15:28 /dev/tty.usbmodem1414
      adi-mm:tests analogdevices$ **screen /dev/tty.usbmodem1414 115200**
   
      Welcome to Pluto
      pluto login: **root**
      Password: **analog**
      # uname -a
      Linux pluto 4.6.0-08511-gc1315e6-dirty #247 SMP PREEMPT Mon Oct 24 16:46:25 CEST 2016 armv7l GNU/Linux
      # 
      **CNTRL-A** **CNTRL-\**
      Really quit and kill all your windows [y/n] **y**
      [screen is terminating]
      adi-mm:tests analogdevices$ 
   


Mass Storage
------------

.. container:: box

   
   ::
   
      adi-mm:tests analogdevices$ **mount | grep Pluto**
      /dev/disk1s1 on /Volumes/PlutoSDR (msdos, local, nodev, nosuid, noowners)
   


Ethernet
--------

.. tip::

   In order to use the ADALM-PLUTO (aka. PlutoSDR) or ADALM2000 (aka. M2k) with Mac OSX the ethernet compatibility mode must be set to **USB CDC-NCM**.

   
   Please see instructions for :doc:`changing the usb ethernet compatibility mode </wiki-migration/university/tools/pluto/users/customizing>`.


.. warning::

   Like most of the network settings on Pluto or the M2k - things are meant to be easy to use. This also means things are inherently insecure.

   
   For example - the root password of Pluto is ``analog``. We post it on the Internet. Think about that for a moment. This could allow anyone with an IP connection to take over the device and use it for malicious purposes.
   
   **Never** set up a bridge between the Internet and a network connected Pluto with the default images.


Unfortunately - nothing on your host understands the what the IP address of the usb device is. You, the human behind the keyboard need to understand this before any sort of networking will work. There are two main ways to do this:


You should see something like this when you goto -> System Preferences -> Network.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/drivers/screen_shot_2017-01-12_at_2.36.55_pm.png
   :width: 400px

.. container:: box

   
   ::
   
      adi-mm:tests analogdevices$ **ifconfig  | grep -B 3 -A 3 192**
      en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1486
          ether 00:e0:22:6d:b2:d8 
          inet6 fe80::2e0:22ff:fe6d:b2d8%en4 prefixlen 64 scopeid 0xa 
          inet 192.168.2.10 netmask 0xffffff00 broadcast 192.168.2.255
          nd6 options=1<PERFORMNUD>
          media: autoselect
          status: active
   


Adding a quick/short :git-plutosdr_scripts:`ssh config file <ssh_config>`, which describes the USB device can be helpful. It's maintained in github, and it's a simple matter of grabbing the raw text file. You shouldn't do the exact below unless you have no ``~/.ssh/config`` file. Otherwise, click `on this link <https://raw.githubusercontent.com/analogdevicesinc/plutosdr_scripts/master/ssh_config>`__ and copy/paste it into the system wide ``/etc/ssh/ssh_config`` file, or the user specific ``~/.ssh/config`` file.

.. container:: box

   
   ::
   
      analog@imhotep:~$ **wget https:%%//%%raw.githubusercontent.com/analogdevicesinc/plutosdr_scripts/master/ssh_config -O ~/.ssh/config**
      --2017-01-26 19:47:51--  https:%%//%%raw.githubusercontent.com/analogdevicesinc/plutosdr_scripts/master/ssh_config
      Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.116.133
      Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.116.133|:443... connected.
      HTTP request sent, awaiting response... 200 OK
      Length: 366 [text/plain]
      Saving to: ‘~/.ssh/config’
   
      ~/.ssh/config         100%[===============>]     366  --.-KB/s    in 0s      
   
      2017-01-26 19:47:51 (6.49 MB/s) - ‘~/.ssh/config’ saved [366/366]
   


Since the ssh key on the pluto changes every boot, we want to be able to never store the key (so we store it to ``/dev/null``. This does make it easier to use (don't need to continually edit the ``known_hosts`` file), but does make things susceptible to man in the middle attacks.

.. container:: box

   
   ::
   
      adi-mm:tests analogdevices$ **ssh plutosdr**
      Warning: Permanently added 'pluto' (ECDSA) to the list of known hosts.
      root@pluto's password: **analog**
      # **uname -a**
      Linux pluto 4.6.0-08511-gc1315e6-dirty #247 SMP PREEMPT Mon Oct 24 16:46:25 CEST 2016 armv7l GNU/Linux
      # **exit**
      Connection to 192.168.2.1 closed.
      adi-mm:tests analogdevices$ 
   


if you have ``sshpass`` installed, you can use that so you dont need to type in a password:

.. container:: box

   
   ::
   
      analog@imhotep:~/pluto$ **sshpass -panalog ssh plutosdr**
      Warning: Permanently added 'pluto' (ECDSA) to the list of known hosts.
      Welcome to:%%
      ______ _       _        _________________
      | ___ \ |     | |      /  ___|  _  \ ___ \
      | |_/ / |_   _| |_ ___ \ `--.| | | | |_/ /
      |  __/| | | | | __/ _ \ `--. \ | | |    /
      | |   | | |_| | || (_) /\__/ / |/ /| |\ \
      \_|   |_|\__,_|\__\___/\____/|___/ \_| \_|
   
      http://wiki.analog.com/university/tools/pluto%%
      # 
   


