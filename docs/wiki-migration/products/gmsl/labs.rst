GMSL Labs
=========

Confirming the Video Path
-------------------------

If you open the GMSL GUI with the hardware running but without the video streaming, we are going to walk through some basic debugging steps. Beginning with the first and simplest one, we will check for link LOCK.

Before any debugging starts, we want to confirm that the device PHYs are locked to each other and able to communicate. Without LOCK, you will only be able to communicate with the local device, so it's required to have link LOCK to communicate over the back channel to the remote devices.

.. container:: group

   
   If your system doesn't have lock, something fundamentally is wrong. This means you should go check power supply levels, crystal stability, connector pin out, and even continuity (if needed).
   
   --------------
   
   Checking for Lock
   ~~~~~~~~~~~~~~~~~
   
   .. container:: half column

      LOCK can be confirmed with a physical LOCK pin (connected to an LED on the EV kit).

         
         .. note::

            On multiple input devices (like the MAX96724), the physical LOCK pin only asserts when all enabled links are locked. Ensure the number of enabled links matches the number of physical links connected.

         

   
   .. container:: half column


         

   
   |image1|

.. container:: half column

   LOCK can also be confirmed by checking the LOCK bit in the corresponding register.

   
   You can choose to route this signal to an LED or GPIO on the processor.


.. container:: half column



|image2|

--------------

Checking for Pixel Clock
------------------------

The first thing to check in any camera system is that the serializer is receiving a valid pixel clock, or PCLK. There is a helpful bit called “PCLKDET” to indicate that PCLK is detected.

.. container:: group

   
   .. container:: half column

         
         .. hint::

            How can we search for a specific bit?

         
         We can use the bitfield search feature to look for this specific bit.
         
         .. hint::

            What is the register and bit position that of "PCLKDET"?

         
         Here we can see that PCLKDET is located in register 0x112 in bit position 7.
         
         .. hint::

            What is the value of the “PCLKDET” bit and what does that indicate?

         
         A status of 0 indicates that the video transmit PCLK is not detected.
         

   
   .. container:: half column

         

   
   |image3|

.. container:: group

   
   .. container:: half column

      There is no PCLK which must mean our imager isn’t outputting video. Let’s turn on the imager with the green play button in the V4L2 utility and start streaming video.

         
         Reread the register to check the status of PCLKDET.
         
         .. hint::

            What is the value of the “PCLKDET” bit and what does that indicate?

         
         A status of 1 indicates that the video transmit PCLK is detected.
         

   
   .. container:: half column

         

   
   |image4|

.. |image1| image:: https://wiki.analog.com/_media/products/gmsl/max96724_lock.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/products/gmsl/max96724_lock_gui.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/products/gmsl/no_pclk.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/products/gmsl/with_pclk.png
   :width: 600px
