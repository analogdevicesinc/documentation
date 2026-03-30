# Hardware Introduction


```{image} phaser_pict.svg
:alt: Phaser Picture
:width: 400px
:align: right
```

The ADALM-PHASER (CN0566) is a phased-array beamforming antenna demonstration platform that allows the user to experience the principles and applications of phased array antennas. The Phaser consists of 3
parts, all connected together:

1.  **The Phaser RF board**

    The RF board hosts the phased array receiver, up and down converters, and an LO ramping synthesizer. A 5V (3.5A) USB-C power cable connects to the RF board and provides power for the entire
    Phaser assembly.

2.  **Raspberry Pi 4**

    This provides control and data transmission. Users can also attach a keyboard/mouse and HDMI monitor directly to this Raspberry Pi.

3.  **ADALM-PLUTO SDR**

    The SDR interfaces between the RF inputs/outputs of the RF board and a computer USB connection for control and baseband data streaming. TX2 of Pluto is connected via a u.FL cable to the TX_IN SMA port on the RF board. RX1 and RX2 of Pluto are connected via u.FL cables to the RX1 and Rx2 ports on the RF board.


```{toctree}
:maxdepth: 1

The Phaser RF Board <basic-rf/index>
Common Phaser Configurations <configs/index>
RF Board Details <detailed-rf/index>
Device Tree Overlay <device-tree/index>
Schematics, Layout, and BOM <schematics/index>
Assembly and Production <assembly/index>
```



```{clear-content}
```
```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```
