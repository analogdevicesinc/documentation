(pluto getstarted firmware_upgrade_section)=
# Updating the Firmware

Shortly after plugging Pluto in your PC it should appear as a storage device:  

```{image} resources/usb_drive.svg
:width: 300px
:align: center
```


Open Pluto and click  on info.html. 
Click on the Firmware (or Version) button:  

```{image} resources/version_button.png
:width: 800px
:align: center
```  


```{image} resources/firmware_version.png
:width: 800px
:align: center
```  


If you are able to do so, upgrade the firmware version by visiting:
- [Firmware Update](https://analogdevicesinc.github.io/documentation/tools/pluto-m2k/firmware.html)  
 
Click on **"Latest ADALM-PLUTO (PlutoSDR) Release"** and download the **"plutosdr-fw-v0.xx.zip"** file.  At the time of this guide, that release was 0.39.  Copy "pluto.frm" to the PlutoSDR USB drive.  This is the only file necessary for a firmware upgrade, however, copying all 5 of the files can sometimes resolve a rare issues with Pluto setup.  And it doesn't hurt anything--so I normally just copy all the files.  

```{image} resources/firmware_copy.svg
:width: 500px
:align: center
```  


After copying the file(s), you **MUST** do a software eject of Pluto.  For Windows systems, just right click on PlutoSDR and select "Eject":

```{image} resources/firmware_eject.svg
:width: 500px
:align: center
```  

Pluto's blue LED will rapidly flash whilst it updates(less the 2 minutes).  When it is complete, PlutoSDR will again appear as a mounted USB drive.  It is **VERY IMPORTANT** that you do not interrupt this process.  DO NOT unplug PlutoSDR while this firmware upgrade is occurring.  If this should happen, and Pluto becomes unresponsive, follow the [DFU Update Procedure](https://analogdevicesinc.github.io/documentation/tools/pluto-m2k/firmware.html#dfu-update) to attempt to recover the PlutoSDR.


```{warning}
 Once PlutoSDR has begun the firmware upgrade and its blue LED is flashing rapidly **do not disconnect Pluto!**  Instead, wait patiently (less the 2 minutes) for the upgrade process to finish.  You will know it is finished because Pluto will appear as a USB drive and the blue LED will flash slowly (not rapidly).  
```

If you have made any "hacks" to Pluto -- such as frequency expansion or enabling the second channels, you will likely have to redo those hacks after a firmware upgrade (particularly if you copied all the files, instead of just pluto.frm). 

Variations of this procedure exist for other operating systems (i.e. Linux).  See [this page](https://analogdevicesinc.github.io/documentation/tools/pluto-m2k/firmware.html#linux) for instructions. Additionally, if you have a computer that does not allow writing to a USB drive, you can instead update Pluto over the network.  Follow the instructions [here](https://analogdevicesinc.github.io/documentation/tools/pluto-m2k/firmware.html#network-update).  

You can now head straight over to the {ref}`Software <pluto software software_section>` section. 

## Further Reading

- [Complete Firmware Upgrade Instructions](https://analogdevicesinc.github.io/documentation/tools/pluto-m2k/firmware.html)
- [Building the Firmware](https://analogdevicesinc.github.io/documentation/tools/pluto-m2k/building_the_image.html)
- [Build Sources](https://analogdevicesinc.github.io/documentation/tools/pluto-m2k/obtaining_the_sources.html)
- [Rebooting](https://analogdevicesinc.github.io/documentation/tools/pluto-m2k/reboot.html)



```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```


