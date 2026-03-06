Kuiper Linux Release Notes
==========================

.. note::

   **Kuiper for ACE**

   
   If you are planning to user Kuiper Linux with ACE - check this :doc:`link </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>` where you will find a Kuiper Linux image updated to provide a complete evaluation experience with ACE.


.. container:: lo round box

   
   2023_r2 Patch1
   --------------
   
   Release Image
   ~~~~~~~~~~~~~
   
   -  Details about how to burn the SD card can be found on :doc:`Kuiper Linux wiki page </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.
   -  :git-adi-kuiper-gen:`Github Release Notes for Kuiper 2023_r2 Patch1 <releases/tag/2023_r2_p1>`
   
   .. admonition:: Download
      :class: download

      **2023_r2 Patch1 Image**

         
         -  `Actual file <https://swdownloads.analog.com/cse/kuiper/image_2025-03-18-ADI-Kuiper-full.zip>`__
         -  MD5SUM for image_2025-03-18-ADI-Kuiper-full.zip: ``6c92259dd61520d08244012f6c92d7c6``
         -  MD5SUM for 2025-03-18-ADI-Kuiper-full.img: ``873b4977617e40725025aa4958f3ca7e``
         

   
   .. admonition:: Download
      :class: download

         
         -  :git-adi-kuiper-imager:`Kuiper Imager tool <releases/tag/v1.0.0-rc3>` can be also used for etching the image on SD card, configure the image for a specific hardware setup and update the boot files to latest.
         -  Details about latest boot files archive can be found `here <https://swdownloads.analog.com/cse/boot_partition_files/2023_r2/latest_boot.txt>`__
         

   
   .. admonition:: Download
      :class: download

         
         -  Microblaze images can be downloaded from :doc:`here </wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze_loading>`
         

   


.. container:: lo round box

   
   Known issues
   ~~~~~~~~~~~~
   
   --------------
   
   1. Writing SD cards with Balena Etcher(Windows) or Disk Image Writer(Ubuntu) may give an error at the end
   
   Even so, SD cards should be written properly, so you can ignore it. As alternatives you can use Win32 Disk Imager (version 1.0) from Windows or 'dd' command from linux systems.
   
   --------------
   
   2. Video output might not work on Xilinx platforms
   
   Please check the `list of monitors supported by Xilinx <https://support.xilinx.com/s/article/68671?language=en_US>`__
   
   --------------
   
   3. No data in buffer for cn0540
   
   The issue is reproducible only when sampling frequency is set from a lower to a higher value.
   
   Please use a previous Kuiper Linux release until we will publish a fix.
   
   --------------
   
   4. AD9081 with 122.88 MHz oscillator doesn't boot
   
   Evaluation Board AD9081 vcxo122p88 on ZCU102 doesn't boot due to a SPI issue.
   
   Please use a previous Kuiper Linux release until we will publish a fix.
   
   --------------
   
   Supported Projects
   ~~~~~~~~~~~~~~~~~~
   
   :doc:`Kuiper Linux Supported Projects and Platforms </wiki-migration/resources/tools-software/linux-software/kuiper-linux/project-list>`
   
   Sources
   ~~~~~~~
   
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Component                       | Repo                                                                                              | Branch      | Version/Tag/Git sha |
   +=================================+===================================================================================================+=============+=====================+
   | Kuiper base image               |                                                                                                   |             | **bullseye**        |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Linux Boot files Kernel version |                                                                                                   |             | **6.1**             |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Scopy                           | :git-scopy.git>`__                                     |             | **v2.0.0-beta-rc2** |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Libm2k                          | `libm2k.git <https::`scopy.git </github.com/analogdevicesinc/libm2k.git>`                                   |             | **v0.9.0**          |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Pyadi-iio                       | :git-pyadi-iio.git>`__                             |             | **v0.0.19**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Kuiper                          | `adi-kuiper-gen.git <https::`pyadi-iio.git </github.com/analogdevicesinc/adi-kuiper-gen.git>`                   | 2023_R2     | **3126a32**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | HDL                             | :git-hdl.git>`__                                         | hdl_2023_r2 | **d146370**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Linux                           | `linux.git <https::`hdl.git </github.com/analogdevicesinc/linux.git>`                                     | 2023_R2     | **2e89089**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Linux_RPI                       | :git-linux.git>`__                                     | rpi-6.1.y   | **a349cf5**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Linux_image_ADI-scripts         | `linux_image_ADI-scripts.git <https::`linux.git </github.com/analogdevicesinc/linux_image_ADI-scripts.git>` | main        | **c643dd0**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Libiio                          | :git-libiio.git>`__                                   | 2023_R2     | **5e1e9cb**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | IIO-Osc                         | `iio-oscilloscope.git <https::`libiio.git </github.com/analogdevicesinc/iio-oscilloscope.git>`               | 2023_R2     | **89b3848**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Libad9361-iio                   | :git-libad9361-iio.git>`__                     | 2023_R2     | **d692a52**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Libad9166-iio                   | `libad9166-iio.git <https::`libad9361-iio.git </github.com/analogdevicesinc/libad9166-iio.git>`                     | 2023_R2     | **2916da3**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Fru_tools                       | :git-fru_tools.git>`__                             | 2023_R2     | **4a18979**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | IIO-fm-radio                    | `iio-fm-radio.git <https::`fru_tools.git </github.com/analogdevicesinc/iio-fm-radio.git>`                       | main        | **e67be7e**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Wiki-scripts                    | :git-wiki-scripts.git>`__                       | main        | **ded20fd**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Jesd-eye-scan-gtk               | `jesd-eye-scan-gtk.git <https::`wiki-scripts.git </github.com/analogdevicesinc/jesd-eye-scan-gtk.git>`             | 2023_R2     | **f3babfb**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Diagnostic_report               | :git-diagnostic_report.git>`__             | main        | **fc0ba06**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Colorimeter                     | `colorimeter.git <https::`diagnostic_report.git </github.com/analogdevicesinc/colorimeter.git>`                         | 2023_R2     | **db018d4**         |
   +---------------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   


