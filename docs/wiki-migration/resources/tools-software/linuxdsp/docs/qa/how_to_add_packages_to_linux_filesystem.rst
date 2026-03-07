How To Add Packages To Your Own Linux Filesystem
================================================

This page introduces a simple way to add packages to your own Linux filesystem in Yocto Linux. Take the example that add the package "ethtool" to your own target adsp-custom-ramdisk image.

| 
| ===== Find the Yocto Project recipe ===== Users could add their own packages instead of the "ethtool", the first step is to find out the Yocto Project recipe that includes "ethtool". The way to find recipes is to go to the `Openembedded Layer Index <https://layers.openembedded.org/layerindex/branch/master/recipes/>`_ web site.

Below picture shows how to find the package "gstreamer" in this website.

| |image1|
| ===== Add the Package to filesystem ===== **Method 1:** After finding the specific recipe name, users need to add it to the image by adding this line to conf/local.conf which is highly recommended:

::

   IMAGE_INSTALL_append = "ethtool"

**Method 2:** Users can also add the package into your own custom-recipe.bb file directly, for example, apply below patch would add the ethtool package into ramdisk filesystem.

.. code:: diff

   diff --git a/meta-custom/recipes-custom/images/adsp-custom-ramdisk.bb b/meta-custom/recipes-custom/images/adsp-custom-ramdisk.bb
   index a98b1f9..e070e6f 100644
   --- a/meta-custom/recipes-custom/images/adsp-custom-ramdisk.bb
   +++ b/meta-custom/recipes-custom/images/adsp-custom-ramdisk.bb
   @@ -6,6 +6,8 @@ IMAGE_INSTALL = " \
        packagegroup-core-boot \
        linux-firmware-fastboot \
        fastboot-listener \
   +    ethtool \
   "
   DISTRO_FEATURES = " ram"

| 
| ===== Build the Target Images ===== Run below command to bitbake the ramdisk filesystem, the package ethtool would be deployed into Linux filesystem directly. Refer to the :doc:`Building The Linux Components </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/building>` for more details on how to build the Yocto Linux Images.

::

   bitbake adsp-custom-ramdisk

options:

::

   ; -c CMD, --cmd=CMD
   : Specify the task to execute. The exact options available depend on the metadata. Some examples might be 'compile' or 'populate_sysroot' or 'listtasks' may give a list of the tasks available.
   ; -C INVALIDATE_STAMP
   : Invalidate the stamp for the specified task such as 'compile' and then run the default task for the specified target(s).

   | 

Installing Linux On The Hardware
--------------------------------

Pease refer this page :doc:`Installing Linux On The Hardware </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing>`.

|

| ---- Back To :doc:`Linux for SC5xx: Frequently Asked Questions </wiki-migration/resources/tools-software/linuxdsp/docs/qa/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/qa/gstreamer.png
