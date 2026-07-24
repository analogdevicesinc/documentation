(adc-jupiter-setup)=
# Setup

<!-- Add an Introduction -->
This page walks through how to connect to Jupiter and verify communication.


## Table of Contents
```{toctree}
:maxdepth: 1

Installing the Drivers <jupiter-driver-installation/index>
Unboxing <unboxing/index>
Transceiver Evaluation Software (TES) <tes/index>
Flashing the SD Card (Detailed) <flashing-sd-card/index1>
Flashing the SD Card (Quick Guide) <flashing-sd-card/index>
```

<!-- ## Two ways to use Jupiter
**Case 1 - data streaming to a host computer Jupiter SDR**
- Micro-USB cable
- USB Type-C cable (or Ethernet cable)
- USB Type-C Power Supply

**Case 2 - stand alone use Jupiter SDR**
- DisplayPort-compatible monitor
- USB Type-C multiport hub, mouse and keyboard
- USB Type-C Power Supply

Below will cover how to connect using Case 1. -->

## Connecting Jupiter

1. When Jupiter is connected you can use ***iio_info -s*** in command prompt to check what devices your computer can see.
It can be seen that there are 5 different devices connected in the image below and that device 2 is the Jupiter SDR. This can be inferred from looking at the 'adrv9002' tag.

```{image} iio-info-s.png
:alt: Put Text Here to Describe the Image
:width: 800px
:align: center
```

```{note}
There are two acceptable IP addresses here: 10.75.162.65 and analog-3.local.
<br>
```

```{clear-content}
```
2. In command prompt type the iio_attr -u (-u allows specification of an IP address) followed by the IP address from the Jupiter and a -d (-d shows the devices) at the end. In this case it is ***iio_attr -u ip:analog-3.local -d*** or ***iio_attr -u ip:10.75.162.65 -d***.

```{image} iio-info-u.png
:alt: Put Text Here to Describe the Image
:width: 700px
:align: center
```

3. Next open a PuTTy terminal or another terminal emulator, connect to Jupiter by either using the IP address from above or connect using the COM port.

```{image} pu-tty-jup-ip.png
:alt: Put Text Here to Describe the Image
:width: 500px
:align: left
```

```{image} pu-tty-jupiter.png
:alt: Put Text Here to Describe the Image
:width: 500px
:align: right
```

```{clear-content}
```
4. In the terminal emulator type in ***iio_attr -d*** the same devices that were in step 2 should be in this step. If this is the case it shows that you are connected to Jupiter.

```{image} iio-attr-d-in-putty.png
:alt: Put Text Here to Describe the Image
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
