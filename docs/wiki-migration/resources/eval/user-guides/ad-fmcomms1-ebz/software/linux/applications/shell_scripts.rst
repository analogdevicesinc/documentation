Shell Scripts for the FMC RF boards
===================================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_


`Shell Scripts <https://en.wikipedia.org/wiki/Shell_script>`_ are scripts written for the shell (`dash <https://en.wikipedia.org/wiki/Debian_Almquist_shell>`_ or `bash <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`_ or `ash <https://en.wikipedia.org/wiki/Almquist_shell>`_) of an operating system. To find out which shell, you are using, try something like:

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
   


DDS passing by
--------------

.. code:: bash

   #!/bin/sh

   # find the DAC
   for i in $(find /sys -name name)
   do
     if [ "`cat $i`" = "cf-ad9122-core-lpc" ] ; then
        dac_path=$(echo $i | sed 's:/name$::')
     fi
   done

   #save the current settings
   init=`cat $dac_path/out_altvoltage0_1A_frequency`

   # Set DDSn_A
   freq_A(){
     echo $1 > $dac_path/out_altvoltage0_1A_frequency
     echo $1 > $dac_path/out_altvoltage2_2A_frequency
   }

   # Set DDSn_B
   freq_B(){
     echo $1 > $dac_path/out_altvoltage1_1B_frequency
     echo $1 > $dac_path/out_altvoltage3_2B_frequency
   }

   for i in 10 20 30 40 50 60 70 80 90 100 110
   do 
     freq_A `expr $i \\* 1000000`
     freq_B `expr \( 120 - $i \) \\* 1000000`
     sleep 1
   done

   freq_A $init
   freq_B $init

Random data on the RF output
----------------------------

.. code:: bash

   #!/bin/sh

   # buffer size, let's use 512 samples, or 1024 bytes
   buffer_size=1024

   # find the DAC
   for i in $(find /sys -name name)
   do
     if [ "`cat $i`" = "cf-ad9122-core-lpc" ] ; then
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
---------------------

I don't like remembering what 1/32 is, so I just use :math:`1/(2^n)` . You just need to provide 'n'.

.. code:: bash

   #!/bin/sh

   #check in the input
   if [ $1 -le -1 ] ; then
     echo "input out of range, (needs to be 0-4)"
     exit
   fi

   if [ $1 -ge 5 ] ; then
     echo "input out of range (needs to be 0-4)"
     exit
   fi

   # find the DAC
   for i in $(find /sys -name name 2>/dev/null)
   do
     if [ "`cat $i`" = "cf-ad9122-core-lpc" ] ; then
        dac_path=$(echo $i | sed 's:/name$::')
     fi
   done

   echo $(echo "scale=4; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage0_1A_scale
   echo $(echo "scale=4; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage1_1B_scale
   echo $(echo "scale=4; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage2_2A_scale
   echo $(echo "scale=4; 1 / ( 2 ^ $1 )" | bc) > $dac_path/out_altvoltage3_2B_scale

   echo -n "amplitude set to "
   cat $dac_path/out_altvoltage0_1A_scale

Sweeping the Tx
---------------

.. code:: bash

   #!/bin/bash

   # find the TX LO generator
   for i in $(find /sys -name name)
   do
     if [ "`cat $i`" = "adf4351-tx-lpc" ] ; then
        tx_lo_path=$(echo $i | sed 's:/name$::')
     fi
   done

   if [ -z $tx_lo_path ] ; then
     echo "Can't find adf4351-tx-lpc"
     exit 1
   fi

   start=$1
   end=$2
   inc=$3
   pause=$4

   if [ -z $start ] ; then
     start=400
   fi

   if [ -z $end ] ; then
     end=4000
   fi

   if [ -z $inc ] ; then
     inc=5 
   fi

   if [ -z $pause ] ; then
     pause=1
   fi

   freq_tx() {
     echo $1 > $tx_lo_path/out_altvoltage0_frequency
   }

   for (( i  = $start; $i <= $end; i+=$inc));
   do
     echo $i
     freq_tx `expr $i \\* 1000000`
     sleep $pause
   done
