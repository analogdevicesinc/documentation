Advanced Audio Projects for the Sharc Audio Module
==================================================

*This is a tutorial which allows users to become familiar with the advanced audio project for the Sharc Audio Module.*

Overview
--------

In addition to the :doc:`Baremetal Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal>` as a software resource for experimenting with the SC589, a more advanced software project exists that allows users to quickly connect various audio inputs and outputs during run-time, giving them the capability to not only experiment with different audio-related technologies, but to also modify and add their own custom settings that may aid in rapid prototyping of their own systems. This is a basic framework that is supported on several different hardware platforms.

This framework supports an application which supports multiple audio sources and shell support, which allows interaction with the application to change various configurations and parameters during run-time.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/sam-audio-starter-terminal2.png
   :width: 400px

**Example interface for shell support**

.. important::

   This is an advanced project which requires users to compile software and navigate serial terminal programs and to use `Unix <https://mally.stanford.edu/~sr/computing/basic-unix.html>`__ based shell utilities for the command line.


--------------

Getting Started
---------------

The goal of this tutorial is to help users with the following:

-  :doc:`Set up pre-requisites required for this tutorial </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/prerequisites>`
-  :doc:`Set up environment and compile program </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/environment_setup>`
-  :doc:`Flash the bootloader and application </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/program-flash>`
-  :doc:`Set up and run the application with a chosen audio sink/source as an example - Analog Audio </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/examples-analog-audio>`
-  :doc:`Set up and run the application with a chosen audio sink/source as an example - USB Audio </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/examples-usb-audio>`
-  :doc:`Set up and run the application with a chosen audio sink/source as an example - Wave File Audio </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/examples-wav-audio>`
-  :doc:`Set up and run the application with a chosen audio sink/source as an example - Ethernet Audio using Static IP </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/examples-ethernet-audio>`
-  :doc:`Set up and run the application with a chosen audio sink/source as an example - Ethernet Audio using MDNS/DHCP </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/examples-ethernet-audio-mdns>`
-   :doc:`Set up and run the application with a chosen audio sink/source as an example - A2B Audio </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/examples-a2b-audio>`
-  :doc:`Set up and run the application with a chosen audio sink/source as an example - Signal Generator </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/examples-signal-generator>`
-  :doc:`Familiarize with additional capabilities of the shell command </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands>`
-  :doc:`Set up a debug session </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/debug-session>`
-  :doc:`Appendix A - Software/Hardware compatibility matrix </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`
-  :doc:`Appendix B - Common problems during setup and known issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`
-  :doc:`Appendix C - System and Audio Configurations </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-c>`
-  :doc:`View the Extended Knowledge Base for additional tips and tricks! </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base>`

--------------

.. note::

   This is a Windows-based tutorial only!


--------------

`Sharc Audio Module#.advanced-audio-projects|Advanced Audio Projects#.advanced-audio-projects:prerequisites|Prerequisites <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.>`__
