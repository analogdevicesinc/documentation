How to develop ADI Yocto Linux with your own repositories
=========================================================

This documentation guides users how to develop Yocto Linux Products on ADI SC5XX platforms with developers' own repositories. 

HOST Setup
----------

.. code:: bash

   $ sudo apt-get update
   $ sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm u-boot-tools
   $ sudo apt-get install repo

Source Code Preparation
-----------------------

Download Source code
~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   $ mkdir ~/yocto
   $ repo init -u https://github.com/analogdevicesinc/lnxdsp-repo-manifest.git -b release/yocto-1.0.0

Change lnxdsp-adi-meta and lnxdsp-scripts to point to your own repo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   $ cd ~/yocto/.repo/manifests/

Aplly below patches into the lnxdsp-repo-manifest

.. code:: diff

   diff --git a/default.xml b/default.xml
   index 244bf04..45abdf8 100644
   --- a/default.xml
   +++ b/default.xml
   @@ -5,12 +5,12 @@
    
      <remote fetch="https://git.yoctoproject.org/git" name="yocto"/>
      <remote fetch="https://github.com/openembedded" name="oe"/>
   -  <remote fetch="https://github.com/analogdevicesinc" name="adigithub"/>
   +  <remote fetch="$YOUR_REPO_PATH" name="dte"/>
    
      <project remote="yocto" revision="50f33d3bfebcbfb1538d932fb487cfd789872026" name="poky" path="sources/poky"/> <!-- thud revision -->
      <project remote="oe" revision="4cd3a39f22a2712bfa8fc657d09fe2c7765a4005" name="meta-openembedded" path="sources/meta-openembedded"/> <!-- thud revision -->
   -  <project remote="adigithub" revision="develop/yocto-1.0.0" name="lnxdsp-adi-meta" path="sources/meta-adi"/>
   -  <project remote="adigithub" revision="develop/yocto-1.0.0" name="lnxdsp-scripts" path="sources">
   +  <project remote="dte" revision="develop/yocto-1.0.0" name="lnxdsp-adi-meta" path="sources/meta-adi"/>
   +  <project remote="dte" revision="develop/yocto-1.0.0" name="lnxdsp-scripts" path="sources">
         <linkfile dest="setup-environment" src="setup-environment"/>
      </project>>

.. code:: bash

   $ repo sync

Change u-boot and linux-kernel URI to point to your own repo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   $ cd ~/yocto/sources/

Aplly below patches into your own build script, take adsp-sc589-ezkit as an example, the same patch should be applied into adsp-sc589-mini, adsp-sc584-ezkit, adsp-sc573-ezkit.

.. code:: diff

   diff --git a/base/adsp-sc589-ezkit/local.conf b/base/adsp-sc589-ezkit/local.conf
   index 260a16b..b3c69f1 100644
   --- a/base/adsp-sc589-ezkit/local.conf
   +++ b/base/adsp-sc589-ezkit/local.conf
   @@ -21,6 +21,11 @@
    # This sets the default machine to be adsp-sc589-ezkit if no other machine is selected:
    MACHINE ?= "adsp-sc589-ezkit"
    
   +UBOOT_GIT_URI ?= "git://$YOUR_REPO_PATH/u-boot.git"
   +UBOOT_BRANCH ?= "develop/yocto-1.0.0"
   +KERNEL_GIT_URI ?= "git://$YOUR_REPO_PATH/lnxdsp-linux.git"
   +KERNEL_BRANCH ?= "develop/yocto-1.0.0"
   +
    #
    # Where to place downloads
    #

Then you can start your development based on your own repos.

::

   $ cd ~/yocto/
   $ source setup-environment -m adsp-sc589-ezkit
   Your build environment has been configured with:

   MACHINE=adsp-sc589-ezkit

   You can now run 'bitbake <target>'
   Some of common targets are:
   u-boot-adi
   linux-adi
   adsp-sc5xx-full
   adsp-sc5xx-minimal
   adsp-sc5xx-ramdisk

   $ bitbake ...

Back To :doc:`Linux for SC5xx: Frequently Asked Questions </wiki-migration/resources/tools-software/linuxdsp/docs/qa/start>`
