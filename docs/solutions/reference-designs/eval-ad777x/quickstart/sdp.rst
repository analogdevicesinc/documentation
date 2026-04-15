.. _eval-ad777x quickstart sdp:

SDP-K1 / Nucleo-L552ZEQ Quick start
===============================================================================

.. figure:: ../images/nucleo.jpeg
   :alt: Nucleo-L552ZEQ controller board

   Nucleo-L552ZEQ controller board

.. esd-warning::

This guide provides step-by-step instructions on how to set up the
:adi:`EVAL-AD7770-AD7779` with an SDP-K1 or Nucleo-L552ZEQ controller
board using the IIO firmware application.

.. note::

   This guide covers the legacy SDP-K1 / Nucleo-L552ZEQ setup using
   MBED and STM32 firmware via UART. For the recommended Linux-based
   setup on a ZedBoard, see :ref:`eval-ad777x quickstart zed`.

Overview
-------------------------------------------------------------------------------

The firmware application leverages the ADI IIO ecosystem to evaluate the
AD777x family. It runs on the SDP-K1 (MBED platform) or Nucleo-L552ZEQ
(STM32 platform) and communicates with IIO Oscilloscope on the host PC
over UART.

.. figure:: ../images/block_diagram.jpeg
   :alt: IIO ecosystem block diagram
   :width: 600

   IIO ecosystem block diagram

Hardware connections
-------------------------------------------------------------------------------

SDP-K1 (MBED platform)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect the VIO_ADJUST jumper on the SDP-K1 board to the 3.3V position
  to drive SDP-K1 GPIOs at 3.3V.

Nucleo-L552ZEQ (STM32 platform)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Refer to the `Nucleo-L552ZEQ User Manual
  <https://www.st.com/content/ccc/resource/technical/document/user_manual/group1/ad/a4/bd/5e/14/15/4e/e8/DM00615305/files/DM00615305.pdf/jcr:content/translations/en.DM00615305.pdf>`_
  for board-level details.

EVAL-AD777x
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Refer to the AD777x evaluation board user guide available on the
  respective device product pages for board-level details.

.. figure:: ../images/stm_diagram_updated.jpeg
   :alt: STM32 hardware connection diagram
   :width: 800

   STM32 hardware connection diagram

Firmware
-------------------------------------------------------------------------------

The firmware source code is hosted in the
:git-precision-converters-firmware:`/`
repository.

app_config.h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file is used to configure the firmware:

- Select the active device by changing ``#define DEV_AD7770`` (default is
  AD7770).
- Select the platform by setting ``#define ACTIVE_PLATFORM`` to
  ``MBED_PLATFORM`` or ``STM32_PLATFORM``.
- Set ``DATA_CAPTURE_MODE`` to ``CONTINUOUS_DATA_CAPTURE`` or
  ``BURST_DATA_CAPTURE``.
- Set ``INTERFACE_MODE`` to ``SPI_MODE`` or ``TDM_MODE``.

.. important::

   The maximum output data rate can only be achieved with ``TDM_MODE``
   on the STM32 platform. ``SPI_MODE`` limits the maximum achievable ODR.

Running IIO Oscilloscope
-------------------------------------------------------------------------------

Open IIO Oscilloscope on the host PC and configure the serial (UART)
settings. Click Refresh - the AD777x device should appear in the IIO
devices list.

.. figure:: ../images/ad77x_iio_osc_init.jpeg
   :alt: IIO Oscilloscope serial connection settings
   :width: 800

   IIO Oscilloscope serial connection settings

Click Connect. The data Capture window opens by default. You can drag it
aside or close it to access the Debug and DMM tab.

.. figure:: ../images/ad777x_iio_osc_windows.jpeg
   :alt: IIO Oscilloscope main window after connecting
   :width: 600

   IIO Oscilloscope main window after connecting

Select the device from the Device list in the Debug tab to access all
device and channel attributes.

.. figure:: ../images/ad777x_debug_window.jpeg
   :alt: IIO Oscilloscope debug window with AD777x attributes
   :width: 800

   IIO Oscilloscope debug window with AD777x attributes

Device attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IIO Oscilloscope exposes two types of attributes:

- **Device attributes** - global parameters common to the device.
- **Channel attributes** - parameters specific to individual channels.

To read an attribute, select it from the list and press Read. To write,
set the value in the value field and press Write.

DMM tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The DMM tab reads the instantaneous voltage on analog input channels.
Select the device and channels, then press Start.

.. figure:: ../images/ad777x_dmm_tab.jpeg
   :alt: IIO Oscilloscope DMM tab
   :width: 400

   IIO Oscilloscope DMM tab

.. note::

   DMM reads instantaneous values only - RMS AC or averaged DC voltage
   is not available. Do not use the DMM tab simultaneously with the
   Capture or Debug tab.

Data capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the device and channels in the Capture window to start data
capture. Data is plotted as ADC raw value vs. number of samples.

.. warning::

   Do not access the DMM or Debug tab while capturing data - this
   impacts capture. DMM uses single conversion; data capture uses
   continuous conversion mode.

- Time domain plot:

  .. figure:: ../images/ad777x_plot_window.jpeg
     :alt: AD777x time domain capture in IIO Oscilloscope
     :width: 800

     AD777x time domain capture in IIO Oscilloscope

Register map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Register Map tab provides byte-level access to the device registers.

.. figure:: ../images/ad777x_register_access.jpeg
   :alt: IIO Oscilloscope register map tab
   :width: 600

   IIO Oscilloscope register map tab

Useful links
-------------------------------------------------------------------------------

- :git-no-OS:`AD777x no-OS drivers <drivers/adc/ad7779>`
- :adi:`AD7770`
- :adi:`AD7771`
- :adi:`AD7779`
