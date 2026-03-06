JESD204 Eye Scan
================

About
-----

The combination of increasing JESD204B serial line rates and PCB based attenuation and distortion increasing, the quality and correctness of differential pair at a JESD204B receiver becomes questionable. The combination of the bit sampling time decreasing (as speed increases), and channel attenuation increasing (as speed increases) both negatively impact the data recovery from the received serial data stream.

This poses a challenge in most designs to system bring-up and release to production because the quality of the line cannot be determined by measuring the far-end eye opening at the receiver pins with readily available lab equipment. Not only does this require prohibitively expensive equipment  [1]_, or it becomes impossible, as the received eye measured on the printed circuit board can appear to be completely closed.

How is anyone supposed to release a product to manufacturing when they don't know if the 10 prototypes that are working are accidentally successful or if they have plenty of design margin?

FPGA Hardware
-------------

Luckily, the problem of verifying high speed transceiver performance was solved by the FPGA manufactures years ago, and we can take advantage of the functionality they have added to their chips to determine the overall design margin in a JESD204B solution without purchasing expensive test equipment.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/xilinx_transceiver.png
   :width: 500px

This illustrates the blocks dedicated to achieving signal integrity in the Xilinx 7-Series FPGA GTP transceivers. All the shaded blocks — PLL, TX pre-emphasis, RX automatic gain control (`AGC <https://en.wikipedia.org/wiki/Automatic_gain_control>`__), RX linear equalization (EQ), RX clock data recovery (`CDR <https://en.wikipedia.org/wiki/Clock_recovery>`__), and adaptation block all ensure as robust as link as possible. The 2-D Eye Scan block attached to the receive path provides the functionality of an on-chip scope to visualize post-equalization signal quality in a JESD204B receiver.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/xilinx_2d_eye_scan.png
   :width: 400px

As shown above, eye scan runs a separate sampler (figure on the left) which can be adjusted in the horizontal (time) and vertical (amplitude) dimension in parallel with the normal CDR data sampler located in the middle of the horizontal and vertical sale. Xilinx uses this to transfer data over JTAG to create a representative picture on your development host with their `IBERT <https://www.xilinx.com/support/documentation/sw_manuals/xilinx13_1/ug811_ChipScopeUsingIBERTwithAnalyzer.pdf>`__ tool.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/xilinx_2d_eye_scan_logic.png
   :width: 400px

For each offset setting, the error counter is cleared, and a specified number of bits are transmitted. The data and offset samples are compared bit by bit. When the two samples are not equal, the error counter is incremented. when the specific number of bits are complete, the comparison stops, and bit error rate can be calculated by dividing the error counts by the number of bits transmitted.

This statistically recreates the eye diagram after the equalizer, showing how much design margin is in the system.

BERT Testing
------------

For a 5.0 Gbps link, there are 5,000,000,000 bits per second. This provides a 2 x 10\ :sup:`-10` seconds per bit.

In order to measure a BERT rate of 10\ :sup:`-10`, the system would need to transmit 10\ :sup:`10` bits, or 2 seconds of data before it could determine that. As BERT goes up by factors of 10, so must the time.

============== ============== ===============================
BERT Rate      Number of Bits time to transmit
============== ============== ===============================
10\ :sup:`-8`  10\ :sup:`8`   20 milliseconds
10\ :sup:`-9`  10\ :sup:`9`   0.2 seconds
10\ :sup:`-10` 10\ :sup:`10`  2 seconds
10\ :sup:`-11` 10\ :sup:`11`  20 seconds
10\ :sup:`-12` 10\ :sup:`12`  200 seconds, or 3.33 minutes
10\ :sup:`-13` 10\ :sup:`13`  33.33 minutes
10\ :sup:`-14` 10\ :sup:`14`  333.33 minutes, or 5.55 hours
10\ :sup:`-15` 10\ :sup:`15`  55.55 hours, or 2.31 days
10\ :sup:`-16` 10\ :sup:`16`  23.14814815 days, or 3.30 weeks
10\ :sup:`-17` 10\ :sup:`17`  33.06 weeks or ~8 months
============== ============== ===============================

