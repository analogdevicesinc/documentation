# Jupiter Driver Installation

The first thing to do, preferably prior to connecting your Jupiter, is to install the necessary drivers for your operating system. The steps for all operating systems are largely the same, with some small variations.

----

## Windows Installation

1. Install the {git-libiio}`libiio <releases+>` library. Download the latest libiio-xxxxx-windows-setup.exe file and install.
2. (Optional, but recommended) Install {git-scopy}`Scopy <releases+>`. Download the latest file for your computer and install.


----

## Linux Installation
(i.e. Ubuntu 24, etc.)

1. Install libiio
    - Pick your Linux distribution from this list {git-libiio}`here <releases+>`
    - Or install from the {git-libiio}`source <main:README_BUILD.md>`
        - But change the git clone line to:
            git clone https://github.com/analogdevicesinc/libiio.git –branch libiio-v0
        - libiio-v0 is always the latest, stable, branch. This command as of (Sept 2024) will install libiio v0.25
        - If you run into any errors with install, try repeating that command with sudo
2. Install {ref}`PYADI-IIO <pyadi-iio>` (from source is recommended but not always necessary)  
3. Install the {git-libad9361-iio}`libad9361-iio library </>`:

```{code-block} bash
git clone https://github.com/analogdevicesinc/libad9361-iio.git
cd libad9361-iio
cmake ./
make
sudo make install
```

4. Install IIO-Scope: Linux users will need to build from {git-iio-oscilloscope}`source </>`  

---

## Check the Driver Installation

As a quick check of the installation, plug in Jupiter using the Micro USB UART, then open up a command prompt and type:  

```{code-block} bash
iio_info -s
```  

You should receive a list of "Available Contexts." These are just ways to address the Jupiter device.  


```{note}
If you are on a Windows system, you might also get an error -- Function not implemented (40).  That warning can be ignored. It occurs because iio_info tries to open local contexts when scanning but they are not supported on Windows. This error will not appear in Linux systems.
```

```{image} iio-info-s2.png
:width: 800px
:align: center
```  

If you see a list of "Available contexts", such as shown above, then you have successfully installed the drivers.  

```{clear-content}
```

If you get something like the message below, then you've probably installed the drivers correctly, but the computer can't find Jupiter (or any IIO device).  Is Jupiter plugged in??? 

```{image} resources/iio_info2.svg
:width: 700px
:align: center
```  

```{clear-content}
```

You might also receive a message like the one below, 'iio_info' is not recognized.  If you see this, then you have not properly installed the drivers.  Check the driver installation steps and complete anything that you missed.  

```{image} resources/iio-info3.png
:width: 700px
:align: center
```  

```{clear-content}
```

```{note}
For questions or help with the Jupiter SDR, please visit:
<br>
{ez}`fpga`
```