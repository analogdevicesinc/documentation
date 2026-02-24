.. _petalinux meta-adi-bypass:

Custom Device Trees with DTG (meta-adi Bypass)
==============================================
For certain applications, it may be necessary to leverage the Kernel, libraries
and other tools provided by *meta-adi*, but bypass the device tree process it
generates.  For this type of application, the device tree will be based on the
Petalinux Device Tree Generator (DTG).    The most practical use case for this
is working with custom hardware, however Petalinux does provide out of the box
support for Xilinx development kits.

.. tip::
    This procedure acts as a “Quick start” guide for getting up and running with
    a custom device tree and Petalinux's DTG.  There are several features of the
    DTG not covered in this, which may be helpful for your project.  Refer to
    Xilinx/AMD UG1144 - Petalinux Tools Reference Guide, DTG Settings sections
    for more detailed information.

    `UG1144 (docs.amd.com) <https://docs.amd.com/r/2023.2-English/ug1144-petalinux-tools-reference-guide/Overview/>`_

1. Bypass meta-adi's Device trees
---------------------------------
In order to strictly use the Petalinux device tree support, and bypass *meta-adi's*
man-in-the-middle approach to device trees, add the following highlighted line
to ``<project>/project-spec/meta-user/conf/layer.conf``. This addition will
still allow meta-adi recipes to run  (for kernel, IIO, etc), but exclude the
device tree support.

.. code-block::
   :caption: conf/layer.conf
   :emphasize-lines: 18

   # We have a conf and classes directory, add to BBPATH
   BBPATH .= ":${LAYERDIR}"

   # We have recipes-* directories, add to BBFILES
   BBFILES += "${LAYERDIR}/recipes-*/*/*.bb \
       ${LAYERDIR}/recipes-*/*/*.bbappend"

   # Define dynamic layers
   BBFILES_DYNAMIC += " \
   xilinx-tools:${LAYERDIR}/meta-xilinx-tools/recipes-*/*/*.bbappend \
   "

   BBFILE_COLLECTIONS += "meta-user"
   BBFILE_PATTERN_meta-user = "^${LAYERDIR}/"
   BBFILE_PRIORITY_meta-user = "7"
   LAYERSERIES_COMPAT_meta-user = "langdale"

   BBMASK += "meta-adi-xilinx/recipes-bsp/device-tree/"

2. Select Petalinux Template
----------------------------
Petalinux's DTG generates a basic device tree based on the exported XSA file from
your HDL project. This will configure the minimal parameters for the SoC.  In
addition to this basic generation, an optional EvKit may be selected.  When
selecting an EvKit template, in addition to the SoC parameters, all of the fixed
devices on the kit (such as power control ICs, PHYs, etc) are also automatically
included into the device tree stack. This is recommended when using an EvKit for
prototyping, to reduce the additional work needed to bring the boards up.

If using custom hardware, or hardware not provided by Xilinx, the additional
board devices will need to be included by you in your custom device tree.
The following table (extracted from the UG1144 Reference Guide) shows the
available EvKits in the Petalinux 2023.2 distribution.  Always refer to
`UG1144 (docs.amd.com) <https://docs.amd.com/r/2023.2-English/ug1144-petalinux-tools-reference-guide/Overview/>`_
for the most up to date information.

.. list-table::
    :header-rows: 1

    * - BSP
      - Machine
    * - ZCU102
      - zcu102-rev1.0
    * - ZCU104
      - zcu104-revc
    * - ZCU106
      - zcu106-reva
    * - ZCU111
      - zcu111-reva
    * - ZCU1275
      - zcu1275-revb
    * - ZCU1285
      - zcu1285-reva
    * - ZCU216
      - zcu216-reva
    * - ZCU208
      - zcu208-reva
    * - ZCU670
      - zcu670-revb
    * - ZCU208-SDFEC
      - zcu208-reva
    * - ZCU100
      - zcu100-revc
    * - ZC702
      - zc702
    * - ZC706
      - zc706
    * - ZEDBOARD
      - zedboard
    * - AC701
      - ac701-full
    * - KC705
      - kc705-full
    * - KCU105
      - kcu105
    * - VCU118
      - vcu118-rev2.0
    * - SP701
      - sp701-rev1.0
    * - VCK190
      - versal-vck190-reva-x-ebm-01-reva
    * - VPK120
      - versal-vpk120-reva
    * - VMK180
      - versal-vmk180-reva-x-ebm-01-reva
    * - VPK180
      - versal-vpk180-reva