However, this is multiplied by the number of "pixels" (offsets in the time and voltages scales) of the that data. In order to get the most detailed picture, the Xilinx 7 series eye scan supports +/- 32 offsets in the horizontal (time) dimension, and 128 offsets in the vertical (voltage) dimension. This is 8192 (64 x 128) pixels per "frame". This means it would take 163.84 seconds, or 2.7 minutes (8192 \* 20 milliseconds) to capture 10\ :sup:`-8` BERT, and 5400+ years to generate the picture at a BERT of 10\ :sup:`-17`.

Clearly - this isn't practical, so what we attempt to do

Mask
----

The JESD204B specification outlines an receive keep-out mask based on channel baud rate. To be compliant, the signals at the receiver must stay outside the pre-defined mask area for the baud rate in use.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/jesd_rx_mask.jpg
   :width: 400px

However, this specification is provided in millivolts and time (in unit intervals). As discussed above, the 2-D eye scan operates after the AGC and equalizer blocks inside the FPGA, so it is difficult (impossible) to correlate voltage on the Rx pins of the FPGA, to the vertical axis in the 2-D statistical eye diagram.

The vertical axis in the 2-D statistical eye diagram is in "codes", not millivolts.

The mask that is shown is not the JESD204B mask, but the Xilinx CDR mask - since this is really the only thing that really matters inside the FPGA.

Software
--------

Overview
~~~~~~~~

The JESD204B eye scan tool that Analog Devices created runs natively on a the ZC706 (under Linux) and creates the pictures below. It does this by using the Xilinx hardware described above, using an HDL/Linux reference design that was created by Analog Devices.

This reference design gathers data directly from the on-chip Receive margin analysis feature in the 7 series IBERT core and manages the data locally inside the FPGA or one of the ARM dual-core Cortex-A9 processors, displaying the data on a HDMI monitor. This measures link robustness using actual JESD204B serial data running from the converter to the FPGA. This use of “live” data enables signal fidelity to be monitored even after the design has been deployed in the field, which allows for real-time and predictive maintenance over the life of the product.

Also see here: :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`

Source
------

`jesd-eye-scan-gtk application <https://github.com/analogdevicesinc/jesd-eye-scan-gtk>`__

When building the source code, make sure that gnuplot & libgtk3-dev & required build dependencies are installed.

On Debian/Ubuntu do:

::

   apt-get update
   apt-get install -y git build-essential gnuplot libgtk-3-dev libncurses-dev

On CentOS/Redhat

::

   yum update
   yum -y groupinstall 'Development Tools'
   yum -y install git ncurses-devel gtk3-devel gnuplot

Related device drivers
~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`JESD204B/C Transmit Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`
-  :doc:`JESD204B/C Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`
-  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

Running the software
~~~~~~~~~~~~~~~~~~~~

