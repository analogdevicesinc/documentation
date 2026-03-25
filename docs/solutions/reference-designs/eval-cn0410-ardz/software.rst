.. _eval-cn0410-ardz software:

Software Guide
==============

The EVAL-CN0410-ARDZ demo software runs on the :adi:`EVAL-ADICUP3029` platform
and provides per-channel LED current control via a serial terminal interface.

.. figure:: images/cn0410_demo.jpg
   :align: center
   :width: 500

   EVAL-CN0410-ARDZ with EVAL-ADICUP3029

Demo Requirements
-----------------

**Hardware**

- :adi:`EVAL-ADICUP3029` development board
- EVAL-CN0410-ARDZ evaluation board
- Micro-USB to USB cable
- PC or laptop with a USB port

**Software**

- ADuCM3029_demo_cn0410 application
- CrossCore Embedded Studio (2.6.0 or higher)
- ADuCM302x DFP (2.0.0 or higher)
- ADICUP3029 BSP (1.0.0 or higher)
- Serial terminal program (such as PuTTY or Tera Term)

Setting up the Hardware
-----------------------

#. Connect the EVAL-CN0410-ARDZ shield to the :adi:`EVAL-ADICUP3029`.
#. Configure the chip select jumper (P21) as needed (default: GPIO 8).
#. Connect a micro-USB cable to the P10 connector on the EVAL-ADICUP3029 and
   connect it to a computer.

Configuring the Software
-------------------------

The software for EVAL-CN0410 does not require any particular configurations in
order to set up the application. The only setting that the user could modify is
the selection of the CS pin. This can be done by modifying the ``SYNC_PORT``
and ``SYNC_PIN`` inside ``adi_cn0410.h``:

.. code-block:: c

   #define SYNC_PORT   ADI_GPIO_PORT1  // this is the CS pin
   #define SYNC_PIN    ADI_GPIO_PIN_12

Outputting Data
---------------

After the application starts, the user can send commands to set the output of
the DAC channels.

**Available commands:**

.. list-table::
   :header-rows: 1

   * - Command
     - Description
   * - ``set_a <value>``
     - Set DAC channel A output (0--65535)
   * - ``set_b <value>``
     - Set DAC channel B output (0--65535)
   * - ``set_c <value>``
     - Set DAC channel C output (0--65535)
   * - ``set_zero``
     - Reset all channels to 0

.. figure:: images/cn0410_putty.png
   :align: center
   :width: 500

   Serial Terminal Output Example

Serial Terminal Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the serial terminal with the following settings:

- **Baud rate**: 9600
- **Data bits**: 8
- **Parity**: None
- **Stop bits**: 1
- **Flow Control**: None

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for
the CN0410:

#. **Drag and Drop** -- Copy the ``.hex`` file to the DAPLINK drive. This is
   the easiest way to get started.
#. **Build and Debug using CCES** -- Import the project into CrossCore Embedded
   Studio to change parameters and customize the software.

**Downloads:**

- `Prebuilt CN0410 Hex File
  <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0410.hex>`__
- `CN0410 Source Code
  <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0410>`__

Project Structure
-----------------

The project is structured in three sections:

- **source** -- Contains the communication, timer, and main modules
- **include** -- Header files
- **sensors** -- DAC driver

.. figure:: images/cn0410_struct.png
   :align: center
   :width: 250

   Project Structure
