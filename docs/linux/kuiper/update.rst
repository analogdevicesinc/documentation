.. _kuiper update:

Updating
========

There are 2 things to update:

#. Userspace Tools (GUI/tools, in the Linux rootfs).
#. ZYNQ Processing System / FPGA Boot Files & Linux kernel (the FAT32 BOOT
   partition).

Upgrading one side, without upgrading the other might cause more problems than
it solves. If you are upgrading, please upgrade both.

Staying up to date is a combination of:

-  Package management via apt-get
-  checking out source code with git tools
-  downloading files via wget

If you need to use a proxy for any of these:

-  `apt-get proxy <https://help.ubuntu.com/community/AptGet/Howto#Setting_up_apt-get_to_use_a_http-proxy>`__
-  `git, wget, and curl proxies <http://www.gnu.org/software/wget/manual/html_node/Proxies.html>`__

User Space Tools
----------------

There are a number of ADI provided tools in the file system. There is an easy
way to rebuild these projects from source. The only requirement is an healthy
image and active Internet connection.

In order to update all ADI tools - simply call the update script as shown below:
In case you only want to update a certain project, the script accepts a single
parameter, the ADI github project name (https://github.com/analogdevicesinc).

.. tip::

   If you are using an old image & old update tools script - you may need
   to run the update tools script twice (the first time it updates the update
   script, and the second time it updates everything else).
   This has been resolved in the most recent update script (the script updates
   itself, and switches over to the new one), so you only need to do this if you
   are using an older version.

.. shell::

   $adi_update_tools.sh

.. collapsible:: Complete update tools log

   .. code-block::

      2022-05-06 14:35:15 URL: http://github.com/analogdevicesinc 200 OK
       *** Updating linux_image_ADI-scripts BRANCH origin/master ***
      HEAD is now at 47416bc update_tools: Add HWMON and examples to libiio builds
      remote: Enumerating objects: 32, done.
      remote: Counting objects: 100% (32/32), done.
      remote: Compressing objects: 100% (16/16), done.
      remote: Total 32 (delta 16), reused 30 (delta 16), pack-reused 0
      Unpacking objects: 100% (32/32), 7.80 KiB | 133.00 KiB/s, done.
      From https://github.com/analogdevicesinc/linux_image_ADI-scripts
       * [new branch]      add_2021_R1_release -> origin/add_2021_R1_release
         47416bc..425510e  master              -> origin/master
       + c989e52...4bf27ce rpi_boot_files      -> origin/rpi_boot_files  (forced update)
       *** Building linux_image_ADI-scripts ***
      ./adi_update_tools.sh has been updated, switching to new one
      2022-05-06 14:35:18 URL: http://github.com/analogdevicesinc 200 OK
       *** Updating linux_image_ADI-scripts BRANCH origin/master ***
      HEAD is now at 425510e adi_update_boot.sh: Replace windows carrige/return
       *** Building linux_image_ADI-scripts ***
      ./adi_update_tools.sh script is the same, continuing
      Reading package lists... Done
      Building dependency tree... Done
      Reading state information... Done
      Note, selecting 'libncurses-dev' instead of 'ncurses-dev'
      bison is already the newest version (2:3.7.5+dfsg-1).
      flex is already the newest version (2.6.4-8).
      libaio-dev is already the newest version (0.3.112-9+rpi1).
      libavahi-client-dev is already the newest version (0.8-5).
      libavahi-common-dev is already the newest version (0.8-5).
      libcdk5-dev is already the newest version (5.0.20180306-3).
      libcurl4-openssl-dev is already the newest version (7.74.0-1.3+deb11u1).
      libfftw3-dev is already the newest version (3.3.8-2).
      libgtkdatabox-dev is already the newest version (1:0.9.3.1-2).
      libjansson-dev is already the newest version (2.13.1-1.1).
      libmatio-dev is already the newest version (1.5.19-2).
      libncurses-dev is already the newest version (6.2+20201114-2).
      libserialport-dev is already the newest version (0.1.1-4).
      libxml2 is already the newest version (2.9.10+dfsg-6.7+deb11u1).
      libxml2-dev is already the newest version (2.9.10+dfsg-6.7+deb11u1).
      cmake is already the newest version (3.18.4-2+rpt1+rpi1).
      libgtk2.0-dev is already the newest version (2.24.33-2+rpt1).
      0 upgraded, 0 newly installed, 0 to remove and 49 not upgraded.
      Reading package lists... Done
      Building dependency tree... Done
      Reading state information... Done
      evtest is already the newest version (1:1.34-1).
      gpsd is already the newest version (3.22-4).
      gpsd-clients is already the newest version (3.22-4).
      u-boot-tools is already the newest version (2021.01+dfsg-5+rpi1).
      0 upgraded, 0 newly installed, 0 to remove and 49 not upgraded.
      Cannot read environment, using default
      Cannot read default environment from file
      sed: can't read /etc/update-motd.d/10-help-text: No such file or directory
      make: *** No rule to make target 'clean'.  Stop.
      install -d /usr/local/bin
      install ./*.sh /usr/local/bin/
      /bin/sh usb-gadget-service/install_gt.sh
      Reading package lists... Done
      Building dependency tree... Done
      Reading state information... Done
      libconfig-dev is already the newest version (1.5-0.4).
      Already up to date.
      checking for a BSD-compatible install... /usr/bin/install -c
      checking whether build environment is sane... yes
      checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
      checking for gawk... no
      checking for mawk... mawk
      checking whether make sets $(MAKE)... yes
      checking whether make supports nested variables... yes
      checking for gcc... gcc
      checking whether the C compiler works... yes
      checking for C compiler default output file name... a.out
      checking for suffix of executables...
      checking whether we are cross compiling... no
      checking for suffix of object files... o
      checking whether we are using the GNU C compiler... yes
      checking whether gcc accepts -g... yes
      checking for gcc option to accept ISO C89... none needed
      checking whether gcc understands -c and -o together... yes
      checking whether make supports the include directive... yes (GNU style)
      checking dependency style of gcc... gcc3
      checking for g++... g++
      checking whether we are using the GNU C++ compiler... yes
      checking whether g++ accepts -g... yes
      checking dependency style of g++... gcc3
      checking for ar... ar
      checking the archiver (ar) interface... ar
      checking for pkg-config... /usr/bin/pkg-config
      checking pkg-config is at least version 0.9.0... yes
      checking for libconfig >= 1.4... yes
      checking for libconfig >= 1.5... yes
      checking build system type... armv7l-unknown-linux-gnueabihf
      checking host system type... armv7l-unknown-linux-gnueabihf
      checking how to print strings... printf
      checking for a sed that does not truncate output... /usr/bin/sed
      checking for grep that handles long lines and -e... /usr/bin/grep
      checking for egrep... /usr/bin/grep -E
      checking for fgrep... /usr/bin/grep -F
      checking for ld used by gcc... /usr/bin/ld
      checking if the linker (/usr/bin/ld) is GNU ld... yes
      checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
      checking the name lister (/usr/bin/nm -B) interface... BSD nm
      checking whether ln -s works... yes
      checking the maximum length of command line arguments... 1572864
      checking how to convert armv7l-unknown-linux-gnueabihf file names to armv7l-unknown-linux-gnueabihf format... func_convert_file_noop
      checking how to convert armv7l-unknown-linux-gnueabihf file names to toolchain format... func_convert_file_noop
      checking for /usr/bin/ld option to reload object files... -r
      checking for objdump... objdump
      checking how to recognize dependent libraries... pass_all
      checking for dlltool... no
      checking how to associate runtime and link libraries... printf %s\n
      checking for archiver @FILE support... @
      checking for strip... strip
      checking for ranlib... ranlib
      checking command to parse /usr/bin/nm -B output from gcc object... ok
      checking for sysroot... no
      checking for a working dd... /usr/bin/dd
      checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
      checking for mt... mt
      checking if mt is a manifest tool... no
      checking how to run the C preprocessor... gcc -E
      checking for ANSI C header files... yes
      checking for sys/types.h... yes
      checking for sys/stat.h... yes
      checking for stdlib.h... yes
      checking for string.h... yes
      checking for memory.h... yes
      checking for strings.h... yes
      checking for inttypes.h... yes
      checking for stdint.h... yes
      checking for unistd.h... yes
      checking for dlfcn.h... yes
      checking for objdir... .libs
      checking if gcc supports -fno-rtti -fno-exceptions... no
      checking for gcc option to produce PIC... -fPIC -DPIC
      checking if gcc PIC flag -fPIC -DPIC works... yes
      checking if gcc static flag -static works... yes
      checking if gcc supports -c -o file.o... yes
      checking if gcc supports -c -o file.o... (cached) yes
      checking whether the gcc linker (/usr/bin/ld) supports shared libraries... yes
      checking whether -lc should be explicitly linked in... no
      checking dynamic linker characteristics... GNU/Linux ld.so
      checking how to hardcode library paths into programs... immediate
      checking whether stripping libraries is possible... yes
      checking if libtool supports shared libraries... yes
      checking whether to build shared libraries... yes
      checking whether to build static libraries... yes
      checking how to run the C++ preprocessor... g++ -E
      checking for ld used by g++... /usr/bin/ld
      checking if the linker (/usr/bin/ld) is GNU ld... yes
      checking whether the g++ linker (/usr/bin/ld) supports shared libraries... yes
      checking for g++ option to produce PIC... -fPIC -DPIC
      checking if g++ PIC flag -fPIC -DPIC works... yes
      checking if g++ static flag -static works... yes
      checking if g++ supports -c -o file.o... yes
      checking if g++ supports -c -o file.o... (cached) yes
      checking whether the g++ linker (/usr/bin/ld) supports shared libraries... yes
      checking dynamic linker characteristics... (cached) GNU/Linux ld.so
      checking how to hardcode library paths into programs... immediate
      checking for doxygen... /usr/bin/doxygen
      checking for perl... /usr/bin/perl
      checking for dot... /usr/bin/dot
      checking for latex... no
      configure: WARNING: latex not found - will not generate doxygen PostScript documentation
      checking for makeindex... no
      checking for dvips... no
      checking for egrep... /usr/bin/egrep
      checking for pdflatex... no
      configure: WARNING: pdflatex not found - will not generate doxygen PDF documentation
      checking for makeindex... no
      checking for egrep... (cached) /usr/bin/egrep
      DX_FLAG_doc=1
      DX_FLAG_dot=1
      DX_FLAG_man=0
      DX_FLAG_html=1
      DX_FLAG_chm=0
      DX_FLAG_chi=0
      DX_FLAG_rtf=0
      DX_FLAG_xml=0
      DX_FLAG_pdf=0
      DX_FLAG_ps=0
      DX_ENV= SRCDIR='.' PROJECT='libusbgx' DOCDIR='doxygen-doc' VERSION='0.2.0' PERL_PATH='/usr/bin/perl' HAVE_DOT='YES' DOT_PATH='/usr/bin' GENERATE_MAN='NO' GENERATE_RTF='NO' GENERATE_XML='NO' GENERATE_HTMLHELP='NO' GENERATE_CHI='NO' GENERATE_HTML='YES' GENERATE_LATEX='NO'
      checking that generated files are newer than configure... done
      configure: creating ./config.status
      config.status: creating Makefile
      config.status: creating src/Makefile
      config.status: creating examples/Makefile
      config.status: creating include/usbg/usbg_version.h
      config.status: creating libusbgx.pc
      config.status: creating doxygen.cfg
      config.status: creating LibUsbgxConfig.cmake
      config.status: executing depfiles commands
      config.status: executing libtool commands
      make[1]: warning: jobserver unavailable: using -j1.  Add '+' to parent make rule.
      make[1]: Entering directory '/usr/local/src/libusbgx'
      Making all in src
      ....
       *** Building libiio ***
      -- cmake version: 3.18.4
      -- The C compiler identification is GNU 10.2.1
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info - done
      -- Check for working C compiler: /usr/bin/cc - skipped
      -- Detecting C compile features
      -- Detecting C compile features - done
      -- Performing Test HAS_WPEDANTIC
      -- Performing Test HAS_WPEDANTIC - Success
      -- Performing Test HAS_WSHADOW
      -- Performing Test HAS_WSHADOW - Success
      -- Looking for strdup
      -- Looking for strdup - found
      -- Looking for strndup
      -- Looking for strndup - found
      -- Looking for strerror_r
      -- Looking for strerror_r - found
      -- Looking for newlocale
      -- Looking for newlocale - found
      -- Looking for pthread_setname_np
      -- Looking for pthread_setname_np - found
      -- Looking for in6addr_any
      -- Looking for in6addr_any - found
      -- Looking for libusb-1.0 : Found
      -- Looking for libusb_get_version
      -- Looking for libusb_get_version - found
      -- Found Git: /usr/bin/git (found version "2.30.2")
      -- Looking for libserialport : Found
      -- Building with Network back end support
      -- Performing Test HAS_O_TMPFILE
      -- Performing Test HAS_O_TMPFILE - Success
      -- Performing Test WITH_NETWORK_EVENTFD
      -- Performing Test WITH_NETWORK_EVENTFD - Success
      -- Performing Test HAS_PIPE2
      -- Performing Test HAS_PIPE2 - Success
      -- Building with Avahi, a DNS SD implementation
      -- Found LibXml2: /usr/lib/arm-linux-gnueabihf/libxml2.so (found version "2.9.10")
      -- Looking for CDK_CSTRING2
      -- Looking for CDK_CSTRING2 - found
      -- bin= lib= inc=
      -- Found Python: /usr/bin/python3.9 (found version "3.9.2") found components: Interpreter
      -- new
      -- Python_EXECUTABLE /usr/bin/python3.9
      -- Found Python: Building bindings
      -- Found BISON: /usr/bin/bison (found version "3.7.5")
      -- Found FLEX: /usr/bin/flex (found version "2.6.4")
      -- Looking for sys/types.h
      -- Looking for sys/types.h - found
      -- Looking for stdint.h
      -- Looking for stdint.h - found
      -- Looking for stddef.h
      -- Looking for stddef.h - found
      -- Check size of struct usb_functionfs_descs_head_v2
      -- Check size of struct usb_functionfs_descs_head_v2 - done
      -- Configuring done
      -- Generating done
      -- Build files have been written to: /usr/local/src/libiio/build
      ....
      Building libiio target  finished Successfully
       *** Updating libad9361-iio BRANCH origin/2019_R2 ***
      Previous HEAD position was fd44358 Fix flags for FMComms5 python tests
      HEAD is now at be7eb02 Update HW test to use environmental variables
      remote: Enumerating objects: 3, done.
      remote: Counting objects: 100% (3/3), done.
      remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0
      Unpacking objects: 100% (3/3), 601 bytes | 120.00 KiB/s, done.
      From https://github.com/analogdevicesinc/libad9361-iio
       * [new branch]      2021_R1           -> origin/2021_R1
       * [new branch]      staging/ci-update -> origin/staging/ci-update
       *** Building libad9361-iio ***
      -- The C compiler identification is GNU 10.2.1
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info - done
      -- Check for working C compiler: /usr/bin/cc - skipped
      -- Detecting C compile features
      -- Detecting C compile features - done
      -- Found Git: /usr/bin/git (found version "2.30.2")
      -- Found Doxygen: /usr/bin/doxygen (found version "1.9.1") found components: doxygen dot
      -- Using default dependencies for packaging
      -- Package dependencies: libc6-dev (>= 2.19)
      -- Configuring done
      -- Generating done
      -- Build files have been written to: /usr/local/src/libad9361-iio/build
      ....
      Building libad9361-iio target  finished Successfully
      *** Updating iio-oscilloscope BRANCH origin/2019_R2 ***
      Previous HEAD position was fb9ec84 plugins: adrv9002: improve temperature reporting
      HEAD is now at 177dd7d filters: add adrv9002 new API profiles
      rm -rf /usr/local/lib/osc /usr/local/share/osc /usr/local/bin/osc /usr/local/lib/libosc.so
      xdg-icon-resource uninstall --noupdate --size 16 adi-osc
      xdg-icon-resource uninstall --noupdate --size 32 adi-osc
      xdg-icon-resource uninstall --noupdate --size 64 adi-osc
      xdg-icon-resource uninstall --noupdate --size 128 adi-osc
      ....

ZYNQ Processing System / FPGA Boot Files
----------------------------------------

The default ADI ZYNQ image supports a variety of ZYNQ boards and reference
designs. In order to keep those boot files up to date. There is a another script
that downloads the latest builds from the ADI Wiki page and installs them onto
the FAT32 partition on the SD Card. The only requirement is a healthy image and
active Internet connection.

In order to update all ADI tools, simply call the **adi_update_boot.sh** script
as shown below:

.. shell:: bash

   $adi_update_boot.sh

.. collapsible:: Complete update boot log

   .. code-block::

      Verifying if ./adi_update_boot.sh is up to date...
      HEAD is now at 425510e adi_update_boot.sh: Replace windows carrige/return
      ./adi_update_boot.sh is up to date, continuing...
      Check latest available version...
      --2022-05-06 14:53:34--  http://swdownloads.analog.com/cse/boot_partition_files/2019_r2/latest_boot.txt
      Resolving swdownloads.analog.com (swdownloads.analog.com)... 104.103.158.171
      Connecting to swdownloads.analog.com (swdownloads.analog.com)|104.103.158.171|:80... connected.
      HTTP request sent, awaiting response... 301 Moved Permanently
      Location: https://swdownloads.analog.com/cse/boot_partition_files/2019_r2/latest_boot.txt [following]
      --2022-05-06 14:53:34--  https://swdownloads.analog.com/cse/boot_partition_files/2019_r2/latest_boot.txt
      Connecting to swdownloads.analog.com (swdownloads.analog.com)|104.103.158.171|:443... connected.
      HTTP request sent, awaiting response... 200 OK
      Length: 160 [text/plain]
      Saving to: ‘latest_boot.txt’
      latest_boot.txt     100%[===================>]     160  --.-KB/s    in 0s
      2022-05-06 14:53:35 (26.0 MB/s) - ‘latest_boot.txt’ saved [160/160]
      Latest version available: 2021_07_27
      Release: 2019_r2
      Current version detected: 2022_04_14
      Release: master
      Warning! You want to update boot files from a different release: 2019_r2 (current release: master)
      In this case there may appear compatibility issues with root file system.
      Are you sure you want to continue?(y/n) Y
      Start downloading latest_boot_partition.tar.gz ...
      --2022-05-06 14:54:41--  https://swdownloads.analog.com/cse/boot_partition_files/master/latest_boot_partition.tar.gz
      Resolving swdownloads.analog.com (swdownloads.analog.com)... 104.103.158.171
      Connecting to swdownloads.analog.com (swdownloads.analog.com)|104.103.158.171|:443... connected.
      HTTP request sent, awaiting response... 200 OK
      Length: 515989728 (492M) [application/x-gzip]
      Saving to: ‘latest_boot_partition.tar.gz’
      ...

.. note::

   It may happen that you have to copy manually the boot files to complete the
   update.
   To do so, plug the SD card into your computer, and:

   * Copy *${CONFIG}/devicetree.dtb* to *devicetree.dtb* on the root of the SD card,
   * Copy *${CONFIG}/BOOT.BIN* to *BOOT.BIN* on the root of the SD card,
   * Copy *common/uImage* to *uImage* on the root of the SD card.

   (Replace *${CONFIG}* with the config name that applies to your board and
   carrier combination, e.g. "zynq-zed-adv7511-ad9361" for a FMCOMMS2/3 on a
   ZedBoard).
