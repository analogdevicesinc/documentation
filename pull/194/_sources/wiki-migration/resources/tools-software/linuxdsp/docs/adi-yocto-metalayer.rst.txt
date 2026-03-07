.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


ADI Yocto Meta-layer
====================

Analog Devices provides a Yocto meta-layer that contains all the required rules to build a distribution and development tools for the ADSP-SC5xx processor.

The ADI meta-layer is located in the repository.

Build Rules
-----------

The following bitbake rules are supported by the ADI Yocto meta-layer:

Where **BUILD RULE** is one of the following:

-  **adsp-sc5xx-minimal**

   -  Minimal filesystem for Analog Devices ADSP-SC589 EZ-KIT, ADSP-SC584 EZ-KIT, ADSP-SC573-EZ-KIT and ADSP-SC589 Mini boards

-  **adsp-sc5xx-full**

   -  Full evaluation filesystem for Analog Devices ADSP-SC589 EZ-KIT, ADSP-SC584 EZ-KIT, ADSP-SC573-EZ-KIT and ADSP-SC589 Mini boards

-  **adsp-sc5xx-ramdisk**

   -  Minimal ramdisk image for Analog Devices ADSP-SC589 EZ-KIT, ADSP-SC584 EZ-KIT, ADSP-SC573-EZ-KIT and ADSP-SC589 Mini boards

-  **u-boot-adi**

   -  U-boot for Analog Devices ADSP-SC589 EZ-KIT, ADSP-SC584 EZ-KIT, ADSP-SC573-EZ-KIT and ADSP-SC589 Mini boards

-  **linux-adi**

   -  The linux kernel for Analog Devices ADSP-SC589 EZ-KIT, ADSP-SC584 EZ-KIT, ADSP-SC573-EZ-KIT and ADSP-SC589 Mini boards

-  **meta-sdk**

   -  SDK containing development tools for the SC5xx Linux environment
