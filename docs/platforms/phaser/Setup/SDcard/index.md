# Download and Image the SD Card

The ADALM-PHASER kit ships with an SD card: 

```{important}
**This SD card MUST be updated with a new image**.  
```  

The Phaser software is tested with Kuiper Linux 2021_R2, which, in spite of the “2021” in the name, was released in Spring, 2023. While there are newer Kuiper Linux releases, this version is required to maintain compatibility with the current phaser software packages.

This image can be downloaded here:
[https://swdownloads.analog.com/cse/kuiper/image_2023-04-02-ADI-Kuiper-full.zip](https://swdownloads.analog.com/cse/kuiper/image_2023-04-02-ADI-Kuiper-full.zip)  

Unzip that file and burn that image onto the SD card using the traditional methods.  This typically means using Win32DiskImager (for Windows) or Etcher (for Linux).  

If needed, more information on this process can be found here:

* [https://wiki.analog.com/resources/tools-software/linux-software/zynq_images/windows_hosts](https://wiki.analog.com/resources/tools-software/linux-software/zynq_images/windows_hosts)
* [https://wiki.analog.com/resources/tools-software/linux-software/zynq_images/linux_hosts](https://wiki.analog.com/resources/tools-software/linux-software/zynq_images/linux_hosts)

After writing the image, if a window pops up saying “this card needs to be formatted, would you like to format it now?”:  

 **The answer is NO**. 
 
Eject the card and insert it into the Raspberry Pi's SD card slot.




<br>
<div style="clear: both;"></div> <!-- Ensures clean section break -->
<br>

```{note}
For questions or help with the Phaser, please visit:
<br>
[https://ez.analog.com/adieducation/university-program/](https://ez.analog.com/adieducation/university-program/)
```

