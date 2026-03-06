-  `Device Tree - Overlays <https://wiki.analog.com/devicetree-overlays>`__

Software for FAEs : Overlay From Scratch - MAX31855
===================================================

This walks through the process of creating an overlay for the RaspberryPI from scratch.  In this example, we'll be adding a brand new device to the system. The target hardware is the MAX31855 Thermocouple to Digital converter, via the MAX31855PMB1 PMOD board. This part was chosen due to an existing Linux driver, but lack of overlay to enable it within the Kuiper Linux system.

Step-by-Step
============

Step 1 - Verify a Driver Exists
-------------------------------

The first step is to verify a driver exists for the device under test.  For ADI devices, a list of support Linux drivers is maintained on the Wiki: :doc:`/wiki-migration/resources/tools-software/linux-drivers-all`

Step 2a - Determine the Driver
------------------------------

There are a couple different approaches to determining the compatible driver. The first step is looking at the Wiki driver listing page. Many devices have a sub wiki describing how to configure the device tree and use the device in Linux.  An example of this would be the `LTC2983 <:doc:`/wiki-migration/resources/tools-software/linux-drivers/iio-temperature/ltc2983`>`__.  Unfortunately the MAX31855 does not have a detailed page on the Wiki.

The next alternative is to look at the device tree bindings within the Linux kernel tree.  This can be found in Documentation/devicetree/bindings/<device class>.  The MAX31855 is a temperature device, and would be located in iio/temperature.  As luck would have it, a documentation entry exists for the MAX31855: :git-linux:`Documentation/devicetree/bindings/iio/temperature/maxim%2Cmax31855k`.yaml

If neither of these documentation sources exist, the next step would be to inspect the actual driver source code.  Similar structure to the bindings folder, the drivers are organized by device class. This part happens to be supported by maxim_thermocouple.c here: :git-linux:`drivers/iio/temperature/maxim_thermocouple`.c.  Code crawling is usually a last resort, and is outside the scope of this walkthrough.

Step 2b - Analyze the Bindings File
-----------------------------------

In the case of the MAX31855 there is not a fully written Wiki page, but rather a device tree bindings file.  Looking at the :git-linux:`maxim,max31855k.yaml <Documentation/devicetree/bindings/iio/temperature/maxim%2Cmax31855k.yaml>` file, we can see human readable format describing how to utilize the device within a device tree. Device properties are described, indicating options available to the user, as well as an example device tree entry (in most cases).  In the case of our MAX31855 device, there are no additional properties with the exception of providing a maximum clock speed for the SPI bus. The provided example entry is quite simple:

.. code:: syntaxhighlighter-pre

   spi {
       #address-cells = <1>;
       #size-cells = <0>;

       temp-sensor@0 {
           compatible = "maxim,max31855k";
           reg = <0>;
           spi-max-frequency = <4300000>;
       };
   };

Step 3 - Starting the Overlay
-----------------------------

The next step is to start the actual overlay file.  We will be performing the work on the actual target RaspberryPI.  Once the RaspberryPI is booted, open your favorite text editor and start a new overlay file by including the necessary header and fragment blocks as a boiler plate:

.. code:: syntaxhighlighter-pre

   /dts-v1/;
   /plugin/;

   / {
       fragment@0 {
       //Fragment 0 work here
       };
   };

Step 4 - Defining the Target
----------------------------

Next we'll need to define the overlay target.  For this hardware setup, the PMOD will be plugged into P1 of a `PMD-RPI-INTZ <:doc:`/wiki-migration/resources/eval/user-guides/circuits-from-the-lab/pmd-rpi-intz`>`__ adapter board, which corresponds to SPI0.  To support SPI0, our target will be defined as follows. 

.. code:: syntaxhighlighter-pre

   /dts-v1/;
   /plugin/;

   / {
       fragment@0 {
           target = <&spi0>;

           __overlay__ {
               #address-cells = <1>;
               #size-cells = <0>;
               status = "okay"; 
           };

       };
   };

You'll note the only content so far is setting the status to okay. This essentially ensures the bus is enabled.  Some handwaving can occur with the #address-cells and #size-cells properties, as these are copy and paste from other SPI related devices.  The description of those fields can be found in the :git-linux:`SPI bus binding documentation. <Documentation/devicetree/bindings/spi/spi-controller.yaml>`

Step 5 - Adding the Device
--------------------------

With the target defined, the device can be added.  The documentation provided a complete device tree entry for the MAX31855, which can be copied directly into the overlay.

.. code:: syntaxhighlighter-pre

   /dts-v1/;
   /plugin/;

   / {
       fragment@0 {
           target = <&spi0>;

           __overlay__ {
               #address-cells = <1>;
               #size-cells = <0>;
               status = "okay"; 

               temp-sensor@0 {
                   compatible = "maxim,max31855k";
                   reg = <0>;
                   spi-max-frequency = <4300000>;
               }; 
           };
       };
   };