Previous Kuiper releases
------------------------

<WRAP> 

.. raw:: html

   <details><summary>**2023_r2** Kuiper Linux Releases (Click to expand)</summary>

\* :git-adi-kuiper-gen:`Github Release Notes for Kuiper 2023_r2 <releases/tag/2023_r2>`

.. admonition:: Download
   :class: download

   **2023_r2 Image**

   
   -  `Actual file <https://swdownloads.analog.com/cse/kuiper/image_2024-11-08-ADI-Kuiper-full.zip>`__
   -  MD5SUM for image_2024-04-04-ADI-Kuiper-full.zip: ``338f747964283b518c6492addca90ad5``
   -  MD5SUM for 2024-04-04-ADI-Kuiper-full.img: ``7764911b0b0da4a022706418a012c411``
   


.. admonition:: Download
   :class: download

   
   -  :git-adi-kuiper-imager:`Kuiper Imager tool <releases/tag/v1.0.0-rc3>` can be also used for etching the image on SD card, configure the image for a specific hardware setup and update the boot files to latest.
   -  Details about latest boot files archive can be found `here <https://swdownloads.analog.com/cse/boot_partition_files/2023_r2/latest_boot.txt>`__
   


.. admonition:: Download
   :class: download

   
   -  Microblaze images can be downloaded from :doc:`here </wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze_loading>`
   


