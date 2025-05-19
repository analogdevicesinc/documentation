Intro to Devicetree
===================

Zephyr contains a concept borrowed from Linux called the "Devicetree",
which is a key differentiator between Zephyr and other Real-Time
Operating Systems (RTOSes). This page will educate a reader on essential
Devicetree concepts as they relate to Zephyr and writing Zephyr
drivers.  The device tree basics and format described here is applicable
to Linux too!

Devicetree: What is it & Why use it?
------------------------------------

The Devicetree is an abstract data structure. Its purpose is to
describe and configure the hardware connected to a system. The reason
this is useful is that embedded developers usually spend a lot (too
much) of their time wrestling with the configuration of hardware
features, pin maps, and peripheral settings instead of approaching the
actual processing of the target signals and data within an application.
The devicetree creates a structure that can be pulled into application
code to determine the connected hardware at runtime (so long as the
device tree has the correct configuration). This means a couple of things:

-  Application code can be much more portable between multiple hardware
   boards, and multiple separate revisions. This is because the driver C
   code is abstracted a layer above the hardware by the device tree. 
-  Hardware configuration no longer needs to happen in C code. It
   instead happens in the Devicetree.
-  Peripheral boards can be slotted in via overlay files which attach to
   an existing Devicetree, so they too can be slotted in without much
   additional driver code configuration. 

How do I read it? 
--------------------

Devicetree has its own syntax...this can be a little tough to read at
first, but the main thing to remember is *it's just a hierarchical
description of hardware*. Device tree files are written in a syntax
called *dts* or "**d**\ evice **t**\ ree **s**\ ource". Thus, one
configures the devicetree in ".dts" or "dtsi" (**d**\ evice **t**\ ree
**s**\ ource **i**\ nclude) files. A .dts file consists of a few things:

The Root Node 
^^^^^^^^^^^^^^

The Devicetree is comprised of one or more nodes, delimited by brackets
{}. Every Devicetree file must at the very least have a root node, named
with a forward slash ("/"). 

.. code:: dts

   / {
   };

The root node mostly serves the purpose of containing individual
subnodes. 

Nodes & Subnodes
^^^^^^^^^^^^^^^^

Subnodes are similarly delimited in a hierarchy starting from the root.
Here's an example .dts file:

.. code:: dts

   / {
       example_node {
           subnode_label: example_subnode {
               subnode_property = <4>;
           };
       };
   };

The above devicetree source contains 3 nodes:

-  The root "/" node

   -  example_node

      -  example_subnode

If we look closer at the example subnode, we'll notice it has
a **label** and a **property**. 

-  A label is a simple shorthand name that can be used to refer to a
   node elsewhere in the device tree, Any node may have 0, 1, or more
   labels. 
-  A property is a name/value pair that is associated with a given node.
   A property can be an array of strings, numbers, bytes, or even a
   mixture of types. 

   -  A boolean property may have an empty value. For these, the simple
      presence or absence of the property conveys sufficient
      information. 

   -  The size and type of property is implied by the enclosing
      brackets ("<>" in the case of the integer subnode_property above)

Each node has a **path** and can be indexed by appending its parent
nodes with forward slashes, such as on Linux. For example, the path to
the example_subnode is "/example_node/example_subnode". 

Aliases
^^^^^^^

One may see an "aliases" node contained within a device tree source
file. The aliases' node has properties whose names are aliases and values
are references to a node in the device tree. A reference to a node can
be given using the reference symbol "&". Here's an example using the
subnode label from earlier:

.. code:: dts

   / {
       aliases {
           subnode_alias = &subnode_label;
       };
   };

These aliases which can be referenced by C/C++ application code to make
it more portable. For example, a "led0" alias may be used to identify a
connected LED without having to directly reference it's GPIO pin or
otherwise tether the application code to a particular board.  

.. code:: dts

   / {
       aliases {
           led0 = &led0;
           led1 = &led1;
           btn0 = &button0;
           btn1 = &button1;
       };
   };

Devicetree Bindings
-------------------

Devicetree bindings declare both the required and optional properties of
a device. Devicetree bindings are required by Zephyr in order to compile
the device tree, and are in the YAML file format. Linux also has a
concept of devicetree bindings, which may be either YAML or free-text
format.  However, unlike Zephyr, Linux device tree bindings are not
required, and are simply used as developer documentation.  It is not
uncommon to find a device tree binding file missing for a driver on
Linux.

"compatible"
^^^^^^^^^^^^

The "compatible" property binds a devicetree node to a group of
requirements. If a node is contained in the devicetree containing a
"compatible" property that matches one given in the devicetree bindings
YAML files, it must have the required properties given in the YAML file
or the devicetree will fail to compile. 

Here's an example .yaml file that specifies a hypothetical "adi,max32xxx" node:

.. code:: yaml

   compatible: "adi,max32xxx"
   properties:
     num-leds:
       type: int
       required: true

Now here's a corresponding devicetree node:

.. code:: dts

   / {
      node0 {
         compatible: "adi,max32xxx";
         num-leds = <4>;
      };
   };

In the above file, "node0" gets mapped to the devicetree bindings via
the "compatible" property. Therefore, it must contain the property
"num-leds" or else the devicetree will fail to compile. 

How does the Devicetree get used?
---------------------------------

Information can be extracted from the Devicetree to use in application
code – that means device drivers now will have a component located in
the Devicetree as well, and application C/C++ code will frequently
reference the Devicetree to extract information about connected
hardware. This adds a layer of complexity with the benefit
of allowing hardware to be described at runtime rather than directly
within the application firmware. This ultimately should mean that more
application code is portable to more hardware variants given that the
application code can afford to be more hardware-agnostic, provided the
target hardware meets the minimum requirements of the application.
Zephyr's build system aggregates all the relevant .dts, .dtsi, and
.dtoverlay files at compile time into a single C header file called
"devicetree.h". 

