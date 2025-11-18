.. _adsp setup:

Getting started
===============

ADSP evaluation boards do not ship with pre-installed software. The chips also
do not support booting directly from SD cards. Therefore the evaluation boards
need to be bootstrapped over JTAG using a :adi:`ADI ICE-1000 or ICE-2000 JTAG
debugger <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/emulators.html>`.

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

In another terminal either ``cd`` into the extracted release archive or the
appropriate build output directory when building from source. Then load and run
the two U-Boot stages using ``gdb``. Note that Debian and Ubuntu ship
multi-architecture GDB support in a separate package.

After loading U-Boot SPL wait 2-3 seconds to allow SPL to complete execution
before interrupting it with ``^C``.

.. code-block:: console

    sudo apt-get install -y gdb-multiarch
    gdb-multiarch
    (gdb) load u-boot-spl
    (gdb) c
    ^C
    (gdb) load u-boot
    (gdb) c
