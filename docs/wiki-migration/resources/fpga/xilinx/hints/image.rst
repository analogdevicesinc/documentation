Creating Graphics for inclusion in FPGA Projects
================================================

There are many times creating a graphics image, and including it into an FPGA project is necessary. The goal of this tutorial is to show you the various methods of doing this. The various methods will differ, depending on the size or depth of the image.

Using the Linux Boot Logo Tools
-------------------------------

The Linux kernel uses a "compressed" image format, which creates a header file from a `Colour_look-up_table <https://en.wikipedia.org/wiki/Colour_look-up_table>`_ scheme. Since it uses the same format used in the Linux kernel, there are some Linux utiltites needed:

-  `GNU Image Manipulation Program <http://www.gimp.org/>`_, which is avalible both `Linux <http://www.gimp.org/downloads/>`_ and `windows <http://www.gimp.org/windows/>`_.
-  `Netpbm tools <http://netpbm.sourceforge.net/>`_ is a toolkit for manipulation of graphic images, including conversion of images between a variety of different formats. There are over 300 separate tools in the package including converters for about 100 graphics formats.
-  `pnmtologo <http://git.kernel.org/?p=linux/kernel/git/torvalds/linux.git;a=blob;f=scripts/pnmtologo.c;hb=HEAD>`_ which is a c source file, which you must download and build.

-  the first step is actually to get the create an svg. Since this was already done, I'm just going to download one from Wikipedia to use an an example.\ :literal:`rgetz@curly:~/logos$ \**wget http://upload.wikimedia.org/wikipedia/commons/8/86/Analog_Devices_Logo.svg*\*
   --2011-12-20 13:41:47--  http:%%//%%upload.wikimedia.org/wikipedia/commons/8/86/Analog_Devices_Logo.svg
   Resolving upload.wikimedia.org... 208.80.152.211
   Connecting to upload.wikimedia.org|208.80.152.211\|:80... connected.
   HTTP request sent, awaiting response... 200 OK
   Length: 4525 (4.4K) [image/svg+xml]
   Saving to: \`Analog_Devices_Logo.svg'

   100%[=============================================================>] 4,525       21.4K/s   in 0.2s    

   2011-12-20 13:41:48 (21.4 KB/s) - \`Analog_Devices_Logo.svg' saved [4525/4525]`
-  the next step is to size it (I create a 349x100), and save it as an ascii .ppm file ``rgetz@curly:~/logos$ **gimp Analog_Devices_Logo.svg**``\ Here I "save as" a ``.ppm`` file.
-  the next step is to quantize the image (reduce the number of colours). The ``pnmquant`` application quantizes the colors in a Netpbm image to a smaller set, and the pnmnoraw application, converts this into a file which can be processed by the script to create a header file. ``rgetz@curly:~/fooo$ **pnmquant 224 Analog_Devices_Logo.ppm | pnmnoraw > Analog_Devices_Logo_clut224.ppm**``
-  The last step is to create the actual header file which is included into your application. ``rgetz@curly:~/logos$ **~/linux/scripts/pnmtologo -t clut224 Analog_Devices_Logo_clut224.ppm -o Analog_Devices_Logo_clut224.h -n Analog_Devices_logo**``
-  Depending on what you are and how you want to use the file, you may need to remove some of the Linux kernel references to the file, and replace them with your own. ``rgetz@curly:~/logos$ **sed -i -e 's:%%__%%initdata::' -e 's:%%__%%initconst::' Analog_Devices_Logo_clut224.h**
   rgetz@curly:~/logos$ **sed -i '/^#include/d' Analog_Devices_Logo_clut224.h**
   rgetz@curly:~/logos$ **sed -i  '/^[[/space|space]]*\.data/d' Analog_Devices_Logo_clut224.h**
   rgetz@curly:~/logos$ **sed -i '/^[[/space|space]]*\.clut/d' Analog_Devices_Logo_clut224.h**
   rgetz@curly:~/logos$ **sed -i '/^[[/space|space]]*\.type/d' Analog_Devices_Logo_clut224.h**
   rgetz@curly:~/logos$ **sed -i 's:linux_logo:logo:' Analog_Devices_Logo_clut224.h**``

And that's it - it's just a matter of including the image data into your application.

