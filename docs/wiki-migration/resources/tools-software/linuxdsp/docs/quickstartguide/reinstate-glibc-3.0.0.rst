Switch back to glibc from musl
==============================

.. note::

   This is relevant to :doc:`Linux for ADSP-SC5xx Processors 3.0.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>` only. Earlier version do not feature this choice, and on later versions this has been simplified a lot


This page provides instructions for reverting a toolchain change introduced in version 3.0.0 of Linux for ADSP-SC5xx Processors.

Why was that changed?
---------------------

It is described in the upstream repo of U-Boot: `U-Boot Falcon Mode <https://github.com/u-boot/u-boot/blob/master/doc/README.falcon>`_. In short, it's a way to shorten the boot time by allowing the SPL (Secondary Program Loader) to boot the kernel directly, without loading the full bootloader.

A change has been made to reduce the rootFS size as seen here :git-lnxdsp-adi-meta:`here <commit/540ce488d3364caf4e783f018b12087857bbdebf>`. Part of that change is to depend on the ``poky-tiny`` DISTRO instead of ``poky``. The ``poky-tiny`` uses **``musl``** to reduce the overall image size. That means that the SDK that is built by Yocto on version 3.0.0 uses **``musl``** libc while prior to that, it generated a **``glibc``** toolchain.

Although **``musl``** is a lot leaner than **``glibc``**, they are largely compatible. There is `a number of functional differences listed on wiki.musl-libc.org <https://wiki.musl-libc.org/functional-differences-from-glibc.html>`_ for further reading.

How to switch back?
-------------------

Switching back to **``glibc``** is as simple as a single commit revert on the ``meta-adi`` layer. Here's how to do that:

Prepare the build
~~~~~~~~~~~~~~~~~

Follow the steps in the :doc:`3.0.0 Quickstart guide </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>` up to and including the '**Preparing the buildtool'** step.

Revert the commit
~~~~~~~~~~~~~~~~~

A single commit must be reverted to fall back into **``glibc``** (``$PROJECTDIR`` being whatever you called your project upon creating it):

.. code:: bash

   $ cd $PROJECTDIR/sources/meta-adi/

   $ git revert 540ce488d3364caf4e783f018b12087857bbdebf

At this point you need to edit ``meta-adi-adsp-sc5xx/classes/adsp-sc5xx.bbclass`` with your favorite text editor, e.g.

.. code:: bash

   $ vi meta-adi-adsp-sc5xx/classes/adsp-sc5xx.bbclass

and delete the bottom conflict text:

.. code:: diff

   <<<<<<< HEAD

   IMAGE_FSTYPES:append = " tar.xz jffs2 "

   #For some reason on poky-tiny, INIT_MANAGER="systemd" does not appear to work
   #For now, let's relink directly to systemd
   fakeroot do_set_init(){
       rm -rf ${IMAGE_ROOTFS}/sbin/init
       ln -s /lib/systemd/systemd ${IMAGE_ROOTFS}/sbin/init
   }

   addtask do_set_init after do_rootfs before do_image
   =======
   >>>>>>> parent of 540ce48... Further reduce RFS size via poky-tiny.conf instead of poky.conf

Proceed with building.
~~~~~~~~~~~~~~~~~~~~~~

You can now proceed with the rest of the Quickstart guide instructions.

.. important::

   Doing this will increase the FIT+RFS sizes such that the SPI boot paths no longer work because of insufficient space on the smaller board flashes (16MB or 32MB). TFTP/NFS/MMC/SD should still work.

