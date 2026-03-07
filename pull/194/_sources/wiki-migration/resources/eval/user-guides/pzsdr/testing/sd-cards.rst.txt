Creating ADRV9361 RF SOM production testing SD cards
====================================================

SOM2
----

The code for all the various pieces required to create testing SD cards can be found on Github. See the following list for links to the various parts:

.. admonition:: Download
   :class: download

   **U-Boot:**

   
   -  U-Boot test branch: :git-u-boot-xlnx:`tree/pzsdr-test`
   -  U-Boot QSPI booting branch: :git-u-boot-xlnx:`tree/qspiboot`
   
   A version of U-Boot built from the test branch will run through the tests assuming a properly formatted SD card while the QSPI branch is for flashing to the device.
   
   **No-OS:**
   
   -  HDL dev branch: :git-hdl:`projects/pzsdr/ccbrk`
   -  Loopback test: :git-no-OS:`pzsdr/ccbrk/loopback`
   
   Xilinx SDK 2015.2 is currently required to build both of these projects.


In order to create an SD card for testing, the various test binaries, u-boot versions, and other files must be built and placed in the correct location in the boot partition of the standard SD card image. See the following hierarchy of test and flash related files on an SD card's boot partition mounted on /media/BOOT:

::

   /media/BOOT
   ├── BOOT.BIN
   ├── devicetree.dtb
   ├── flash
   │   ├── BOOT.BIN
   │   ├── system.bit
   │   └── uramdisk.image.gz
   ├── ad9361.elf
   ├── loopback.elf
   └── uImage

Follow the instructions below to create the various files in the hierarchy seen above. Note that it is assumed the required Xilinx SDKs are installed and initialized properly for use in the current environment.

FPGA bitstream
~~~~~~~~~~~~~~

The bitstream is already available on the SD card in the bootgen_sysfiles.tgz file located in the related platform directory on the BOOT partition. This assumes the SD card's BOOT partition is already mounted at /media/BOOT.

::

   mkdir -p ~/zynq-picozed-sdr2/bootgen
   cd /media/BOOT/zynq-picozed-sdr-bob
   tar -xvf bootgen_sysfiles.tgz -C ~/zynq-picozed-sdr2/bootgen
   mkdir -p /media/BOOT/flash
   cp ~/zynq-picozed-sdr2/bootgen/system.bit /media/BOOT/flash/

Now we have to build a different bitstream used for various test features:

::

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/hdl.git
   cd hdl/projects/pzsdr/ccbrk
   git checkout dev
   make pzsdr.ccbrk

Symlink the created bitstream into the unpacked bootgen directory for future use when building BOOT.BIN files.

::

   cd ~/zynq-picozed-sdr2/bootgen
   ln -s ~/zynq-picozed-sdr2/hdl/projects/pzsdr/ccbrk/ccbrk_pzsdr.runs/impl_1/system_top.bit

Creating the main U-Boot test binary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main U-Boot test ELF should be created using a process similar to the following:

::

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/u-boot-xlnx.git
   cd u-boot-xlnx
   git checkout pzsdr-test
   export CROSS_COMPILE=arm-xilinx-eabi-
   make zynq_picozed_sdr2_defconfig
   make -j$(nproc)

Next the BOOT.BIN file must be created. Note that the default bif file used for BOOT.BIN generation has a few file name mismatches in it. We've already corrected the bitstream name mismatch (since we symlinked our own version in) and to fix the FSBL so do the below (or change the name in the bif file):

::

   cd ~/zynq-picozed-sdr2/bootgen
   mv zynq_fsbl_0.elf fsbl.elf

Copy in the U-Boot ELF file you just built:

::

   cd ~/zynq-picozed-sdr2/bootgen
   cp ~/zynq-picozed-sdr2/u-boot-xlnx/u-boot ./u-boot-picozed.elf

Create the BOOT.BIN file:

::

   cd ~/zynq-picozed-sdr2/bootgen
   bootgen -image zynq.bif -w -o BOOT.BIN

Copy the BOOT.BIN file to the root directory of the SD card's BOOT partition:

::

   cp BOOT.BIN /media/BOOT/

Creating the QSPI U-Boot binary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This assumes you have already cloned the U-Boot repository in the previous step.

Build the U-Boot version targeting booting from QSPI flash:

::

   cd ~/zynq-picozed-sdr2/u-boot-xlnx
   git clean -fxd
   git checkout qspiboot
   make zynq_picozed_sdr2_defconfig
   make -j$(nproc)

Copy it into the previously created folder of bootgen files:

::

   cp u-boot ~/zynq-picozed-sdr2/bootgen/u-boot-picozed-qspi.elf

Create a new bif file in ~/zynq-picozed-sdr2/bootgen named zynq-qspi.bif with the following content:

