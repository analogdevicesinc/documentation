SHARC Reusable Components
=========================

*This page will describe the SHARC Reusable Components repository and discuss how it can be used to customize frameworks and end applications for supported SHARC processors.*

Overview
--------

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sharc-reusable-components-github.png
   :align: center

The :git-https::`SHARC Reusable Components </github.com/analogdevicesinc/sharc-reusable-components/tree/1.2.0-Github>` are a collection of embedded C code packaged into a library of reusable components and starter examples designed to facilitate customers’ easy deployment into demo or production systems using a SHARC DSP. The construction of the modules and overall repository is based on a few key design metrics worth highlighting:

-  Modularity

   -  Ideally each module is self-contained and interoperability between modules is easy to develop.

-  Reusability

   -  Each module can be ported to new hardware (or even a new HAL) with minimal need for additional configuration.

-  Ease-of-Development

   -  A developer (customer or internal) should have to spend minimal time to prototype and test with each new module they roll in. Each module contains a readme.md or .txt which fully explains the entire integration process to roll it into a new framework (or for new hardware).
   -  Items are added based on how each module enables a customer use case, and how critical that use case is. A developer (customer or internal) should have to spend minimal time to prototype and test with each new module they roll in.

-  Ease-of-Licensing

   -  A "LICENSE" file is contained in every module which fully describes its licensing conditions. All open-source and proprietary components are labelled, and care is taken during development to try and use open-source-licensed libraries where possible.

This is **not a full-fledged framework** ready to run on a SHARC core for evaluation. Those do exist at the following links:

-  :git-https::`SAM-Audio-Starter (ADSC589-MINI) </github.com/analogdevicesinc/sam-audio-starter>`
-  :git-https::`ADZS-SC584-EZLITE Audio Starter </github.com/analogdevicesinc/ADZS-SC584-EZLITE-Audio-Starter>`
-  :git-https::`EV-SC594-EZKIT Audio Starter </github.com/analogdevicesinc/EV-SC594-EZKIT-Audio-Starter>`

These frameworks have documentation for getting started in the ":doc:`Advanced Audio Projects </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects>`" section of our Analog wiki. They are based on the Baremetal Framework for the SHARC Audio Module (SAM), so the full API documentation relies on the documentation for the :doc:`Baremetal Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal>`. The point of the Reusable Components repository is to enable customers to have their own frameworks for their own applications that are built from a bedrock of reliable high-quality components.

The SHARC Reusable Components are rigorously tested and written to as high a level of code quality and reliability as possible. However, users must be aware that this code is **<fc #ff0000>not cleared for production or validated by any third-party standards</fc>**. Users of the SHARC Reusable Components repository are responsible for validating their end applications to meet relevant standards needed for production. This collection of modules is to be considered high-quality evaluation code.

--------------

`SW Architecture #.|SW Architecture #.sharc-reusable-components:usage|Using SHARC Reusable Components <https://wiki.analog.com/_media/navigation Software Architecture #.>`__