The software is started from the command line (it's better to do this as root):

::

   Usage: jesd_eye_scan [-p PATH] 
       -p     Allows setting a different directory root. Default is /. 
              This is useful when running the tool remote

Running local
^^^^^^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any root shell prompt running on the target

   
   ::
   
      root ~ # **jesd_eye_scan &**
   


Running remote (X11 forwarding)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When using the :doc:`AD-FMC-SDCARD for Zynq/Intel SoC </wiki-migration/resources/tools-software/linux-software/zynq_images>` without display connected,you can use X11 forwarding over SSH to run this application remotely

::

   ssh -X root@IP-ADDRESS jesd_eye_scan

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on a remote host

   
   ::
   
      dave@HAL9000:/home/dave& **ssh -X root@10.44.3.53 jesd_eye_scan**
      root@10.44.3.53's password: 
      Select axi-adxcvr-rx device!
   


Running remote (sshfs)
^^^^^^^^^^^^^^^^^^^^^^

This remote option uses the Secure SHell FileSystem (SSHFS), and might be suitable for remote systems without X support, such as our minimal Microblaze systems. It therefore requires sshd running on the target.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on a remote host

   
   ::
   
      dave@HAL9000:/home/dave# **mkdir /home/dave/mnt**
      dave@HAL9000:/home/dave# **sudo sshfs -o direct_io,sync_read,allow_other -o StrictHostKeyChecking=no root@10.44.2.224:/ /home/dave/mnt**
      dave@HAL9000:/home/dave# **LC_ALL=c jesd_eye_scan -p /home/dave/mnt**
   


.. important::

   The **LC_ALL=c** prefix for the command is important when running remote, because the locale on the client system can influence the format of the data. If it is incorrect, the plot will be empty.


Output
~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/jesd204-eye-scan1.png
   :alt: Main Window
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/jesd204-eye-scan2.png
   :alt: Status Information
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/jesd204-eye-scan3.png
   :alt: Lane Information
   :align: center
   :width: 600px

The numbers under the "Eye Opening", define the eye opening (same amount of errors in the H and V dimensions as the centre (no errors). The units are in Unit intervals (in the time domain), and "codes" in the Voltage scale. Codes are a unit-less dimension since this is after the equalizer and there is no way to correlate voltage at the pins, and the offset codes that are used to control this value.

The colours in the `Heat Map <https://en.wikipedia.org/wiki/Heat_map>`__ are the number of errors at that point.

Requirements
~~~~~~~~~~~~

-  JESD204B converter
-  ZC706, ZCU102 or running remote VC707, KC705, KCU105
-  ADI Linux image on SD Card (ZC706), or ADI kernel with the ADI Microblaze Root File System (VC707, KC705, KCU105)

Tweaking
--------

Now that you have a way to look at the JESD204B receive link, and can start determining what the tweaks you can make to the JESD204B interface on the transmit side (converter). The converter settings can adjust:

-  JESD204B pre-emphasis
-  JESD204B CML differential output drive level

By tweaking these values, you can open/close the eye while trading off power consumption, and potentiality EMI emissions.

References/More reading
-----------------------

-  `Serial Link Signal Integrity Analysis with IBIS-AMI Simulation and On-Chip Eye Scan for Low-Cost, High-Volume FPGA Transceivers <https://www.xilinx.com/support/documentation/white_papers/wp428-7Series-Serial-Link-Signal-Analysis.pdf>`__, Xilinx
-  `Eye Scan with MicroBlaze Processor MCS <https://www.xilinx.com/support/documentation/application_notes/xapp743-eye-scan-mb-mcs.pdf>`__, Xilinx
-  `7 Series FPGAs GTX/GTH Transceivers User Guide <https://www.xilinx.com/support/documentation/user_guides/ug476_7Series_Transceivers.pdf>`__, RX Margin Analysis section, Xilinx
-  `ChipScope Pro Tutorial: Using an IBERT Core with ChipScope Pro Analyzer <https://www.xilinx.com/support/documentation/sw_manuals/xilinx13_1/ug811_ChipScopeUsingIBERTwithAnalyzer.pdf>`__, Xilinx
-  `Serial Link Signal Integrity Analysis with IBIS-AMI Simulation and On-Chip Eye Scan for Low-Cost, High-Volume FPGA Transceivers <https://www.xilinx.com/support/documentation/white_papers/wp428-7Series-Serial-Link-Signal-Analysis.pdf>`__, Xilinx
-  :adi:`The JESD204B Survival Guide <jesd204>`, Analog Devices

.. [1]
   Many would recommend an oscilloscope bandwidth of anywhere from 16 GHz to 32 GHz is appropriate for JESD204B testing. `JESD204B PHY Layer Compliance Test, JULY 2012, Vol. 11 No. 7, High Frequency Electronics <http://www.highfrequencyelectronics.com/Archives/Jul12/1207_HFE_layerCompTest.pdf>`__, typically these scopes are over $150k
