.. _eval-ad7616-sdz user-guide:

User guide
===============================================================================

HDL reference design
-------------------------------------------------------------------------------

An in-depth presentation and instructions about the HDL design can be found in
the :external+hdl:ref:`HDL User Guide <user_guide>`. For a detailed description
of the ``axi_ad7616`` core, refer to its documentation page.

Data path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HDL data path is structured as follows:

- The **parallel** interface is controlled by the ``axi_ad7616`` IP core.
- The **serial** interface is controlled by the **SPI Engine Framework**.
- Data is written into memory by a DMA (``axi_dmac`` core).
- All control pins of the device are driven by GPIOs.

Switching between interface types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before powering up the board, choose the required interface and configure the
hardware jumpers as described in the quickstart guide for your carrier. Then
build the HDL project with the matching parameter:

Serial interface:

.. code-block:: bash

   $ make SER_PAR_N=1

Parallel interface:

.. code-block:: bash

   $ make SER_PAR_N=0

CPU/memory interconnect addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Instance
     - Address
   * - axi_ad7616_dma
     - 0x44A30000
   * - ad7616_pwm_gen
     - 0x44B00000
   * - spi_ad7616_axi_regmap
     - 0x44A00000
   * - axi_ad7616
     - 0x44A80000

.. note::

   - ``spi_ad7616_axi_regmap`` is instantiated only when ``SER_PAR_N=1``
   - ``axi_ad7616`` is instantiated only when ``SER_PAR_N=0``

PL interrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PS7 EMIO offset = 54

.. list-table::
   :header-rows: 1

   * - Instance
     - HDL interrupt
     - PS7 interrupt
   * - ---
     - 0
     - 89
   * - ---
     - 1
     - 90
   * - ---
     - 2
     - 91
   * - ---
     - 3
     - 92
   * - ---
     - 4
     - 93
   * - ---
     - 5
     - 94
   * - ---
     - 6
     - 95
   * - ---
     - 7
     - 96
   * - ---
     - 8
     - 104
   * - ---
     - 9
     - 105
   * - axi_ad7616
     - 10
     - 106
   * - ---
     - 11
     - 107
   * - spi_ad7616
     - 12
     - 108
   * - axi_ad7616_dma
     - 13
     - 109
   * - ---
     - 14
     - 110
   * - ---
     - 15
     - 111

.. note::

   - ``spi_ad7616`` is instantiated only when ``SER_PAR_N=1``
   - ``axi_ad7616`` is instantiated only when ``SER_PAR_N=0``

GPIO signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PS7 EMIO offset = 54

.. list-table::
   :header-rows: 1

   * - GPIO signal
     - GPIO number
     - HDL GPIO number
   * - adc_reset_n
     - 97
     - 43
   * - adc_hw_rngsel
     - 96–95
     - 42–41
   * - adc_os
     - 94–92
     - 40–38
   * - adc_seq_en
     - 91
     - 37
   * - adc_burst
     - 90
     - 36
   * - adc_chsel
     - 89–87
     - 35–33
   * - adc_crcen
     - 86
     - 32

Downloads
-------------------------------------------------------------------------------

- :git-hdl:`HDL project <projects/ad7616_sdz>`
- :git-no-OS:`No-OS project (ZedBoard/ZC706) <projects/ad7616-sdz>`
- :git-no-OS:`No-OS project (SDP-K1) <projects/ad7616-st>`