.. container:: lo round box

   
   .. _known-issues-1:
   
   Known issues
   ~~~~~~~~~~~~
   
   --------------
   
   1. Writing SD cards with Balena Etcher(Windows) or Disk Image Writer(Ubuntu) may give an error at the end
   
   Even so, SD cards should be written properly, so you can ignore it. As alternatives you can use Win32 Disk Imager (version 1.0) from Windows or 'dd' command from linux systems.
   
   --------------
   
   2. Video output might not work on Xilinx platforms
   
   Please check the `list of monitors supported by Xilinx <https://support.xilinx.com/s/article/68671?language=en_US>`__
   
   --------------
   
   3. Jesd Eye Scan application doesn't work
   
   There is an error '*Failed to read JESD204 device...*' when 'Start' button from application UI is pushed.
   
   Please use a previous Kuiper Linux release until we will publish a fix.
   
   --------------
   
   4. Colorimeter Demo - CN0363 application doesn't work
   
   There is error "*Device not found: [Errno 13] Permission denied...*" show in Colorimeter Demo.
   
   Please use a previous Kuiper Linux release until we will publish a fix.
   
   --------------
   
   5. No data in buffer for cn0540
   
   The issue is reproducible only when sampling frequency is set from a lower to a higher value.
   
   Please use a previous Kuiper Linux release until we will publish a fix.
   
   --------------
   
   6. AD9081 with 122.88 MHz oscillator doesn't boot
   
   Evaluation Board AD9081 vcxo122p88 on ZCU102 doesn't boot due to a SPI issue.
   
   Please use a previous Kuiper Linux release until we will publish a fix.
   
   --------------
   
   7. "Segmentation Fault" issue on all evaluation boards that use ad7768 device
   
   Evaluation boards ad7768, ad7768-4 and cn0579 give "*Segmentation fault*" error when running '*iio_info*' or other libiio commands.
   
   .. _supported-projects-1:
   
   Supported Projects
   ~~~~~~~~~~~~~~~~~~
   
   :doc:`Kuiper Linux Supported Projects and Platforms </wiki-migration/resources/tools-software/linux-software/kuiper-linux/project-list>`
   
   .. _sources-1:
   
   Sources
   ~~~~~~~
   
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Component               | Repo                                                                                              | Branch      | Version/Tag/Git sha |
   +=========================+===================================================================================================+=============+=====================+
   | Kuiper base image       |                                                                                                   |             | **bullseye**        |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Kernel version          |                                                                                                   |             | **6.1**             |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Scopy                   | :git-scopy.git>`__                                     |             | **v1.4.1**          |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Libm2k                  | `libm2k.git <https::`scopy.git </github.com/analogdevicesinc/libm2k.git>`                                   |             | **v0.8.0**          |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Pyadi-iio               | :git-pyadi-iio.git>`__                             |             | **v0.0.18**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Kuiper                  | `adi-kuiper-gen.git <https::`pyadi-iio.git </github.com/analogdevicesinc/adi-kuiper-gen.git>`                   | 2023_R2     | **a10c8bc**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | HDL                     | :git-hdl.git>`__                                         | hdl_2023_r2 | **2156ac7**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Linux                   | `linux.git <https::`hdl.git </github.com/analogdevicesinc/linux.git>`                                     | 2023_R2     | **54eb23f**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Linux_RPI               | :git-linux.git>`__                                     | rpi-6.1.y   | **de2e45c**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Linux_image_ADI-scripts | `linux_image_ADI-scripts.git <https::`linux.git </github.com/analogdevicesinc/linux_image_ADI-scripts.git>` | main        | **2b8b630**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Libiio                  | :git-libiio.git>`__                                   | 2023_R2     | **bdd5c00**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | IIO-Osc                 | `iio-oscilloscope.git <https::`libiio.git </github.com/analogdevicesinc/iio-oscilloscope.git>`               | 2023_R2     | **fbd5aa5**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Libad9361-iio           | :git-libad9361-iio.git>`__                     | 2023_R2     | **d692a52**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Libad9166-iio           | `libad9166-iio.git <https::`libad9361-iio.git </github.com/analogdevicesinc/libad9166-iio.git>`                     | 2023_R2     | **2916da3**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Fru_tools               | :git-fru_tools.git>`__                             | 2023_R2     | **4a18979**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | IIO-fm-radio            | `iio-fm-radio.git <https::`fru_tools.git </github.com/analogdevicesinc/iio-fm-radio.git>`                       | main        | **e67be7e**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Wiki-scripts            | :git-wiki-scripts.git>`__                       | main        | **ded20fd**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Jesd-eye-scan-gtk       | `jesd-eye-scan-gtk.git <https::`wiki-scripts.git </github.com/analogdevicesinc/jesd-eye-scan-gtk.git>`             | 2023_R2     | **90cad36**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Diagnostic_report       | :git-diagnostic_report.git>`__             | main        | **fc0ba06**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+
   | Colorimeter             | `colorimeter.git <https::`diagnostic_report.git </github.com/analogdevicesinc/colorimeter.git>`                         | 2023_R2     | **524674a**         |
   +-------------------------+---------------------------------------------------------------------------------------------------+-------------+---------------------+

