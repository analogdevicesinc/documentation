Device Tree - Overlays
======================

Device trees are inherently complex files encapsulating the entire hardware profile of an embedded system, ranging from the lowest level DMA and interrupt controllers of a SoC, all the way through all the peripherals attached to all buses.  Prior to device trees being incorporated into Linux, hardware information was hard coded into the kernel, meaning the entire Linux system needed to be rebuilt for hardware tweaks. Not practical at all.  Device trees improved upon this by having a single source of hardware information being read in at boot time to describe how to initialize the system, which can be built separately from the main Linux kernel.

Device tree overlays are the next iteration of this progression, by allowing portions of the system's device tree to be patched at boot time through simple overlay files.  This allows the overlay developer to focus just on necessary changes the overlay needs and has several benefits:

-  The complexities of the entire system can be ignored
-  Reduces risk of accidental modify a core system function when working with the full tree
-  Lots of overlays can be developed for a hardware platform, changing which are enabled from boot to boot
-  Overlays can be applied to multiple hardware platforms (under certain conditions)

A Practical Use Case
--------------------

One great use case to illustrate the benefits of device tree overlays is utilizing ADI's Kuiper Linux distribution to evaluate hardware with a Raspberry PI.   The Kuiper Linux kernel comes pre-installed with all of ADI's Linux device drivers pre-loaded.   This is a great feature, and time saver for customers, as rebuilding a Linux kernel can be cumbersome and problematic.  However, since most (if not all) of our devices sit on non-enumerable buses (I2C, SPI, etc), a device tree entry must exist for the devices present.  This is where overlays come in.  An overlay for each device can be created, allowing customers to mix and match which overlays are included at boot to support their hardware.  Similarly, if a device parameter needs to be modified, a new overlay for that device can simply be created, versus a full device tree modification.   This can also facilitate testing multiple device configurations easily.

A listing of the overlays that come pre-included with Kuiper Linux can be found here: :git-linux:`tree/rpi-6`.1.y/arch/arm/boot/dts/overlays

Overlay Format
--------------

The device tree overlay format is nearly identical to a standard device tree.  Some basic syntax is discussed here: :doc:`Devicetree Syntax </wiki-migration/playground/devicetree-intro>`.  The follow breaks down the key components of an overlay file

Header
~~~~~~

Device tree overlays are essentially standalone device trees.  As such, all overlay files must start with the device tree header:

.. code:: syntaxhighlighter-pre

   /dts-v1/;
   /plugin/;

If there are any include files (discussed later), the #include statements will occur prior to header:

.. code:: syntaxhighlighter-pre

   #include <dt-bindings/gpio/gpio.h>
    
   /dts-v1/;
   /plugin/;

Root Node
~~~~~~~~~

Following the header, the remainder of the overlay is encapsulated within the root node block. The root node starts with a ``%%/ { ''and is closed with a'' }; %%`` All of the text between these brackets make up the actual content of the overlay.

.. code:: syntaxhighlighter-pre

   /dts-v1/;
   /plugin/;

   / {
   /*
     * Useful overlay content goes here
    */
   };

.. tip::

   Device trees use the same commenting syntax as C files. Use // and /\* \*/ as necessary to comment the device trees.


Fragments
~~~~~~~~~

Fragments are a unique feature specific to overlay files.  For every node of the system's device tree that will be modified by the overlay, it should be encapsulated in a fragment.  The following example shows 2 fragments within the root node, but the count is not limited.

.. code:: syntaxhighlighter-pre

   /dts-v1/;
   /plugin/;

   / {
       fragment@0 {
           //Fragment 0 work here
       };
    
       fragment@1 {
           //Fragment 1 work here
       };
   };

Defining the Target
~~~~~~~~~~~~~~~~~~~

The first item within a fragment is defining the target node to modify.  This would be the alias of an existing node within the baseline device tree.  The ``__overlay__`` block is created to house the modified values.

.. code:: syntaxhighlighter-pre

   /dts-v1/;
   /plugin/;

   / {
       fragment@0 {
           target = <&i2c1>;
           __overlay__ {
               //The real work happens here
           };
       };
    
       fragment@1 {
            target = <&spi0>;
           __overlay__ {
               //The real work happens here
           }; 
       };
   };

Overlay Content
~~~~~~~~~~~~~~~

Finally, the actual content of each overlay fragment is defined. In this very simple, hypothetical, example, an adxl375 is added to i2c1, and a ad5686 added to spi0.

.. code:: syntaxhighlighter-pre

   /dts-v1/;
   /plugin/;

   / {
       fragment@0 {
           target = <&i2c1>;
           __overlay__ {
               status = "okay";
               adxl375@053 {
                   compatible = "adi,adxl375";
                   reg = <0x53>;
                   interrupt-parent = <&gpio>;
                   interrupts = <25 2>;
               };
           };
       };
    
       fragment@1 {
            target = <&spi0>;
           __overlay__ {
               status = "okay";
               ad5686r@0{
                   compatible = "adi,ad5686r";
                   reg = <0>;
                   spi-max-frequency = <1000000>;
                   spi-cpha;
               };
           }; 
       };
   };

Building an Overlay
-------------------

Compiling device tree overlays (and full device trees for that matter), is done using the device tree compiler or ``dtc`` tool.  Luckily for us, ``dtc`` is included with Kuiper Linux, so no additional installation is required.  To compile the device tree the command syntax is simple:

.. code:: syntaxhighlighter-pre

   dtc -I dts -O dtb my_overlay.dtso > my_overlay.dtbo

where:

-  ``%% ''''-I dts'''' %%`` indicates the input format is device tree source
-  ``%%-O dtb %%``\ indicates the output format is device tree binary/blob
-  ``my_overlay.dtso`` is our overlay source file
-  ``> my_overlay.dtbo`` is the output redirected to be written to the ``my_overlay.dtbo`` file

This command performs the necessary steps for simple overlays which do not rely on any #include or other pre-processor directives.

Overlays with #include
~~~~~~~~~~~~~~~~~~~~~~

As hardware and systems become more complicated, as well as a desire to limit the use of 'magic numbers' and replace them with constants, device trees have begun to utilize include files to standardize definitions. This is nearly identical to the process a C compiler will use to handle a #include statement.   It's easy to understand benefits to having cleaner, more maintainable device trees through the use of pre-processor constants.  However, utilizing the #include feature makes building the device trees and overlays more complicated. This will be covered in an upcoming page.

Applying Overlays
-----------------

RaspberryPI
~~~~~~~~~~~

For RaspberryPI's the overlay .dtbo file can be placed in the /boot/overlays folder of the SD card to allow it to be found at boot time.  To enable the overlay, the /boot/config.txt file must modified.  Open /boot/config.txt in your favorite editor (such as mousepad) add or remove the necessary dtoverlay lines.

.. important::

   You'll need to be an administrator, or open the config.txt as ``sudo`` to be able to save the changes.


The dtoverlay line(s) specify which overlay files should be incorporated at boot time.  The following example shows adding the rpi-adxl345.dtbo overlay, simply use your overlay file name instead. Important! Note the .dtbo file extension is omitted as this is automatically implied. 

.. code:: syntaxhighlighter-pre

   dtoverlay=rpi-adxl345

You can add as many overlays to the config.txt file as you need to describe your hardware.  Once saved, reboot the system to see the changes applied.
