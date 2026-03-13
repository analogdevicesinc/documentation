Setting Up The Sources
======================

Repository URLs
---------------

The following ADI managed repositories are used for the development of Linux for SC5xx:

+------------------------------------------------------------------------------------+----------------------+---------------------------+-----------------------+
| URL                                                                                | Description          | Latest Development Branch | Latest Release Branch |
+====================================================================================+======================+===========================+=======================+
| `lnxdsp-adi-meta <https://github.com/analogdevicesinc/lnxdsp-adi-meta>`_           | ADI Yocto meta layer | develop/yocto-1.0.0       | release/yocto-1.0.0   |
+------------------------------------------------------------------------------------+----------------------+---------------------------+-----------------------+
| `lnxdsp-repo-manifest <https://github.com/analogdevicesinc/lnxdsp-repo-manifest>`_ | Google repo manifest | develop/yocto-1.0.0       | release/yocto-1.0.0   |
+------------------------------------------------------------------------------------+----------------------+---------------------------+-----------------------+
| `lnxdsp-scripts <https://github.com/analogdevicesinc/lnxdsp-scripts>`_             | ADI scripts          | develop/yocto-1.0.0       | release/yocto-1.0.0   |
+------------------------------------------------------------------------------------+----------------------+---------------------------+-----------------------+
| `u-boot-sharc <https://github.com/analogdevicesinc/u-boot-sharc>`_                 | U-Boot Bootloader    | develop/yocto-1.0.0       | release/yocto-1.0.0   |
+------------------------------------------------------------------------------------+----------------------+---------------------------+-----------------------+
| `lnxdsp-linux <https://github.com/analogdevicesinc/lnxdsp-linux>`_                 | Linux kernel         | develop/yocto-1.0.0       | release/yocto-1.0.0   |
+------------------------------------------------------------------------------------+----------------------+---------------------------+-----------------------+
| `lnxdsp-examples <https://github.com/analogdevicesinc/lnxdsp-examples>`_           | ADI SHARC examples   | develop/yocto-1.0.0       | release/yocto-1.0.0   |
+------------------------------------------------------------------------------------+----------------------+---------------------------+-----------------------+

| 
| === Download Source code === In order to simplify the checkout process, ADI recommends using Google's `repo tool <https://gerrit.googlesource.com/git-repo/>`_. To use the repo tool create a workspace directory and clone the tool:

::

   mkdir <WORKSPACE>
   cd <WORKSPACE>
   mkdir bin
   curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ./bin/repo
   chmod a+x ./bin/repo

To set up the sources for development invoke repo with the path to the repo manifest and the active development branch:

::

   ./bin/repo init -u `lnxdsp-repo-manifest <https://github.com/analogdevicesinc/lnxdsp-repo-manifest>`_ -b release/yocto-1.0.0
   ./bin/repo sync

After the sync finished, you would get files just like the picture shows below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/yocto.png
   :width: 400px

--------------

**PREV:** :doc:`Setting Up The Host </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/setting_up_your_host_pc>` **NEXT:** :doc:`Building The Components </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/building>`
