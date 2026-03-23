ARRADIO
=======

The `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`_ board is an `HSMC <http://www.altera.com/literature/ds/hsmc_spec.pdf>`_ board by `Arrow <https://www.arrow.com/en/manufacturers/analog-devices>`_ & `Terasic <http://arradio.terasic.com/>`_ for the :adi:`AD9361`, a highly integrated RF Agile Transceiver™. While the complete chip level design package can be found on the :adi:`the ADI web site <ad9361_design_files>`. Information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found on this page.

The ARRADIO board is not a product of Analog Devices, and questions about purchase, or returns should go to Arrow. You can purchase the board from `Arrow's web site <https://www.arrow.com/en/products/arradio/terasic-technologies>`_.

The purpose of the ARRADIO board is to provide an RF platform to which shows maximum performance of the AD9361. It’s expected that the RF performance of this platform can meet the datasheet specifications without issues at 2.4 GHz, and not much anywhere else. This is due to the external Johanson Technology's `2450BL15B050E <https://www.johansontechnology.com/datasheets/baluns/JTI_Balun-2450BL15B050_12-03.pdf>`_ 2.45 GHz Balun that is on the board. This balun is rated for a operating frequency of 2400~2500 MHz.

This platform is primarily for hardware / RF investigation and bring up of various waveforms from a RF team before their custom hardware is complete, where they want to see waveforms at their frequency of interest, and are not afraid of changing out the balun if necessary. (Have a look in the `Configuration <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>`_ sections).

The ARRADIO board is very similar to the `ad-fmcomms2-ebz <https://wiki.analog.com/ad-fmcomms2-ebz>`_, except it utilizes the HSMC connector which connects to the `Arrow SoCKit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_.

|image1| |image2|

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to `ask <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_.

-  `Introduction <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`_
-  Hardware (Schematics) see `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`_

   -  `Functional Overview & Specifications <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/functional_overview>`_
   -  `Configuration options <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>`_
   -  `Tuning the system <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`_

-  Use the board to better understand the AD9361

   -  `What you need to get started <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`_
   -  `Quick Start Guides <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`_

      -  :doc:`Linux on Altera SoCKit </solutions/reference-designs/arradio/quickstart/alterasockit>`
      -  `Configure a pre-existing SD-Card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
      -  `Update the old card you received with your hardware <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

   -  Linux Applications

      -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_
      -  `AD9361 Control in the IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_plugin>`_
      -  `Advanced AD9361 Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`_
      -  `Command Line/Shell scripts <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`_

   -  Push custom data into/out of the AD9361

      -  `Basic Data files and formats <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`_
      -  `Create and analyze data files in MATLAB <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`_
      -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`_
      -  `AD9361 libiio streaming example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_

-  Design with the AD9361

   -  `Understanding the AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`_

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  `MATLAB Filter Design Wizard for AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`_

   -  Simulation

      -  `MathWorks SimRF Models of the AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`_

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`_
         -  `Beacon Frame Receiver Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`_
         -  `QPSK Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/qpsk_example>`_
         -  `LTE Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/lte_example>`_

      -  `GNU Radio <https://wiki.analog.com/resources/tools-software/linux-software/gnuradio>`_
      -  `FM Radio/Tuner <https://wiki.analog.com/resources/tools-software/fm-radio>`_ (listen to FM signals on the HDMI monitor)
      -  `C example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_

   -  Design a custom AD9361 based platform

      -  `Linux software <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`_

         -  `Linux Device Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`_
         -  `Build the demo on Altera SoCKit from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`_
         -  `Build the 2014_R2 Release Linux kernel from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`_
         -  `Customizing the devicetree on the target <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`_

      -  `No-OS Driver <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`_

         -  `Build the HDL & No-OS from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal/arradio_noos>`_

      -  `HDL Reference Design <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`_ which you must use in your FPGA.

         -  `Digital Interface Timing Validation <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`_

-  Additional Documentation about SDR Signal Chains

   -  `The math behind the RF <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/math>`_

-  `Help and Support <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_

Videos
======

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/youtube>rdwdi8eixrq
   :alt: youtube>rdwdi8eIxRQ

.. |image1| image:: images/rfc_top_01.jpg
   :width: 420
.. |image2| image:: images/rfc_bot_01.jpg
   :width: 420


.. toctree::
   :hidden:

   quickstart/alterasockit
