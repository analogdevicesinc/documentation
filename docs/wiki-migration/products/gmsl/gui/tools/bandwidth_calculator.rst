GMSL Link Bandwidth Calculator
==============================

The GMSL Link Bandwidth Calculator allows for calculating if a specific use case will fit on a GMSL link after overhead. The calculator takes the horizontal and vertical timings along with the frame rate and bit depth to calculate the video bandwidth.

Display Required Video Details
------------------------------

To use the calculator, the minimum details required are:

-  Horizontal Timing: H_active and H_front_porch, H_sync_width, and H_back porch or blanking percentage
-  Vertical Timing: V_active and V_front_porch, V_sync_width, and V_back porch or blanking percentage
-  Frame Rate
-  Bit Depth (bits per pixel, or bpp)

The blanking time (front porch, sync width, and back porch) is mandatory to include in the overall calculations.

.. tip::

   If blanking is not known, a percentage is sufficient to start. Typically, an overall number of 10-20% is used. In the calculator, this can be done by zeroing out the front porch, sync, and back porch fields and entering 10-20% of the active pixels.


Camera Required Video Details
-----------------------------

To use the calculator, the minimum details required are:

-  CSI Port Type
-  Number of MIPI lanes
-  Mbps/lane
-  Data Type

Control Channel Details
-----------------------

GMSL devices can support a number of communication protocols on the control channel. They usually do not consume a large amount of bandwidth but the calculator can provide insight into the overall utilization.

--------------

Additional documentation and details can be found in the Help tab of the GUI.
