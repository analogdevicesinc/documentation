# Using Python with Pluto

Programming with Python is a popular choice for working with PlutoSDR due to its simplicity and the availability of powerful libraries for signal processing and data analysis. There are two Python libraries that can be used with Pluto:  pyADI-IIO and pyLIBIIO:

| Library Name  |  Python Import Command   |  Comments
|---|---|---|
| PyADI-IIO    |  import adi  | Best, and easiest Python library to use
| pyLIBIIO     |   import iio   | Use when a pyADI-IIO object is not available for your system


## PyADI-IIO

```{image} resources/pyadi.png
:width: 200px
:align: right
```  

For most users, the `pyadi-iio` library (commonly called PyADI) provides a more user-friendly and high-level API for controlling Pluto and accessing its data. The PyADI quick start guide, installation instructions, and examples are all found [here](https://analogdevicesinc.github.io/pyadi-iio/index.html
).

This library can be installed using pip, but note that PyADI also requires the pylibiio library.  

```bash
pip install pylibiio
pip install pyadi-iio
```
Once you have these libraries installed, you can start using it to control Pluto and access its data. Here is a simple example of how to use `pyadi-iio` to read samples from Pluto:


***PyADI Example for 1t1r version of Pluto:***

```{code-block} python
import adi

PLUTO_IP_ADDR = "192.168.2.1"

# Create a PlutoSDR object
my_sdr = adi.Pluto(uri="ip:" + PLUTO_IP_ADDR)

# Configure Pluto (e.g., set the sample rate and center frequency)
my_sdr.sample_rate = 1e6  # Set sample rate to 1 MHz
my_sdr.center_freq = 2.4e9  # Set center frequency to 2.4 GHz

# Read samples from Pluto
data = my_sdr.rx()  # Read samples from Pluto

# Process the samples (e.g., print the first 10 samples)
print(data[:10])
```

***PyADI Example for 2t2r version of Pluto:***
```{code-block} python
import adi

PLUTO_IP_ADDR = "192.168.2.1"

my_sdr = adi.ad9361(uri="ip:" + PLUTO_IP_ADDR)

# Configure Pluto (e.g., set the sample rate and center frequency)
my_sdr.sample_rate = 1e6  # Set sample rate to 1 MHz
my_sdr.center_freq = 2.4e9  # Set center frequency to 2.4 GHz

# Read samples from Pluto
data = my_sdr.rx()  # Read samples from Pluto
rx1 = data[0]
rx2 = data[1]

# Process the samples (e.g., print the first 10 samples from each Rx)
print(rx1[:10])
print(rx2[:10])
```


