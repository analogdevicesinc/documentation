DAQ Board Overview
==================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/AD-FMCLIDAR1-EBZ/DAQ top pic.jpg
   :align: right
   :width: 350px

The Data Acquisition (DAQ) board connects to the FPGA carrier via an FMC HPC connector. This board is where the analog-to-digital conversion is completed and the result is sent to the FPGA via a JESD 204B interface. The low phase-noise and synchronized clock signals required by the ADC as well as all the signals needed for JESD Subclass 1 operation, ensuring deterministic latency, are also generated here. Additionally, low noise voltages are supplied to the ADC, PLL and clock buffer. All the digital signals between the FPGA carrier board and the AFE and Laser boards pass through the DAQ board going to two 100 pin high speed connectors that correspond to similar connectors on the other two boards. The digital connection between the boards is made with ribbon cables. The 4 ADC channels are exposed on SMA connectors to mate with the corresponding signal sources on the AFE and Laser boards. This modular design allows the AFE and Laser boards to be oriented in the desired direction as well as to use different variantes of these boards designed according to specific applications requirements.

The ADC on the DAQ board is the :adi:`AD9094 <en/products/ad9094.html>`, a quad, 8-bit, 1GSPS ADC. It supports JESD204B lane rate up to 15 Gbps, four integrated wideband decimation filters, numerically controlled oscillator blocks and it is programmable via an SPI interface.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/AD-FMCLIDAR1-EBZ/DAQ Board.png
   :alt: DAQ Block Diagram
   :align: left
   :width: 350px

The IC selection for clock signals generation ensures low phase-noise, programmable delays for proper deterministic latency and low power consumption. The :adi:`ADF4360-7 <en/products/adf4360-7.html>` is a PLL which takes a crystal generated 25MHz input and outputs a low phase-noise 1GHz clock signal. This signal is then fed to an :adi:`AD9528 <en/products/ad9528.html>`, which outputs five clock signals as required by the ADC and JESD204B interface. The AD9528 can divide frequencies and/or delay clock signals, thus ensuring synchronization for deterministic latency. The AD9528 is used in buffer mode to reduces power consumption. In this mode the internal PLLs are disabled and the AD9528 acts as a clock distribution chip, dividing the input clock to get the desired clock rates at the output.

The stringent noise challenges posed by the 1GSPS analog-to-digital conversion are met by ultralow noise regulators such as the :adi:`ADP7156 <en/products/adp7156.html>` and :adi:`ADP7159 <en/products/adp7159.html>`. All the power for this board is derived for the 3.3V and 12V supplies coming off the FPGA board via the FMC connector.

The DAQ board meets the VITA 57 design specs for width but not for length.

The ADC input creates a 100Ω differential impedance. The external components account for the equivalent circuit of the analog inputs of the ADC. The user has the option to add capacitors and filter out both differential and common mode noise voltages.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmclidar1-ebz/adc_input_1.jpg
   :alt: ADC Input
   :align: center
   :width: 600px

The clocking scheme on the DAQ board provides 5 clock signals: two for the ADC and three for the FPGA. They ensure the proper functioning of the system with deterministic latency. The five signals are generated according to the block diagram in the next figure. The AD9528 is used as a buffer only for low power consumption.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmclidar1-ebz/daq_clocking.jpg
   :alt: Clock Diagram
   :align: center
   :width: 600px

The DAQ board allows for an alternative use of the AD9528 where both its PLL stages are used in addition to the output buffer. This option doesn’t use the separate PLL – ADF4360-7. The block diagram along with the higher power consumption are given in the next figure.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmclidar1-ebz/daq_clocking_option.jpg
   :alt: Clock Option
   :align: center
   :width: 400px

--------------

.. admonition:: Download
   :class: download

   `AD-FMCLIDAR1-EBZ FMC Connector Pinout <https://wiki.analog.com/_media/resources/eval/user-guides/AD-FMCLIDAR1-EBZ/fmclidar1_fmc_pinout.xlsx>`_


.. admonition:: Download
   :class: download

   `Design Files(Schematics, Layout, BOM) <https://wiki.analog.com/_media/resources/eval/user-guides/AD-FMCLIDAR1-EBZ/revb_daq.zip>`_


--------------

.. image:: https://wiki.analog.com/_media/navigation AD-FMCLIDAR1-EBZ#none#./
   :alt: Overview#none#
