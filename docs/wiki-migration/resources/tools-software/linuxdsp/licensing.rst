Yocto Linux for ADSP-SC5xx Processors: Licensing Information
============================================================

The Yocto Linux for ADSP-SC5xx Processors product is provided in source form. Each source code module (zip file, Git repository) is provided with licensing information. As applications are developed and the development board file-system built, different packages will be added and removed, resulting in different licensing requirements for each customer. It is your responsibility to understand the software you are distributing and the licensing restrictions upon that software. The following information provided to assist you in understanding the license requirements that you will need to comply with when distributing your product.

Finding the Licensing Requirements for your Product Build
---------------------------------------------------------

When building your application images with Yocto, the licensing information for all modules included in the build will be collated in to the **build/tmp/deploy/licenses** directory.

Within the **build/tmp/deploy/licenses/<target>-<board>-<datestamp>** directory you can also find a full package manifest file containing a list of all the package used, their version and license type.

For example, when building the **adsp-sc5xx-full** for the **ADSP-SC589 EZ-KIT** the license.manifest file is created in the **build/tmp/deploy/licenses/adsp-sc5xx-full-adsp-sc589-ezkit-20200605083605** directory containing information in the following format:

::

   PACKAGE NAME: acl
   PACKAGE VERSION: 2.2.52
   RECIPE NAME: acl
   LICENSE: GPLv2+

   PACKAGE NAME: alsa-conf
   PACKAGE VERSION: 1.1.6
   RECIPE NAME: alsa-lib
   LICENSE: LGPLv2.1 & GPLv2+

   PACKAGE NAME: alsa-lib
   PACKAGE VERSION: 1.1.6
   RECIPE NAME: alsa-lib
   LICENSE: LGPLv2.1 & GPLv2+

   PACKAGE NAME: alsa-state
   PACKAGE VERSION: 0.2.0
   RECIPE NAME: alsa-state
   LICENSE: MIT

Excluding specific licenses from your product build
---------------------------------------------------

Yocto provides a build-time configuration option that allows you to avoid specific licenses in your product build. By correctly defining the **INCOMPATIBLE_LICENSE** option in you **conf/local.conf** file you can prohibit the inclusion of packages which match the list of defined incompatible licenses.

For more information please refer to the `Yocto Reference Manual <https://www.yoctoproject.org/docs/2.4/ref-manual/ref-manual.html#var-INCOMPATIBLE_LICENSE>`__.

| 
| ---- \**HOME PAGE: \*\* :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>`
