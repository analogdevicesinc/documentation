# Troubleshooting Guide

Reference for resolving common issues with the X-Band Phased Array Development Platform. Use the section headings below to navigate to the relevant issue category.

## Power and Boot Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| No power LEDs | Power supply not connected | Verify all power connections and switch positions |
| Board gets hot quickly | Short circuit | Power off immediately, check for shorts with multimeter |
| ZCU102 won't boot | SD card not inserted | Verify SD card fully seated in J1001 |
| ZCU102 won't boot | Wrong boot mode | Check SW6 settings: ON-OFF-OFF-OFF |
| Intermittent boot | Loose FMC connection | Reseat AD9081-FMCA-EBZ board |
| No Ethernet link | Cable not connected | Check cable, verify link LED on RJ45 |
| Board doesn't power on or powers off | Insufficient PSU current | Use a 12V 6A+ supply; 8A+ when FMC cards are installed |

## VADJ and AD9081 Power Issues

Two issues commonly prevent 1.8V VADJ from powering the AD9081-FMCA-EBZ:

1. **ADXUD1AEBZ FMC EEPROM** — Non-compliant EEPROM prevents VADJ from enabling during boot.
   - Program the FMC EEPROM (see {ref}`EEPROM Programming <x-band-eeprom>`), then perform a full power cycle of the FPGA.

2. **AD9081 LTM4616 enable pin voltage** — The run-control threshold is 1.7 V. If R1M voltage falls below this, VADJ will not enable.
   - Replace R1M (2.2 kΩ) with a 220 Ω 0402 resistor to raise the enable pin voltage above 1.7 V.

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| 1.8V VADJ missing after EEPROM programming | Incomplete power cycle | Full power cycle: disconnect AC, wait 10 s, reconnect |
| VADJ not enabling | LTM4616 enable voltage too low | Replace R1M (2.2 kΩ → 220 Ω 0402) |
| Wrong voltage on VADJ | Wrong EEPROM programmed | Verify I2C path: `/sys/bus/i2c/devices/15-0050/eeprom` |
| VADJ intermittent | FMC connector issue | Reseat FMC connector; inspect pins for damage |

## EEPROM Programming Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| `find /sys -name eeprom` returns no results | FMC not fully seated | Reseat FMC connector and reboot |
| EEPROM I2C device missing | ZCU102 not booted | Confirm boot completed; run `i2cdetect -y 15` to rescan |
| `fru-dump` returns error | FRU binary not found | Verify: `ls /usr/local/src/fru_tools/masterfiles/AD-FMCOMMS2-EBZ-FRU.bin` |
| Permission denied during write | Not logged in as root | Log in as `root` user |
| Write fails to I2C device | Wrong I2C bus number | Verify correct bus number with `i2cdetect` |
| Readback shows incorrect data | Programming incomplete | Reprogram EEPROM; check file integrity with `md5sum` |
| EEPROM data doesn't persist | No power cycle after programming | Always perform a full power cycle after EEPROM changes |
| Write-protect error | Hardware write-protect enabled | Check for and disable hardware write-protect jumpers |

## Firmware Verification (MD5 Checksums)

If you suspect corrupted or mismatched boot files, you can verify integrity by comparing MD5 checksums on the ZCU102:

```bash
md5sum /boot/Image
md5sum /boot/BOOT.BIN
md5sum /boot/system.dtb
```

Compare the output against the checksums of the files you originally copied to the SD card (run `md5sum` on your host machine against the source files). If they don't match, the file was corrupted during copy or the SD card has errors — reflash and recopy.

```{note}
Checksums will NOT match between different firmware builds or software versions. This check is only useful to confirm that the files on the SD card are identical to what you intended to copy — not to verify a specific "correct" version.
```