**Additional PyADI examples:**
- [https://analogdevicesinc.github.io/pyadi-iio/guides/examples.html](https://analogdevicesinc.github.io/pyadi-iio/guides/examples.html)
- {git-documentation}`pluto.py <https://github.com/analogdevicesinc/pyadi-iio/blob/master/examples/pluto.py>`
- {git-documentation}`ad9361_example.py <https://github.com/analogdevicesinc/pyadi-iio/blob/master/examples/ad9361_example.py>`


```{video} https://www.youtube.com/watch?v=ZnCi-LHJ0GQ
:align: left
```
```{clear-content}
```

```{video} https://www.youtube.com/watch?v=ph0Kv4SgSuI
:align: left
```

```{clear-content}
```

## pyLIBIIO

There is another Python library that works with every IIO device -- pyLIBIIO.  Prior to the creation of PyADI-IIO, pyLIBIIO was the only recommended Python library for the PlutoSDR.  But now, with the advent of PyADI-IIO, there is not much reason to use pyLIBIIO for Pluto.  However, there is occasionally a command, or debug attribute, that is easier to access with pyLIBIIO than with pyADI-IIO. So if you absolutely have a good reason to use pyLIBIIO instead of (or in addition to) PySDR-IIO, then here's how you do it:

***pyLIBIIO Installation***

```
pip install pylibiio
```

***pyLIBIIO Simple Use Case***

pyLIBIIO communicates directly with the attributes and properties of the LIBIIO driver.  As such, it will work for any IIO device.  The downside is that you need to use exactly the text description and value of each attribute and context.  For example, if you wanted to change the attenuation of the Pluto TX1 output to -30 dB, here's how you would do it:

```{code-block} python
import iio
ctx = iio.Context('ip:192.168.2.1')
ctrl = ctx.find_device("ad9361-phy")
tx = ctrl.find_channel("voltage0",True)
tx.attrs['hardwaregain'].value = '-30'
```

So this code will work on Pluto, but you can see that it is not nearly as intuitive as the PyADI-IIO library. 

Below is a more complete example of a full Pluto python program using only pyLIBIIO:


***pyLIBIIO Example Code***

```{code-block} python
import iio
import sys
import numpy as np

PLUTO_IP_ADDR = "192.168.2.1"

ctx = iio.Context("ip:" + PLUTO_IP_ADDR)

dev_ctrl = ctx.find_device("ad9361-phy")
dev_dma  = ctx.find_device("cf-ad9361-lpc")
if dev_ctrl is None or dev_dma is None:
    raise RuntimeError("Missing ad9361-phy or cf-ad9361-lpc")

# --- Control channels (ad9361-phy) ---
rx_chan = dev_ctrl.find_channel("voltage0", False)        # RX control => is_output=False
if rx_chan is None:
    raise RuntimeError("RX control channel voltage0 not found on ad9361-phy")

rx_lo = dev_ctrl.find_channel("altvoltage0", True)        # LO is usually output => is_output=True
if rx_lo is None:
    raise RuntimeError("RX LO channel altvoltage0 not found on ad9361-phy")

# Set RX sample rate and LO
rx_chan.attrs["sampling_frequency"].value = "1000000"
rx_lo.attrs["frequency"].value = "2400000000"

# (Strongly recommended) bandwidth + gain mode
rx_chan.attrs["rf_bandwidth"].value = "1000000"
rx_chan.attrs["gain_control_mode"].value = "slow_attack"   # or "manual"

# --- Data channels (cf-ad9361-lpc) ---
rx_i = dev_dma.find_channel("voltage0", False)  # I
rx_q = dev_dma.find_channel("voltage1", False)  # Q
if rx_i is None or rx_q is None:
    raise RuntimeError("RX channels voltage0/voltage1 not found on cf-ad9361-lpc")

rx_i.enabled = True
rx_q.enabled = True

buf = iio.Buffer(dev_dma, 4096, False)  # 4096 samples per enabled channel
buf.refill()

raw = buf.read()
print("Received", len(raw), "bytes")

iq = np.frombuffer(raw, dtype=np.int16).reshape(-1, 2)
iq_complex = (iq[:, 0].astype(np.float32) + 1j * iq[:, 1].astype(np.float32)) / 32768.0

print("Samples:", iq_complex.shape[0])
print("First 5 samples:", iq_complex[:5])

sys.exit(0)
```  


Here's another pyLIBIIO example, this time using the FPGA DDS to generate a tone on the transmitter and plot the data:

```{code-block} python

# Copyright (C) 2018 Analog Devices, Inc.
# Author: Travis Collins <travis.collins@analog.com>
#
# Licensed under the GPL-2.
 
import iio

import sys
import numpy as np
import matplotlib.pyplot as plt

# User configurable
TXLO = 1000000000
TXBW = 5000000
TXFS = 3000000
RXLO = TXLO
RXBW = TXBW
RXFS = TXFS
 
# Setup contexts
try:
   ctx = iio.Context('ip:192.168.2.1')
except:
    print("No device found")
    sys.exit(0)

ctrl = ctx.find_device("ad9361-phy")
txdac = ctx.find_device("cf-ad9361-dds-core-lpc")
rxadc = ctx.find_device("cf-ad9361-lpc")
 
# Configure transceiver settings
rxLO = ctrl.find_channel("altvoltage0", True)
rxLO.attrs["frequency"].value = str(int(RXLO))
txLO = ctrl.find_channel("altvoltage1", True)
txLO.attrs["frequency"].value = str(int(TXLO))
 
tx = ctrl.find_channel("voltage0",True)
tx.attrs["rf_bandwidth"].value = str(int(RXBW))
tx.attrs["sampling_frequency"].value = str(int(RXFS))
tx.attrs['hardwaregain'].value = '-30'
 
rx = ctrl.find_channel("voltage0")
rx.attrs["rf_bandwidth"].value = str(int(TXBW))
rx.attrs["sampling_frequency"].value = str(int(TXFS))
rx.attrs['gain_control_mode'].value = 'slow_attack'
 
# Enable all IQ channels
v0 = rxadc.find_channel("voltage0")
v1 = rxadc.find_channel("voltage1")
v0.enabled = True
v1.enabled = True
 
# Create buffer for RX data
rxbuf = iio.Buffer(rxadc, 2**15, False)
 
# Enable single tone DDS
dds0 = txdac.find_channel('altvoltage0',True)
dds2 = txdac.find_channel('altvoltage2',True)
dds0.attrs['raw'].value = str(1)
dds0.attrs['frequency'].value = str(100000)
dds0.attrs['scale'].value = str(0.9)
dds0.attrs['phase'].value = str(90000)
dds2.attrs['raw'].value = str(1)
dds2.attrs['frequency'].value = str(100000)
dds2.attrs['scale'].value = str(0.9)
dds2.attrs['phase'].value = str(0)
 
# Collect data
reals = np.array([])
imags = np.array([])
 
for i in range(10):
  rxbuf.refill()
  data = rxbuf.read()
  x = np.frombuffer(data,dtype=np.int16)
  reals = np.append(reals,x[::2])
  imags = np.append(imags,x[1::2])
 
# Plot
plt.plot(reals)
plt.plot(imags)
plt.xlabel("Samples")
plt.ylabel("Amplitude [dbFS]")
plt.show()
```





```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```
