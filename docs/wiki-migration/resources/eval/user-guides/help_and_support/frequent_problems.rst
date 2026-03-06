Frequent Issues and Solutions
=============================

HDL
---

Building the reference design results in an error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue:**

When trying to build the HDL reference design Xilinx Vivado aborts with an error.

**Solution:**

To work correctly the reference designs needs to be built with a specific version of Xilinx Vivado.

======================== ==============
Reference design release Vivado Version
======================== ==============
2014_R1                  2013.4
2014_R2                  2014.2
======================== ==============

Only the versions listed in this table are supported. Even if the reference design builds without errors with a different version it will most likely not work as expect and may result undefined behavior at runtime.

FMC
---

The FMC add-on board is not detected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue:**

After powering up the FMC carrier board the add-on board is not detect and the boot log contains "Unsupported product ID 0xff" or similar.

**Solution**:

Some carrier boards like the ZC702 or ZC706 have multiple FMC slots. The FMC add-on board needs to be plugged into the correct into the correct FMC slot.

**Solution**:

Some revisions of the ZC702 have an issue with the FMC power-good signal not being asserted. A ZC702 is affected if DS24 does not light up after the board has been powered up. For more information one the issue and how to fix it refer to `Xilinx AR#51438 <https://www.xilinx.com/support/answers/51438.html>`__.

Video Output
------------

The monitor stays black
~~~~~~~~~~~~~~~~~~~~~~~

**Issue:**

After powering the carrier board with a HDMI output the monitor stays black.

**Solution:**

...

The borders of the image is cropped off
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**:

When connecting a TV to a carrier board with a HDMI video output the image appears on the TV, but the boarders appear to be cropped.

**Solution:**

For historical reasons TVs tend to perform something called `overscan <https://en.wikipedia.org/wiki/Overscan>`__. The HDMI standard allows the video source to explicitly request that the sink does not perform overscan, but some TVs ignore this request. Sometimes this behavior can be turned of in the TV settings.
