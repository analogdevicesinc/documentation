# Phaser Assembly and Production Test

This page is mostly intended for those companies that are assembling and building the Phaser kits.  If you are purchasing EVAL-CN0566-RPZ, then all of this assembly and testing has already performed.  Nevertheless, it may still be instructive, or a useful debug activity, to review this material.

## Board Level Assembly

A video walkthrough of the entire board assembly, including all of the cables, is found here:

```{video} https://www.youtube.com/watch?v=WR1DHfraLf8
:align: left
```
```{clear-content}
```

## Assembly

1. Install the u.fl cables as shown. Ensure that the connector is aligned before seating, and use a flat surface to press, such as an unused pencil eraser:

```{image} u_fl_cables.jpg
:width: 300px
:align: center
```

2. Install the 40-pin M-F extender on the reverse side of the board. Place the board on stiff antistatic foam while doing this, and use a steady, even pressure.

```{image} rpi_riser.jpg
:width: 300px
:align: center
```

3. Install a 22 mm M-F standoff and 12 mm M-F standoff as shown below. The threads from the 22 mm standoff enter from the reverse side of the board.

```{image} standoff_stackup.png
:width: 300px
:align: center
```

4. Install the camera mount using two 3 mm pan head screws as shown. Do not over-tighten.

```{image} camera_mount.jpg
:width: 300px
:align: center
```

5. Install the four tall standoffs from the top side of the board, at the four corners.


6. Prepare the ADALM-Pluto:
   - Remove the board from the enclosure, leaving the SMA panel intact Solder the 14-pin header as noted.

```{image} pluto_prep.jpg
:width: 300px
:align: center
```

7. Mount the ADALM-Pluto from the top side of the board. Note that the threaded ends of the standoff will need to be flexed slightly. Secure with 4x M2.5 nylon nuts. 

8. Connect the U.FL cables to the ADALM-Pluto as shown:

```{image} pluto_u_fls_8.jpg
:width: 300px
:align: left
```

```{note}
- Ensure that RX2 cable from the CN0566 board to Pluto RX2A is installed
- Snap the second cable onto the SMA to U.FL adapter.
- Snap the other end of the second cable onto Pluto TX2A, then snake the adapter between the Pluto and CN0566, thread onto CN0566 TX_IN SMA.
- Install a 90-degree SMA adapter onto CN0566 J1 as shown, facing downward.
```

```{clear-content}
```

9. Connect the 14-pin ribbon cable between CN0566 and Pluto as shown:

```{image} ribbon_cable_installation_9.jpg
:width: 300px
:align: center
```

10. Mount the Raspberry Pi from the reverse side of the board. Use 4x M2.5 x 4 mm pan head screws to secure.

```{image} rpi_mounting_10.jpg
:width: 300px
:align: center
```

## Test

Place the Vivaldi antenna / Selfie-Stick directly above the assembly as shown. The antenna should aim directly down at the center of the array:

```{image} test_front_view.jpg
:width: 300px
:align: center
```

- Plug a micro HDMI to HDMI cable into the Raspberry Pi HDMI connector closest to the USB-C power input.
- Insert a pre-prepared SD card into the Raspberry Pi. (To create this SD card, follow the instructions [here](../../setup/sd-card/index.md))
- Plug a keyboard into one of the remaining USB ports on the Raspberry Pi (A mouse is optional.)
- Connect a 3 Amp USB-C power adapter to the USB-C power input on the CN0566 board.  Do not use the USB-C Power input on the Raspberry Pi.  The CN0566 board will power the Raspberry Pi.
- Wait for the Raspberry Pi to boot.
- Open a terminal on the Raspberry Pi and type the following commands:

```{code-block}
cd ~/pyadi-iio/examples/phaser
python3 phaser_prod_tst.py
```

Then press enter. The test script will automatically run and print pass / fail results.

Example test results (taken from a random board on May 24, 2025). Your results may differ a bit. 

```{image} example_test_results.png
:width: 800px
:align: center
```

```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```
