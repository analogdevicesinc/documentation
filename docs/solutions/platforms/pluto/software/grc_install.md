# GNU Radio Installation and Examples

```{image} resources/grc4.svg
:width: 400px
:align: center
```  

[GNU Radio](https://www.gnuradio.org/) is a powerful open-source software development toolkit that provides signal processing blocks to implement software-defined radios and signal processing systems. You can use GNU Radio to create flowgraphs that interface with PlutoSDR and process the data it receives. To use PlutoSDR with GNU Radio, you need to install the `gr-iio` module, which provides blocks for interfacing with IIO devices like PlutoSDR. Once you have the `gr-iio` module installed, you can create a flowgraph in GNU Radio Companion (GRC) that includes the `IIO Source` block to read samples from PlutoSDR and process them using other GNU Radio blocks.

```{clear-content}
```

## GNU Radio Installation

### Windows Install

GNU Radio Companion (GRC), works best in Linux.  However, if you need to use it with a Windows operating system, then the best way to do this is through Radioconda:
1. Download the most recent “radioconda-Windows-x86_64.exe” Radioconda install package [here](https://github.com/radioconda/radioconda-installer).
2. Update Radioconda to the latest version of PYADI-IIO
   - Delete Radioconda's “adi” folder in radioconda/lib/site-packages
   - Clone the [pyadi-iio](https://github.com/analogdevicesinc/pyadi-iio) repo.  Or just download the repo by clicking on the green "Code" button and selecting "Download ZIP"
   - Unzip and copy the “adi” folder in that cloned PYADI-IIO repo to radioconda/lib/site-packages

### Linux Installation
(Ubuntu 24, etc...)

Just install GNU Radio by following these instructions: 
    [https://wiki.gnuradio.org/index.php/UbuntuInstall](https://wiki.gnuradio.org/index.php/UbuntuInstall)


### ADI-Kuiper Linux
(Instructions for Raspberry Pi are given)

(instructions for Raspberry Pi 4 are given):

1. Download the latest ADI-Kuiper Linux image [here](https://github.com/analogdevicesinc/adi-kuiper-gen/actions/workflows/kuiper2_0-build.yml).
- Just click on the first "workflow run"
- Download the kuiper_full_64_image (only the "full" image has GNU Radio pre installed)
- Write ADI-Kuiper-full.img to an SD card
- Windows users can use Win32 Disk Imager. Writing img files to an SD card will work even on computers with bitlocker or where normally writing to an SD card is encrypted.
2. Install SD Card into Raspberry Pi, and boot up. First boot may take a few minutes extra
3. GNU Radio is installed by default on ADI-Kuiper Linux (full)


### Test the Installation
Whichever operating system you use, let's test the GRC installation now.  
1. Open the installed GNU Radio Companion application.
2. Find the "Python Module" block and place it in the workflow.
3. Open that "Python Module" and click "Open in Editor"
4. In the editor, type:
```{code-block} python
import iio
print(iio.version)
import adi
print(adi.__version__)
```
5. Save that text file and then click "Run" in GRC
6. The command line should print the pyLIBIIO and PyADI-IIO library versions
   - Sometimes it is necessary to include the path to the cloned pyadi-iio directory (as shown in the image below) 

```{image} resources/grc1.svg
:width: 400px
:align: center
```  

7. Delete that "Python Module"
8. Now click on "Find" and type "pluto"

```{image} resources/grc2.svg
:width: 400px
:align: center
```  

9. Place a "PlutoSDR Sink" and "PlutoSDR Source" into the flowgraph:

```{image} resources/grc3.svg
:width: 400px
:align: center
```  

10. Double click on the blocks and set the context as follows:
    - IIO context URI:  'ip:192.168.2.1'
    - There are other contexts you could use, but this ip address method works the best

11. Try out some of the graph sink objects: 

```{image} resources/grc4.svg
:width: 400px
:align: center
```  


### Pluto GNU Radio Resources

1. [GNU Radio](https://www.gnuradio.org/)
2. [IIO GRC Blocks](https://wiki.analog.com/resources/tools-software/linux-software/gnuradio)
3. [Practical SDR Book](https://nostarch.com/practical-sdr)
4. [Field Expedient SDR Books](https://www.factorialabs.com/fieldxp/)
5. [Learn SDR (Harvey Mudd College)](https://gallicchio.github.io/learnSDR/)
6. [Using Python with GRC and Pluto 7h16m](https://www.youtube.com/watch?v=PVlWK-39cCw&t=26140s)




```{video} https://www.youtube.com/watch?v=Yx3RPOtv7x8
:align: left
```
```{clear-content}
```

```{video} https://www.youtube.com/watch?v=63qY9tYhhro
:align: left
```
```{clear-content}
```






```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```
