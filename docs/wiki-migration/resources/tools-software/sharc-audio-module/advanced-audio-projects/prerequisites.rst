Sharc Audio Module - Prerequisites
==================================

*The following items below list the hardware and software prerequisites needed to setup and run the Audio Starter Projects. Verify hardware and software compatibility requirements here:* :doc:`Hardware-Software Compatibility </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`\ *!*

Hardware Prerequisites
----------------------

*Choose the setup and needs based on desired example.*

Basic Analog Audio Only
~~~~~~~~~~~~~~~~~~~~~~~

-  Windows PC or laptop computer
-  :adi:`ICE-1000/ICE-2000 JTAG Emulator <ice1000>`
-  :doc:`ADZS-SC589-MINI </wiki-migration/resources/tools-software/sharc-audio-module/hardware/main-board>` *or* :adi:`ADZS-SC584-EZLITE <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-adsp-sc584.html>` *or* :adi:`EV-SC594-SOM <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-sc594-som.html#eb-overview>` plus :adi:`Carrier <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-somcrr-ezkit.html>` *or* :adi:`EV-SC598-SOM <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ev-sc598-som.html>` plus :adi:`Carrier <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-somcrr-ezkit.html>`
-  `Portable speaker with 3.5mm Aux Jack <https://www.amazon.com/Wireless-Speakers-Leadsound-Portable-computer/dp/B01HB18IZ4?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=AHMAYDZNJIWS6&th=1>`_ or equivalent
-  `3.5MM Stereo Audio Cable <https://www.amazon.com/Sabrent-Plated-Premium-Auxiliary-CB-AUX5/dp/B01277P0CG/ref=sr_1_3?crid=1UF9AE07JP2YC&keywords=3.5mm+stereo+cable+male+to+male+sabrent&qid=1666283694&qu=eyJxc2MiOiIwLjc4IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=3.5mm+stereo+cable+male+to+male+sabrent%2Caps%2C113&sr=8-3>`_ or equivalent
-  `RCA to 3.5mm cable <https://www.amazon.com/AmazonBasics-3-5mm-2-Male-Adapter-Stereo/dp/B01D5H8JW0?th=1>`_

Ethernet Audio
~~~~~~~~~~~~~~

*Note that this requires the Networking versions of the Audio Starter software to run! By default, the software that will be downloaded/cloned as per the upcoming instructions will be NOT be the Networking software. If you want to run the Ethernet examples, be sure to grab the Networking branch for your specific project (not all projects support Networking).* :doc:`See our software list here! </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`

-  Windows PC or laptop computer
-  :adi:`ICE-1000/ICE-2000 JTAG Emulator <ice1000>`
-  :doc:`ADZS-SC589-MINI </wiki-migration/resources/tools-software/sharc-audio-module/hardware/main-board>` *or* :adi:`ADZS-SC584-EZLITE <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-adsp-sc584.html>` *or* :adi:`EV-SC594-SOM <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-sc594-som.html#eb-overview>` plus :adi:`Carrier <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-somcrr-ezkit.html>` *or* :adi:`EV-SC598-SOM <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ev-sc598-som.html>` plus :adi:`Carrier <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-somcrr-ezkit.html>`
-  `Ethernet Cable x 2 <https://www.amazon.com/Mediabridge-Ethernet-Cable-Feet-31-399-10X/dp/B003O973OA/ref=pd_bxgy_vft_none_img_sccl_2/137-4526917-0523426?pd_rd_w=3uGzb&content-id=amzn1.sym.26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_p=26a5c67f-1a30-486b-bb90-b523ad38d5a0&pf_rd_r=XRSRR6S3PTDYRE3MM6V1&pd_rd_wg=aQXAF&pd_rd_r=cc85d224-3a33-499c-815d-389d76ded4d2&pd_rd_i=B003O973OA&psc=1>`_
-  `Ethernet Switch <https://www.amazon.com/TP-LINK-TL-SG105E-5-Port-Gigabit-Version/dp/B00N0OHEMA?pd_rd_w=fKCOS&content-id=amzn1.sym.724fac2e-0491-4f7a-a10d-2221f9a8bc9a&pf_rd_p=724fac2e-0491-4f7a-a10d-2221f9a8bc9a&pf_rd_r=FSPJ47F190XTS4JHG4FB&pd_rd_wg=am33y&pd_rd_r=7f216575-ecce-4c08-824b-d9c92ab1df2c&pd_rd_i=B00N0OHEMA&ref_=pd_bap_d_grid_rp_0_1_ec_t&th=1>`_ - :doc:`Not required for projects using MDNS/DHCP </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`!
-  `Portable speaker with 3.5mm Aux Jack <https://www.amazon.com/Wireless-Speakers-Leadsound-Portable-computer/dp/B01HB18IZ4?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=AHMAYDZNJIWS6&th=1>`_ or equivalent