Note: In the case of SPI devices the reg property indicates which Chip Select line of the bus to use. In this case, the PMOD is connected to CS0.  For I2C devices, the reg property is the bus address.

Step 6 - Deconflicting the Tree
-------------------------------

Prior to building the overlay, we need to ensure there is no conflict with existing entries. This takes some knowledge of what is currently running in the hardware system, and when possible it is best to replicate work done on other overlays which may use the same hardware bus.  In the case of the RaspberryPI, we need to ensure the userspace SPI bus access is not available.  To do this the spidev0 device will be set to disabled.    It is not guaranteed that spidev0 was enabled in the baseline device tree, but this is a precautionary measure.

.. code:: syntaxhighlighter-pre

   /dts-v1/;
   /plugin/;

   / {
       fragment@0 {
           target = <&spi0>;
           __overlay__ {
               #address-cells = <1>;
           #size-cells = <0>;
           status = "okay";  
               temp-sensor@0 {
                   compatible = "maxim,max31855k";
                   reg = <0>;
                   spi-max-frequency = <4300000>;
               };
           };
       };

       fragment@1 {
          target = <&spidev0>;
           __overlay__ {
               status = "disabled";
           };
       };
   }; 

Step 7 - Building the Overlay
-----------------------------

The overlay can now be built using the dtc utility. From the command line run ``dtc -I dts -O dtb rpi-max31855.dtso > rpi-max31855.dtbo``.  In my case, the source file was named rpi-max31855.dtso.

.. code:: syntaxhighlighter-pre

   analog@rpi1:~ $ dtc -I dts -O dtb rpi-max31855.dtso > rpi-max31855.dtbo

Step 8 - Deploying the Overlay
------------------------------

Copy the output file from the ``%%dtc ''command, in this case ''rpi-max31855.dtbo'' to the'' /boot/overlays'' folder.  You will need to use ''sudo %%``\ to perform this operation.

.. code:: syntaxhighlighter-pre

   analog@rpi1:~ $ sudo cp rpi-max31855.dtbo /boot/overlays/

Edit the /boot/config.txt file to include the new overlay.  You will also need to be sudo to perform this action.  Recall, the line is dtoverlay=<overlay>, with the file extension omitted.  Be sure to comment out (#) or delete any other overlays which may conflict on the SPI bus with this part.

.. code:: syntaxhighlighter-pre

   #dtoverlay=rpi-ad5592r
   dtoverlay=rpi-max31855
   #dtoverlay=spi0-2cs
   #dtparam=cs_pin=1,irq_gpio=25

Save the file and reboot the Raspberry PI.

Step 9a - Verifying the Overlay (Functional)
--------------------------------------------

With the overlay deployed, we can verify it was loaded and the device is functioning.  The easiest way to verify is to check the actual functionality of the driver. In the case of the MAX31855 it is an IIO temperature device.  We can run ``%%iio_info %%``\ to verify if the device exists as well as capture data from it.  In this case the device is present, with a raw value of 355 and a scale factor of 62.5.  The scale factor is in mC, which corresponds to 355*0.0652 = 22.1875C (71.9F), matching the ambient environment.

.. image:: https://wiki.analog.com/_media/software/learn/linux/980665874.png
   :alt: 980665874.png

Step 9b - Verifying the Overlay (Device Tree)
---------------------------------------------

In addition to the functional aspect, it is also possible to verify the overlay by inspecting the run-time device tree.  The systems device tree is located in the ``%%/proc/device-tree ''folder. From here, we can inspect everything that is currently mapped in the system.  This method is slightly more challenging as you need to have some fundamental understanding of the complete device tree. In the case of the SPI bus, it's parent is the ''soc''.  The ''soc ''has several SPI busses.  We make an assumption the lowest memory address is SPI0.  From there, we can see the ''temp-sensor@0%%`` device, and inspect its properties to confirm successful loading.

.. image:: https://wiki.analog.com/_media/software/learn/linux/980665887.png
   :alt: 980665887.png

Verification Hardware
---------------------

-  Raspberry PI 3B+

::

   *[[:adi:`en/resources/evaluation-hardware-and-software/evaluation-boards-kits/pmd-rpi-intz`.html|PMD-RPI-INTZ]] Raspberry Pi to PMOD/QuikEval™/LTpowerPlay® Adaptor HAT
   *[[:adi:`en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max31855pmb1`.html|MAX31855PMB1]], also available in the [[:adi:`media/en/news-marketing-collateral/solutions-bulletins-brochures/maxim-analog-essentials-collection`.pdf|Analog Essentials Kit]]

.. image:: https://wiki.analog.com/_media/software/learn/linux/980665904.png
   :alt: 980665904.png
