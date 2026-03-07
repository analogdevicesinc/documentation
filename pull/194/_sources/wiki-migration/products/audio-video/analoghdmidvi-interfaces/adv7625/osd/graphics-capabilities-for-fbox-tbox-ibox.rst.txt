:doc:`⇐ Back </wiki-migration/products/audio-video/analoghdmidvi-interfaces/adv7625>`

ADV7625/ADV7626/ADV7627 OSD graphic capabilities using Fbox, Ibox and Tbox
==========================================================================

Overview
========

The ADV7625/ADV7626/ADV7627 offer a simple low cost on screen display for video overlay on HDMI. The hardware implementation uses Text boxes ( Tbox), filled boxes ( Fbox) and icon boxes (Ibox) to create basic text based OSD overlay. The hardware offers a 16x16 resolution for text characters with ability to scale from 1 to 15 using pixel repetition. The pixel repetition in most cases does not provide good quality text as a result. The Blimp OSD Designer software tool abstracts the drawing hardware components and optimizes their use by treating them all as graphic components that can display both images or text and can span across multiple 16x16 boundaries in the case of Tboxes to create larger high quality fonts. On larger resolutions like 1080p and 4k, a compromise will usually have to be made between limiting OSD content or using scaling to have more content but with lower resolution.

This application note details the capabilities of the ADV7625 OSD as implemented in Blimp. with these guidelines, user can plan the graphic and text layout of each pages for their OSD design. the best way to verify is by using Blimp to add graphics and text to a page and test it with the OSD hardware emulator which comes with Blimp.

Reference parts
===============

:adi:`ADV7625 - 3GHz HDMI 5:2 cross point Transceiver with On-Screen Display <adv7625>`

:adi:`ADV7626 - 3GHz HDMI 2:2 cross point Transceiver with On-Screen Display <adv7625>`

:adi:`ADV7627 - 3GHz HDMI 5:1 Transceiver with On-Screen Display <adv7625>`

TBox
====

-  Each Tbox has 256x16 pixels. Each Tbox uses 16x16 blocks from graphic memory assigned by index.
-  Graphic memory: Up to 256 unique blocks of 16x16 pixels with for each color = 65536 pixels ( Graphic memory of 256 16x16 blocks)
-  Blocks of n multiples of 16x16 can be reused for maximum of 262144 pixels ( 640 256x16 blocks) Example: 16x16 blocks that are all same color or pattern can be reused.

Limitations
-----------

-  Limit of 2560 pixels horizontally. Can be grouped by multiple of 160 pixels blocks in width.
-  Height can be grouped by a multiple of 16 pixels block
-  Up to 16 colors can be displayed at any time. So different pages cold use different set of 16 colors. This needs to be discussed during page layout when defining demo graphics. We will clearly indicate which images are by pages. Each color uses overlapped display memory from above.

**Table 1: Tbox image size limits by number of colors ( with scaling = 1 )**

+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| # colors | Pixels span Tbox limit ( if some glyphs are identical)) | Pixel span Glyph limit ( can be more if some 16x16 blocks are re-used) |
+==========+=========================================================+========================================================================+
| 1        | 262144 ( 64 blocks of 256 x 16)                         | 65536                                                                  |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 2        | 131072 ( 32 blocks of 256 x 16)                         | 32768                                                                  |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 3        | 86016 ( 21 blocks of 256 x 16)                          | 21760                                                                  |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 4        | 65536 ( 16 blocks of 256 x 16)                          | 16384                                                                  |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 5        | 49152 ( 12 blocks of 256 x 16)                          | 13056                                                                  |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 6        | 40960 ( 10 blocks of 256 x 16)                          | 10752                                                                  |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 7        | 36864 ( 9 blocks of 256 x 16)                           | 9216                                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 8        | 32768 ( 8 blocks of 256 x 16)                           | 8192                                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 9        | 28672 ( 7 blocks of 256 x 16)                           | 7168                                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 10       | 28672 ( 6 blocks of 256 x 16)                           | 6400                                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 11       | 20480 ( 5 blocks of 256 x 16)                           | 5888                                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 12       | 20480 ( 5 blocks of 256 x 16)                           | 5376                                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 13       | 16384 ( 4 blocks of 256 x 16)                           | 4864                                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 14       | 16384 ( 4 blocks of 256 x 16)                           | 4608                                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 15       | 16384 ( 4 blocks of 256 x 16)                           | 4352                                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+
| 16       | 16384 ( 4 blocks of 256 x 16)                           | 4096 ( same as Ibox)                                                   |
+----------+---------------------------------------------------------+------------------------------------------------------------------------+

Ibox
====

-  Up to 64 blocks of 8x8 pixels with 32 colors support = 4096 pixels.
-  Blocks of n multiple of 8x8 can be reused for maximum of 8192 pixels ( 128 8x8 blocks)

.. _limitations-1:

Limitations
-----------

-  Limit of 80 pixels horizontally. Can be grouped by multiple of 8 pixels blocks in width.
-  Height can be grouped in multiple for 8 pixels
-  Up to 32 colors at any time on a page

Fbox
----

-  Rectangular boxes with border
-  Up to 64 boxes of any width and height with border of 1 or few pixels. Top bottom left and right border can be enabled/disabled individually.
-  Up to 8 color sets with fbox color and border color pair.

Scaling
=======

-  The sizes shown above are with both vertical and horizontal scaling to 1.
-  The size can be increased by the scaling factor at the cost of losing resolution quality

Graphics examples
=================

Luminance gradient
------------------

-  Ibox: 32 color luminance gradient. Limited to Ibox size
-  Fbox: Each Fbox can specify box color and border. By activating only one boarder, a 16 color vertical or horizontal box can be created.
-  Tbox: Only 16 color gradient possible

Support
=======

:ez:`EngineerZone Video Support Community <community/video>`
