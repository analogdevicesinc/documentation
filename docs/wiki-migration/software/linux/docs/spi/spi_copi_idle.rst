Linux SPI COPI Idle Configuration
=================================

The behavior of an SPI controller data output line (SDO or MOSI or COPI (Controller Output Peripheral Input) for disambiguation) is not specified when the controller is not clocking out data on SCLK edges (:adi:`1 <en/resources/analog-dialogue/articles/introduction-to-spi-interface.html>`, `2 <https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all>`_, `3 <https://en.wikipedia.org/wiki/Serial_Peripheral_Interface>`_, `4 <https://ww1.microchip.com/downloads/en/devicedoc/spi.pdf>`_, `5 <https://www.ti.com/lit/pdf/sprugp2>`_). However, there do exist SPI peripherals that require specific COPI line state when data is not being clocked out of the controller.

The AD4000 Series
-----------------

The devices that belong to the AD4000 series of ADCs are an example of devices that require particular COPI idle state. Let's take :adi:`ADAQ4003` to illustrate how the series relies on specific COPI idle behavior and how SPI controllers can support it.

The timing diagrams for register read/write and ADC sampling (for datasheet "3-wire" mode (which has nothing to do with conventional spi-3wire configuration)) all specify peripheral SDI = 1 (high) throughout transfers.

|image1| |image2| |image3| |image4|

Here is how SPI transfers execute when running the ad4000 Linux kernel driver with :adi:`EVAL-ADAQ40xx` connected to BCM2835 SPI controller present on RPI 4. The figures show a reg read, reg write of 0xE1, reg read, sample read, and sample read.

|image5| |image6| |image7| |image8| |image9|

We notice register access operations work properly despite the COPI line not being kept high prior to transfers. However, when sampling the ADC, the peripheral brings CIPO/MISO low and keeps the line at that state while output data close to 0xF7BA0000 was expected.

One thing that can make the COPI line behavior similar to what is described in :adi:`ADAQ4003` datasheet is to fill the transfer tx buffer with 1s. Though, that turned out not to solve the ADC sampling issue.

|image10| |image11|

The SPI COPI Idle Configuration Feature
---------------------------------------

So, to properly support devices of the AD4000 series, ADI developers elaborated the concept of SPI controller SDO/MOSI/COPI idle configuration feature. In sum, the idea is that a device that requires specific COPI idle behavior may request it to the SPI controller. If the controller supports COPI idle configuration, then the data output line state would remain at the configured level when the controller is not clocking out data. Let's see how it works with the spi-gpio and spi-engine controllers.

SPI COPI Idle Configuration with SPI-GPIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Linux kernel provides a bitbanging SPI host driver that implements a SPI bus from GPIO pins. That controller can implement the SPI COPI idle configuration feature by setting COPI GPIO state according to what SPI peripherals request (through SPI mode bits). With the SPI COPI line configured to idle high, SPI transfers to :adi:`ADAQ4003` execute as follows. Figures show a reg read, reg write of 0xE1, reg read, sample read, sample read.

|image12| |image13| |image14| |image15| |image16|

SPI COPI Idle Configuration with SPI-Engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SPI-Engine controller can also implement COPI idle state configuration with proper output handling made on SPI-Engine HDL (SDI/SDO from controller perspective). Again, figures show a reg read, reg write of 0xE1, reg read, sample read, and a sample read.

|image17| |image18| |image19| |image20| |image21|

Last Considerations
-------------------

So, devices that belong to the AD4000 series can be supported properly by SPI controllers that can keep the COPI line high or that support COPI idle state configuration. But, since the SPI protocol does not define any behavior for the COPI line when data is not being clocked out/in, SPI controllers might need to be enhanced (when possible) to sample data from AD4000 devices connected in "3-wire" mode.

Lastly, here an overview of the [STRIKEOUT:mess] test setups for RPI 4 and CoraZ7 with :adi:`EVAL-ADAQ40xx`.

|image22| |image23|

.. |image1| image:: https://wiki.analog.com/_media/software/linux/docs/spi/adaq4003_reg_read.png
.. |image2| image:: https://wiki.analog.com/_media/software/linux/docs/spi/adaq4003_reg_write.png
.. |image3| image:: https://wiki.analog.com/_media/software/linux/docs/spi/adaq4003-3wire-connection.png
.. |image4| image:: https://wiki.analog.com/_media/software/linux/docs/spi/adaq4003_sample_read.png
.. |image5| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-reg-read1.jpg
.. |image6| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-reg-write1.jpg
.. |image7| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-reg-read2.jpg
.. |image8| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-sample-read1.jpg
.. |image9| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-sample-read2.jpg
.. |image10| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-sample-read-ff1.jpg
.. |image11| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-sample-read-ff2.jpg
.. |image12| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-gpio-reg-read1.jpg
.. |image13| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-gpio-reg-write1.jpg
.. |image14| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-gpio-reg-read2.jpg
.. |image15| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-gpio-sample-read1.jpg
.. |image16| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-gpio-sample-read2.jpg
.. |image17| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-engine-reg-read1.jpg
.. |image18| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-engine-reg-write1.jpg
.. |image19| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-engine-reg-read2.jpg
.. |image20| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-engine-sample-read1.jpg
.. |image21| image:: https://wiki.analog.com/_media/software/linux/docs/spi/spi-engine-sample-read2.jpg
.. |image22| image:: https://wiki.analog.com/_media/software/linux/docs/spi/adaq4003-rpi-setup.jpg
.. |image23| image:: https://wiki.analog.com/_media/software/linux/docs/spi/adaq4003-cora-setup.jpg