Zephyr Devicetree Bindings Index
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Zephyr, some node definitions and properties are vendor specific.
This is useful for implementations of vendor-specific hardware, such as
I2C controller drivers across different microcontroller SDKs. As such,
questions such as "How do I enable internal pullups for a GPIO?" are
answered differently for different vendors. The place to look for where
these properties are defined is the `Zephyr Devicetree Bindings
Index <https://docs.zephyrproject.org/latest/build/dts/api/bindings.html>`__.
Here you can find different vendor-specific properties by looking at the
vendor's implementation of particular drivers. For example, the ADI
Zephyr driver for MAX32xxx GPIO controllers is under "`adi,
max32-gpio <https://docs.zephyrproject.org/latest/build/dts/api/bindings/gpio/adi%2Cmax32-gpio.html#dtbinding-adi-max32-gpio>`__". 

.dts vs .dtsi vs .dtoverlay
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A typical Devicetree file that will go into the compiler is called a
device tree source or .dts file. Some file are meant to be included in
other .dts files, and as such as called device tree source include, or
.dtsi files. Finally, a given custom board that integrates pre-existing
hardware (such as sensors, processors, etc) can be described in terms of
a device tree overlay, or .dtoverlay file. 

.. code:: dts

   /*
    * Copyright (c) 2025 Analog Devices, Inc
    * SPDX-License-Identifier: Apache-2.0
    */

   /*
    * This Devicetree overlay will connect an ADT7420 Pmod
    * to an AD-APARD32690-SL board.
    */

   /* ADT7420 I2C Configuration */
   pmod_i2c: &i2c0 {
       status = "okay";

       pinctrl-0 = <&i2c0a_scl_p0_31>, <&i2c0a_sda_p0_30>;
       pinctrl-names = "default";

       temp1: adt7420@48 {
           compatible = "adi,adt7420";
           status = "okay";
           friendly-name = "ADT7420 Temperature Sensor";

           // i2c address
           reg = <0x48>;
       };
   };

   /* Set logic to 3.3V & optionally enable internal pullups */
   &i2c0a_scl_p0_31{
       power-source = <MAX32_VSEL_VDDIOH>;
       // bias-pull-up;
   };
   &i2c0a_sda_p0_30{
       power-source = <MAX32_VSEL_VDDIOH>;
       // bias-pull-up;
   };

   /*
    * Aliases node gives a convenient alias to a node, which
    * can be used in C code using Zephyr Devicetree macros
    */
   / {
       aliases {
           i2c-temp1 = &temp1;
       };
   };

How can I look at the compiled Devicetree? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A helpful way to view compiled devicetree within a Zephyr project is
the `dtsh Python module <https://pypi.org/project/dtsh/>`__. This module
has some small bugs on Windows at the time of writing, but is mostly
cross-platform, and can be used to analyze the compiled Devicetree in a
neat, readable format. 

Blinky in Zephyr (Using the Devicetree)
---------------------------------------

Below is the classic "Blinky" sample code given in Zephyr. It uses the
Devicetree by grabbing "led0" from a Devicetree alias. The flow of the
example is as follows:

-  Include Zephyr kernel and GPIO driver API
-  Extract the first connected LED from a devicetree alias. This could
   also be done using a Devicetree node label.

   -  The LED is given the type "const struct **gpio_dt_spec**", which
      is defined by the Zephyr GPIO API. 
   -  Most objects extracted from the devicetree will be a type defined
      by an API or type "const struct device" (e.g. "const struct device
      \*uart")

-  Utilize the Zephyr GPIO API to...

   -  Check if the GPIO port is ready
   -  Configure & enable the pin as a GPIO output
   -  Toggle the LED within a while loop. 

The code is located here:
https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/basic/blinky/src/main.c
and documented here:
`README.rst <https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/basic/blinky/README.rst>`__

.. code:: cpp

   /*
    * Copyright (c) 2016 Intel Corporation
    *
    * SPDX-License-Identifier: Apache-2.0
    */

   #include <zephyr/kernel.h>
   #include <zephyr/drivers/gpio.h>

   /* 1000 msec = 1 sec */
   #define SLEEP_TIME_MS   1000

   /* The devicetree node identifier for the "led0" alias. */
   #define LED0_NODE DT_ALIAS(led0)

   /*
    * A build error on this line means your board is unsupported.
    * See the sample documentation for information on how to fix this.
    */
   static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED0_NODE, gpios);

   int main(void)
   {
       int ret;

       if (!gpio_is_ready_dt(&led)) {
           return 0;
       }

       ret = gpio_pin_configure_dt(&led, GPIO_OUTPUT_ACTIVE);
       if (ret < 0) {
           return 0;
       }

       while (1) {
           ret = gpio_pin_toggle_dt(&led);
           if (ret < 0) {
               return 0;
           }
           k_msleep(SLEEP_TIME_MS);
       }
       return 0;
   }

Further References
------------------

Next step – go read the specs!

-  If you have to develop or modify Devicetree beyond this level, it's
   likely you need to read the Devicetree specification:
   `The Devicetree Project <https://www.devicetree.org/>`__
-  For Zephyr-specific devicetree APIs, pair the Devicetree spec
   (platform-independent) with the Zephyr Devicetree API Reference:
   `Devicetree — Zephyr Project Documentation <https://docs.zephyrproject.org/latest/build/dts/index.html>`__
