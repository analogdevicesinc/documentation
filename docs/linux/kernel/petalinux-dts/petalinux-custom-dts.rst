.. _petalinux custom-dts:

Custom Device Trees with meta-adi
=================================
This method of device tree modification allows for a custom dts files located
outside of the kernel source tree, that gets incorporated in via the *meta-adi*
device tree recipe.  This allows the flexibility and fine grained control of
a custom device tree, while still being able to include and reference other dts
files from the kernel source, such as a evaluation kit's base file.

Procedure
---------
The following procedure describes how to incorporate a custom device tree file
into the *meta-adi* device tree recipe.

.. note::
    These instructions leverage the *meta-user* layer of the project, but can easily
    be incorporated into a custom layer if desired.

#. Add your desired dts/dtsi files to the ``project-spec/meta-user/recipes-bsp/device-tree/files``
   folder. This includes the device tree contents and pl-delete-nodes file.

    .. important::
        Even if you don't intend to delete any PL nodes, the *meta-adi* build
        steps require a ``pl-delete-nodes-<dtsfile>`` file. It can be empty
        if you want.  Existing ``pl-delete-nodes-`` files are located in
        ``meta-adi/meta-adi-xilinx/recipes-bsp/device-tree/files``.

#. Add the files to the ``SRC_URI:append`` line of the
   ``project-spec/meta-user/recipes-bsp/device-tree/device-tree.bbappend`` file.
#. In ``device-tree.bbappend`` Set the ``KERNEL_DTB_PATH`` to ``"${WORKDIR}"``
   to point to the correct files folder.
#. Modify ``project-spec/meta-user/conf/petalinuxbsp.conf`` for the newly created
   ``KERNEL_DTB`` device tree name.
#. Build the project as normal using ``petalinux-build``.

The following example copied the ``zynqmp-zcu102-rev10-ad9081-m8-l4.dts`` from
the kernel sources and ``pl-delete-nodes-zynqmp-zcu102-rev10-ad9081-m8-l4.dtsi``
from *meta-adi* into the ``device-tree/files`` folder of *meta-user* as described
above. The copied files were named ``my_ad9081.dts`` and
``pl-delete-nodes-my_ad9081.dtsi`` respectively. The remainder of the changes
are highlighted for reference.

.. code-block::
    :caption: device-tree.bbappend
    :emphasize-lines: 4,5,7

    FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

    SRC_URI:append = " file://system-user.dtsi \
                    file://pl-delete-nodes-my_ad9081.dtsi \
                    file://my_ad9081.dts"

    KERNEL_DTB_PATH = "${WORKDIR}"
    require ${@'device-tree-sdt.inc' if d.getVar('SYSTEM_DTFILE') ≠ '' else ''}

.. code-block::
    :caption: petalinuxbsp.conf
    :emphasize-lines: 4

    #User Configuration

    #OE_TERMINAL = "tmux"
    KERNEL_DTB="my_ad9081"

