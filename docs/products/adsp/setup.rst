.. _adsp setup:

Getting started
===============

ADSP evaluation boards do not ship with pre-installed software. The chips also
do not support booting directly from SD cards. Therefore the evaluation boards
need to be bootstrapped over JTAG using a :adi:`ADI ICE-1000 or ICE-2000 JTAG
debugger <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/emulators.html>`.

Download a binary release
-------------------------

Navigate to the :git-br2-external:`br2-external releases page <releases+>` and
download the appropriate `images-*.tar.xz` release archive.

Setup a JTAG connection
-----------------------

Build and install the ADI fork of OpenOCD:

.. shell:: sh

    $git clone https://github.com/analogdevicesinc/openocd
    $cd openocd
    $./bootstrap
    $./configure
    $make -j$(nproc)

Run ``openocd`` with either ``ice1000.cfg`` or ``ice2000.cfg`` and one of the
following configs:

- ``adspsc58x.cfg``
- ``adspsc59x_a55.cfg``

For example, for the ICE-1000 and ADZS-SC589-EZLITE run the following:

.. shell:: sh

    ~/openocd
    $src/openocd -f ice1000.cfg \
    $    -f adspsc58x.cfg \
    $    --search tcl/ \
    $    --search tcl/interface/ \
    $    --search tcl/target/

Boot U-Boot Proper
------------------

To boot U-Boot SPL and U-Boot Proper using GDB install
``gdb-multiarch`` on Debian or Ubuntu systems:

.. shell:: sh

    $sudo apt-get install -y gdb-multiarch

In the terminal, ``cd`` into the extracted release archive or the appropriate
build output directory.

Then download the GDB automation :download:`u-boot.gdb` script using:

.. shell:: sh

    $curl -O https://raw.githubusercontent.com/analogdevicesinc/documentation/refs/heads/main/docs/products/adsp/u-boot.gdb

Once downloaded, start GDB and run the following command with the script in order to
load and run both U-Boot stages as:

.. shell:: sh

    $gdb-multiarch -x u-boot.gdb

Boot Linux
----------

Once U-Boot Proper is running and a U-Boot prompt is accessible over serial it
is possible to load and boot Linux.

In a new terminal ``cd`` into the extracted release archive and run a web
server (e.g. ``python -m http.server``).

In the console of U-Boot, we can load images as:

.. code-block:: console

    => dhcp
    => wget ${fdt_addr_r} <host-ip-addr>:/<path-to-image>