A2B Audio
~~~~~~~~~

-  Windows PC or laptop computer
-  :adi:`ICE-1000/ICE-2000 JTAG Emulator <ice1000>`
-  :doc:`ADZS-SC589-MINI </wiki-migration/resources/tools-software/sharc-audio-module/hardware/main-board>` *or* :adi:`EV-SC594-SOM <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-sc594-som.html#eb-overview>` plus :adi:`Carrier <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-somcrr-ezkit.html>` *or* :adi:`EV-SC598-SOM <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ev-sc598-som.html>` plus :adi:`Carrier <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-somcrr-ezkit.html>`
-  :adi:`EVAL-AD2428WB1BZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad2428wb1bz.html>` with 1.8m twisted-pair CAT5e-rated cable with DuraClik™ connectors (should come with EVAL kit)
-  :adi:`ADZS-AD2428MINI <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adzs-ad2428mini.html>` - Only required for hardware platforms using EV-SOMCRR-EZKIT!
-  `Portable speaker with 3.5mm Aux Jack <https://www.amazon.com/Wireless-Speakers-Leadsound-Portable-computer/dp/B01HB18IZ4?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=AHMAYDZNJIWS6&th=1>`_ or equivalent
-  `3.5MM Stereo Audio Cable <https://www.amazon.com/Sabrent-Plated-Premium-Auxiliary-CB-AUX5/dp/B01277P0CG/ref=sr_1_3?crid=1UF9AE07JP2YC&keywords=3.5mm+stereo+cable+male+to+male+sabrent&qid=1666283694&qu=eyJxc2MiOiIwLjc4IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=3.5mm+stereo+cable+male+to+male+sabrent%2Caps%2C113&sr=8-3>`_ or equivalent

--------------

--------------

Software Prerequisites
----------------------

**The following software tools are required for this tutorial:**

-  `Git for Windows <https://gitforwindows.org/>`_
-  :adi:`CrossCore Embedded Studio <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>`
-  Software Package with bootloader/pre-built LDRs.
-  Software Package with Audio Starter
-  Your Preferred Serial Terminal Program such as `TeraTerm <https://osdn.net/projects/ttssh2/releases/>`_
-  If running the Ethernet Audio example - your preferred VBAN audio player such as Voicemeeter Standard

Install GIT For Windows
~~~~~~~~~~~~~~~~~~~~~~~

*Git for Windows is a build environment that includes various tools for version control, compilation, etc. In this project we are using Git for Windows to access Git, which is a version control system/tool used for source code management. Additionally, Git for Windows comes with a set of unix-like tools such as Git bash which we will use to access makefile tools. For this tutorial, we will be using the command-line interface (Git bash) for compiling the Audio Starter projects since it contains some extra open source tools needed for compilation.*

+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
| 1. Download Git for Windows: https://gitforwindows.org/                                                                |                                                          |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
| 2. Follow the instructions to install provided by the setup installer, choosing the options that best suit your needs. | |image7| |image8| |image9| |image10| |image11| |image12| |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+

--------------

Install CrossCore Embedded Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the instructions :doc:`here </wiki-migration/resources/tools-software/sharc-audio-module/gettingstarted>` for installing CCES and for help getting started with CrossCore. //CrossCore is required for compilation and access to `make <https://www.gnu.org/software/make/>`_ as well as the compilers required for the ARM and SHARC Cores. //

