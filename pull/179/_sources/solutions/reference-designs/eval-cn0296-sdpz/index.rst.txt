.. _eval-cn0296-sdpz:

EVAL-CN0296-SDPZ
=================

Multi-Channel Sound Bar Audio System.

Overview
--------

:adi:`CN0296` is a low-cost, high-performance sound bar system that can accept
an analog stereo audio signal as an input and can output up to eight channels
of audio with discrete processing on each channel. The circuit is ideal for
small docking stations and portable media devices. It offers low power
consumption and high efficiency operation without sacrificing audio quality.
The circuit is also capable of driving headphones without the need for
additional components.

The :adi:`ADAU1761` is a low-power, stereo audio codec with integrated digital
audio processing (SigmaDSP). It has two ADCs to accept two audio channels and
can apply digital processing with the integrated SigmaDSP core. SigmaDSP
processors are optimized for audio applications and programmed using
SigmaStudio development software for ease of use and faster development. Its
output can send up to eight channels of digital audio data to the output
amplifiers using the serial interface. It allows different audio signal
processing in each channel, such as volume control, custom equalization,
filtering, and spatialization effects tuned to the specific speaker
configuration. The :adi:`ADAU1761` processes and converts analog audio to
digital format and drives the :adi:`SSM2518` power amplifier.

The :adi:`SSM2518` is a digital-input class-D audio power amplifier that can
output two channels of audio with a continuous power of 2 W each into a 4 Ohm
load. Its channel-mapping feature allows it to select the specific channel to
output among those that are available in the interface. This makes it ideal for
surround sound applications.

Required Equipment
------------------

- :adi:`EVAL-CN0296-SDPZ <CN0296>` evaluation board
- :adi:`EVAL-SDP-CB1Z` evaluation board (SDP-B board)
- CN0296 Evaluation Software (supplied with provided CD in kit)
- +5 V DC power supply
- USB Type-A to USB Mini-B cable
- 4 Ohm or 8 Ohm speakers, rated at least 2 W

Minimum PC/System Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Windows XP SP2, Windows Vista, or Windows 7
  Business/Enterprise/Ultimate editions
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM and 2 GB available hard disk space
- .NET 3.5 Framework

Installing the Software
------------------------

#. Extract the file **CN0296 Eval Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0296 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0296\`` and
      all National Instruments products to
      ``C:\Program Files\National Instruments\``.

   .. figure:: destination_directory.png

      CN0296 Evaluation Software destination directory.

#. Click **Next** to view the installation review page.

   .. figure:: cn0296_evaluation_software_files.png

      CN0296 Evaluation Software installation review.

#. Click **Next** to start the installation.

   .. figure:: cn0296_evaluation_software_files_2.png

      CN0296 Evaluation Software installation progress.

#. Upon completion of the installation of the **CN0296 Evaluation Software**,
   the installer for the **ADI SDP Drivers** will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: adi_sdp_drivers.png

      ADI SDP Drivers installer.

#. Press **Next** to set the installation location for the **SDP Drivers**.

   It is recommended that you install the drivers to the default directory
   path ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: adi_sdp_drivers_2.png

      ADI SDP Drivers destination directory.

#. Press **Next** to install the **SDP Drivers** and complete the installation
   of all software. Click **Finish** when done.

   .. figure:: adi_sdp_drivers_4.png

      ADI SDP Drivers installation complete.

Hardware Setup
--------------

.. figure:: hardware_setup.png

   EVAL-CN0296-SDPZ hardware setup.

#. Connect the 120-pin connector on the :adi:`EVAL-CN0296-SDPZ <CN0296>`
   circuit board to the connector marked **CON A** on the :adi:`EVAL-SDP-CB1Z`
   evaluation (SDP) board. Nylon hardware should be used to firmly secure the
   two boards, using the holes provided at the ends of the 120-pin connectors.

#. Plug the mini end of the USB cable into connector **J2** of the
   :adi:`EVAL-SDP-CB1Z` and connect the other end of the USB cable to the PC.

#. Plug in the wall wart and connect it to connector **J2** of the
   :adi:`EVAL-CN0296-SDPZ <CN0296>`.

#. Populate a jumper across **P6** and **P11**.

#. Connect speakers to the designated male headers.

Opening and Enabling the Evaluation Software
----------------------------------------------

.. figure:: cn0296_gui_1.png

   CN0296 Evaluation Software GUI.

#. Launch the executable found at
   ``C:\Program Files\Analog Devices\CN0296`` and press the **Connect**
   button.

#. After pressing the **Connect** button, a prompt will appear informing the
   user if the SDP is already connected.

#. Press the **Play Soundbar** button to start using the functions of the
   sound bar.

Using the Evaluation Software
------------------------------

The following software controls are grouped according to their location in the
software GUI:

System Controls
~~~~~~~~~~~~~~~~

- **Connect** -- Configures the :adi:`ADAU1761` and :adi:`SSM2518` by writing
  the necessary registers. The display label at the bottom of the GUI will
  provide a prompt once the sound bar is configured properly.

Configuration
~~~~~~~~~~~~~~

**Play Soundbar** -- Writes the preconfigured algorithms in :adi:`ADAU1761`
registers to enable it to demonstrate the ADI Effects.

ADI Effects (preconfigured algorithms from SigmaStudio):

- **None** -- Resets the sound bar to implement no special algorithms.
- **Spatializer** -- An advanced algorithm that allows for a wider stereo
  image to be played back from two closely spaced speakers. This spatializer
  algorithm is only meant to widen signals that are already in stereo format,
  in order to enhance the image. The function is similar to the Phat-Stereo
  algorithm but performs a more advanced implementation to achieve a better
  effect.
- **Superbass** -- Provides input-level dependent bass boost. Lower level
  signals are boosted more than higher-amplitude signals. Using a variable-Q
  filter, this algorithm dynamically adjusts the amount of boost.
- **Loudness** -- Amplifies lower level and higher level amplitude signals to
  maximize the volume range.
- **Test Tone** -- Provides a 1 kHz test tone to test the board even in the
  absence of an input signal.

Additional controls:

- **Volume, Bass, Treble Controls** -- Provide adjustable volume, bass, and
  treble levels of the input signal.
- **Channel Mute Control** -- Enables and disables the eight channels
  individually or collectively.

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~~

- **Configure ADAU1761** -- Configures the :adi:`ADAU1761` using user-defined
  algorithms from SigmaStudio.
- **Firmware Version** -- Provides details on the firmware version of the
  Blackfin used by the SDP board.

Documents
---------

- :adi:`CN0296 Circuit Note <CN0296>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0296-SDPZ Design & Integration Files
   <https://www.analog.com/cn0296-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`ADAU1761 Product Page <ADAU1761>`
- :adi:`SSM2518 Product Page <SSM2518>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