To set the template, run ``petalinux-config`` for your project. Navigate to
**DTG Settings**, then select **MACHINE_NAME** to choose the board.
Enter the appropriate machine from the list above.  In this example,
the ZCU102 is used, so the machine is set to ``zcu102-rev1.0``.

.. tip::
    For custom hardware, or to not utilize a provided board, the ``MACHINE_NAME``
    should be set to *template*.

.. image:: petalinux-config-machinename.png
.. image:: petalinux-config-machine-zcu102.png

3. Disabling PL Node Generation
-------------------------------
By default, Petalinux's DTG generates device tree nodes for any IP blocks
included in the PL.  This may be applicable for some scenarios, however when
attempting to use device specific Linux drivers (such as IIO drivers ), this
will cause device tree conflicts and require deleting nodes similar to what
*meta-adi* does.  To disable the automatic generation of PL nodes and avoid the
conflicts, run ``petalinux-config``, navigate to **DTG Settings**, and enable
**Remove PL From Devicetree**.

.. image:: petalinux-config-remove-pl.png

4. Adding Custom Device Trees
-----------------------------
At this point, Petalinux & DTG will generate a barebones device tree of either
the SoC only (if *template* was selected for ``MACHINE_NAME``), or the core
components for the EvKit selected for ``MACHINE_NAME``.  To add custom nodes,
the ``project-spec/meta-user/recipes-bsp/device-tree`` configuration will be used.

All of the device tree information can be placed in ``system-user.dtsi``, or it
may be included via separate file(s) for modularity and maintainability.
In this example, we'll assume we have a device tree file ``ad9081_fmc_support.dtsi``,
which includes all of the nodes needed to talk to the AD9081 FMC card.
By leveraging a modular device tree like this, it is possible to include it in
multiple different projects for common function through different boards.

**1. Add files to the correct folder location**

First, copy all device tree files you'd like to use to
``project-spec/meta-user/recipes-bsp/device-tree/files``. There should already
be a ``system-user.dtsi`` file in there. Keep that file.

**2. Add your files to device-tree.bbappend**

Next, any provided files above must be added to ``device-tree.bbappend``.
Open ``project-spec/meta-user/recipes-bsp/device-tree/device-tree.bbappend``
and edit as shown below.  You may have more files, or files with different names.

In addition, the ``KERNEL_INCLUDE:append`` line must be specified to allow
inclusion of various device tree bindings files.  By default, Petalinux DTG only
references a small subset of available bindings. The inclusion of this line
allows access to all binding files within the kernel sources.

.. code-block::
    :caption: device-tree.bbappend
    :emphasize-lines: 4, 6, 7

    FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

    SRC_URI:append = " file://system-user.dtsi \
                       file://ad9081_fmc_support.dtsi"

    KERNEL_INCLUDE:append = " \
        ${STAGING_KERNEL_DIR}/include"

    KERNEL_DTB_PATH = "${WORKDIR}"
    require ${@'device-tree-sdt.inc' if d.getVar('SYSTEM_DTFILE') != '' else ''}

**3. Edit system-user.dtsi**

``System-user.dtsi`` is automatically included at the tail end of the
Petalinux/DTG device tree hierarchy.  Modifications may be performed directly in
here, or this may include additional files, or both.  In this case, we'll just
include the new FMC support file. Edit
``project-spec/meta-user/recipes-bsp/device-tree/files/system-user.dtsi``:

.. code-block:: dts
    :caption: system-user.dtsi
    :emphasize-lines: 3

    /include/ "system-conf.dtsi"

    #include "ad9081_fmc_support.dtsi"

Petalinux can now be built and deployed as normal, incorporating your new device
trees and updates. The resulting dts hierarchy can be found in
``<project>/components/plnx_workspace/device-tree/device-tree`` for reference
purposes.
