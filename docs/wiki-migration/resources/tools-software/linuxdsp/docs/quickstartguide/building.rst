Building The Linux Components
=============================

Linux for SC5xx uses `Yocto <https://www.yoctoproject.org/software-overview/>`_ to build and package all the components required for you to install Linux on your development board and build your own applications.

| 
| ==== Setting Up The Components ==== To build the components we first setup the environment for Yocto, telling it what we want to build, then we build the components.

To set up the environment for your sc5xx board:

::

   $ source setup-environment -m adsp-sc589-ezkit

.. note::

   **$ source setup-environment -m <MACHINE> -b <BUILDDIR>**

   
   ::
   
      ;options: 
      ;**-m <MACHINE>** 
      :if you setup the MACHINE, the local.conf would be automatically set to the default template, 
   
   so make sure to save your own changes in local.conf once you pass this option to the script Supported MACHINE:
   
   ::
   
                     *adsp-sc573-ezkit
                     *adsp-sc584-ezkit
                     *adsp-sc589-ezkit
                     *adsp-sc589-mini
   
   ::
   
      ;**-b <BUILDDIR> **
      :The default BUILDDIR is "build", you could pass another dir to the script
   
   If no option passed to the script, the YOCTO would reuse the build/ dir as your default build environment.


| 
| ==== Building The Components ==== To build your components:

::

   $ bitbake <TARGET>

::

   ;**''TARGET'':**
   :u-boot-adi         
   :linux-adi          
   :adsp-sc5xx-ramdisk 
   :adsp-sc5xx-minimal 
   :adsp-sc5xx-full    

Remember add "**-C compile**" option to bitbake if you want to compile and deploy your images at second time.

Other build rules are summarized on the :doc:`ADI Yocto Metalayer </wiki-migration/resources/tools-software/linuxdsp/docs/adi-yocto-metalayer>` page.

.. tip::

   Warning: Your first build will be slow. Yocto will be downloading all the required sources and building all the toolchains required for the creation of your tools. Subsequent builds will be faster.


| 
| ==== The Build Output ==== The build output can be found in the **build/tmp/deploy/images/<MACHINE>** directory.

| 
| ---- **PREV:** :doc:`Setting Up The Sources </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/source-setup>` **NEXT:** :doc:`Install Linux On The Hardware </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing>`
