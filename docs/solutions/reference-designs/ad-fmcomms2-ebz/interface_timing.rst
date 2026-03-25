.. _ad-fmcomms2-ebz-interface-timing:

Digital Interface Timing Validation
====================================

The FMCOMMS2/3/4/5 boards featuring :adi:`AD9361` have a digital tuning
feature (programmable IO delay), and in most cases the FPGA features
programmable IO delay elements as well. The software tunes this interface for
an optimal delay setting, ensuring that the interface works over part-to-part
variations (AD9361 and the baseband/FPGA), voltage, temperature, interface
speeds, and across different carrier boards (trace differences in PCB layout).

The tuning may be done either in FPGA, AD9361, or both (though not necessary).
In the ADI reference designs and software, only the AD9361 tuning is used,
since not all FPGA devices have programmable IO delays.

Tuning Algorithm
----------------

The tuning algorithm works as follows:

**Receive Path (tuned first)**:

#. The AD9361 is programmed to generate a PRBS (pseudo-random binary sequence)
   BIST pattern at the digital interface.
#. A corresponding sequence monitor is implemented in the FPGA.
#. The delay is swept from minimum to maximum, monitoring the status signals.
   The function sweeps all data delays (0..15) and then all clock delays
   (0..15).
#. This happens at three different interface rates: 25 MSPS (low), 40 MSPS,
   and 61.44 MSPS (high).
#. All pass/fail results are stored, and the low and high rate results are
   overlaid.
#. The optimal delay is selected as the midpoint of the range where the
   monitor locks.

**Transmit Path (tuned second)**:

Since the AD9361 has no monitors in the transmit path, it is set to digital
loopback mode. Individual PRBS patterns are sent from the FPGA in the transmit
path and monitored in the receive path. The optimal delay is calculated the
same way as for receive.

FIR Filter Considerations
--------------------------

When enabling the FIR filter blocks inside the AD9361, the data/clock delay
slightly shifts. When running with a high baseband sample rate of 61.44 MSPS,
the delays computed during driver initialization may not work with FIR enabled.
For this reason, the interface tuning algorithm is always re-run whenever a
filter is enabled at the target baseband rate. If the FIR is disabled, the
original settings are restored.

Interface tuning upon FIR enable can be omitted by setting:

- **Linux**: ``adi,digital-interface-tune-fir-disable`` device tree attribute
- **No-OS**: ``init_param->digital_interface_tune_fir_disable``

BIST Timing Analysis
--------------------

The ``bist_timing_analysis`` debugfs file performs a 2D print of all clock and
data delay combinations on RX at a given baseband rate:

- ``o`` = PASS
- ``.`` = FAIL

.. code-block:: bash

   root@analog:/sys/kernel/debug/iio/iio:device1# echo 1 > bist_timing_analysis
   root@analog:/sys/kernel/debug/iio/iio:device1# cat bist_timing_analysis
   CLK: 10000000 Hz 'o' = PASS
   DC0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:. . . . . . . . . . . . . . . .
   1:. . . . . . . . . . . . . . . .
   ...
   8:o . . . . . . . . . . . . . . .
   9:o o . . . . . . . . . . . . . .
   a:o o o . . . . . . . . . . . . .
   ...
   f:o o o o o o o o . . . . . . . .

In this output, clock delays are on the horizontal axis and data delays on the
vertical axis. The ``ad9361_dig_tune()`` function overlays results from multiple
rates to select the optimal delay.

Skip Mode
----------

In some cases the full timing analysis is not required, for example on well
understood custom board designs where layout is fixed and properly matched.

.. list-table::
   :header-rows: 1

   * - AD9361/4 Driver
     - Method
     - Values
   * - Linux
     - ``adi,digital-interface-tune-skip-mode`` (device tree)
     - 0, 1, 2
   * - No-OS
     - ``init_param->digital_interface_tune_skip_mode``
     - 0, 1, 2

.. list-table::
   :header-rows: 1

   * - Skip Mode Value
     - Explanation
   * - 0
     - Perform RX and TX path tune
   * - 1
     - Perform RX and skip TX path tune, use default TX CLK/DATA delay values
   * - 2
     - Skip RX and TX path tune, use default RX/TX CLK/DATA delay values

Default RX/TX CLK/DATA delay values can be configured with:

.. list-table::
   :header-rows: 1

   * - Linux Device Tree Attribute
     - No-OS Init Parameter
     - Range
   * - ``adi,delay-rx-data``
     - ``init_param->delay_rx_data``
     - 0..15
   * - ``adi,rx-data-clock-delay``
     - ``init_param->rx_data_clock_delay``
     - 0..15
   * - ``adi,rx-data-delay``
     - ``init_param->rx_data_delay``
     - 0..15
   * - ``adi,tx-fb-clock-delay``
     - ``init_param->tx_fb_clock_delay``
     - 0..15

Debugging
---------

When running into failures, enable extended debugging information by adding
``BE_VERBOSE`` and ``BE_MOREVERBOSE`` flags in the ``ad9361_post_setup()``
function:

.. code-block:: c

   /* Change: flags = 0; to: */
   flags = BE_VERBOSE | BE_MOREVERBOSE;

With these flags set, kernel messages will show detailed pass/fail tables for
each sample rate and RX/TX path, allowing identification of the optimal delay
selection.

Runtime API
~~~~~~~~~~~

The ``digital_tune`` debugfs file takes two arguments:

#. Whether to tune on the current baseband rate only (``0``) or on all three
   rates like during initialization (``1``).
#. A bitmask flag for verbosity level (recommended: ``1`` or ``3``).

.. code-block:: c

   enum dig_tune_flags {
       BE_VERBOSE       = 1,
       BE_MOREVERBOSE   = 2,
       DO_IDELAY        = 4,
       DO_ODELAY        = 8,
       SKIP_STORE_RESULT = 16,
       RESTORE_DEFAULT  = 32,
   };

Example:

.. code-block:: bash

   # Current baseband rate only, verbose output
   root@analog:/sys/kernel/debug/iio/iio:device1# dmesg -n7
   root@analog:/sys/kernel/debug/iio/iio:device1# echo 0 3 > digital_tune