.. raw:: html

   </details>


</WRAP>

<WRAP> 

.. raw:: html

   <details><summary>Previous Kuiper Linux Releases (Click to expand)</summary>

.. admonition:: Download
   :class: download

   
   -  **18 June 2024 release (2022_r2 Patch 2)**
   -  `Actual file <https://swdownloads.analog.com/cse/kuiper/image_2024-06-18-ADI-Kuiper-full.zip>`__
   -  MD5 Sum image_2024-04-04-ADI-Kuiper-full.zip: ``62c8cd382fc40c87900b83a09d9650f2``
   -  MD5 Sum 2024-04-04-ADI-Kuiper-full.img: ``fe7a015548c79c08f4da507d1fa97e99``
   


.. admonition:: Download
   :class: download

   
   -  \**04 April 2024 release (2022_r2 Patch 1) \*\*
   -  `Actual file <https://swdownloads.analog.com/cse/kuiper/image_2024-04-04-ADI-Kuiper-full.zip>`__
   -  Checksum image_2024-04-04-ADI-Kuiper-full.zip: ``7118fc7fce9a5f102332976b6d5c1537``
   -  Checksum checksum 2024-04-04-ADI-Kuiper-full.img: ``4867cdcf7d13306f045fd4fb97e76404``
   


.. admonition:: Download
   :class: download

   
   -  \**13 December 2023 release (2022_r2) \*\*
   -  `Actual file <https://swdownloads.analog.com/cse/kuiper/image_2023-12-13-ADI-Kuiper-full.zip>`__
   -  Checksum image_2023-12-13-ADI-Kuiper-full.zip: ``9dfd5d57573e14e06715a08b19a6a26a``
   -  Checksum 2023-12-13-ADI-Kuiper-full.img: ``e3620b6d36ad0481b79eee6041769f38``
   


.. admonition:: Download
   :class: download

   
   -  \**2 April 2023 release (2021_r2) \*\*
   -  `Actual file <https://swdownloads.analog.com/cse/kuiper/image_2023-04-02-ADI-Kuiper-full.zip>`__
   -  Checksum image_2023-04-02-ADI-Kuiper-full.zip: ``0cdcf6e131318113a137cf54335b9614``
   -  Checksum 2023-04-02-ADI-Kuiper-full.img: ``aeff476b577b45cc6ce6ce02403a57c2``
   


.. admonition:: Download
   :class: download

   
   -  \**4 August 2022 release (2021_r1) \*\*
   -  `Actual file <https://swdownloads.analog.com/cse/kuiper/image_2022-08-04-ADI-Kuiper-full.zip>`__
   -  Checksum image_2022-08-04-ADI-Kuiper-full.zip: ``9201b9e6580a0ce5c606f40f99c11b9a``
   -  Checksum 2022-08-04-ADI-Kuiper-full.img: ``dbbee112f5174dc23b4f5142994e4ff9``
   


.. admonition:: Download
   :class: download

   
   -  \**28 July 2021 release (2019_r2) \*\*
   -  `Actual file <https://swdownloads.analog.com/cse/kuiper/image_2021-07-28-ADI-Kuiper-full.zip>`__
   -  Checksum image_2021-07-28-ADI-Kuiper-full.zip: ``279097240dec7156ff5e15b7ce0b8a25``
   -  Checksum 2021-07-28-ADI-Kuiper-full.img: ``b160453396e482234094a92134769ec6``
   


.. admonition:: Download
   :class: download

   
   -  \**22 June 2020 release (2019_r1) \*\*
   -  `Actual file <http://swdownloads.analog.com/cse/2019_R1-2020_06_22.img.xz>`__
   -  Checksum 2019_R1-2020_06_22.img.xz ``6ac6fc0733baba361acb66bd4cb050be``
   -  Checksum 2019_R1-2020_06_22.img ``3135f400387c39f29dc877e68636a875``
   


