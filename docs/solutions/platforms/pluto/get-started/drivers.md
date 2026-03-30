# Pluto Driver Installation

The first thing to do, preferably prior to connecting your Pluto, is to install the necessary drivers for your operating system.  The steps for all operating systems are largely the same, with some small variations.  


## Windows Installation
1. Install the [PlutoSDR Windows Driver](https://github.com/analogdevicesinc/plutosdr-m2k-drivers-win/releases).  Download the latest PlutoSDR-M2k-USB-Drivers.exe file and install.
2. Install the [libiio](https://github.com/analogdevicesinc/libiio/releases/) library.  Download the latest libiio-xxxxx-windows-setup.exe file and install.
3. (Optional, but recommended) Install [IIO-Scope](https://github.com/analogdevicesinc/iio-oscilloscope/releases). Download the latest adi-osc-setup.exe file and install.


## Linux Installation
(i.e. Ubuntu 24, etc.)

1. Install libiio:
   * Pick your Linux distribution from the list [here](https://github.com/analogdevicesinc/libiio/releases/).
   * Or install from [source](https://github.com/analogdevicesinc/libiio/blob/main/README_BUILD.md)
     * But change the git clone line to:

        ```{code-block}
        git clone https://github.com/analogdevicesinc/libiio.git --branch libiio-v0
        ```

     * libiio-v0 is always the latest, stable, branch. This command as of (Sept 2024) will install libiio v0.25
     * If you run into any errors with install, try repeating that command with sudo
2. Install [PYADI-IIO](https://analogdevicesinc.github.io/pyadi-iio/guides/quick.html) (from source is recommended but not always necessary)

3. Install the [libad9361-iio library](https://github.com/analogdevicesinc/libad9361-iio). Instructions for building it are [here](https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms5-ebz/multi-chip-sync#linux):

```{code-block} bash
git clone https://github.com/analogdevicesinc/libad9361-iio.git
cd libad9361-iio
cmake ./
make
sudo make install
```

4. Install IIO-Scope: Linux users will need to build from [source](https://github.com/analogdevicesinc/iio-oscilloscope). Build instructions are [here](https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope#linuxos_x). You can skip the build of libiio and libad9361-iio steps, since you already did that.


## ADI-Kuiper Linux
(instructions for Raspberry Pi 4 are given):

1. Download the latest ADI-Kuiper Linux image [here](https://github.com/analogdevicesinc/adi-kuiper-gen/actions/workflows/kuiper2_0-build.yml).
- Just click on the first "workflow run"
- Download the kuiper_full_64_image (only the "full" image has GNU Radio pre installed)
- Write ADI-Kuiper-full.img to an SD card
- Windows users can use Win32 Disk Imager. Writing img files to an SD card will work even on computers with bitlocker or where normally writing to an SD card is encrypted.
2. Install SD Card into Raspberry Pi, and boot up. First boot may take a few minutes extra


## Check the Driver Installation

As a quick check of the installation, plug in Pluto (use the middle USB port), then open up a command prompt and type:

```{code-block} bash
iio_info -s
```

You should receive a list of "Available Contexts." These are just ways to address the Pluto device.  Note:  if you are on a Windows system, you might also get an error -- Function not implemented (40).  That warning can be ignored. It occurs because iio_info tries to open local contexts when scanning but they are not supported on Windows. This error will not appear in Linux systems.

```{image} resources/iio_info.svg
:width: 800px
:align: center
```  

If you see a list of "Available contexts", such as shown above, then you have successfully installed the drivers.  


If you get something like the message below, then you've probably installed the drivers correctly, but the computer can't find Pluto (or any IIO device).  Is Pluto plugged in??? And are you using the center USB port???

```{image} resources/iio_info2.svg
:width: 400px
:align: center
```  
You might also receive a message like the one below, 'iio_info' is not recognized.  If you see this, then you have not properly installed the drivers.  Check the driver installation steps and complete anything that you missed.  

```{image} resources/iio_info3.png
:width: 400px
:align: center
```  


```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```


