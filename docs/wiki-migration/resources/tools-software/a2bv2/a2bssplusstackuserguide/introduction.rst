Introduction
============

| :doc:`Click here to return to the A2B SSPLUS STACK USER GUIDE </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`
| This document guides the user in porting the A2B Stack onto custom platforms. The document provides details of stack layers that need to be reused and the layers that need to be re-implemented when porting to a custom platform. The document also provides code snippets to enable users to build an A2B application on a custom platform using the stack.

A2B Stack is a highly portable and flexible framework for developing and deploying A2B networks in automotive environments. The Stack embodies the following set of features:

-  Full power and Line fault diagnostics
-  Extensive logging and debug capability
-  Modular plugin architecture
-  Well-defined Platform Abstraction Layer (PAL)
-  Message-based command and control
-  Extensible command set

Scope
-----

The scope of this document is to briefly illustrate the steps to integrate the A2B Stack (Core A2B Network stack referred to below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/introduction>`) to any platform and build an A2B application using exported ‘Bus configuration files’ from SigmaStudio.

A2B Software Stack Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/a2bsoftwarestackarchitecture_a2bplus.jpg
   :align: center

.. container:: centeralign

   \ **Figure:** A2B Software Stack Architecture


Refer to :doc:`drawinga2bschematics </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/drawinga2bschematics>` for the steps to draw customized A2B schematics using the SigmaStudioPlus tool.
