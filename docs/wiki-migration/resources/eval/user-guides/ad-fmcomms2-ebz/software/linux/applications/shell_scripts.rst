Shell scripts
=============

`Shell scripts <https://en.wikipedia.org/wiki/Shell_script>`__ are scripts written for the shell (`dash <https://en.wikipedia.org/wiki/Debian_Almquist_shell>`__, `bash <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`__, or `ash <https://en.wikipedia.org/wiki/Almquist_shell>`__) of an operating system. To find out which shell, you are using, try something like:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      rgetz@pinky ~ $ **which sh**
      /usr/bin/sh
      rgetz@pinky ~ $ **ls -l /usr/bin/sh**
      lrwxrwxrwx 1 root root 9 2009-05-13 20:39 /usr/bin/sh -> /bin/bash
   
   OR
   
   ::
   
      rgetz@pinky ~ $ **ps -p $$**
        PID TTY          TIME CMD
       1321 pts/0    00:00:00 bash
   


To check out these scripts, simply do something like:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      rgetz@pinky ~ $ **git clone https://github.com/analogdevicesinc/linux_image_ADI-scripts.git**
   


This should give you the most up to date scripts.

Linux scripts
-------------

Enabling a static IP address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the Linux setup provided by ADI will try to automatically get an IP address from the network using DHCP. To instead use a static IP instead, do the following:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@linaro-ubuntu-desktop:~# **sudo adi_update_tools.sh**
      root@linaro-ubuntu-desktop:~# **sudo enable_static_ip.sh <IP address>**
   


In more detail, first make sure the latest software is installed on the host so the ``enable_static_ip.sh`` script is available. Then it can be used to set a static IP address for a network interface (defaults to eth0). Note that the specified IP address should generally be an unused one on the same subnet the device is getting added to. As a warning, note that these scripts will overwrite /etc/network/interfaces so do not run them on devices where you have specifically customized the network configuration.

An interface can be specified as the second argument otherwise the script defaults to eth0, e.g. in order to use 192.168.0.2 for eth1 run the following:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@linaro-ubuntu-desktop:~# **sudo enable_static_ip.sh 192.168.0.2 eth1**
   


In order to revert back to acquiring IP addresses for all interfaces via DHCP use the following:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@linaro-ubuntu-desktop:~# **sudo enable_dhcp.sh**
   


Scripts for FMComms boards
--------------------------

DDS passing by
~~~~~~~~~~~~~~

.. code:: bash

   #!/bin/sh

   # find the DAC
   for i in $(find /sys -name name)
   do
     if [ "`cat $i`" = "cf-ad9361-dds-core-lpc" ] ; then
        dac_path=$(echo $i | sed 's:/name$::')
     fi
   done

   #save the current settings
   init=`cat $dac_path/out_altvoltage0_TX1_I_F1_frequency`

   sampl=`cat $dac_path/out_altvoltage_TX1_I_F1_sampling_frequency`
   ny=`expr $sampl / 2`

   # Set DDSn_A
   freq_A(){
     echo $1 > $dac_path/out_altvoltage0_TX1_I_F1_frequency
     echo $1 > $dac_path/out_altvoltage2_TX1_Q_F1_frequency
     echo $1 > $dac_path/out_altvoltage4_TX2_I_F1_frequency
     echo $1 > $dac_path/out_altvoltage6_TX2_Q_F1_frequency
   }

   # Set DDSn_B
   freq_B(){
     echo $1 > $dac_path/out_altvoltage3_TX1_Q_F2_frequency
     echo $1 > $dac_path/out_altvoltage1_TX1_I_F2_frequency
     echo $1 > $dac_path/out_altvoltage7_TX2_Q_F2_frequency
     echo $1 > $dac_path/out_altvoltage5_TX2_I_F2_frequency
   }

   for i in `seq 1000000 1000000 $ny`
   do
     freq_A $i
     freq_B `expr $ny - $i`
     sleep 1
   done

   freq_A $init
   freq_B $init

Random data on the RF output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   #!/bin/sh

   # buffer size, let's use 512 samples, or 1024 bytes
   buffer_size=1024

   # find the DAC
   for i in $(find /sys -name name)
   do
     if [ "`cat $i`" = "cf-ad9361-dds-core-lpc" ] ; then
        dac_path=$(echo $i | sed 's:/name$::')
     fi
   done

   # Get the associated dev file
   dev=/dev/$(echo $dac_path |  awk -F "/" '{print $NF}')
   if [ ! -c $dev ] ; then
     echo "Can't find device $dev"
     exit
   fi

   # set the buffer size
   echo $buffer_size > $dac_path/buffer/length

   # generate the random data, and give it to the DAC
   dd if=/dev/urandom of=$dev bs=$buffer_size count=1

   #enable things
   echo 1 > $dac_path/buffer/enable

   #Wait 5 seconds
   sleep 5

   #turn if off before we bring down everyone's WiFi
   echo 0 > $dac_path/buffer/enable

Setting the amplitude
~~~~~~~~~~~~~~~~~~~~~

I don't like remembering what 1/32 is, so I just use :math:`1/(2^n)` . You just need to provide 'n'.

.. code:: bash

   #!/bin/sh

   #check in the input
   if [ $1 -le -1 ] ; then
     echo "input out of range, (needs to be 0-15)"
     exit
   fi

   if [ $1 -ge 16 ] ; then
     echo "input out of range (needs to be 0-15)"
     exit
   fi

   # find the DAC
   for i in $(find /sys -name name 2>/dev/null)
   do
     if [ "`cat $i`" = "cf-ad9361-dds-core-lpc" ] ; then
        dac_path=$(echo $i | sed 's:/name$::')
     fi
   done

   echo $(echo "scale=6; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage0_TX1_I_F1_scale
   echo $(echo "scale=6; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage1_TX1_I_F2_scale
   echo $(echo "scale=6; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage2_TX1_Q_F1_scale
   echo $(echo "scale=6; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage3_TX1_Q_F2_scale

   echo $(echo "scale=6; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage4_TX2_I_F1_scale
   echo $(echo "scale=6; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage5_TX2_I_F2_scale
   echo $(echo "scale=6; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage6_TX2_Q_F1_scale
   echo $(echo "scale=6; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage7_TX2_Q_F2_scale

   echo -n "amplitude set to "
   cat $dac_path/out_altvoltage0_TX1_I_F1_scale

Sweeping the Tx
~~~~~~~~~~~~~~~

.. code:: bash

   #!/bin/sh

   # find the TX LO generator
   for i in $(find /sys -name name)
   do
     if [ "`cat $i`" = "ad9361-phy" ] ; then
        tx_lo_path=$(echo $i | sed 's:/name$::')
     fi
   done

   if [ -z $tx_lo_path ] ; then
     echo "Can't find ad9361-phy"
     exit 1
   fi

   start=$1
   end=$2
   inc=$3
   pause=$4

   if [ -z $start ] ; then
     start=100
   fi

   if [ -z $end ] ; then
     end=6000
   fi

   if [ -z $inc ] ; then
     inc=5
   fi

   if [ -z $pause ] ; then
     pause=1
   fi

   freq_tx() {
     echo $1 > $tx_lo_path/out_altvoltage1_TX_LO_frequency
   }

   for i in `seq $start $inc $end`;
   do
     echo $i
     freq_tx `expr $i \\* 1000000`
     sleep $pause
   done
