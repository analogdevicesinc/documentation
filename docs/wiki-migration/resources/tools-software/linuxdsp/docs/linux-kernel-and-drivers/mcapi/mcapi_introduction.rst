Introduction of MCAPI examples
==============================

Introduction
------------

This document gives a more detailed introduction of MCAPI examples.

This example involves two following parts:

-  Baremetal: MCAPI Baremetal CCES projects run on SHARC 1 core and shrac 2 core
-  Linux: Linux MCAPI demo examples run on ARM core

There are 3 MCAPI inter-operability demos included in the libmcapi tests, currently we only support msg demo:

-  msg (unconnected message protocol)   – supported
-  sclchan (connected scalar channel protocol)   –  unsupported
-  pktchan (connected packet channel protocol)  – unsupported

There are 2 ways to load the MCAPI baremetal project: loaded by remoteproc and loaded by ICE1000 in CCES.

| For more information about "**loaded by Remoteproc**", please refer to ``Multicore loading using the Remoteproc``
| For more information about "**loaded by ICE1000 in CCES**", please refer to ``Run Linux on ARM and bare-metal application on SHARC``

MCAPI Baremetal test examples
-----------------------------

The MCAPI example for ARM core (Running Linux) is included in the YOCTO, and you can get the MCAPI example for SHARC+ Cores from the gitbub `lnxdsp-examples <https://bitbucket.analog.com/projects/DTE/repos/lnxdsp-examples>`_

The examples code in "lnxdsp-exmaples/mcapi/mcapi-message-example". You'll find three folders which are for msg, sclchan and pktchan, each folder contains the baremetal mcapi cces projects for sc589, sc584 and sc573 boards, "Mcapi_Test_Core1.c" is the main application c file. You should use CCES to open and build the project, since we only support msg test example, we'll take the MCAPI Baremetal MSG test as the example in the next section.

MCAPI Linux demos
-----------------

The MCAPI example for ARM core (Running Linux) is included in the YOCTO through the package "libmcapi" demos can be found in "build/tmp/work/armv7at2hf-neon-poky-linux-gnueabi/libmcapi", "arm_sharc_msg_demo.c" is the main application c file.

Once the linux boot finished, one command for MCAPI demo test can be found in linux, you are able to use "**arm_sharc_msg_demo -h**" to get more information about the command:

::

   # arm_sharc_msg_demo -h
   Usage: arm_sharc_msg_demo <options>
   Available options:
           -h,--help               this help
           -m,--mode               select the mode:                    
                                   0 --- nonblocking mode0(default)                    
                                   1 --- nonblocking mode1             
                                   2 --- nonblocking mode2             
                                   3 --- blocking mode
           -t,--timeout            timeout value in jiffies(default:5000)
           -r,--round              number of test round(default:100)

"arm_sharc_msg_demo" shows the example use of blocking/nonblocking message send/receive between two different endpoints on different nodes, the endpoint of ARM sends a message then receives a message from another endpoint of CORE1 in one round, after comparing the receive data with the data you expect, the number of passed rounds will be increased, only when the passed rounds and the test rounds are equal, it'll give demo passed log.

Each mode means the different ways to do message transaction between two endpoints using different MCAPI APIs we supported, and you can choose the way by "-m":

========== ===========
 Options    Descrition   
========== ===========
========== ===========

::

   ;**-m,--mode** 
   :mode 0   |nonblocking send    |nonblocking recv  |mcapi_test() / mcapi_msg_available() 
   :mode 1   |nonblocking send    |nonblocking recv  |mcapi_test()                         
   :mode 2   |nonblocking send    |nonblocking recv  |mcapi_wait()                         
   :mode 3   |blocking send

   |blocking recv  
   ;**-t,--timeout**   
   :Timeout value is used to set the maximum wait time for wait and blocking function
   ;**-r,--round**     
   :Round is the number of rounds you want to test, the default check round is 100, if number equals 100,  passed log will be output in CCES. 

|

| ---- **BACK TO** :doc:`Multi-Core Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/start>`
