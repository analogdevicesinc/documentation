AXI ADC No-OS Driver
====================

Description
-----------

The AXI ADC HDL driver is the driver for :doc:`Generic AXI ADC IP core </wiki-migration/resources/fpga/docs/axi_adc_ip>` which is used on various FPGA designs. The driver is implemented as an Linux IIO driver. It's register map can be found here: :doc:`Base register map (common to all cores) </wiki-migration/resources/fpga/docs/hdl/regmap>`

Initialization example
======================

.. code:: c

   struct axi_adc_init rx_adc_init = {
       .name = "rx_adc",
       .base = RX_CORE_BASEADDR,
       .num_channels = 2,
   };
   struct axi_adc *rx_adc;

   /* Initialize the ADC core */
   status = axi_adc_init(&rx_adc, &rx_adc_init);
   if (status != 0) {
       printf("axi_adc_init() error: %"PRIi32"\n", status);
       return status;
   }

Code Documentation
------------------

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available at:

-  `AXI ADC Core Header file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__adc__core_8h.html>`__
-  `AXI ADC Core Source file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__adc__core_8c.html>`__

Source Code
===========

.. admonition:: Download
   :class: download

   
   -


   
   |Implementation of AXI ADC Core Driver.|

   -

   |Header of AXI ADC Core Driver.|

.. |Implementation of AXI ADC Core Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/axi_adc_core/axi_adc_core`.c
.. |Header of AXI ADC Core Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/axi_adc_core/axi_adc_core`.h
