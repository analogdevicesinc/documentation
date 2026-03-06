GMSL522 Labs -- Follow Along Guides
===================================

The following guides are to be used in conjunction with the relevant GMSLU course pertaining to the GMSL522 labs section of the GMSLU curriculum. When watching a GMSL522 lab video that has a "Follow Along Guide", having this page open on another tab allows students to easily see important bullet points about the videos and also to easily copy and paste Linux commands from this website, to their Linux PC, or GMSL522 development board. Follow this link to be taken to the GMSLU page pertaining to the GMSL522 labs: :ez:`adieducation/gmslu/?courseGroup=812#courseList`

.. note::

   Use the Table of Contents on the right side of the page to easily navigate to the guide for the course you are interested in.


   | 

GMSLU Course: GMSL522D - Quick Start
------------------------------------

Coming soon!

|

GMSLU Course: GMSL522E - MAX96724 Video Pattern Generator
---------------------------------------------------------

In this course, the MAX96724 is programmed to output a repeating colorbar pattern without any necessary video input. This feature allows customers to easily test out their SoC's MIPI receiver very easily and quickly. Make sure to watch the proceeding GMSLU lab videos pertaining to the GMSL522 development board before continuing with this exercise.

::

   -Connect a USB cable between P6 of the GMSL522 board, and your Windows PC. 
   -On the GMSL522 board, change directory to where the GMSL server app is located: **//cd ~/gmsl/AD-GMSL522-SL/gmsl-uart-server-app///**
   -Run the server: **//./gmsl-uart-server -i /dev/i2c-1 -s /dev/ttyGS0 -v//**
   -Open the GMSL Windows GUI on your Windows PC. 
   -Once the GUI is pulled up, you should see a MAX96717 on the serializer tab, and a MAX96724 on the deserializer side. 
   -Open the video timing and pattern generator tool in the GUI. This tool is located under the Tools>Video Config tab.
   -Set you pattern generator tool to the following settings:{{ :resources:eval:user-guides:ad-gmsl522-sl:724_pgen.png?400

   |}}
   -Click Start Video Generation
   -Open a new terminal
   -Configure the video pipeline on the GMSL522 board: **//v4l2-ctl --device /dev/video2 --set-fmt-video=width=1920,height=1080,pixelformat=AR24//**
   -start the video streaming app, QV4L2: **//qv4l2 -d /dev/video2//**

|

GMSL522F - MAX96717 Video Pattern Generator
-------------------------------------------

In this course, the MAX96717 to output a repeating colorbar pattern without any necessary video input. This feature allows customers to easily test out many of the features in both the MAX96717 as the MAX96724 without the added difficulty of bringing up an image sensor. Make sure to watch the proceeding GMSLU lab videos pertaining to the GMSL522 development board before continuing with this exercise.

::

   -Connect a USB cable between P6 of the GMSL522 board, and your Windows PC. 
   -Connect a fakra coax cable between J7 and J2 of the GMSL522 board. 
   -On the GMSL522 board, change directory to where the GMSL server app is located: **//cd ~/gmsl/AD-GMSL522-SL/gmsl-uart-server-app///**
   -Run the server: **//./gmsl-uart-server -i /dev/i2c-1 -s /dev/ttyGS0 -v//**
   -Open the GMSL Windows GUI on your Windows PC. 
   -Once the GUI is pulled up, you should see a MAX96717 on the serializer tab, and a MAX96724 on the deserializer side. 
   -Open the CSI Programming Tool in the GMSL GUI. 
   -Configure the tool like the following: 
     *DES = MAX96724
     *SER = MAX96717 -- I2C Address 0x84
     *Incoming DT = RGB888 on the SER side (technically it is generated within the serializer, but we do this so that the serializer’s video pipes are correctly configured). 
     *Outgoing datatype: RGB888 from the MAX96724 Port B
   -Generate and export the script. 
   -Configure the SERDES by loading that CPP file.
   -Open the video timing and pattern generator tool in the GUI. This tool is located under the Tools>Video Config tab. 
   -Set your pattern generator tool to the following settings:{{ :resources:eval:user-guides:ad-gmsl522-sl:717_pgen.png?400 |}}
   -Click "Start Video Generation"
   -Open a new terminal on the GMLS522
   -Configure the video pipeline on the GMSL522 board: **//v4l2-ctl --device /dev/video2 --set-fmt-video=width=1920,height=1080,pixelformat=AR24//**
   -start the video streaming app, QV4L2: **//qv4l2 -d /dev/video2//**
