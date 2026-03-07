.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


Building The SDK
================

.. important::

   In order to build the SDK it is necessary to follow the relevant Quickstart Guide (:doc:`SC589-EZKIT and SC589-MINI </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc589>`, :doc:`SC594-EZKIT </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc594>`, :doc:`SC598-EZKIT </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc598>`) for Setting Up Your Host PC.


Preparing the buildtool
-----------------------

Yocto requires the environment to be configured before building is possible.  A setup-environment script in the griffin, gxp or gxp2 folder contains all the required environment settings.

::

   $ source setup-environment -m adsp-sc589-ezkit

or

::

   $ source setup-environment -m adsp-sc589-mini

or

::

   $ source setup-environment -m adsp-sc594-som-ezkit

or

::

   $ source setup-environment -m adsp-sc598-som-ezkit

Sourcing the script will configure your build environment and create a build folder along with a local build configuration file.  See the Yocto Manual for further details.

.. important::

   Note that the build environment needs to be sourced once only before building.  If later working in a different terminal the setup-environment script should be sourced again.  If sourcing the setup-environment script is done without specifying the machine Yocto will reuse the previous configuration settings and retain any changes made to the files in the conf folder.


| 
| ==== Building the SDK ==== The SDK can be built for the adsp-sc5xx-minimal image or the adsp-sc5xx-full image. To build the SDK for the adsp-sc5xx-minimal image invoke bitbake from within the build directory created previously.

::

   $ bitbake adsp-sc5xx-minimal -c populate_sdk

or for the adsp-sc5xx-full image

::

   $ bitbake adsp-sc5xx-full -c populate_sdk

When the build has completed you will find a set of files in the <BUILD_DIR>/tmp/deploy/sdk directory. For the minimal image on SC594:

::

   $ ls tmp/deploy/sdk
   poky-glibc-x86_64-adsp-sc5xx-minimal-armv7at2hf-neon-adsp-sc594-som-ezkit-toolchain-3.1.8.host.manifest
   poky-glibc-x86_64-adsp-sc5xx-minimal-armv7at2hf-neon-adsp-sc594-som-ezkit-toolchain-3.1.8.sh
   poky-glibc-x86_64-adsp-sc5xx-minimal-armv7at2hf-neon-adsp-sc594-som-ezkit-toolchain-3.1.8.target.manifest
   poky-glibc-x86_64-adsp-sc5xx-minimal-armv7at2hf-neon-adsp-sc594-som-ezkit-toolchain-3.1.8.testdata.json

or the full image on SC598:

::

   $ ls tmp/deploy/sdk
   poky-glibc-x86_64-adsp-sc5xx-full-aarch64-adsp-sc598-som-ezkit-toolchain-3.1.8.host.manifest
   poky-glibc-x86_64-adsp-sc5xx-full-aarch64-adsp-sc598-som-ezkit-toolchain-3.1.8.sh
   poky-glibc-x86_64-adsp-sc5xx-full-aarch64-adsp-sc598-som-ezkit-toolchain-3.1.8.target.manifest
   poky-glibc-x86_64-adsp-sc5xx-full-aarch64-adsp-sc598-som-ezkit-toolchain-3.1.8.testdata.json

The poky-glibc-x86_64-adsp-sc5xx-minimal-armv7at2hf-neon-adsp-sc594-som-ezkit-toolchain-3.1.8.sh and the poky-glibc-x86_64-adsp-sc5xx-full-aarch64-adsp-sc598-som-ezkit-toolchain-3.1.8.sh are self-extracting archives containing the SDK.

| 
| ==== Installing the SDK ==== Invoke the self-extracting archive. It will default to installing to /opt/poky/3.1.8 but gives you the option to select your own install folder during the installation. For the minimal image on SC594

::

   $ ./poky-glibc-x86_64-adsp-sc5xx-minimal-armv7at2hf-neon-adsp-sc594-som-ezkit-toolchain-3.1.8.sh
   Poky (Yocto Project Reference Distro) SDK installer version 3.1.8
   =================================================================
   Enter target directory for SDK (default: /opt/poky/3.1.8): 
   You are about to install the SDK to "/opt/poky/3.1.8". Proceed [Y/n]? y
   Extracting SDK...................................................................done
   Setting it up...done
   SDK has been successfully set up and is ready to be used.
   Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
   $ . /opt/poky/3.1.8/environment-setup-armv7at2hf-neon-poky-linux-gnueabi

or for the full image on SC598

::

   ./tmp/deploy/sdk/poky-glibc-x86_64-adsp-sc5xx-full-aarch64-adsp-sc598-som-ezkit-toolchain-3.1.8.sh
   Poky (Yocto Project Reference Distro) SDK installer version 3.1.8
   =================================================================
   Enter target directory for SDK (default: /opt/poky/3.1.8):
   You are about to install the SDK to "/opt/poky/3.1.8". Proceed [Y/n]? y
   Extracting SDK................................................................................................................................................................................................................done
   Setting it up...done
   SDK has been successfully set up and is ready to be used.
   Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
    $ . /opt/poky/3.1.8/environment-setup-aarch64-poky-linux

Your SDK is now installed.
