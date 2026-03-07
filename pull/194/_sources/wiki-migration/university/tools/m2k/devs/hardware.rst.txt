ADALM2000 Hardware
==================

Whether you want to understand the changes between revisions, or just understand how to probe the PCB, this is where all the information should be.

Connectors
----------

The ADALM2000 includes a button (S1 on the PCB), and two USB connectors |image1|


|image2|

The button can be defined by software, it is normally held on with a paper clip or thumb tack during power on to put the device into a recovery mode. It can be re-purposed to do other things.

The first USB connector (the middle one) is the USB OTG connector (can be the USB HOST connector (cabled to a USB peripheral), or the USB peripheral connector (cabled to a USB Host)).

The second USB connector (the one on the side) is for power only when running in Host mode.

Removing the case
-----------------

|image3| |image4|

The plastic case comes off quite easily, with the removal of two black `Phillips <https://en.wikipedia.org/wiki/List_of_screw_drives#Phillips>`_ screws on the bottom of the case. The production version may be different. It will for sure be `CE and FCC certified <https://wiki.analog.com/../common/regulatory_compliance>`_. (already passed).

Removing the screws will allow you to take the top off the case, and expose the PCB.

If you want to remove the PCB, and place it on the table, we recommend that you attach `Cylindrical Bumpers <https://www.digikey.com/3M156065-ND>`_ (also known as feet), on the PCB to protect the components on the bottom of the PCB. These are not included in the design, and must be purchased separately (as we don't expect too many people wanting to do this).

Mating connectors
-----------------

It's likely that you might want to make a board that mates directly to the ADALM2000 - check out these connectors. There are listed here as a convenience.

+-----------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Manufacture                 | Part Number                                                               | Possible providers                                                                                                                                                |
+-----------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sullins Connector Solutions | PPPC152LJBN-RC                                                            | `Digikey <https://www.digikey.com/PPPC152LJBN-RC>`_                                                                                                               |
+-----------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Samtec                      | `SSQ-115-02-T-D-RA <https://www.samtec.com/products/ssq-115-02-t-d-ra>`_  | `Digkey <https://www.digikey.com/SAM1224-15-ND>`_ `Mouser <https://www.mouser.com/ProductDetail/Samtec/SSQ-115-02-T-D-RA?qs=rU5fayqh%252BE2UN30xyNQdAQ%3D%3D>`_   |
+-----------------------------+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Revision D
----------

.. admonition:: Download
   :class: download

   
   -  `Rev D Schematics <https://wiki.analog.com/_media/university/tools/m2k/devs/02_042233d_top_updated_sch.pdf>`_
   -  `Rev D Gerbers <https://wiki.analog.com/_media/university/tools/m2k/devs/09-042233-01d.zip>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_)
   -  `Rev D Bill of materials <https://wiki.analog.com/_media/university/tools/m2k/devs/05-042233-01-d2-adalm2000_d_bom.xlsx>`_
   -  `Rev D Allegro Board File <https://wiki.analog.com/_media/university/tools/m2k/devs/adalm2000_brd_revd.7z>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ to view.
   -  `Rev D Cadence project <https://wiki.analog.com/_media/university/tools/m2k/devs/20_042233e_compress.zip>`_
   -  `Rev D 3D model (Case, bare PCB, connectors) <https://wiki.analog.com/_media/university/tools/m2k/devs/m2k_with_case.zip>`_
   


Revision C
----------

.. admonition:: Download
   :class: download

   
   -  `Rev C Schematics <https://wiki.analog.com/_media/university/tools/m2k/devs/adalm2000_revc_schematic.pdf>`_
   -  `Rev C Gerbers <https://wiki.analog.com/_media/university/tools/m2k/devs/09-042233-01c.zip>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_)
   -  `Rev C Bill of materials <https://wiki.analog.com/_media/university/tools/m2k/devs/05-042233-01-cadalm2000-revc-bom.xlsx>`_
   -  `Rev C Allegro BoardFile <https://wiki.analog.com/_media/university/tools/m2k/devs/08_042233c-revc-brd.7z>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ to view.
   -  `Rev C Cadence project <https://wiki.analog.com/_media/university/tools/m2k/devs/20-042233-01c.zip>`_
   


Why do a Rev D?
~~~~~~~~~~~~~~~

Revision B
----------

.. admonition:: Download
   :class: download

   
   -  `Rev B Schematics <https://wiki.analog.com/_media/university/tools/m2k/devs/adalm2000_revb_schematic.pdf>`_
   
   ::
   
      *[[https://wiki.analog.com/_media/university/tools/m2k/devs/09-042233-01b.zip|Rev B Gerbers]] (This file is [[http://www.7-zip.org/7z.html|compressed]])
      *[[https://wiki.analog.com/_media/university/tools/m2k/devs/05-042233-01-b_adalm2000_b_bom.xlsx|Rev B Bill of materials]]
      *[[https://wiki.analog.com/_media/university/tools/m2k/devs/08_042233brevb_brd.7z|Rev B Allegro Board File]] (This file is [[http://www.7-zip.org/7z.html|compressed]]). Get the [[https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html|Allegro FREE Physical Viewer]] to view.
      *[[https://wiki.analog.com/_media/university/tools/m2k/devs/20-042233-01b.zip|Rev B Cadence Project]]
   


Why do a Rev C?
~~~~~~~~~~~~~~~

-  A voltage divider should be added TX calibration path
-  Two 10 uF capacitors need to be added at USB power inputs.
-  The negative rail of the AD8066 should have a power down and for this is needed a -5V LDO.
-  ADP198 in the positive power supplies analog stage can be removed.
-  The analog power sequence has to be improved.
-  The 2.4 Ohm resistor at output of User power supply needs to be replaced with 4.7Ohm.
-  The user power supplies should have individual power down and a 6V protection Zenner diode at the output.

Revision A
----------

.. admonition:: Download
   :class: download

   
   -  `Rev A Schematics <https://wiki.analog.com/_media/university/tools/m2k/devs/adalm2000_reva_schematic.pdf>`_
   -  `Rev A Gerbers <https://wiki.analog.com/_media/university/tools/m2k/devs/09-042233-01a.zip>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_)
   -  `Rev A Bill of materials <https://wiki.analog.com/_media/university/tools/m2k/devs/042233a_adalm2000_a_bom.xlsx>`_
   -  `Rev A Allegro Board File <https://wiki.analog.com/_media/university/tools/m2k/devs/08_042233areva_brd.7z>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ to view.
   -  `Rev A Cadence project <https://wiki.analog.com/_media/university/tools/m2k/devs/20-042233-01a.zip>`_
   


Why do a Rev B?
~~~~~~~~~~~~~~~

-  Because of heating on the board the supply for the scope input buffers is reduced. The buffers are supplied on rev B at -3V3 and 3V8 (obtained with an LDO from Vin).
-  The digital and analog 1V8 rails are merged but the footprint of the LDO for 1V8_A is kept in case there will be too much noise.
-  For lower power consumption the ADC divers are replaced with ADA4940-2ACPZ.
-  To remove the back powering of the analog section the DACs controlled by I2C are powered from the digital supplies.
-  The user power supplies could use an amplifier that provides low power, smaller noise and larger bandwidth, such as ADA4805.
-  The AWG protection and the power supplies monitor can be removed.
-  The input choke needs to be replaced with a version with a higher current rating for a lower impedance at high frequencies.

Images
------

Click to get the full size image

-  |JPG| 4401 x 2664 JPEG 2.9 MB
-  |image5| 4401 × 2664 PNG 5 MB
-  |image6| 4401 x 2664 JPEG 2.9 MB
-  |image7| 1200 × 726 JPEG 415.5 KB
-  |PNG| 300 × 182 PNG 50.9 KB

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/button_connectors.jpg
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/zoom_conn.jpg
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/removing_the_case.jpg
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/exposed_pcb.jpg
   :width: 210px
.. |JPG| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/m2k.jpg
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/m2k.png
   :width: 200px
.. |image6| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/m2k_50033.jpg
   :width: 200px
.. |image7| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/m2k_50034.jpg
   :width: 200px
.. |PNG| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/m2k_50037.png
   :width: 200px