.. admonition:: Download
   :class: download

   
   -  \**23 May 2019 release (2018_R2) \*\*
   -  `Actual file <http://swdownloads.analog.com/cse/2018_R2-2019_05_23.img.xz>`__
   -  Checksum 2018_R2-2019_05_23.img.xz ``c377ca95209f0f3d6901fd38ef2b4dfd``
   -  Checksum 2018_R2-2019_05_23.img ``59c2fe68118c3b635617e36632f5db0b``
   


.. admonition:: Download
   :class: download

   
   -  \**26 June 2018 release (2018_R1) \*\*
   -  `Actual file <http://swdownloads.analog.com/cse/2018_R1-2018_06_26.img.xz>`__
   -  Checksum 2018_R1-2018_06_26.img.xz ``5075da2695de84c88f086e85f1a6da51``
   -  Checksum 2018_R1-2018_06_26.img ``e48c63736517b4c4051be5486fd62ad5``
   


.. admonition:: Download
   :class: download

   
   -  \**29 January 2018 release (2017_R1) \*\*
   -  `Actual file <http://swdownloads.analog.com/cse/2017_R1-2018_01_29.img.xz>`__
   -  Checksum 2017_R1-2018_01_29.img.xz ``020d696244655d19056ce1fff1f63f25``
   -  Checksum 2017_R1-2018_01_29.img ``a698a6ef59825bd63654c1d45b99f4c8``
   


.. admonition:: Download
   :class: download

   
   -  \**29 June 2017 release (2016_R2) \*\*
   -  `Actual file <http://swdownloads.analog.com/cse/2016_R2-2017_06_29.img.xz>`__
   -  Checksum 2016_R2-2017_06_29.img.xz ``9f20adb27c5502a96fa56fa0f3088bd9``
   -  Checksum 2016_R2-2017_06_29.img ``71b91e14dd1bd83779487850461440ea``
   


.. admonition:: Download
   :class: download

   
   -  \**23 December 2016 release (2016_R1) \*\*
   -  `Actual file <http://swdownloads.analog.com/cse/2016_R1-2016_12_23.img.xz>`__
   -  Checksum 2016_R1-2016_12_23.img.xz ``f167bfad87f9b9856d3b94297385a375``
   -  Checksum 2016_R1-2016_12_23.img ``edf8ea425576c9dd913e74e44c404e04``
   


.. admonition:: Download
   :class: download

   
   -  \**26 July 2016 release (2015_R2) \*\*
   -  `Actual file <http://swdownloads.analog.com/cse/2015_R2-2016_07_26.img.xz>`__
   -  Checksum 2015_R2-2016_07_26.img.xz ``1520D974FBAADA6107B4C41606C40264``
   -  Checksum 2015_R2-2016_07_26.img ``E0D5748101D476FCA807C20EEF03E788``
   


.. admonition:: Download
   :class: download

   
   -  \**22 December 2015 release (2015_R1) \*\*
   -  `Actual file <http://swdownloads.analog.com/cse/2015_R1-2015_12_22.img.xz>`__
   -  Checksum 2015_R1-2015_12_22.img.xz ``a8f3ed68625043e180c95677123794bd``
   -  Checksum 2015_R1-2015_12_22.img ``fd1e4154e59e7dc62e508a4cdc522db5``
   


.. admonition:: Download
   :class: download

   
   -  \**6 February 2015 release (2014_R2) \*\*
   -  `Actual file <http://swdownloads.analog.com/cse/2014_R2-2015_02_06.img.xz>`__
   -  Checksum 2014_R2-2015_02_06.img.xz ``bb76031fcd68fd9b1a175a2f7fd3e053``
   -  Checksum 2014_R2-2015_02_06.img ``132d03a2888db34f10f0ebbcb3100ae7``

.. raw:: html

   </details>


</WRAP>

Support
-------

Analog Devices provides online support for anyone using Analog Devices reference designs via :ez:`EngineerZone <community>`. The support is provided just for last two Kuiper Linux releases and the version that it is in work (main and next_stable branches).