::

   the_ROM_image:
   {
   [bootloader]./fsbl.elf
   ./u-boot-picozed-qspi.elf
   }

This removes the FPGA bitstream from the generated BOOT.BIN (it'll be flashed separately) and points to our newly generated U-Boot ELF file.

Generate the new BOOT.BIN file:

::

   cd ~/zynq-picozed-sdr2/bootgen
   bootgen -image zynq-qspi.bif -w -o BOOT.BIN

Copy the BOOT.BIN file to the flash directory of the SD card's BOOT partition:

::

   cp BOOT.BIN /media/BOOT/flash/

Creating the no-OS test ELFs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/no-OS.git
   cd no-OS/pzsdr/ccbrk/loopback
   ln -s ~/zynq-picozed-sdr2/hdl/projects/pzsdr/ccbrk/ccbrk_pzsdr.sdk/system_top.hdf
   make
   cp sdk/loopback/Release/loopback.elf /media/BOOT

TODO: ad9361

Linux and the device tree
~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

SOM1
----

TODO

.. _fpga-bitstream-1:

FPGA bitstream
~~~~~~~~~~~~~~

TODO

.. _creating-the-main-u-boot-test-binary-1:

Creating the main U-Boot test binary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

.. _creating-the-qspi-u-boot-binary-1:

Creating the QSPI U-Boot binary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

.. _creating-the-no-os-test-elfs-1:

Creating the no-OS test ELFs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

TODO: ad9361

.. _linux-and-the-device-tree-1:

Linux and the device tree
~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

FMC Carrier
-----------

The code for all the various pieces required to create testing SD cards can be found on Github. See the following list for links to the various parts:

.. admonition:: Download
   :class: download

   **U-Boot:**

   
   -  U-Boot test branch: :git-u-boot-xlnx:`tree/pzsdr-ccfmc-test`
   
   **No-OS:**
   
   -  Tests for various loopback modules (PMOD, camera, FMC, SFTP+) that are run at the U-Boot level: :git-no-OS:`pzsdr/ccfmc/loopback`
   -  HDL dev branch: :git-hdl:`projects/pzsdr/ccfmc`
   
   **Test script:**
   
   -  Bash script to automate the various interface tests: :git-board-tests:`picozed-sdr2-fmc/runtests`.sh
   
   The remaining files used by the tests can be found in the parent directory: :git-board-tests:`picozed-sdr2-fmc`


First, write the latest available SD card image found at :doc:`/wiki-migration/resources/tools-software/linux-software/zynq_images` to a spare card and prepare the card to boot into Linux as detailed on that page.

When that is ready follow the instructions below the create the various files necessary to run the test suite.

.. _fpga-bitstream-2:

FPGA bitstream
~~~~~~~~~~~~~~

Unpack the bootgen_sysfiles.tgz file located in the related platform directory on the BOOT partition of the SD card. The following commands assume the SD card's BOOT partition is already mounted at /media/BOOT.

::

   mkdir -p ~/zynq-picozed-sdr2/bootgen
   cd /media/BOOT/zynq-picozed-sdr-bob
   tar -xvf bootgen_sysfiles.tgz -C ~/zynq-picozed-sdr2/bootgen

Build a loopback-enabled bitstream:

::

   mkdir -p ~/zynq-picozed-sdr2
   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/hdl.git
   cd hdl/projects/pzsdr/ccfmc
   git checkout dev
   make pzsdr.ccfmc

Symlink the created bitstream into the unpacked bootgen directory for future use when building BOOT.BIN files.

::

   cd ~/zynq-picozed-sdr2/bootgen
   ln -s ~/zynq-picozed-sdr2/hdl/projects/pzsdr/ccbrk/ccbrk_pzsdr.runs/impl_1/system_top.bit

.. _creating-the-main-u-boot-test-binary-2:

Creating the main U-Boot test binary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main U-Boot test ELF should be created using a process similar to the following:

::

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/u-boot-xlnx.git
   cd u-boot-xlnx
   git checkout pzsdr-ccfmc-test
   export CROSS_COMPILE=arm-xilinx-eabi-
   make zynq_picozed_sdr2_defconfig
   make -j$(nproc)

Next the BOOT.BIN file must be created. Note that the default bif file used for BOOT.BIN generation has a few file name mismatches in it. We've already corrected the bitstream name mismatch (since we symlinked our own version in) and to fix the FSBL so do the below (or change the name in the bif file):

::

   cd ~/zynq-picozed-sdr2/bootgen
   mv zynq_fsbl_0.elf fsbl.elf

Copy in the U-Boot ELF file you just built:

::

   cd ~/zynq-picozed-sdr2/bootgen
   cp ~/zynq-picozed-sdr2/u-boot-xlnx/u-boot ./u-boot-picozed.elf

Create the BOOT.BIN file:

::

   cd ~/zynq-picozed-sdr2/bootgen
   bootgen -image zynq.bif -w -o BOOT.BIN

Copy the BOOT.BIN file to the root directory of the SD card's BOOT partition:

::

   cp BOOT.BIN /media/BOOT/

.. _creating-the-no-os-test-elfs-2:

Creating the no-OS test ELFs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next, create the no-OS loopback test ELF:

::

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/no-OS.git
   cd no-OS/pzsdr/ccfmc/loopback
   ln -s ~/zynq-picozed-sdr2/hdl/projects/pzsdr/ccbrk/ccbrk_pzsdr.sdk/system_top.hdf
   make
   cp sdk/loopback/Release/loopback.elf /media/BOOT

Linux test scripts
~~~~~~~~~~~~~~~~~~

Finally the test script repository must cloned onto the rootfs of the card and the script must be set to be run automated on boot. This can either be done by mounting the SD card on another computer or running the SD card on a board connected to the Internet which we'll assume is the case here.

Once the board is booted up open a terminal and run the following commands:

First, clone the board testing git repo analog user's home directory:

::

   git clone https://github.com/analogdevicesinc/board-tests.git

Then remove all applications that are currently set to run at boot:

::

   rm -f /home/analog/.config/autostart/*

Next, create a desktop launcher to launch the tests on boot:

::

   cat << EOF > /home/analog/.config/autostart/picozed-sdr2-fmc-tests.desktop
   [Desktop Entry]
   Exec=sudo /home/analog/board-tests/picozed-sdr2-fmc/runtests.sh
   Terminal=True
   Type=Application
   Name=PicoZed SDR2 FMC tests
   GenericName=PicoZed SDR2 FMC tests
   EOF

Finally, make the test script executable:

::

   chmod +x /home/analog/.config/autostart/picozed-sdr2-fmc-tests.desktop

Now the SD card could be ready to automatically launch the test script in a terminal window on startup.

Breakout Board
--------------

ADI image changes
~~~~~~~~~~~~~~~~~

-  Run ``mount /dev/mmcblk0p1 /media/boot/``
-  Run ``dtc -I dtb -O dts -o /media/boot/devicetree.dts /media/boot/devicetree.dtb`` to obtain the source file in text format (.dts) from binary blob (.dtb)
-  Remove all gpio_keys mappings from the device tree (``vim /media/boot/devicetree.dts``)\ ``gpio_keys {
           compatible = "gpio-keys";
           #address-cells = <0x1>;
           #size-cells = <0x0>;
           autorepeat;

           pb0 {
               label = "Left";
               linux,code = <0x69>;
               gpios = <0x6 0x36 0x0>;
           };

           pb1 {
               label = "Right";
               linux,code = <0x6a>;
               gpios = <0x6 0x37 0x0>;
           };

           pb2 {
               label = "Up";
               linux,code = <0x67>;
               gpios = <0x6 0x38 0x0>;
           };

           pb3 {
               label = "Down";
               linux,code = <0x6c>;
               gpios = <0x6 0x39 0x0>;
           };

           sw0 {
               label = "SW0";
               linux,input-type = <0x5>;
               linux,code = <0x0>;
               gpios = <0x6 0x3e 0x0>;
           };

           sw1 {
               label = "SW1";
               linux,input-type = <0x5>;
               linux,code = <0x1>;
               gpios = <0x6 0x3f 0x0>;
           };

           sw2 {
               label = "SW2";
               linux,input-type = <0x5>;
               linux,code = <0x2>;
               gpios = <0x6 0x40 0x0>;
           };

           sw3 {
               label = "SW3";
               linux,input-type = <0x5>;
               linux,code = <0x3>;
               gpios = <0x6 0x41 0x0>;
           };
       };``
-  Run ``dtc -I dts -O dtb -o /media/boot/devicetree.dtb /media/boot/devicetree.dts`` to convert back the source file (.dts) in binary blob (.dtb)
-  Copy ``runtests.sh`` to ``/root``
-  Run ``chmod +x runtests.sh`` to make the script executable
-  Add in ``/etc/rc.local`` a call to ``/root/runtests.sh``

Raspberry Pi image changes
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Configure `Adafruit PiTFT 2.2" HAT Mini Kit - 320x240 2.2" TFT - No Touch <https://www.adafruit.com/product/2315>`_
-  Add in ``/home/pi/`` the ``breakout_board_test.py`` and ``reboot_poweroff.py`` files.
-  Add at the end of ``.bashrc`` file this line:

   -  ``python /home/pi/breakout_board_test.py & python /home/pi/reboot_poweroff.py &``
