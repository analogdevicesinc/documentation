:doc:`⇐ Back </wiki-migration/products/audio-video/analoghdmidvi-interfaces/adv8005>`

Picture in Picture overlay on up to 4k30
========================================

Overview
========

Picture in picture on home AVR, TVs and pro audio still remains a popular trend but its availability is possibly overlooked by customer and maybe omitted by supplier due to higher hardware costs in a market driven by low cost devices for home entertainment. Nevertheless, companies have been looking into low-mid cost hardware ICs that can be integrated in their system to provide the dynamics on video overlay, picture in picture and picture out of picture as well. The ADV8005 offers the capability for picture in picture as well as picture out of picture for various products ranging in applications in consumer market to professional video market. The ADV8005 offers picture in picture on HDMI and on video resolution up to 4k2k30. The pip processor uses DDR2 external memory.

Reference parts
===============

:adi:`ADV8005 - NatureVue™ Video Signal Processor with Bitmap OSD, Dual HDMI Tx, and Encoder <adv8005>`

Application summary
===================

PIP Preview window
------------------

One common application is a preview window of another input video while still watching the selected channel or also while browsing the input list from a menu. The ADV8005 offers all these possibilities as it can overlay an external video over main video, and also has an internal OSD engine to display custom menu with embedded external video.

External OSD menu
-----------------

If you already have an SOC generating your OSD, the ADV8005 can display your menu either overlaid on main video, or in full screen, or even blended with the internal OSD engine. It is also possible to blend with alpha regions in 2 ways. a. By using the OSD blend, an transparent color can be used for color keying where any pixel set to this color from the external OSD input will appear as transparent at the output. This is the easiest case of using color keying where edges are transparent or not with no per pixel alpha smoothing around edges. b. The second option which requires a bit more hardware is to send the external SOD alpha channel through TTL pins which basically is like a color channel of your video but it is routed to the OSD blend block in order to apply fine alpha blend one pixel at a time. This would allow to create per pixel alpha blending of the external OSD menu with either main video or internal OSD or even both.

Streaming preview video from SPI
--------------------------------

The link to DDR2 memory through SPI can be used to load video frames for a small preview of video or live streaming. While video frame rate, quality and size will be limited by SPI speed and available DDR2 DMA speed in ADV8005, small lower quality preview window can be displayed.

Multiple PIP using external OSD
-------------------------------

If using an SOC to generate external video, multiple preview video can be tiled int one video which is sent to the external OSD TTL and the ADV8005 internal OSD can partition each tile into PIP sub-windows at different location. This could achieve even live streaming preview as seen on smart TVs.

Capabilities
============

Overlaying on 4k30
------------------

The OSD engine is able to overlay a video of maximum resolution of 1080p onto up to 4k30. It is possible to overlay internal OSD and external OSD onto 4k resolution by upscaling 1080p OSD video to 4k resolution.

Downscaling 4k30 for PIP
------------------------

The ADV8005 can downscale 1 4k30 video input to 1080p by using the HPS and SVSP.

Picture out of Picture (POP)
----------------------------

POP uses a feature of the PVSP called album mode which can downscale the input video within the input resolution video. Only the PVSP can do album mode. Usually only main video needs POP while all other videos will be pip within the main video resolution.

DDR2 bandwidth reference
========================

For bandwidth calculation, a reference is provided for each common resolution at 60 Hz and width 60Hz to 24Hz frame rate conversion and for both 24 bits and 32 bits. The OSD engine max pixel size is 32bits for ARGB8888 which is RGB with alpha channel. Extnerla OSd with extenrla alpha is also 32 bits, without external alpha it is 24 bits.

Bandwidth calculation
---------------------

PVSP
~~~~

The bandwidth is from input video resolution and frame rate. Note that RNR, interlaced input or frame rate conversion would increase the bandwidth usage if used.

SVSP
~~~~

Bandwidth is from output video resolution and frame rate. For downscaling, only 1080p to 720p can be done in bypass mode without any DDR2 memory. All other formats will need DDR2 memory.

HPS
~~~

HPS does not use any bandwidth.

OSD
~~~

The OSD bandwidth varies as per each region size which is better calculated using Blimp’s emulator. Bandwidth maximum is calculated per video line. Of course overlapping regions can double the bandwidth for a video line. To get Blimp OSD designer tool, go to :ez:`Blimp OSD Designer tool for NatureVue™ ADV800x and Advantiv® ADV7625 <docs/DOC-10635>`

External OSD
~~~~~~~~~~~~

If an external OSD region is received directly from external OSD TTL input, then it will use the bandwidth of its input video resolution and frame rate.

================ ========== ============================================
Video resolution Video bits Bandwidth (gbps) For video frame rate = 60Hz
================ ========== ============================================
1080p            24 bits    5.561828613
:::              32 bits    7.415771484
720p             24 bits    2.471923828
:::              32 bits    3.295898438
480p             24 bits    0.926971436
:::              32 bits    1.235961914
240p             24 bits    0.463485718
:::              32 bits    0.617980957
================ ========== ============================================

• For 16 bits input video, simply divide 32bits value by 2 • If frame rate different from 60, multiply by frame rate and divide by 60

Available DDR2 memory bandwidth
===============================

+-------------+--------------------------------------------------------------------------------+
| DDR2 memory | Bandwidth (gbps) ( frequency = 250MHz, Data bits width = 16, Efficiency = 70%) |
+=============+================================================================================+
| Dual        | 14.90116119 gbps                                                               |
+-------------+--------------------------------------------------------------------------------+
| Single      | 7.450580597 gbps                                                               |
+-------------+--------------------------------------------------------------------------------+

DDR2 chip options
=================

When the bandwidth requirement and size for the ADV8005 are below 7.45 gpbs, only one DDR2 chip can be used. This might be especially useful to reduce hardware and costs for systems requirement multiple ADV8005.

Application analysis
====================

4k30 and 1080p input video with 4k30 or 1080p60 video combinations
------------------------------------------------------------------

======= ===== ========== ========== =========
\             Inputs                
======= ===== ========== ========== =========
\             1080p Main 1080p Main 4k30 Main
:::           1080p PIP  4k30 PIP   1080p PIP
Outputs 1080p Supported  Supported  Supported
:::     4k30  Supported  Supported  Supported
======= ===== ========== ========== =========

This table assumes PVSP is only used for upscaling with no RNR or interlaced conversion. If any of these features are required, some configurations will need 2 ADV8005 due to bandwidth exceeding.

In the only case above that requires 2 ADV8005, because both inputs need to be downscaled to 1080p, it would need 2 ADV8005. However, note that the ADV8005 doing only downscaling from 4k30 to 1080p would need only one DDR2 memory chip.

Glossary
========

OSD: On Screen Display

TTL: Parallel video bus which can be fed using ADV7842 or ADV7619

PIP: Picture in picture

POP: Picture out of picture

Gbps: gigabits per second
