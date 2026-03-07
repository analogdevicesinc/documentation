CN0549 CbM Pelican Kit
======================

This wiki page will assist you in designing a standalone CN0549 CbM kit that can travel with you anywhere. The following steps assume that you have already completed the instructions for assembling the CN0549 system. If you have not configured the hardware or software, please visit the :doc:`CN0549 user guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0549>`, before continuing to build this kit.

Required Materials
------------------

Hardware:

-  :adi:`EVAL-CN0532-EBZ <en/design-center/reference-designs/circuits-from-the-lab/CN0532.html>`
-  :adi:`EVAL-CN0540-ARDZ <en/design-center/reference-designs/circuits-from-the-lab/CN0540.html>`
-  :adi:`EVAL-XLMOUNT1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-xlmount1.html>`
-  Cabling the CN0532 to the CN0540

   -  `1m Shielded male to male SMA cable <https://www.digikey.com/135101-02-M1.00>`_ or
   -  Twisted pair set of wires cut to the desired length

-  `DE10-Nano FPGA Board <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`_
-  `Class 10 16GB SD Card <https://www.amazon.com/gp/product/B073K14CVB>`_
-  `USB OTG <https://www.amazon.com/Rankie-Female-Adapter-Convertor-3-Pack/dp/B00YOX4JU6>`_ (micro USB to USB Type A female USB 2.0 Compatible)
-  `Pelican Case 1400 w/Foam <https://www.pelican.com/us/en/product/cases/protector/1400>`_
-  `10.1 Inch HDMI Display <https://www.amazon.com/gp/product/B076GZVCP2>`_
-  `HDMI cable (male to male) <https://www.monoprice.com/product?p_id=24187>`_ (2ft length)
-  `USB Wireless Keyboard + Mouse <https://www.amazon.com/Wireless-Keyboard-Jelly-Comb-Portable/dp/B0756XFFJZ>`_ (Needs to be less than 11.5 inches width and 4.5 inches tall)

Software:

-  `ADI Kuiper Image for CN0540 <https://swdownloads.analog.com/cse/kuiper/2021-02-18-ADI-Kuiper-CN0540.img.xz>`_

Creating a Pelican Kit
----------------------

The following sections describe how to take the CN0549 and integrate it into a single pelican case for easy use, carry, and shipping. The following steps already assume that you have followed the instructions for setting up the CN0549 hardware, software, and system. If you have not configured the hardware or software, please visit the :doc:`CN0549 user guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0549>`.

Mount the HDMI Monitor
~~~~~~~~~~~~~~~~~~~~~~

Mount the HDMI monitor to the inside of the Pelican 1400 case, on the lid side. In order to do this, you MUST cut into the foam provided in the case.

-  Align the edge of the monitor with the lefthand side of the case as shown in the picture (assuming you are looking at it with the case open and the lid in the air) This will leave about 2 inches of foam on the righthand side\


|image1|

-  Roughly locate the monitor about 1 inch from the top and 2 inches from the bottom edge of the foam.\ |image2|\

|image3|

-  Start cutting around the outline of the monitor with a very sharp knife.\

|image4|

-  After you are done cutting out the space for the monitor, it should look like this.\

|image5|

-  After cutting out the placement for the monitor, its time to adhere it to the Pelican case lid. Using velcro, cut 4 strips and place them down the back of the monitor as shown below. Be careful not to cover venting holes or other important things you might want access to later.\

|image6|

-  Looking at the righthand side you'll see the connector panel. Connect the HDMI cable and the DC barrel jack to the monitor.\ |image7|\

|image8|

-  Once complete, use the monitor to align the other side of the velcro to the case. Remove the adhesive backing and insert the monitor into the Pelican case lid. Apply light force as to ensure a safe, stable connection, but not to hard as to damage the screen.\ |image9|\

|image10|

Cutting the Foam
~~~~~~~~~~~~~~~~

All the other items needed to run the demo must fit inside this Pelican case. There are probably several ways you could do this, but I believe I have determined the optimal way in the following steps.

Start out by prepping the foam. The Pelican case is sold with foam which is perforated into .5 inch squares. This allows you to customize how things are arranged and how they can best fit in the case.

-  Lift the foam block from the main basin of the Pelican case, and remove the thin single piece of foam located at the bottom. Place this aside for later use.
-  If you were to view the foam from the top, there is an outside layer of foam that is non-perforated along with an inner coordinate system of perforations.
-  Remove all the foam pieces colored in BLUE using the grid pattern outlined below. Note the outside edge is non-perforated\ |image11|\ |image12|\

.. important::

   
   Try to remove foam in 5 or 6 larger sections. You will need the foam later to act as padding from the bottom of the case.


-  Next you are going to want to create padding using the foam you removed in the previous steps.
-  There are 3 different padding heights, which are broken up by equipment section.\

|image13|

   -  Keyboard == No Padding
   -  HDMI and Power cords == 1 inch of padding
   -  DAQ, FPGA, Sensor, Mounting block, USB OTG, Mouse == 1.5 inches of padding

-  After you cut the padding, its now time to reinsert the padding back into the foam cutout. If you do everything correctly your Pelican case should look like this at the end\


|image14|

Equipping the Pelican case
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Now you can start adding the required items into your Pelican case for standalone operation.
-  The keyboard should be the first items you place into the assigned foam slots.\

|image15|

-  Next, connect the DE10-Nano with the CN0540, CN0532, Mounting block, SMA cable, and USB OTG and place them into their assigned position.\

|image16|

-  Nicely coil up the wires for the CN0532, mounting block, SMA cable, and USB OTG cable so that they fit into correct position. Add the wireless mouse on top of these.
-  Next attach the HDMI cable and the DC barrel jack into the correct connector slots on the DE10-Nano, and make sure you coil the cables up so that everything fits into its assigned position.

|image17|

-  When everything is all complete, the main basin of the Pelican case should look something like this.\

|image18|

-  The entire open CN0549 case will look similar to this.\

|image19|

-  Before closing the lid, the protective foam should be added as to not damage the HDMI monitor.\

|image20|

-  Now you are ready to close the case and bring your setup along with you!\

|image21|

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_monitor_positioning.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_monitor_foam_top_width.jpg
   :width: 280px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_monitor_foam_bottom_width.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_monitor_foam_cutting.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_monitor_foam_outline.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_monitor_velcro.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/monitor_input_power_ports.jpg
   :width: 380px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/monitor_input_power_connected.jpg
   :width: 410px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_velco.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0549_pelican_case_buildup_monitor.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_foam_cutout_grid2.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_foam_cutout_grid_legend2.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_foam_cutout_grid_map2.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0549_pelican_case_buildup_keyboard2.jpg
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0549_pelican_case_buildup_keyboard3.jpg
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0549_pelican_case_buildup_cn0540_cn0532_de10_otg2.jpg
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0549_pelican_case_buildup_cn0540_cn0532_de10_otg_mouse_hdmi_power1.jpg
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0549_pelican_case_buildup_cn0540_cn0532_de10_otg_mouse_hdmi_power2.jpg
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_complete_open2.jpg
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_case_complete_open_protected2.jpg
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0549_pelican_case_complete_closed.jpg
   :width: 400px
