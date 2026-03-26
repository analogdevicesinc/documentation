<!--
   ADEF Platforms documentation master file, created by
   sphinx-quickstart on Tue Sep 30 12:05:43 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   -->
# ADC System Platforms Documentation

## Complete Evaluation & Demonstration Systems for ADI Data Converters

The **ADC System Platforms** team develops and supports fully integrated
evaluation and demonstration systems built around ADI data-converter
technologies.

Each platform delivers a validated system stack --- from RF hardware to
application software --- enabling rapid performance evaluation and
real-world system development.


## What Makes a Platform?

````{grid} 1 2 4 4
:gutter: 2

```{grid-item-card} Signal-Chain Hardware
:img-bottom: resources/Signal_Chain_Hardware_transparent.png

ADI MxFE, SDR, MEMS and power solutions integrated into validated system architectures.
```

```{grid-item-card} FPGA + Reference HDL
:img-bottom: resources/FPGA_Reference_HDL_transparent.png

COTS FPGA platforms with production-grade HDL reference designs.
```

```{grid-item-card} Linux + IIO
:img-bottom: resources/Linux_IIO_transparent.png

Embedded Linux builds with native [IIO](https://www.kernel.org/doc/html/latest/driver-api/iio/index.html) support.
```

```{grid-item-card} Application Software
:img-bottom: resources/Application_Software_transparent.png

System-level control via Python, MATLAB, or QIQ using libIIO APIs.
```
````

## Platforms

```{toctree}
:maxdepth: 1
:hidden:

Phaser (CN0566)<phaser/index>
Pluto SDR<pluto/index>
```

For more information on each of ADC Platforms, please click on the links below:


````{grid} 1 2 4 4
:gutter: 4

```{grid-item-card} Phaser (CN0566)
:link: phaser/index
:link-type: doc
:img-bottom: resources/phaser_pict.svg
:class-card: platform-card
X-Band Beamforming and Radar Learning Platform
```

```{grid-item-card} Pluto SDR
:link: pluto/index
:link-type: doc
:img-bottom: resources/pluto.png
:class-card: platform-card

Low-cost SDR system based on the AD9361
```
````  



## Platform Pilots

```{image} resources/pilot_ships.svg
:width: 400px
:align: right
```

Each platform includes at least one **Pilot** --- a fully documented system-level example of a representative use case--complete with all the key elements to implement that use case.   

**Pilots are more than just a demo!**  A Pilot provides:

-   Hardware + software setup
-   Stable drivers, APIs, and plug-ins
-   Example scripts in Python, MATLAB, or QIQ Systems
-   Documented workflows (setup → configure → run → analyze → modify)
-   A foundation for customer algorithm development

Pilots range from basic *"boot and capture"* examples to advanced
demonstrations including:

-   RF beamforming
-   FMCW radar operation
-   Wideband streaming
-   JESD bring-up validation 


## ADC Catalyst

ADI operates dedicated **ADC Catalyst Centers** where customers can
experience platforms and pilots live, receive training, and collaborate
directly with ADI engineers.

```{image} resources/rtp_nc_adaptive.jpeg
:width: 400px
:align: right
```

We have a Catalyst centres in:  
- North Carolina (USA): Contact [Ian Beavers](mailto:Ian.Beavers@analog.com)
- Limerick (Ireland): Contact [Simon Walkin](mailto:Simon.Walkin@analog.com)

### Catalyst Mission​


1.  **Elevate System-Level Expertise**\
    Enable customers to solve real-world system integration challenges.

2.  **Empower Customer Learning**\
    Provide hands-on access to ADI hardware, tools, and training.

3.  **Drive Collaborative Innovation**\
    Co-develop system-level solutions with customers and ADI design
    teams.


