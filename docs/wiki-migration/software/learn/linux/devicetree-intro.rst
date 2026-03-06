Devicetree - Intro
==================

This page will educate a reader on essential Devicetree concepts and syntax   The device tree basics and format described here is applicable to embedded Linux and the popular Zephyr RTOS.

Devicetree: What Is It & Why Use It?
------------------------------------

The Devicetree is an abstract data structure. It's purpose is to describe and configure the hardware connected to a system. The reason this is useful is that embedded developers usually spend a lot (too much) of their time wrestling with the configuration of hardware features, pin maps, and peripheral settings instead of approaching the actual processing of the target signals and data within an application. The devicetree creates a structure that can be pulled into application code to determine the connected hardware at compile time (Zephyr) or boot/runtime (Linux) so long as the device tree has the correct configuration. This means a couple things:

-  Application code can be much more portable between multiple hardware boards, and multiple separate revisions. This is because the driver C code is abstracted a layer above the hardware by the device tree. 
-  Hardware configuration no longer needs to happen in C code. It instead happens in the Devicetree.
-  Peripheral boards can be slotted in via overlay files which attach to an existing Devicetree, so they too can be slotted in without much additional driver code configuration. 

How do I read this?
-------------------

Devicetree has its own syntax...this can be a little tough to read at first, but the main thing to remember is *it's just a hierarchical description of hardware*. Device tree files are written in a syntax called *dts* or "**d**\ evice **t**\ ree **s**\ ource". Thus, one configures the devicetree in ".dts" or "dtsi" (**d**\ evice **t**\ ree **s**\ ource **i**\ nclude) files. A .dts file consists of a few things:

The Root Node
~~~~~~~~~~~~~

The Devicetree is comprised of one or more nodes, delimited by brackets {}. Every Devicetree file must at the very least have a root node, named with a forward slash ("/"). 

**Devicetree Root Node**

.. code:: syntaxhighlighter-pre

   / {
   };

The root node mostly serves the purpose of containing individual subnodes. 

Nodes & Subnodes
~~~~~~~~~~~~~~~~

Subnodes are similarly delimited in a hierarchy starting from the root. Here's an example device tree source file:

**Devicetree Source Example**

.. code:: syntaxhighlighter-pre

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

If we look closer at the example subnode, we'll notice it has a **label** and a **property**. 

-  A label is a simple shorthand name that can be used to refer to a node elsewhere in the device tree, Any node may have 0, 1, or more labels. 
-  A property is a name/value pair that is associated with a given node. A property can be an array of strings, numbers, bytes, or even a mixture of types. 

   -  A boolean property may have an empty value. For these, the simple presence or absence of the property conveys sufficient information. 
   -  The size and type of a property is implied by the enclosing brackets ("<>" in the case of the integer subnode_property above)

Each node has a **path** and can be indexed by appending it's parent nodes with forward slashes, such as in Linux. For example, the path to the example_subnode is "/example_node/example_subnode". 

Aliases
~~~~~~~

One may see an "aliases" node contained within a device tree source file. The aliases node has properties whose names are aliases and values are references to a node in the device tree. A reference to a node can be given using the reference symbol "&". Here's an example using the subnode label from earlier:

**Aliases Node**

.. code:: syntaxhighlighter-pre

   / {
       aliases {
           subnode_alias = &subnode_label;
       };
   };

These aliases which can be referenced by C/C++ application code to make it more portable. For example, an "led0" alias may be used to identify a connected LED without having to directly reference it's GPIO pin or otherwise tether the application code to a particular board.  

**A "Real" Aliases Node**

.. code:: syntaxhighlighter-pre

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

Devicetree bindings declare both the required and optional properties of a device. Devicetree bindings are required by Zephyr in order to compile the device tree, and are in the YAML file format. Linux also has a concept of devicetree bindings, which may be either YAML or free-text format.  However unlike Zephyr, Linux device tree bindings are not required, and are simply used as developer documentation.  It is not uncommon to find a device tree binding file missing for a driver in Linux.

"compatible"
~~~~~~~~~~~~

The "compatible" property binds a devicetree node to a group of requirements. If a node is contained in the devicetree containing a "compatible" property that matches one given in the devicetree bindings YAML files, it must have the required properties given in the YAML file or the devicetree will fail to compile. 

**Devicetree Bindings (YAML) : "compatible"**

.. code:: syntaxhighlighter-pre

   compatible: "adi,max32xxx"
   properties:
     num-leds:
       type: int
       required: true

**Devicetree source (.dts or .dtsi): "compatible"**

.. code:: syntaxhighlighter-pre

   node0 {
       compatible: "adi,max32xxx";
       num-leds = <4>;
   };

In the above file, "node0" maps to the devicetree bindings via the "compatible" property. Therefore, it must contain the property "num-leds" or else the devicetree will fail to compile. 

How Does the Devicetree Get Used?
---------------------------------

Information can be extracted from the Devicetree to use in application code – that means device drivers now will have a component located in the Devicetree as well, and application C/C++ code will frequently reference the Devicetree to extract information about connected hardware. This adds an additional layer of complexity with the benefit of allowing hardware to be described at runtime rather than directly within the application firmware. This ultimately should mean that more application code is portable to more hardware variants given that the application code can afford to be more hardware-agnostic, provided the target hardware meets the minimum requirements of the application. 

Devicetree in Embedded Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For examples of how devicetree is used in the context of Embedded Linux, please view the following additional material:

-  Devicetree Overlays [Coming Soon]
-  Devicetree-Overlay-MAX31855 [Coming Soon]

Blinky in Zephyr (Using the Devicetree)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is the classic "Blinky" sample code given in Zephyr. It uses the Devicetree by grabbing "led0" from a Devicetree alias. The flow of the example is as follows:

-  Include Zephyr kernel and GPIO driver API
-  Extract the first connected LED from a devicetree alias. This could also be done using a Devicetree node label.

   -  The LED is given the type "const struct **gpio_dt_spec**", which is defined by the Zephyr GPIO API. 
   -  Most objects extracted from the devicetree will be a type defined by an API or type "const struct device" (e.g. "const struct device \*uart")

-  Utilize the Zephyr GPIO API to...

   -  Check if the GPIO port is ready
   -  Configure & enable the pin as a GPIO output
   -  Toggle the LED within a while loop. 

The code is located here: https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/basic/blinky/src/main.c and documented here: `README.rst <https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/basic/blinky/README.rst>`__

**Zephyr "Blinky"**

.. code:: syntaxhighlighter-pre

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

**Further References**

Next step – go read the specs!

-  If you have to develop or modify devicetree beyond this level, it's likely you need to read the Devicetree spec: `The Devicetree Project <https://www.devicetree.org/>`__.
-  For Zephyr-specific devicetree APIs, pair the Devicetree spec (platform-independent) with the Zephyr Devicetree API Reference:

   -  `Devicetree — Zephyr Project Documentation <https://docs.zephyrproject.org/latest/build/dts/index>`__

      -  `Introduction to devicetree — Zephyr Project Documentation <https://docs.zephyrproject.org/latest/build/dts/intro.html>`__

In addition, if you're starting out with a Raspberry Pi for a project, it can help to read the README for the devicetree overlays available in the Raspbian kernel:

-  `RaspberryPi Github - firmware/boot/overlays/README <https://github.com/raspberrypi/firmware/blob/master/boot/overlays/README>`__
