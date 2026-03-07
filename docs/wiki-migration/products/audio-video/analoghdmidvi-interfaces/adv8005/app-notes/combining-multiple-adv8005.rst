Applications combining multiple ADV8005 devices
===============================================

Some applications can combine multiple ADV8005 devices to achieve functionality that would not be possible with a single device. This section gives some examples of those possibilities, and makes some recommendations for best system performance.

Example application:

-  Video walls

CONFIGURATION OPTIONS
=====================

Frame Locked Mode
-----------------

This is a mode where the output timing can be fractionally locked (to an accuracy of a few clock cycles) to the VS timing of the input video, even if the output resolution differs from the input resolution. Additionally, if desired, a user-programmable delay can be added from input to output timing.

**Advantages:** As output and input timing are locked, it will never be necessary to drop or repeat frames of the output video. This ensures that if there is a scene change on the input, it will appear at the same time on all ADV8005 devices which are being driven by it.

**Disadvantages:** When the input changes resolution or frame rate, the output timing may be temporarily disturbed as the new input is acquired.

**Best suited for:** System configurations where the same input signal is processed through multiple ADV8005 devices.

External Sync Mode
------------------

This is supported only by the ADV8005. In this mode, output video is read from a frame buffer based on the externally applied master HS and VS.

**Advantages:** The outputs of several ADV8005 devices can be synchronized to within a few clock cycles, even if they are being fed by input signals of different resolutions and frame rates.

**Disadvantages:** As the output timing is decoupled from the input video timing, they will drift over time. Therefore, it will be necessary to occasionally drop or repeat a frame on the output video.

**Best suited for:** System configurations where different input signals are processed through multiple ADV8005 devices and the outputs need to be recombined. Not suitable if the same signal is applied to each ADV8005, as the frame drop/repeat may occur at different times for each device.

USE CASES
=========

Star Connected ADV8005 Devices
------------------------------

This is typical of some video wall or signage applications. One source signal is sent through a splitter to multiple ADV8005 devices in multiple sinks. Each ADV8005 crops a portion of the image and upscales it to full-screen. For example, using 4 ADV8005 devices, each one processes top-left, top-right, bottom-left or bottom-right of the image and upscales it to full-screen. Outputs are not combined; they each drive their own display.

The requirement is that a scene change happening on the input will appear to the human eye to happen at the same time on all of the ADV8005 outputs.

.. image:: https://wiki.analog.com/_media/products/audio-video/analoghdmidvi-interfaces/adv8005/app-notes/adv8005pic1.png
   :align: center
   :width: 600px

::

           Figure 1. Star-Connected Devices

Best solution: Use ADV8005 in frame locked mode.

Daisy-Chained ADV8005 Devices
-----------------------------

This is typical of some video wall or signage applications. One source signal is sent to ADV8005 devices in multiple sinks. They are connected in daisy-chain fashion. Each ADV8005 crops a portion of the image and upscales it to full-screen and outputs that on its output port. On its other output port, it passes through the input to the next ADV8005 device in the chain. For example using 4 ADV8005 devices, each one processes top-left, top-right, bottom-left or bottom-right of the image and upscales it to full-screen. Outputs are not combined; they each drive their own display.

The requirement is that a scene change happening on the input will appear to the human eye to happen at the same time on all of the ADV8005 outputs.

.. image:: https://wiki.analog.com/_media/products/audio-video/analoghdmidvi-interfaces/adv8005/app-notes/adv8005pic1.png
   :align: center
   :width: 600px

::

             Figure 2. Daisy-Chained Devices

**Best solution:** Use ADV8005 in frame locked mode and program a delay adjustment for each device in the chain to compensate for the pass-through delay from one device to the next.

Combining Parallel Connected ADV8005 Devices –All Same Input Signal
-------------------------------------------------------------------

One source signal is sent to multiple ADV8005 devices in parallel. Each ADV8005 crops a portion of the image and upscales it to full-screen and outputs that on its output port. For example, using four ADV8005 devices, each one processes top-left, top-right, bottom-left or bottom-right of the image and upscales it to full-screen. The outputs from all ADV8005 devices are combined, in an FPGA for example, to produce an image of higher resolution, (really an image of larger size) than the input.

The requirement is that the output video of all ADV8005 devices are synchronised to within a few clock cycles of each other. This means the outputs of several ADV8005 devices may be combined in a modest FPGA, with no line or frame memories necessary, just a small FIFO on each input to transfer all inputs onto a common clock. An additional requirement is that a scene change happening on the input will appear to the human eye to happen at the same time on all of the ADV8005 outputs.

.. image:: https://wiki.analog.com/_media/products/audio-video/analoghdmidvi-interfaces/adv8005/app-notes/adv8005-parrallel-sameinput.png
   :align: center
   :width: 600px

::

        Figure 3. Parallel-Connected Devices – Same Input Signal

**Best solution:** Use ADV8005 in frame locked mode. Combine outputs in FPGA, passing input data from each ADV8005 device through a small FIFO to transfer all ADV8005 outputs onto a common FPGA clock.

Combining Parallel Connected ADV8005 Devices – All Different Input Signals
--------------------------------------------------------------------------

Different source signals of varying resolutions and refresh rates are sent to several parallel ADV8005 devices. Each ADV8005 de-interlaces and/or scales its input to a common output format. Outputs are then combined in an FPGA.

The requirement is that the output video of all ADV8005 devices is the same resolution/refresh rate and those outputs are synchronised to within a few clock cycles of each other. This means the outputs of several ADV8005 devices may be combined in a modest FPGA, with no line or frame memories necessary, just a small FIFO on each input to transfer all inputs onto a common clock.

.. image:: https://wiki.analog.com/_media/products/audio-video/analoghdmidvi-interfaces/adv8005/app-notes/adv8005-parrallel-diffinput.png
   :align: center
   :width: 600px

::

         Figure 4. Parallel-Connected Devices – Different Input Signals

**Best solution:** Use ADV8005 in external sync mode. Combine outputs in FPGA, passing input data from each ADV8005 device through a small FIFO to transfer all the ADV8005 outputs onto a common FPGA clock.
