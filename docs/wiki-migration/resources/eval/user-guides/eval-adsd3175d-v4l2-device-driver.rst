EVAL-ADSD3175D V4L2 Device Driver
=================================

Driver Scripts
--------------

With the SD Card Image, several scripts are provided. These scripts operate the ADSD3500 without the SDK to stream frames.

You can find these script in the **~/Workspace/adsd3500_getframe** directory.

As of writing there are ten (10) scripts available.

-  get_frame_8_full.sh
-  get_frame_8.sh
-  get_frame_adsd3030.sh
-  get_frame_mp_16.sh
-  get_frame_mp_ab.sh
-  get_frame_mp.sh
-  get_frame.sh

In each case a command line parameter can be specified to stream the desired number of frames and the output is to a file named **frame.bin**. If no parameter is specified only one (1) frame is streamed.

These scripts make use of the `v4l2-ctl <https://manpages.ubuntu.com/manpages/bionic/man1/v4l2-ctl.1.html>`_ command line tool in Linux. Note, this is pre-installed on the EVAL-ADTF3175D Linux.

`adsd3500.c <https://github.com/ToF?master/drivers/adsd3500/nxp/src/adsd3500.c>`_

To see a list of command supported by v4l2-ctl:

::

   $ v4l2-ctl --list-ctrls   --device=/dev/v4l-subdev1 --list-formats

   User Controls

                    operating_mode 0x009819e0 (int)    : min=0 max=10 step=1 default=0 value=7
                       chip_config 0x009819e1 (u8)     : min=0 max=255 step=1 default=0 [4099] flags=has-payload
                  phase_depth_bits 0x009819e2 (intmenu): min=2 max=6 default=2 value=4
                           ab_bits 0x009819e3 (intmenu): min=0 max=6 default=0 value=0
                   confidence_bits 0x009819e4 (intmenu): min=0 max=2 default=0 value=0
                      ab_averaging 0x009819e5 (bool)   : default=1 value=0
                      depth_enable 0x009819e6 (bool)   : default=1 value=0

   Image Processing Controls

                    link_frequency 0x009f0901 (intmenu): min=0 max=0 default=0 value=0 flags=read-only
                        pixel_rate 0x009f0902 (int64)  : min=1 max=2147483647 step=1 default=1 value=488000000 flags=read-only
   ioctl: VIDIOC_ENUM_FMT
           Type: Video Capture

phase_depth_bits

-  6 - 16-bits
-  5 - 14-bits
-  4 - 12-bits
-  3 - 10-bits
-  2 - 8-bits

ab_bits

-  6 - 16-bits
-  5 - 14-bits
-  4 - 12-bits
-  3 - 10-bits
-  2 - 8-bits
-  1 - N/A
-  0 - AB Off

confidence_bits

-  2 - 8-bits
-  1 - 4-bits
-  0 - Off

ab_averaging

0 - Disable AB averaging 1 - Enable AB averaging

depth_enable

0 - Depth is computed using depth compute library. 1 - Depth/phase is computed using ADSD3500.

Let's look more closely at one example: get_frame_mp.sh

Example call: ./get_frame_mp.sh 10

This will stream 10 frames, saving them to the file frame.bin.

::

   1: #!/bin/bash
   2: nr_frames=${1:-1}
   3: v4l2-ctl --set-ctrl=operating_mode=10 -d /dev/v4l-subdev1
   4: v4l2-ctl --set-ctrl=phase_depth_bits=4 -d /dev/v4l-subdev1
   5: v4l2-ctl --set-ctrl=ab_bits=0 -d /dev/v4l-subdev1
   6: v4l2-ctl --set-ctrl=confidence_bits=0 -d /dev/v4l-subdev1
   7: v4l2-ctl --set-ctrl=ab_averaging=0 -d /dev/v4l-subdev1
   8: v4l2-ctl --set-ctrl=depth_enable=0 -d /dev/v4l-subdev1
   9: v4l2-ctl --device /dev/video0 --set-fmt-video=width=1024,height=3072,pixelformat=BG12 --stream-mmap --stream-to=frame.bin --stream-count=$nr_frames

Lines 3 to 8 essentially interacts with the ADSD3500 host command SET IMAGER MODE.

Line 3: Select mega-pixel mode (10)

Line 4: Set the phase/depth bits to 12-bits

Line 5: Set AB frames to off

Line 6: Set confidence frames to off

Line 7: Disable AB averaging

Line 8: Disable depth processing

Line 9: Start the stream; width is MP width of 1024; height is 3072 pixels - 3 phase frames (1024x1024 each), no AB, no confidence; pixel format `BG12 <https://www.kernel.org/doc/html/v4.8/media/uapi/v4l/pixfmt-srggb12.html>`_.