.. code:: c

   #include "Analog_Devices_Logo_clut224.h"

   int main(void)
   {

     for (h = 0; h < height; h++) {
       for (w = 0; w < width; w++) {
         pixel_data = Analog_Devices_data[pixel_cnt];
         if ((pixel_data < 32) || (pixel_data > 252)) {
           printf("Error: pixel data at(%d): 0x%02x\n", pixel_cnt, pixel_data);
           return(-1);
         }
         pixel_data = pixel_data - 32;
         pixel_r = Analog_Devices_clut[(pixel_data * 3) + 0];
         pixel_g = Analog_Devices_clut[(pixel_data * 3) + 1];
         pixel_b = Analog_Devices_clut[(pixel_data * 3) + 2];
         waddr = baseaddr + (h\*2048) + (w\*4);
         wdata = (pixel_r << 16) | (pixel_b << 8) | pixel_g;
         printf("mwr 0x%08x 0x%08x\n", waddr, wdata);
         pixel_cnt = pixel_cnt + 1;
       }
       waddr = baseaddr + (h\*2048);
       printf("set logfile [open \"demo_img.log\" \"a\"]\n");
       printf("puts $logfile [mrd 0x%08x]\n", waddr);
       printf("close $logfile\n");
     }
   }

Once this is done, you can have a quick look, to see how big things are.

::

   rgetz@curly:~/logos$ **readelf -s Analog_Devices_Logo | grep Analog_Devices**
       42: 0000000000601040 34900 OBJECT  LOCAL  DEFAULT   24 Analog_Devices_logo_data
       43: 00000000006098a0   672 OBJECT  LOCAL  DEFAULT   24 Analog_Devices_logo_clut

The data and colour lookup table are 35,572 bytes (~35k) to represent a 349 pixel x 100 pixel (RGB) image (uncompressed, this would be 104,700 bytes) - the clut data is 1/3 of the size, and minimal overhead.

Using U-Boot's Logo Tools
-------------------------

`U-Boot <http://www.denx.de/wiki/U-Boot>`_ or `Das_U-Boot <https://en.wikipedia.org/wiki/Das_U-Boot>`_ also includes tools for including graphics as splash screens. All that is needed to do, is download a recent version of U-Boot, and do a:

::

   rgetz@curly:~/u-boot$ **make tools-all HOST_TOOLS_ALL=y**

This will provide you with multple tools which you can used to create the header files.

bmp_logo
~~~~~~~~

``bmp_logo`` takes a 256-colour bitmap file, and creates a header file. This is similar to the Linux tools in size.

::

   rgetz@curly:~/u-boot$ **~/u-boot/tools/bmp_logo Analog_Devices_Logo.bmp > Analog_Devices_Logo_bmp.h**

easylogo
~~~~~~~~

``easylogo`` takes a 24-bit TGA image, and can output YUYV, RGB888, RGB565, and optionally Compress with `gzip <http://tools.ietf.org/html/rfc1952>`_.

::

   rgetz@curly:~/fooo$ **ppmtotga -rgb -norle Analog_Devices_Logo.ppm > Analog_Devices_Logo.tga**
   rgetz@curly:~/fooo$ **~/u-boot/tools/easylogo/easylogo Analog_Devices_Logo.tga -r Analog_Logo Analog_Devices_Logo_tga.h**
   Using 24-bit RGB888 Output Fromat
   Doing 'Analog_Devices_Logo_tga.h' (Analog_Logo) from 'Analog_Devices_Logo.tga'...LSS
   rgetz@curly:~/fooo$ **~/u-boot/tools/easylogo/easylogo Analog_Devices_Logo.tga -r -g Analog_Logo Analog_Devices_Logo_tga_zip.h**
   Using 24-bit RGB888 Output Fromat
   Compressing with gzip
   Doing 'Analog_Devices_Logo_tga_zip.h' (Analog_Logo) from 'Analog_Devices_Logo.tga'...LSS

Using the gzip version, does require a little more processing on the target (to decompress things), but offers substational saving in space.

::

   rgetz@curly:~/fooo$ **readelf -s Analog_Devices_Logo | grep Analog -i**
       41: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS Analog_Devices_Logo.c
       59: 00000000006032c0    32 OBJECT  GLOBAL DEFAULT   24 Analog_Logo
       64: 0000000000601040  8805 OBJECT  GLOBAL DEFAULT   24 DEF_ANALOG_LOGO_DATA

This is 8805 bytes, to store the same 349 pixel x 100 pixel (RGB) image (uncompressed, this would be 104,700 bytes) - the gzip data is 1/12 of the size, making up for the extra processing required. For decompression, check out the ``./contrib/puff`` lib/application in `zlib <http://zlib.net/>`_ compression library.
