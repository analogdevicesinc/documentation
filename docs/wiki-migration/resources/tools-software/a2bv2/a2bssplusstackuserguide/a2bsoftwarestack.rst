A2B Software Stack
==================

| :doc:`Click here to return to the A2B SSPLUS STACK USER GUIDE </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`
| A2B Software Stack or simply referred as A2B Stack is a collection of functional blocks designed to efficiently configure, troubleshoot, and deploy A2B networks. The below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/a2bsoftwarestack>` shows the architecture of the stack software.

A2b Software Stack Architecture
-------------------------------

|image1|

.. container:: centeralign

   \ **Figure: A2b Software Stack Architecture**\


A2B Stack is platform agnostic. The functionalities of the core stack remain the same irrespective of the target platform. The stack can be used to build applications specific to any platform by re-implementing the Platform abstraction layer (PAL) as per the targeted platform.

PAL and Application layers need to be re-implemented depending on the target platform and the end application requirements.

Wrapper Services Layer helps in easy stack integration. It is the integrator’s choice to use it as-is or can be re-implemented. This layer can be further visualized as Wrapper Services Layer 1 (top-most layer) and Wrapper Services Layer 2 (layer just above the A2B stack and below Wrapper Services Layer 1)

The Stack is comprised of the following subsystems.

1. Scheduler

-  The scheduler is designed to efficiently coordinate network activities, especially during the discovery and configuration phase, and execute units of work encapsulated in messages and jobs.

2. Plugin Management

-  Plugin Management initializes and integrates a single master plugin and zero or more slave plugins into the Stack.

3. Diagnostics

-  The diagnostic APIs provide a uniform means for slave plugins, and the Stack itself, to transfer diagnostic information to the Application software.

4. Logging/Tracing

-  The logging and tracing subsystems provide a uniform way for plugins, and the Stack itself, to log interesting events throughout the network lifecycle.

5. Bus Configuration Parsing

-  The bus configuration parsing subsystem, which is external to the Stack, is responsible for parsing the output (BCF/BDD) of the Host Tool like SigmaStudioPlus.

6. Slave I2C/SPI communication

-  The slave I2C/SPI communication subsystem provides a more direct interface for plugins to communicate with slave devices. Depending on the role of the software entity (e.g. master plugin, slave plugin, or application) protective limits are placed on device access over I2C/SPI to minimize the potential of the issues.

7. Logging/Tracing

-  Optional Trace Support

   -  Trace domains (e.g., I2C, Plugin, Stack) and severity levels.

-  Optional Sequence Chart Generation

   -  Utilize PlantUML for Presentation
   -  Preprocessing support for enhanced charts

-  Stack APIs

   -  Register dumps, BERT counts, Node GPIO manipulation

Host-Target Software Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target software is a framework that hosts A2B Stack, Application, and other components specific to the targeted processor platform.

A2B stack, running on the Target Software framework, requires a bus configuration file produced by a Host network design tool like SigmaStudioPlus to configure an A2B network. Refer to the link: :doc:`a2bssplususerguide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>` for more details on drawing customized A2B schematics using SigmaStudioPlus.

Once an A2B schematic, corresponding to the Target system is modeled, and validated in SigmaStudioPlus, the schematic information is then exported (adi_a2b_busconfig.c file) and added to the Target software project. The Stack running on Target parses the information in this file and programs the A2B network accordingly.

The Host-Target software workflow in building an A2B application is shown in the Figure below


|image2|

.. container:: centeralign

   \ **Figure: Host Tool - Target Software Workflow**\


.. note::

   1.3.x stack differs from 19.11.x stack on the addition of new transceiver support for AD2430, AD2437 and AD2438


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/a2bsoftwarestackarchitecture_a2bplus.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/target_software_workflow.png
