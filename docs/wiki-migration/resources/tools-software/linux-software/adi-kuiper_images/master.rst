HDL and Linux projects are build whenever there are new commits in `HDL </repo>hdl/tree/master>`__ or `Linux </repo>linux>`__ repositories. Output boot files are structured in folders as they would be on SD card, and archived.

Master Boot partition files
===========================

.. container:: center round box

   
   .. admonition:: Download
      :class: download

         
         -  `Master boot files <https://swdownloads.analog.com/cse/boot_partition_files/master/latest_boot_partition.tar.gz>`__
         
         -  MD5 checksum can be verified `here <https://wiki.analog.com/https/swdownloads.analog.com/cse/boot_partition_files/master/latest_boot.txt>`__
         

   
   .. important::

         
         -  It is recommended to use **master boot files** only if you really need them (for example features that are not part of any release yet) since the files may not be always in a good state. Check :doc:`Latest release </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>` for most recent tested boot files.
         

   
   .. tip::

         
         -  Inside downloaded archive is a **ReadMe.txt** file describing what files you need to copy on boot partition root depending on your hardware setup, and **VERSION.txt** file containing build dates and git commits.
         

   


Master Microblaze images
========================

.. container:: center round box

   
   .. admonition:: Download
      :class: download

         
         -  `Master microblaze images <https://swdownloads.analog.com/cse/microblaze/master/latest_microblaze_images.tar.gz>`__
         

   
   .. important::

         
         -  It is recommended to use **master microblaze images** only if you really need them (for example features that are not part of any release yet) since the files may not be always in a good state. Check :doc:`Latest microblaze released images </wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze_loading>` for most recent and tested images.
         

   
   .. tip::

         
         -  Inside every archive there is system_top.bit, simpleImage.<project name>.strip and a script to program it.
         

   


Master Nios2 images
===================

.. container:: center round box

   
   .. admonition:: Download
      :class: download

         
         -  `Master nios2 images <https://swdownloads.analog.com/cse/nios2/master/latest_nios2_images.tar.gz>`__
         

   
   .. important::

         
         -  It is recommended to use **master nios2 images** only if you really need them (for example features that are not part of any release yet) since the files may not be always in a good state. Check :doc:`Latest nios2 released images </wiki-migration/resources/tools-software/linux-drivers/platforms/nios2>` for most recent and tested images.
         

   
   .. tip::

         
         -  Inside every archive, there is zimage, <project name>.sof and a script to program it.
         

   


Master NO-OS files
==================

.. container:: center round box

   
   .. admonition:: Download
      :class: download

         
         -  `Master NO-OS images <https://swdownloads.analog.com/cse/nios2/master/latest_nios2_images.tar.gz>`__
         

   
   .. tip::

         
         -  Inside every archive there are different configurations <project name>.elf.
         -  Check :doc:`no-OS </wiki-migration/resources/no-os>` and :doc:`Quick validation with NO-OS for more information </wiki-migration/resources/fpga/quick_validation>`
         

   

