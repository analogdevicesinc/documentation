AXI_AD7606x
===========

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_ad7606x/index.html\


Overview
--------

| The :git-hdl:`library/axi_ad7606x` IP core can be used to interface the :adi:`AD7606B`, :adi:`AD7606C-16` and :adi:`AD7606C-18` devices using an FPGA. The core supports the parallel data interface of the device, and has a simple FIFO interface for the DMAC.
| More about the generic framework interfacing ADCs, that contains the up_adc_channel and up_adc_common modules, can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`.

Block diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_ad7606_ip_diagr_v2.svg
   :align: center

Configuration parameters
------------------------

+-----------------------+-----------------------------------------------------------------------------------------+---------------+
| Name                  | Description                                                                             | Default Value |
+=======================+=========================================================================================+===============+
| ``ID``                | Core ID, it can be used in case of multiple cores on a system                           | 0             |
+-----------------------+-----------------------------------------------------------------------------------------+---------------+
| ``DEV_CONFIG``        | Defines the device which will be used: 0 - AD7606B, 1 - AD7606C-16, 2 - AD7606C-18      | 0             |
+-----------------------+-----------------------------------------------------------------------------------------+---------------+
| ``ADC_TO_DMA_N_BITS`` | Defines the number of bits to be transmitted to DMA: 16 - AD7606B/C-16, 32 - AD7606C-18 | 16            |
+-----------------------+-----------------------------------------------------------------------------------------+---------------+
| ``ADC_N_BITS``        | Defines the number of bits of each device: 16 - AD7606B/C-16, 18 - AD7606C-18           | 16            |
+-----------------------+-----------------------------------------------------------------------------------------+---------------+
| ``ADC_READ_MODE``     | Defines the ADC Read Mode option: 0 - Simple, 1 - STATUS, 2 - CRC, 3 - CRC_STATUS       | 0             |
+-----------------------+-----------------------------------------------------------------------------------------+---------------+
| ``EXTERNAL_CLK``      | Defines the external clock option for the ADC clock: 0 - No, 1 - Yes                    | 0             |
+-----------------------+-----------------------------------------------------------------------------------------+---------------+

Interface
---------

+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
| Interface   | Pin                                   | Type             | Description                                                                              |
+=============+=======================================+==================+==========================================================================================+
| ``rx_*``    | **Parallel data/control interface**   |                  |                                                                                          |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``rx_db_o``                           | ``output[15:0]`` | Parallel data out                                                                        |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``rx_db_i``                           | ``input[15:0]``  | Parallel data in                                                                         |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``rx_db_t``                           | ``output``       | Active high 3-state T pin for IOBUF                                                      |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``rx_rd_n``                           | ``output``       | Active low parallel data read control                                                    |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``rx_wr_n``                           | ``output``       | Active low parallel data write control                                                   |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``rx_cs_n``                           | ``output``       | Active low chip select                                                                   |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``external_clk``                      | ``input``        | External clock if the corresponding option is enabled                                    |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``rx_busy``                           | ``input``        | Active low busy signal                                                                   |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``rx_first_data``                     | ``input``        | Active high status signal indicating when the first channel is available on the data bus |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
| ``s_axi_*`` | **AXI Slave Memory Map interface**    |                  |                                                                                          |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
| ``adc_*``   | **Write FIFO interface for the DMAC** |                  |                                                                                          |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``adc_valid``                         | ``output``       | Shows when a valid data is available on the bus                                          |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``adc_data_x``                        | ``output[15:0]`` | ADC data channels (x - channel number)                                                   |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``adc_enable_x``                      | ``output``       | ADC enable signal for each channel                                                       |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``adc_clk``                           | ``output``       | ADC clock                                                                                |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+
|             | ``adc_dovf``                          | ``input``        | ADC data overflow signaling                                                              |
+-------------+---------------------------------------+------------------+------------------------------------------------------------------------------------------+

Register map
------------

The register map of the core contains instances of several generic register maps like ADC common, ADC channel or PWM Generator. The following table presents the base addresses of each instance, after that can be found the detailed description of each generic register map.

.. include:: hdl/regmap.rst .. include:: hdl/regmap.rst .. include:: hdl/regmap.rst .. include:: hdl/regmap.rst

Theory of operation
-------------------

The axi_ad7606x IP can be configured in various operation modes, this feature being integrated in the device register map. Thus, to be able to configure the operation mode and any other features available through the mentioned register map, **adc_config_ctrl** signal, that is available in the *up_adc_common* module, is used in this way: bit 1 - RD ('b1) \| WR ('b0) and bit 0 - enable WR/RD operation.

ADC Register Mode (AD7606x familiy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As regards the register mode, AD7606x family devices have the following workflow: DB[15] - RD ('b0) \| WR ('b1), DB[14:8] - register address and DB[7:0] - register data or don't care data. Besides the data output signal, WR_N and RD_N signals are also used in order to make a write or read request to the device. The following timing diagram shows a parallel interface register read operation followed by a write operation.

.. tip::

   In case of the :adi:`AD7606C-18` chip, the **x** identifier, this being the number of the DB pins, will be the **x** identifier from the :adi:`AD7606B` or :adi:`AD7606C-16` chips + 2 (e.g. DB0 from :adi:`AD7606B` or :adi:`AD7606C-16` will be DB2 in :adi:`AD7606C-18`. The pinout of the :adi:`AD7606C-18` chip can be obtained from the page 12 of the :adi:`AD7606C-18 Datasheet <media/en/technical-documentation/data-sheets/ad7606c-18.pdf>`.


.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_reg_mode_ad7606x_fam.png
   :align: center

The following timing diagrams illustrate available ADC read modes using the AD7606x family devices.

ADC Read Mode (AD7606B/C-16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_read_mode_ad7606b_c-16.png
   :align: center

ADC Read Mode (AD7606C-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/ad8283/adc_read_mode_ad7606c-18.png
   :align: center

ADC Read Mode with CRC enabled (AD7606B/C-16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_crc_ad7606b_c-16.png
   :align: center

ADC Read Mode with CRC enabled (AD7606C-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_crc_ad7606c-18.png
   :align: center

ADC Read Mode with Status enabled (AD7606B/C-16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_status_ad7606b_c-16.png
   :align: center

ADC Read Mode with Status enabled (AD7606C-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_status_ad7606c18.png
   :align: center

ADC Read Mode with Status and CRC enabled (AD7606B/C-16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_status_ad7606b_c-16_crc.png
   :align: center

ADC Read Mode with Status and CRC enabled (AD7606C-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adc_status_ad7606c-18_crc.png
   :align: center

Software Support
----------------

Analog Devices recommends to use the provided software drivers.

References
----------

-  :git-hdl:`axi_ad7606x IP source code <library/axi_ad7606x>`
   \* :adi:`AD7606B Information <ad7606B>`
   \* :adi:`AD7606C-16 Information <ad7606C-16>`
   \* :adi:`AD7606C-18 Information <ad7606C-18>`
   \* :adi:`AD7606B Documentation <media/en/technical-documentation/data-sheets/ad7606b.pdf>`
   \* :adi:`AD7606C-16 Documentation <media/en/technical-documentation/data-sheets/ad7606c-16.pdf>`
   \* :adi:`AD7606C-18 Documentation <media/en/technical-documentation/data-sheets/ad7606c-18.pdf>`
   \* :adi:`EVAL-AD7606B Information <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7606b-fmcz.html>`
   \* :adi:`EVAL-AD7606C-16/18 Information <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7606c-18.html>`
   \* `EVAL-AD7606B User Guide <https://www.analog.com/media/en/[[adi>media/en/technical-documentation/user-guides/EVAL-AD7606BFMCZ-UG-1225.pdf>`__
   \* :adi:`EVAL-AD7606C-16/18 User Guide <media/en/technical-documentation/user-guides/eval-ad7606c-fmcz-ug-1870.pdf>`
   \* :doc:`AD7606X FMC HDL Reference Design </wiki-migration/resources/eval/user-guides/ad7606x-fmc/hdl>`

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
