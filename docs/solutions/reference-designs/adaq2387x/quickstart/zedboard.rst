.. _eval-adaq23875-fmcz quickstart zedboard:

ZedBoard Quickstart
===============================================================================

This guide provides step-by-step instructions on how to set up the
:adi:`EVAL-ADAQ23875FMCZ <EVAL-ADAQ23875>` on the:

- :xilinx:`ZedBoard (AES-Z7EV-7Z020-G) <products/boards-and-kits/1-8dyf-11.html>`
  FMC LPC connector

.. esd-warning::

Required Hardware
-------------------------------------------------------------------------------

- :xilinx:`ZedBoard (AES-Z7EV-7Z020-G) <products/boards-and-kits/1-8dyf-11.html>`
  and its 12 V DC power supply
- :adi:`EVAL-ADAQ23875FMCZ <EVAL-ADAQ23875>` evaluation board
- SD card (16 GB or larger)
- LAN cable (Ethernet)
- SMA cable
- XLR-to-SMA adapter cable
- Low-noise signal source (e.g. Audio Precision APX525 audio analyser)
- Host PC running Windows 10 or higher

Required Software
-------------------------------------------------------------------------------

- :external+kuiper:doc:`Analog Devices Kuiper Linux <index>` image
- :ref:`IIO Oscilloscope <iio-oscilloscope>` (installed on host PC)

More details on why you need these can be found at
:ref:`eval-adaq23875-fmcz prerequisites`.

Setting Up the SD Card
-------------------------------------------------------------------------------

Loading the Kuiper Linux Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full instructions for downloading and flashing the Kuiper Linux image are
available at :external+kuiper:doc:`Kuiper Linux <index>`.

.. note::

   Use the **CN0577** Kuiper image for the EVAL-ADAQ23875FMCZ.

Configuring the SD Card for EVAL-ADAQ23875FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After flashing the Kuiper image, copy the following files to the **root
(boot) folder** of the SD card:

- ``BOOT.BIN``
- ``devicetree.dtb``
- ``uImage`` (from the ``zynq-common`` folder of the Kuiper image)

Hardware Connection
-------------------------------------------------------------------------------

.. image:: ../images/hardware-connection-adaq23875.jpg
   :align: center
   :width: 600

Perform the following steps **with all equipment powered off**:

#. Insert the configured SD card into the ZedBoard SD card slot.
#. Attach the EVAL-ADAQ23875FMCZ to the ZedBoard via the FMC LPC connector.
   Ensure all pins are fully seated and properly aligned.
#. Connect the LAN cable between the ZedBoard and your network switch or
   directly to the host PC.
#. Connect the XLR-to-SMA adapter cable between the Audio Precision analyser
   output and the SMA input connectors (VIN+ and VIN−) on the evaluation board.
#. Connect the Audio Precision analyser USB cable to the host PC.
#. Power on the ZedBoard using the 12 V DC cable.

Navigating the IIO Oscilloscope
-------------------------------------------------------------------------------

Download and install the latest release of IIO Oscilloscope from the
`IIO Oscilloscope GitHub releases <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`__.

Main Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main window displays a configuration panel (plugin) for each IIO device
recognised on the network. Plugins can be detached by clicking the button on
the right side of the plugin name bar; closing a detached window reattaches it.

Additional plugins for debugging and monitoring are also available:

Debug Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Debug plugin provides low-level access to IIO device attributes and
registers.

- **Device Selection** — sets the active IIO device
- **IIO Device Attributes** — read/write device attributes
- **Register Section**:

  - *Address* — register address field
  - *Value* — value at the given address
  - *Enable AutoRead* — automatically re-reads the register as the address
    changes

DMM Plugin (Digital Multimeter)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The DMM plugin continuously displays device-specific channel data once the
Start button is activated.

- **Device tab** — lists all available IIO devices
- **Active channels tab** — lists enabled channels (use **All Channels** to
  enable all)
- **Right panel** — displays live data readings for enabled channels

Capture Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The capture window provides time-domain and frequency-domain plotting.

**Menu options:**

- *File* → Save As, Quit
- *Edit* → Plot Title
- *View* → Show Settings, Full Screen

**Plot controls:**

- Capture/Stop — start or stop data capture
- Zoom In / Zoom Out / AutoZoom
- Save As — save captured data to a file
- Full Screen
- Auto scale — automatically rescale the visible area
- Show grid — toggle grid display
- Y Max / Y Min — manual vertical axis limits (when Auto scale is disabled)
- New Plot — open a new plot of the same type

**Plot types:**

*Time Domain*

Displays raw samples in the time domain.

- *Sample Count* — number of samples to capture
- *Graph Type* — lines or dots

*Frequency Domain*

Performs an FFT on the captured signal.

- *FFT size* — number of samples for the FFT
- *Window* — FFT window function (see :dokuwiki:`window functions <resources/tools-software/linux-software/iio_oscilloscope/window_functions>`)
- *FFT Average* — averaging weight applied to successive FFT frames
- *PWR Offset* — vertical offset applied to the FFT plot

*Constellation*

I-channel on the x-axis, Q-channel on the y-axis.

*Cross Correlation*

Cross-correlation between two channels.

**Markers** (frequency domain and cross-correlation):

Markers are activated via right-click on the plot (capture must be running and
the appropriate domain selected):

- Single channel: Peak, Fixed, Single Tone
- Dual channel: Peak, Fixed, Single Tone, Image
- Constellation: Peak Marker

Five markers are displayed by default; additional markers can be added or
removed via the right-click menu.

**Saving captured data:**

Supported export formats: Agilent VSA, CSV, MAT (.mat), PNG.

Evaluating the EVAL-ADAQ23875FMCZ
-------------------------------------------------------------------------------

#. Launch IIO Oscilloscope on the host PC.
#. Click **Refresh** to discover available IIO devices on the network.
#. When ``ltc2387`` appears in the device list, click **Connect**.
#. In the Capture window, set the plot type to **Frequency Domain**.
#. Under *FFT size*, select the preferred number of samples.
#. Set the *Window* function to **Blackman-Harris**.
#. Press **Run** to start capturing data and view the FFT result.

.. figure:: ../images/waveform-plot-adaq23875.png
   :align: center
   :width: 700

   Time domain waveform capture

.. figure:: ../images/fft-plot-adaq23875.png
   :align: center
   :width: 700

   Frequency domain FFT capture