## SD Card and Boot Media Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| ZCU102 doesn't boot | SD card not fully inserted | Verify SD card fully seated in slot J1001 |
| "No SD card" errors | Wrong boot mode | Check SW6: ON-OFF-OFF-OFF |
| Card not recognized | Incompatible SD card | Use SanDisk or Samsung; try a different card |
| Intermittent boot failures | Corrupted SD card | Reformat and reflash using BalenaEtcher |
| Boot hangs at U-Boot | Missing or misnamed boot files | Verify `BOOT.BIN`, `Image`, and `system.dtb` are in SD card root (case-sensitive) |
| Linux boots but fewer than 40 IIO devices | Wrong device tree | Copy matching `system.dtb` for your clocking config; full power cycle |
| VADJ not present after boot | EEPROM not programmed | See {ref}`EEPROM Programming <x-band-eeprom>` |
| "Flash Failed" in BalenaEtcher | Expected behavior | This is normal — verification always fails for Kuiper Linux images; proceed |
| File copy errors on ADI PCs | Windows auto-encryption | Use network drive mapping; never copy directly through Windows Explorer to SD card |

## ZCU102 Configuration Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| No boot activity or UART output | Wrong boot mode | Verify SW6: ON-OFF-OFF-OFF |
| USB keyboard or mouse not detected | Wrong USB jumper configuration | Check J7, J109, J110, J112, J113 are on the correct pin pairs |
| Terminal connected but shows no output | Wrong COM port or settings | Use 115200 baud, 8N1, no flow control; verify CP210x driver installed |
| Ethernet link doesn't come up or no IP | Cable or DHCP issue | Try a different cable; configure static IP if DHCP is unavailable |
| Network not reachable from PC | Subnet mismatch | Ensure PC and ZCU102 are on the same subnet (e.g., 192.168.0.x) |

## Boot Log Errors (Expected)

| Symptom | Cause | Action |
|---------|-------|--------|
| `Failed to read/write scratchpad` errors during boot | ADAR1000 SPI accessed before Stingray power sequencing completes | **None — this is expected.** The kernel driver probes the ADAR1000s before the power-up script has finished enabling all rails. The devices initialize correctly once the sequencing script runs. |

## Communication and Network Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Cannot ping ZCU102 | Wrong IP address | Check actual IP via serial console: `ip addr show`; update URI in `main.py` |
| `iio_info` shows no devices | FPGA not configured | Verify FPGA bitstream loaded; check DS2 LED |
| `iio_info` "Connection refused" | IIO network daemon not running | Check boot log; verify IIO daemon is active |
| ADAR1000 not detected | SPI daisy-chain not connected | Verify all SPI connections on hardware |
| USB-UART not working | Driver not installed | Install Silicon Labs CP210x drivers; check Device Manager |
| IIO attribute access fails | Wrong device path or driver | Run `iio_attr -d` to list all IIO devices and verify path |

## RF Connection Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Poor RF performance | Loose SMA connectors | Hand-tight plus 1/4 turn on all RF cables |
| Phase errors between channels | Unmatched cable lengths | Use matched-length cable sets for all signal paths |
| High insertion loss | Damaged connectors | Inspect center pins; replace any damaged cables |
| No LO distribution | MMCX not fully seated | Re-seat all MMCX connections (push until click) |
| Poor impedance matching | Wrong cable type | Verify 50 Ω cables rated for >10 GHz (X-Band) |
| Control interfaces not responding | Loose PMOD or FMC connection | Verify all PMOD and FMC connections are fully seated |

## TDD Timing Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| No transitions seen on TR probe point | TDD not enabled or driver not loaded | Run `iio_attr -c axi-core-tdd enable`; check `lsmod \| grep tdd` |
| IIO TDD device not found | Bitstream doesn't include TDD core | Confirm FPGA bitstream and device tree include the TDD core |
| Measured timing doesn't match configuration | Wrong units or unstable clock | Verify system clock frequency; check µs vs. clock-cycle unit settings |
| TX leakage visible during RX window | Guard time too short | Increase guard time between TX and RX windows |
| ADC saturates at TX-to-RX transition | Insufficient guard time | Increase guard time; verify TR switch transitions with oscilloscope |
| JESD204B errors during TX/RX switching | Clock-domain crossing or sync issue | Increase guard times; verify MxFE sample clock alignment with TDD timing |
| TDD configuration changes have no effect | Parameters only take effect after disable/enable cycle | Disable TDD → update parameters → re-enable |

