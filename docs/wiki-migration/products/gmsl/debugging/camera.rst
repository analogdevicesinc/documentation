Camera Debugging
================

Once you've confirmed that the GMSL portion of the system is operating correctly, you can begin to walk through the signal chain to find where the video feed is having issues.

Sensor Serializer Debugging
===========================

The GMSL sensor serializer is connected directly to the sensor PHY. If there are any issues with receiving the data, you want to start at the source of the data and work towards the processor.

Pixel Clock Detection
---------------------

The first thing to check in any camera system is that the serializer is receiving a valid pixel clock, or PCLK. There is a helpful bit called “PCLKDET” to indicate that PCLK is detected. If there is no PCLK detected, then we know that there is no MIPI data streaming. Without data streaming, it is hard to isolate an issue.

Serializer MIPI-CSI2 PHY Input
------------------------------

PHY lane config

Serializer Internal Routing
---------------------------

Deserializer GMSL Input
-----------------------

VID_LOCK VIDEO_LOCK