*Note that CCES requires a license to run. The SAM board comes with an ICE-1000 evaluation license which can be found here:* :doc:`gettingstarted#installing_and_activating_crosscore_embedded_studio </wiki-migration/resources/tools-software/sharc-audio-module/gettingstarted>`\ *. For more details about licensing, refer to:* :ez:`how-can-i-obtain-and-install-a-licenses-for-crosscore-embedded-studio <dsp/software-and-development-tools/cces/w/documents/5311/how-can-i-obtain-and-install-a-licenses-for-crosscore-embedded-studio>`

//You will also need a *myAnalog* account, so proceed to register or log-in, if prompted when installing CCES://


|image13|

--------------

Download Bootloader Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Some of the Audio Starter projects require a bootloader to be flashed first. This section only applies to software running on the ADZS-SC589-MINI!* **Skip this step if it doesn't apply to you!** *This allows the use of the SAM flasher tool to make application updates. Software can be found here:*\ :doc:`Hardware-Software Compatibility </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`\ *.*

+-------------------------------------------------------------------------------------------------------------+-----------+
| 1. The software package can be downloaded directly (Be sure to unzip after download).                       | |image15| |
+-------------------------------------------------------------------------------------------------------------+-----------+
| 2. Keep track of where this project is unzipped as it will be referenced later as <BOOTLOADER_PROJECT_ROOT> |           |
+-------------------------------------------------------------------------------------------------------------+-----------+

--------------

Clone Repository/Download Application Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*The Audio Starter projects contain all of the source code and some additional setup scripts that allows you to compile, flash and run the application. Software can be found here:*\ :doc:`Hardware-Software Compatibility </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`\ *.*

*If you don't want to use the command-line to clone the software and prefer to download a zip instead, skip to step 5 in this table!*

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Open the Git Bash application                                                                                                                                                                                                                      | |image21| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Change your directory to your preferred cloning location                                                                                                                                                                                           | |image22| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Clone the repository by running the command                                                                                                                                                                                                        | |image23| |
| *git clone <Repository>*                                                                                                                                                                                                                              |           |
| Where <Repository> can be acquired from the Hardware-Software Compatibility matrix                                                                                                                                                                    |           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Note that by default the cloning action will create the default folder named the same as the repository and will clone the default branch *2.0.0-Github*. A specific branch can be specified by using the *--branch <branch_name>*, alternatively. | |image24| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. Alternatively, the software package can be downloaded directly instead of being cloned (Be sure to unzip after download).                                                                                                                          | |image25| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 6. Keep track of where the application was cloned or downloaded as it will be referred to later as <project_root>                                                                                                                                     |           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

Install Your Preferred Serial Terminal Program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*A serial terminal program, such as* `TeraTerm <https://github.com/TeraTermProject/teraterm/releases>`_ *or* `Putty <https://www.putty.org/>`_ *is required for serial communication with the SAM. Download and install your preferred tool. This tutorial will use TeraTerm.
Note that some parts of the SAM program use* `XMODEM <https://en.wikipedia.org/wiki/XMODEM>`_\ *. Be sure to select a terminal with XMODEM capability if you will be using this part of the SAM program.*

.. tip::

   TeraTerm v5.0 or greater users may want to adjust their Enconding and Font settings. :doc:`See known issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`.


--------------

Install Your Preferred VBAN Audio Program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*A VBAN audio streaming device is required to pass audio over Ethernet/UDP to the hardware. Follow any instructions for your VBAN audio program for installation. Please refer to any licensing rules for use.*

--------------

.. important::

   Having trouble? Check out our list of :doc:`common issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`!


--------------

`Advanced Audio Projects#.|Advanced Audio Projects#.environment_setup|Environment Setup and Compilation <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git1.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git2.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git3.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git4.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git5.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git6.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git1.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git2.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git3.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git4.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git5.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/git6.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cces_install.jpg
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/downloadzip.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/downloadzip.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/gitclone1.png
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/changedirectory.png
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/clone1.png
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/clone2.png
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternateclone.png
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/gitclone1.png
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/changedirectory.png
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/clone1.png
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/clone2.png
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternateclone.png
