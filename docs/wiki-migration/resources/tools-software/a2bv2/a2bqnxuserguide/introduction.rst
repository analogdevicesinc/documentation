:doc:`Click here to return to A2B QNX User Guide Homepage. </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide>`

Introduction
============

The demo A2B Application on QNX is built by re-implementing A2B Stack’s Platform Abstraction Layer (PAL) for QNX operating system. The architecture of A2B Stack Software PAL and demo application on QNX is as shown in below Figure. The PAL layer on QNX resides in user space. It utilizes the standard device drivers to interact with the hardware. Hence the PAL layer on QNX and demo application can be configured to be run on any platform supporting a port of QNX.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/a2b_stack_on_qnx_arch.png
   :align: center
   :width: 600px

The demo application on QNX supports A2B network discovery and configuration.

Scope
-----

The scope of the document is to provide steps to build and run the A2B Stack Software and demo application on QNX running on BeagleBone Black Board. Guidelines are also provided to port the demo application on QNX for a different platform. The document also covers the various features of demo application and A2B Stack Software on QNX.
