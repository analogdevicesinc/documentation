Building The SDK
================

.. important::

   This version is under development


.. important::

   In order to build the SDK it is necessary to follow the relevant Quickstart Guide. For instructions, please refer to :doc:`Linux for ADSP-SC5xx Processors 3.0.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`\


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

When the build has completed you will find a set of files in the <BUILD_DIR>/tmp/deploy/sdk directory. For example, the full image on SC594:

::

   $ ls tmp/deploy/sdk
   adi-distro-musl-x86_64-adsp-sc5xx-full-cortexa5t2hf-neon-adsp-sc594-som-ezkit-toolchain-4.0.1.host.manifest
   adi-distro-musl-x86_64-adsp-sc5xx-full-cortexa5t2hf-neon-adsp-sc594-som-ezkit-toolchain-4.0.1.sh
   adi-distro-musl-x86_64-adsp-sc5xx-full-cortexa5t2hf-neon-adsp-sc594-som-ezkit-toolchain-4.0.1.target.manifest
   adi-distro-musl-x86_64-adsp-sc5xx-full-cortexa5t2hf-neon-adsp-sc594-som-ezkit-toolchain-4.0.1.testdata.json

The ``adi-distro-musl-x86_64-adsp-sc5xx-full-cortexa5t2hf-neon-adsp-sc594-som-ezkit-toolchain-4.0.1.sh`` is a self-extracting archive containing the SDK.

| 
| ==== Installing the SDK ==== Invoke the self-extracting archive. It will default to installing to ``/opt/adi-distro/4.0.1`` but gives you the option to select your own install folder during the installation. For the minimal image on SC594

::

   $ ./adi-distro-musl-x86_64-adsp-sc5xx-full-cortexa5t2hf-neon-adsp-sc594-som-ezkit-toolchain-4.0.1.sh
   Poky (Yocto Project Reference Distro) SDK installer version 4.0.1
   =================================================================
   Enter target directory for SDK (default: /opt/adi-distro/4.0.1):
   The directory "/opt/adi-distro/4.0.1" already contains a SDK for this architecture.
   Extracting SDK............................................................................................................................................................................done
   Setting it up...done
   SDK has been successfully set up and is ready to be used.
   Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
    $ . /opt/adi-distro/4.0.1/environment-setup-cortexa5t2hf-neon-poky-linux-musleabi

Your SDK is now installed.
