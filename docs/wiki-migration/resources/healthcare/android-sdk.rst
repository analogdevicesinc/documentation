Android SDK
===========

Description
-----------

The ADI Study Watch provides an object-oriented interface for interacting with ADI's VSM study watch platform. User application can use the SDK to receive complete bytes packets over a physical interface (USB or BLE) and decode it. The functionality is organized into applications, manages the sensors, system-level functionality (i.e. file system), and algorithms. The hierarchy of objects within the SDK mirrors the applications present on the device. Each application has its own object within the SDK hierarchy, which is used to interact with that application.

Brief guide on using the SDK
----------------------------

-  Firmware Setup - To set up firmware for the Study Watch follow the steps provided in :git-study-watch-sdk:`Firmware Upgrade Guide <firmware/Study_Watch_Firmware_Upgrade.pdf>`
-  Getting started with SDK - For details click :git-study-watch-sdk:`Using SDK <android#study-watch-android-sdk>`

Sample Implementations
----------------------

**Example 1**: :git-study-watch-sdk:`Streaming EDA sensor data <android/AndroidSamples/app/src/main/java/com/analog/androidsamples/EDAExample.java>` - Start and subscribe to the EDA stream; the watch starts sending stream through BLE, SDK receives packets and sends back to the user callback for EDA data.

**Example 2**: :git-study-watch-sdk:`Taking input from internal storage file <android/AndroidSamples/app/src/main/java/com/analog/androidsamples/InputFromInternalStorage.java>` - Reading a file in android can be tricky, this example explaining how to write dcb from a file to the Study watch.

**Example 3**: :git-study-watch-sdk:`Running SDK commands in ExecutorService <android/AndroidSamples/app/src/main/java/com/analog/androidsamples/UsingExecutorService.java>` - How to run SDK commands on a separate thread as an executor service; this allows users to run commands without blocking their UI threads.

**Example 4**: :git-study-watch-sdk:`Streaming ADPD sensor data <android/AndroidSamples/app/src/main/java/com/analog/androidsamples/ADPDStreamExample.java>` - configurations required to stream all 4 LEDs simultaneously for ADPD.

SDK Documentation
-----------------

Documentation is located at - `SDK Documentation <https://analogdevicesinc.github.io/study-watch-sdk/android>`_
