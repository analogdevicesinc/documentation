# Jupiter vs. Pluto

A common question is: "How does Jupiter differ from Pluto?" Pluto (ADALM-PLUTO) is a software-defined radio platform that is geared toward flexibility and teaching electrical engineering topics like SDR, RF, and communications. The PlutoSDR is self-contained and is entirely USB-powered with the default firmware. It comes in at about $300 and is based on the AD9363 transceiver and the Zynq Z-7010 SoC. In contrast, the Jupiter SDR is about $4k, has a more powerful SoC, and allows for multiple-unit synchronization, where the Pluto does not. Another difference is that Pluto is more customizable, allowing easier changes to the LOs. While Pluto is typically used for education, Jupiter is typically used for industry applications in aerospace, defense, and communications.



| Feature | AD-JUPITER-EBZ | ADALM-PLUTO |
| --- | --- | --- |
| Transceiver | ADRV9002 | AD9363 |
| Multi-Chip Sync | Yes | No |
| DPD | Yes | No |
| Channels | 2Tx / 2Rx | 1Tx / 1Rx |
| Frequency Range | 30 MHz – 6 GHz | 325 MHz – 3.8 GHz |
| IBW | 12 KHz – 40 MHz | 200 kHz - 20 MHz |
| FPGA/SoC | Zynq Ultrascale+ MPSoC | Zynq Z-7010 |
| Form Factor | Ruggedized aluminum case | Small USB dongle |
| Power | USB-C or PoE | USB |


<!-- ## Configurability?
 Pluto exposes many radio parameters in a very flexible way, making it suited for experimentation and learning. Jupiter, by contrast, relies more heavily on predefined profiles and structured configuration to ensure repeatable, deterministic behavior. This tradeoff is intentional and enables features like multi‑chip synchronization and coherent RF operation. -->


## When should I choose Jupiter?

```{image} ../ad-jupiter-ebz-angle-web.jpg
:alt: Jupiter SDR
:width: 250px
:align: right
```

Jupiter is a good choice if you:
- Need multi‑channel or multi‑device coherent operation
- Are experimenting with beamforming, MIMO, or spatial processing
- Require deterministic timing and synchronization
- Are prototyping systems for aerospace, defense, or communications
- Need higher RF performance and system scalability

## When should I choose Pluto?

```{image} ../adalm-pluto-web.png
:alt: ADALM-Pluto SDR
:width: 250px
:align: right
```

Pluto is a good choice if you:
- Are learning SDR, RF, or communications concepts
- Need a low‑cost, portable SDR
- Want a simple USB‑powered setup
- Are developing or teaching basic waveforms and protocols
- Do not require multi‑device synchronization or coherence




```{clear-content}
```
```{note}
For questions or help with the Jupiter SDR, please visit:
<br>
{ez}`fpga`
```