```{warning}
Always verify TDD timing with an oscilloscope before enabling high-power TX modes. Insufficient guard time can expose the LNA to transmit energy and cause hardware damage.
```

## pyRadar Software Issues

**Installation**

| Issue | Solution |
|-------|----------|
| `pip` not recognized | Add Python to PATH and restart terminal |
| Package installation fails | Use `python -m pip install <package>` |
| Genalyzer install error | Requires Python 3.10.0 — not compatible with 3.11+ |
| Permission denied | Run terminal as administrator (Windows) |

**Hardware Connection**

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Cannot ping ZCU102 | Wrong IP address | Check serial console; update `uri` in `main.py` |
| `iio_info` shows no devices | FPGA not configured | Verify FPGA bitstream loaded; check boot log |
| Device connection timeout | Network subnet mismatch | Confirm PC and ZCU102 are on the same subnet |

**Python Environment**

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| `ModuleNotFoundError: adi` | Dependencies not installed | Run `pip install -r requirements.txt` |
| Genalyzer import fails | Wrong Python version | Verify IDE is using Python 3.10.0 interpreter |
| Package version conflicts | Multiple Python installations | Use `python -m pip` to target the 3.10.0 environment explicitly |
| Import errors after install | Wrong interpreter selected | Verify IDE Python interpreter path |

**Hardware Initialization**

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| AD9081 not detected | IIO device not loaded | Run `iio_info`; reload FPGA if needed |
| ADAR1000 connection timeout | SPI daisy-chain issue | Verify all SPI connections on hardware |
| XUD1A initialization fails | Wrong device path | Check device paths in hardware setup configuration |
| Calibration fails at startup | Corrupted previous config | Delete `rx_cal_data.csv` and re-run calibration |

**Calibration**

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Phase errors after calibration | Reference element disabled | Verify reference element is enabled; check channel mapping |
| Amplitude imbalance persists | Incorrect gain settings | Re-run calibration; check ADAR1000 gain settings |
| Calibration file not found | Wrong working directory | Verify `rx_cal_data.csv` is in the `pyRadar/` directory |
| High residual errors | RF connection issue | Inspect all SMA/MMCX connections for damage or looseness |
| Calibration timeout | Hardware not responding | Check all hardware connections; verify device initialization |

**Radar Pilot Runtime**

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| No plot window appears | Missing PyQt5 backend | Run `pip install PyQt5` |
| Data capture returns zeros | Wrong channel mapping | Verify ADC channel configuration in `tx_rx_cal.py` |
| Pilot crashes immediately | Uncaught exception | Run with debug output; check error messages |
| Keyboard controls don't work | `keyboard` library permissions | Run script with administrator privileges |
| Plot updates very slow | RX buffer size too large | Reduce RX buffer size in hardware setup |
| Range calculation incorrect | Wrong FMCW parameters | Verify chirp bandwidth and sample rate settings |

**Performance**

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Low frame rate in live plots | CPU overloaded | Close other applications; reduce plot complexity |
| Memory usage grows over time | Buffer accumulation in loop | Ensure proper buffer cleanup; check for array accumulation |
| Network latency high | Slow Ethernet connection | Use gigabit Ethernet; verify cable quality |
| FFT processing slow | Large buffer sizes | Optimize buffer size for your application |
| Beam steering lag | Slow SPI communication | Minimize SPI I/O operations per processing frame |

## Additional Support

- **ADI EngineerZone**: :ez:`ez.analog.com/adef-system-platforms <adef-system-platforms/>`
- {external+pyadi-iio:doc}`pyadi-iio Documentation <index>`
- {ref}`Kuiper Linux Documentation <kuiper>`
