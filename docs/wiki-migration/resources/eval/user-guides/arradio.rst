ARRADIO
=======

The `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`__ board is an `HSMC <http://www.altera.com/literature/ds/hsmc_spec.pdf>`__ board by `Arrow <https://www.arrow.com/en/manufacturers/analog-devices>`__ & `Terasic <http://arradio.terasic.com/>`__ for the :adi:`AD9361`, a highly integrated RF Agile Transceiver™. While the complete chip level design package can be found on the :adi:`the ADI web site <ad9361_design_files>`. Information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found on this page.

The ARRADIO board is not a product of Analog Devices, and questions about purchase, or returns should go to Arrow. You can purchase the board from `Arrow's web site <https://www.arrow.com/en/products/arradio/terasic-technologies>`__.

The purpose of the ARRADIO board is to provide an RF platform to which shows maximum performance of the AD9361. It’s expected that the RF performance of this platform can meet the datasheet specifications without issues at 2.4 GHz, and not much anywhere else. This is due to the external Johanson Technology's `2450BL15B050E <https://www.johansontechnology.com/datasheets/baluns/JTI_Balun-2450BL15B050_12-03.pdf>`__ 2.45 GHz Balun that is on the board. This balun is rated for a operating frequency of 2400~2500 MHz.

This platform is primarily for hardware / RF investigation and bring up of various waveforms from a RF team before their custom hardware is complete, where they want to see waveforms at their frequency of interest, and are not afraid of changing out the balun if necessary. (Have a look in the :doc:`Configuration </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>` sections).

The ARRADIO board is very similar to the `ad-fmcomms2-ebz <https://wiki.analog.com/ad-fmcomms2-ebz>`__, except it utilizes the HSMC connector which connects to the `Arrow SoCKit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`__.

|image1| |image2|

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`.

-  :doc:`Introduction </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`
-  Hardware (Schematics) see `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`__

   -  :doc:`Functional Overview & Specifications </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/functional_overview>`
   -  :doc:`Configuration options </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>`
   -  :doc:`Tuning the system </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`

-  Use the board to better understand the AD9361

   -  :doc:`What you need to get started </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`
   -  :doc:`Quick Start Guides </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`

      -  :doc:`Linux on Altera SoCKit </wiki-migration/resources/eval/user-guides/arradio/quickstart/alterasockit>`
      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/zynq_images>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/zynq_images>`

   -  Linux Applications

      -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
      -  :doc:`AD9361 Control in the IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms2_plugin>`
      -  :doc:`Advanced AD9361 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      -  :doc:`Command Line/Shell scripts </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   -  Push custom data into/out of the AD9361

      -  :doc:`Basic Data files and formats </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`
      -  :doc:`Create and analyze data files in MATLAB </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`
      -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      -  :doc:`AD9361 libiio streaming example </wiki-migration/resources/tools-software/linux-software/libiio>`

-  Design with the AD9361

   -  :doc:`Understanding the AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  :doc:`MATLAB Filter Design Wizard for AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`

   -  Simulation

      -  :doc:`MathWorks SimRF Models of the AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         -  :doc:`Beacon Frame Receiver Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`
         -  :doc:`QPSK Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/qpsk_example>`
         -  :doc:`LTE Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/lte_example>`

      -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
      -  :doc:`FM Radio/Tuner </wiki-migration/resources/tools-software/fm-radio>` (listen to FM signals on the HDMI monitor)
      -  :doc:`C example </wiki-migration/resources/tools-software/linux-software/libiio>`

   -  Design a custom AD9361 based platform

      -  :doc:`Linux software </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`

         -  :doc:`Linux Device Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
         -  :doc:`Build the demo on Altera SoCKit from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`
         -  :doc:`Build the 2014_R2 Release Linux kernel from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`
         -  :doc:`Customizing the devicetree on the target </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

      -  :doc:`No-OS Driver </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`

         -  :doc:`Build the HDL & No-OS from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal/arradio_noos>`

      -  :doc:`HDL Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>` which you must use in your FPGA.

         -  :doc:`Digital Interface Timing Validation </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`

-  Additional Documentation about SDR Signal Chains

   -  :doc:`The math behind the RF </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/math>`

-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`

Videos
======

.. image:: https://wiki.analog.com/_media/youtube>rdwdi8eIxRQ
   :alt: youtube>rdwdi8eIxRQ

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/rfc_top_01.jpg
   :width: 420px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/rfc_bot_01.jpg
   :width: 420px
