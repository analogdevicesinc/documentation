Linux Drivers
=============

Building the ADI Linux kernel
-----------------------------

Common elements for all kernel builds:

-  make sure you have ``make`` installed on your system, but we generally recommend installing the build-essentials tools for your Linux distribution
-  some builds will require you to have ``u-boot-tools`` installed, to have the ``mkimage`` utilities available, so it's good to have them available/installed

.. admonition:: Download
   :class: download

   If you would like a pre-compiled kernel with complete user space, check out ADI's :doc:`Kuiper Linux Distribution </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`


Target specific details:

-  :doc:`Building the Zynq Linux kernel and devicetrees from source </wiki-migration/resources/tools-software/linux-build/generic/zynq>`
-  :doc:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source </wiki-migration/resources/tools-software/linux-build/generic/zynqmp>`
-  :doc:`Building the Intel SoC-FPGA Linux kernel and devicetrees from source </wiki-migration/resources/tools-software/linux-build/generic/socfpga>`
-  :doc:`Building the Nios II kernel from source </wiki-migration/resources/tools-software/linux-build/generic/nios2>`
-  :doc:`Building with buildroot (microblaze) </wiki-migration/resources/tools-software/linux-build/generic/buildroot>`
-  :doc:`Building with Petalinux </wiki-migration/resources/tools-software/linux-build/generic/petalinux>`
-  :doc:`Building for Raspberry PI </wiki-migration/resources/tools-software/linux-build/generic/raspberrypi>`

The rapid increase in use of free and open-source software (FOSS), in particular Linux, represents the most significant, all-encompassing, and long-term trend that the embedded industry has seen since the early 1980s. [1]_ Like many, Analog Devices creates and maintains Linux Drivers for various Analog Devices products.

Life Cycle
~~~~~~~~~~

Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions. Drivers for obsolete devices are still tracked/maintained/supported on a best effort basis, since we understand the life cycle of end products that ADI's devices are designed into can be longer than the life cycle of the semiconductor product itself.

Maintenance and Support
~~~~~~~~~~~~~~~~~~~~~~~

These drivers are a combinations of written and maintained by Analog Devices developers, and by many other open source volunteers (most times end-users of various devices). All these drivers (and their corresponding device trees), independent of origin, are supported by ADI Linux kernel Engineers, on-line at :ez:`linux-software-drivers`. This is a combination of drivers that are maintained at Analog Devices `github <https://github.com/analogdevicesinc/linux>`__ and the mainline `mainline kernel </git.linux.org>>`__ at https://kernel.org/.

It is a common practice during driver development to support a subset of what the hardware/chip is capable of. If you find a driver does not expose a feature you require in your design, please make a request in our :ez:`support forums <linux-software-drivers>`.

Requests
~~~~~~~~

If you find a ADI device that you would like a driver for, please ask on our :ez:`support forums <linux-software-drivers>`. While we would like support every request, and do try to support most; this does go through a quick internal process before development starts. Our metrics to create device driver additions are pretty simple, it depends on development efforts (adding a part into an existing subsystem is easier than developing a completely new subsystem, or extending something), and popularity of the device (we are much more likely to do something that is recently released, than something 25 years old). If you have a local ADI contact (like a Sales Engineer or FAE) it's always a great idea to contact them at the same time so we can better understand your application and schedule. If you are an ADI employee who wants to make a request, click on *Submit Reference Design Idea* (under Tools and Services) on the main intranet page.

Driver List
-----------

Devices are organized by Linux subsystem.

Backlight
~~~~~~~~~

-  `ADP5020: Power Management Unit for Imaging Modules <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/video/backlight/adp5520_bl.c>`__ :adi:`ADP5020`
-  :doc:`ADP5501: Programmable Current Backlight Driver with Ambient Light Sensor Input </wiki-migration/resources/tools-software/linux-drivers/multifunction-device/adp5520>` :adi:`Obsolete <adp5501>`
-  :doc:`ADP5520: Backlight Driver with I/O Expander </wiki-migration/resources/tools-software/linux-drivers/multifunction-device/adp5520>`
-  :doc:`ADP8860: Charge Pump, 7-Channel Smart LED Driver with I2C Interface </wiki-migration/resources/tools-software/linux-drivers/backlight/adp8860>`
-  :doc:`ADP8861: Charge Pump, 7-Channel Smart LED Driver with I2C Interface </wiki-migration/resources/tools-software/linux-drivers/backlight/adp8860>`
-  :doc:`ADP8863: Charge Pump, 7-Channel Fun Lighting LED Driver </wiki-migration/resources/tools-software/linux-drivers/backlight/adp8860>`
-  :doc:`ADP8870: Charge Pump Parallel Backlight Driver with Image Content PWM Input </wiki-migration/resources/tools-software/linux-drivers/backlight/adp8870>`
-  `LT3593: 1MHz White LED Driver with Output Disconnect and One Pin Current Programming <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/leds/leds-lt3593.c>`__ :adi:`LT3593`

Battery Charger
~~~~~~~~~~~~~~~

-  :doc:`ADP5061: I2C Programmable Linear Battery Charger with Power Path and USB Mode Compatibility </wiki-migration/resources/tools-software/linux-drivers-all/battery-charger/adp5061>`
-  `LTC4162-L: 35V/3.2A Multi-Cell Lithium-Ion Step-Down Battery Charger with PowerPath and I2C Telemetry <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ltc4162-l-charger.c>`__ :adi:`LTC4162`
-  `MAX14656: USB Charger Detection with Integrated Overvoltage Protection <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max14656_charger_detector.c>`__ `MAX14656 <https://www.maximintegrated.com/MAX14656>`__
-  `MAX77650: Ultra-Low Power PMIC with 3-Output SIMO and Power Path Charger for Small Li+ 0.8-3.95V Output <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/mfd/max77650.c>`__ `MAX77650 <https://www.maximintegrated.com/MAX77650>`__
-  `MAX77651: Ultra-Low Power PMIC with 3-Output SIMO and Power Path Charger for Small Li+ 2.4-5.25V Output <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/mfd/max77650.c>`__ `MAX77651 <https://www.maximintegrated.com/MAX77651>`__
-  `MAX8903A: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter Power <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903A <https://www.maximintegrated.com/8903A>`__
-  `MAX8903B: 2A 1-Cell Li+ DC-DC Charger for USB, Adapter Power and Power-Enable on Battery Detection <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903B <https://www.maximintegrated.com/8903B>`__
-  `MAX8903C: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter Power <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903C <https://www.maximintegrated.com/8903C>`__
-  `MAX8903D: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter Power <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903D <https://www.maximintegrated.com/8903D>`__
-  `MAX8903E: 2A 1-Cell Li+ DC-DC Charger for USB, Adapter Power and Power-Enable on Battery Detection <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903E <https://www.maximintegrated.com/8903E>`__
-  `MAX8903G: 2A 1-Cell Li+ DC-DC Charger for USB, Adapter Power and Power-Enable on Battery Detection <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903G <https://www.maximintegrated.com/8903G>`__
-  `MAX8903H: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter Power <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903H <https://www.maximintegrated.com/8903H>`__
-  `MAX8903J: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter Power <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903J <https://www.maximintegrated.com/8903J>`__
-  `MAX8903N: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter Power <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903N <https://www.maximintegrated.com/8903N>`__
-  `MAX8903Y: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter Power <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max8903_charger.c>`__ `8903Y <https://www.maximintegrated.com/8903Y>`__

Battery Gas Gauge
~~~~~~~~~~~~~~~~~

-  `DS2760: High-Precision Li+ Battery Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ds2760_battery.c>`__ `DS2760 <https://www.maximintegrated.com/DS2760>`__
-  `DS2780: Stand-Alone Fuel Gauge IC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ds2780_battery.c>`__ `DS2780 <https://www.maximintegrated.com/DS2780>`__
-  `DS2781: 1-Cell or 2-Cell Stand-Alone Fuel Gauge IC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ds2781_battery.c>`__ `DS2781 <https://www.maximintegrated.com/DS2781>`__
-  `DS2782: Stand-Alone Fuel Gauge IC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ds2782_battery.c>`__ `DS2782 <https://www.maximintegrated.com/DS2782>`__
-  `DS2786: Stand-Alone OCV-Based Fuel Gauge <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ds2782_battery.c>`__ `DS2786 <https://www.maximintegrated.com/DS2786>`__
-  `LT3651-4.x: Monolithic 4A High Voltage 1 Cell Li-Ion Battery Charger <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/lt3651-charger.c>`__ :adi:`LT3651-4.1`
-  `LT3651-8.x: Monolithic 4A High Voltage 2-Cell Li-Ion Battery Charger <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/lt3651-charger.c>`__ :adi:`LT3651-8.2`
-  `LTC2941: Battery Gas Gauge with I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ltc2941-battery-gauge.c>`__ :adi:`LTC2941`
-  `LTC2942: Battery Gas Gauge with Temperature, Voltage Measurement <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ltc2941-battery-gauge.c>`__ :adi:`LTC2942`
-  `LTC2943: Multicell Battery Gas Gauge with Temperature, Voltage and Current Measurement <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ltc2941-battery-gauge.c>`__ :adi:`LTC2943`
-  `LTC2944: 60V Battery Gas Gauge with Temperature, Voltage and Current Measurement <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/ltc2941-battery-gauge.c>`__ :adi:`LTC2944`
-  `MAX17040: 1-Cell/2-Cell Fuel Gauge with ModelGauge <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17040_battery.c>`__ `MAX17040 <https://www.maximintegrated.com/MAX17040>`__
-  `MAX17041: 1-Cell/2-Cell Fuel Gauge with ModelGauge <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17040_battery.c>`__ `MAX17041 <https://www.maximintegrated.com/MAX17041>`__
-  `MAX17043: 1-Cell/2-Cell Fuel Gauge with ModelGauge and Low-Battery Alert <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17040_battery.c>`__ `MAX17043 <https://www.maximintegrated.com/MAX17043>`__
-  `MAX17044: 1-Cell/2-Cell Fuel Gauge with ModelGauge and Low-Battery Alert <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17040_battery.c>`__ `MAX17044 <https://www.maximintegrated.com/MAX17044>`__
-  `MAX17047: 1-Cell Fuel Gauge with ModelGauge m3 <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17042_battery.c>`__ `MAX17047 <https://www.maximintegrated.com/MAX17047>`__
-  `MAX17048: 3µA 1-Cell/2-Cell Fuel Gauge with ModelGauge <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17040_battery.c>`__ `MAX17048 <https://www.maximintegrated.com/MAX17048>`__
-  `MAX17049: 3µA 1-Cell/2-Cell Fuel Gauge with ModelGauge <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17040_battery.c>`__ `MAX17049 <https://www.maximintegrated.com/MAX17049>`__
-  `MAX17050: 1-Cell Fuel Gauge with ModelGauge m3 <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17042_battery.c>`__ `MAX17050 <https://www.maximintegrated.com/MAX17050>`__
-  `MAX17055: 7µA 1-Cell Fuel Gauge with ModelGauge m5 EZ <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17042_battery.c>`__ `MAX17055 <https://www.maximintegrated.com/MAX17055>`__
-  `MAX17058: 1-Cell/2-Cell Fuel Gauge with ModelGauge and Low-Battery Alert <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17040_battery.c>`__ `MAX17058 <https://www.maximintegrated.com/MAX17058>`__
-  `MAX17059: 1-Cell/2-Cell Fuel Gauge with ModelGauge <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max17040_battery.c>`__ `MAX17059 <https://www.maximintegrated.com/MAX17059>`__
-  `MAX17211: Stand-Alone ModelGauge m5 Fuel Gauge with SHA-256 Authentication <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max1721x_battery.c>`__ `MAX17211 <https://www.maximintegrated.com/MAX17211>`__
-  `MAX17215: Stand-Alone ModelGauge m5 Fuel Gauge with SHA-256 Authentication <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/max1721x_battery.c>`__ `MAX17215 <https://www.maximintegrated.com/MAX17215>`__

Battery Manager
~~~~~~~~~~~~~~~

-  `LTC1760: Dual Smart Battery System Manager <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/supply/sbs-manager.c>`__ :adi:`LTC1760`

CLOCK
~~~~~

-  :doc:`AD9545: Quad Input, 10-Output, Dual DPLL/IEEE 1588, 1 pps Synchronizer and Jitter Cleaner </wiki-migration/resources/tools-software/linux-drivers/clk/adi/clk-ad9545.c>`
-  `MAX9485: Programmable Audio Clock Generator <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/clk/clk-max9485.c>`__ `MAX9485 <https://www.maximintegrated.com/MAX9485>`__

Card Bus
~~~~~~~~

-  `MAX1600: Dual-Channel CardBus and PCMCIA VCC VPP Power Switching Networks <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/pcmcia/max1600.c>`__ `MAX1600 <https://www.maximintegrated.com/MAX1600>`__

GPIO
~~~~

-  :doc:`ADP5520: Backlight Driver with I/O Expander </wiki-migration/resources/tools-software/linux-drivers/multifunction-device/adp5520>`
-  :doc:`ADP5587: Mobile I/O Expander and QWERTY Keypad Controller </wiki-migration/resources/tools-software/linux-drivers/gpio/adp5588-gpio>`
-  :doc:`ADP5588: Mobile I/O Expander and QWERTY Keypad Controller </wiki-migration/resources/tools-software/linux-drivers/gpio/adp5588-gpio>`
-  `MAX31910: Ultra-Low Power Industrial, Octal, Digital Input Translator/Serializer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max3191x.c>`__ `MAX31910 <https://www.maximintegrated.com/MAX31910>`__
-  `MAX31912: Ultra-Low Power Industrial, Octal, Digital Input Translator/Serializer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max3191x.c>`__ `MAX31912 <https://www.maximintegrated.com/MAX31912>`__
-  `MAX31913: Industrial, Octal, Digital Input Translator/Serializer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max3191x.c>`__ `MAX31913 <https://www.maximintegrated.com/MAX31913>`__
-  `MAX31953: Octal Industrial Digital Input with Isolated SPI Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max3191x.c>`__ `MAX31953 <https://datasheets.maximintegrated.com/en/ds/MAX31953-MAX31963.pdf>`__
-  `MAX31963: Octal Industrial Digital Input with Isolated SPI Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max3191x.c>`__ `MAX31963 <https://datasheets.maximintegrated.com/en/ds/MAX31953-MAX31963.pdf>`__
-  `MAX7300: 2-Wire-Interfaced, 2.5V to 5.5V, 20-Port or 28-Port I/O Expander <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max7300.c>`__ `MAX7300 <https://www.maximintegrated.com/MAX7300>`__
-  `MAX7301: 4-Wire-Interfaced, 2.5V to 5.5V, 20-Port and 28-Port I/O Expander <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max7301.c>`__ `MAX7301 <https://www.maximintegrated.com/MAX7301>`__
-  `MAX7310: 2-Wire-Interfaced 8-Bit I/O Port Expander with Reset <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-pca953x.c>`__ `MAX7310 <https://www.maximintegrated.com/MAX7310>`__
-  `MAX7312: 2-Wire-Interfaced 16-Bit I/O Port Expander with Interrupt and Hot-Insertion Protection <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-pca953x.c>`__ `MAX7312 <https://www.maximintegrated.com/MAX7312>`__
-  `MAX7313: 16-Port I/O Expander with LED Intensity Control, Interrupt, and Hot-Insertion Protection <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-pca953x.c>`__ `MAX7313 <https://www.maximintegrated.com/MAX7313>`__
-  `MAX7315: 8-Port I/O Expander with LED Intensity Control, Interrupt, and Hot-Insertion Protection <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-pca953x.c>`__ `MAX7315 <https://www.maximintegrated.com/MAX7315>`__
-  `MAX7319: I²C Port Expander with Eight Inputs and Maskable Transition Detection <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7319 <https://www.maximintegrated.com/MAX7319>`__
-  `MAX7320: I²C Port Expander with Eight Push-Pull Output <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7320 <https://www.maximintegrated.com/MAX7320>`__
-  `MAX7321: I2C Port Expander with 8 Open-Drain I/Os <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7321 <https://www.maximintegrated.com/MAX7321>`__
-  `MAX7322: I²C Port Expander with 4 Push-Pull Outputs and 4 Inputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7322 <https://www.maximintegrated.com/MAX7322>`__
-  `MAX7323: I²C Port Expander with 4 Push-Pull Outputs and 4 Open-Drain I/Os <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7323 <https://www.maximintegrated.com/MAX7323>`__
-  `MAX7324: I²C Port Expander with Eight Push-Pull Outputs and Eight Inputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7324 <https://www.maximintegrated.com/MAX7324>`__
-  `MAX7325: I2C Port Expander with 8 Push-Pull and 8 Open-Drain I/Os <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7325 <https://www.maximintegrated.com/MAX7325>`__
-  `MAX7326: I²C Port Expander with 12 Push-Pull Outputs and Four Inputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7326 <https://www.maximintegrated.com/MAX7326>`__
-  `MAX7327: I²C Port Expander with 12 Push-Pull Outputs and 4 Open-Drain I/Os <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7327 <https://www.maximintegrated.com/MAX7327>`__
-  `MAX7328: I²C Port Expanders with Eight I/O Ports <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7328 <https://www.maximintegrated.com/MAX7328>`__
-  `MAX7329: I²C Port Expanders with Eight I/O Ports <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpio/gpio-max732x.c>`__ `MAX7329 <https://www.maximintegrated.com/MAX7329>`__

Secondary function
^^^^^^^^^^^^^^^^^^

-  :doc:`ADP5585: Keypad Decoder and I/O Expansion </wiki-migration/resources/tools-software/linux-drivers/input-keyboard/adp5589>`
-  :doc:`ADP5587: Mobile I/O Expander and QWERTY Keypad Controller </wiki-migration/resources/tools-software/linux-drivers/input-keyboard/adp5588>`
-  :doc:`ADP5588: Mobile I/O Expander and QWERTY Keypad Controller </wiki-migration/resources/tools-software/linux-drivers/input-keyboard/adp5588>`
-  :doc:`ADP5589: Keypad Decoder and I/O Expansion </wiki-migration/resources/tools-software/linux-drivers/input-keyboard/adp5589>`

HWMon & PMBus
~~~~~~~~~~~~~

HWMon
^^^^^

-  `AD7314: Complete Temperature Monitoring System in an 8-Pin µSOIC Package <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ad7314.c>`__ :adi:`AD7314`
-  `AD7414: SMBus/I2C Digital Temperature Sensor in 6-Pin SOT with SMBus Alert and Over Temperature Pin <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ad7414.c>`__ :adi:`ad7414`
-  `AD7416: 10-Bit Digital Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ad7418.c>`__ :adi:`AD7416`
-  `AD7417: 10-Bit Digital Temperature Sensor and Four Channel ADC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ad7418.c>`__ :adi:`AD7417`
-  `AD7418: 10-Bit Digital Temperature Sensor and Single Channel ADC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ad7418.c>`__ :adi:`AD7418`
-  `ADM1177: Hot Swap Controller and Digital Power Monitor with Soft Start Pin <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adm1177.c>`__ :adi:`ADM1177`
-  `ADM1266: Cascadable Super Sequencer with Margin Control and Fault Recording <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/adm1266.c>`__ :adi:`ADM1266`
-  `ADT7301: 13-Bit, ±1ºC Accurate, MicroPower Digital Temperature Sensor in 6-Lead SOT-23 and 8-Lead MSOP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ad7314.c>`__ :adi:`ADT7301`
-  `ADT7302: ±2°C Accurate, MicroPower Digital Temperature Sensor in 6-Lead SOT-23 <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ad7314.c>`__ :adi:`ADT7302`
-  `ADT7310: ±0.5°C Accurate, 16-Bit Digital SPI Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adt7x10.c>`__ :adi:`ADT7310`
-  `ADT7320: ±0.25°C Accurate, 16-Bit Digital SPI Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adt7x10.c>`__ :adi:`ADT7320`
-  `ADT7408: ± 2°C Accurate, 12-Bit Digital Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/jc42.c>`__ :adi:`ADT7408`
-  `ADT7410: ±0.5°C Accurate, 16-Bit Digital I2C Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adt7x10.c>`__ :adi:`ADT7410`
-  `ADT7411: SPI-/I2C-Compatible, 10-Bit Digital Temperature Sensor and 8-Channel ADC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adt7411.c>`__ :adi:`ADT7411`
-  `ADT7420: ±0.25°C Accurate, 16-Bit Digital I2C Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adt7x10.c>`__ :adi:`ADT7420`
-  `ADT7470: Temperature Sensor Hub and Fan Controller <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adt7470.c>`__ :adi:`ADT7470`
-  `ADT75: ±1°C Accurate, 12-Bit Digital Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm75.c>`__ :adi:`ADT75`
-  `DS1621: Digital Thermometer and Thermostat <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ds1621.c>`__ `DS1621 <https://www.maximintegrated.com/DS1621>`__
-  `DS1631: High-Precision Digital Thermometer and Thermostat <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ds1621.c>`__ `DS1631 <https://www.maximintegrated.com/DS1631>`__
-  `DS1721: Digital Thermometer and Thermostat <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ds1621.c>`__ `DS1721 <https://www.maximintegrated.com/DS1721>`__
-  `DS1731: High-Precision Digital Thermometer and Thermostat <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ds1621.c>`__ `DS1731 <https://www.maximintegrated.com/DS1731>`__
-  `DS1775: Digital Thermometer and Thermostat in SOT23 <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm75.c>`__ `DS1775 <https://www.maximintegrated.com/DS1775>`__
-  `DS1780: CPU Peripheral Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adm9240.c>`__ `DS1780 <https://www.maximintegrated.com/DS1780>`__
-  `DS620: Low-Voltage, ±0.5°C Accuracy Digital Thermometer and Thermostat <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ds620.c>`__ `DS620 <https://www.maximintegrated.com/DS620>`__
-  `DS7505: High-Precision Digital Thermometer and Thermostat <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm75.c>`__ `DS7505 <https://www.maximintegrated.com/DS7505>`__
-  :doc:`Fan Control IP core: Core to control the fan used for cooling Xilinx Zynq Ultrascale+ MPSoC </wiki-migration/resources/tools-software/linux-drivers/hwmon/axi_fan_control>` :doc:`axi_fan_control </wiki-migration/resources/fpga/docs/axi_fan_control>`
-  `LM75: Digital Temperature Sensor and Thermal Watchdog with 2-Wire Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm75.c>`__ `LM75 <https://www.maximintegrated.com/LM75>`__
-  `LTC2945: Wide Range I2C Power Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc2945.c>`__ :adi:`LTC2945`
-  :doc:`LTC2947: High Precision Power and Energy Monitor </wiki-migration/resources/tools-software/linux-drivers/hwmon/ltc2947>` :adi:`LTC2947`
-  `LTC2990: Quad I2C Voltage, Current and Temperature Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc2990.c>`__ :adi:`LTC2990`
-  `LTC2992: Dual Wide Range Power Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc2992.c>`__ :adi:`LTC2992`
-  `LTC4151: High Voltage I2C Current and Voltage Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc4151.c>`__ :adi:`LTC4151`
-  `LTC4215: Hot Swap Controller with I2C Compatible Monitoring <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc4215.c>`__ :adi:`LTC4215`
-  `LTC4222: Dual Hot Swap Controller with I2C Compatible Monitoring <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc4222.c>`__ :adi:`LTC4222`
-  `LTC4245: Multiple Supply Hot Swap Controller with I2C Compatible Monitoring <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc4245.c>`__ :adi:`LTC4245`
-  `LTC4251: Negative Voltage Hot Swap Controllers in SOT-23 <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc4215.c>`__ :adi:`LTC4251`
-  `LTC4260: Positive High Voltage Hot Swap Controller with I2C Compatible Monitoring <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc4260.c>`__ :adi:`LTC4260`
-  `LTC4261: Negative Voltage Hot Swap Controllers with ADC and I²C Monitoring <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/ltc4261.c>`__ :adi:`LTC4261`
-  `MAX1110: +2.7V, Low-Power, Multichannel, Serial, 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max1111.c>`__ `MAX1110 <https://www.maximintegrated.com/MAX1110>`__
-  `MAX1111: +2.7V, Low-Power, Multichannel, Serial, 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max1111.c>`__ `MAX1111 <https://www.maximintegrated.com/MAX1111>`__
-  `MAX1112: +5V, Low-Power, Multichannel, Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max1111.c>`__ `MAX1112 <https://www.maximintegrated.com/MAX1112>`__
-  `MAX1113: +5V, Low-Power, Multichannel, Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max1111.c>`__ `MAX1113 <https://www.maximintegrated.com/MAX1113>`__
-  `MAX127: Multirange, +5V, 12-Bit DAS with 2-Wire Serial Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max127.c>`__ `MAX127 <https://www.maximintegrated.com/MAX127>`__
-  `MAX16065: 12-Channel/8-Channel Flash-Configurable System Managers with Nonvolatile Fault Registers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max16065.c>`__ `MAX16065 <https://www.maximintegrated.com/MAX16065>`__
-  `MAX16066: 12-Channel/8-Channel Flash-Configurable System Managers with Nonvolatile Fault Registers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max16065.c>`__ `MAX16066 <https://www.maximintegrated.com/MAX16066>`__
-  `MAX16067: 6-Channel, Flash-Configurable System Manager with Nonvolatile Fault Registers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max16065.c>`__ `MAX16067 <https://www.maximintegrated.com/MAX16067>`__
-  `MAX16068: 6-Channel, Flash-Configurable System Manager with Nonvolatile Fault Registers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max16065.c>`__ `MAX16068 <https://www.maximintegrated.com/MAX16068>`__
-  `MAX16070: 12-Channel/8-Channel, Flash-Configurable System Monitors with Nonvolatile Fault Registers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max16065.c>`__ `MAX16070 <https://www.maximintegrated.com/MAX16070>`__
-  `MAX16071: 12-Channel/8-Channel, Flash-Configurable System Monitors with Nonvolatile Fault Registers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max16065.c>`__ `MAX16071 <https://www.maximintegrated.com/MAX16071>`__
-  `MAX1617A: Remote/Local Temperature Sensor with SMBus Serial Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adm1021.c>`__ `MAX1617A <https://www.maximintegrated.com/MAX1617A>`__
-  `MAX1617: Remote/Local Temperature Sensor with SMBus Serial Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/adm1021.c>`__ `MAX1617 <https://www.maximintegrated.com/MAX1617>`__
-  `MAX1619: Remote/Local Temperature Sensor with Dual Alarm Outputs and SMBus Serial Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max1619.c>`__ `MAX1619 <https://www.maximintegrated.com/MAX1619>`__
-  `MAX1668: Multichannel Remote/Local Temperature Sensors <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max1668.c>`__ `MAX1668 <https://www.maximintegrated.com/MAX1668>`__
-  `MAX1805: Multichannel Remote/Local Temperature Sensors <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max1668.c>`__ `MAX1805 <https://www.maximintegrated.com/MAX1805>`__
-  `MAX197: Multi-Range (±10V, ±5V, +10V, +5V), Single +5V, 12-Bit DAS with 8+4 Bus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max197.c>`__ `MAX197 <https://www.maximintegrated.com/MAX197>`__
-  `MAX1989: Multichannel Remote/Local Temperature Sensors <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max1668.c>`__ `MAX1989 <https://www.maximintegrated.com/MAX1989>`__
-  `MAX199: 8-Channel, Multi-Range, 5V, 12-Bit DAS with 8+4 Bus Interface and Fault Protection <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max197.c>`__ `MAX199 <https://www.maximintegrated.com/MAX199>`__
-  `MAX31722: Digital Thermometers and Thermostats with SPI/3-Wire Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max31722.c>`__ `MAX31722 <https://www.maximintegrated.com/MAX31722>`__
-  `MAX31723: Digital Thermometers and Thermostats with SPI/3-Wire Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max31722.c>`__ `MAX31723 <https://www.maximintegrated.com/MAX31723>`__
-  `MAX31730: 3-Channel Remote Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max31730.c>`__ `MAX31730 <https://www.maximintegrated.com/MAX31730>`__
-  `MAX31790: 6-Channel PWM-Output Fan RPM Controller <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max31790.c>`__ `MAX31790 <https://www.maximintegrated.com/MAX31790>`__
-  `MAX6581: ±1°C Accurate 8-Channel Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6581 <https://www.maximintegrated.com/MAX6581>`__
-  `MAX6602: 5-Channel Precision Temperature Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6602 <https://www.maximintegrated.com/MAX6602>`__
-  `MAX6604: Precision Temperature Monitor for DDR Memory Modules <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/jc42.c>`__ `MAX6604 <https://www.maximintegrated.com/MAX6604>`__
-  `MAX6621: PECI-to-I²C Translator <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6621.c>`__ `MAX6621 <https://www.maximintegrated.com/MAX6621>`__
-  `MAX6622: 5-Channel Precision Temperature Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6622 <https://www.maximintegrated.com/MAX6622>`__
-  `MAX6625: 9-Bit/12-Bit Temperature Sensors with I²C-Compatible Serial Interface in a SOT23 <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm75.c>`__ `MAX6625 <https://www.maximintegrated.com/MAX6625>`__
-  `MAX6626: 9-Bit/12-Bit Temperature Sensors with I²C-Compatible Serial Interface in a SOT23 <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm75.c>`__ `MAX6626 <https://www.maximintegrated.com/MAX6626>`__
-  `MAX6635: 12-Bit Plus Sign Temperature Sensors with SMBus/I²C-Compatible Serial Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm92.c>`__ `MAX6635 <https://www.maximintegrated.com/MAX6635>`__
-  `MAX6636: 7-Channel Precision Temperature Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6636 <https://www.maximintegrated.com/MAX6636>`__
-  `MAX6642: ±1°C, SMBus-Compatible Remote/Local Temperature Sensor with Overtemperature Alarm <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6642.c>`__ `MAX6642 <https://www.maximintegrated.com/MAX6642>`__
-  `MAX6646: +145°C Precision SMBus-Compatible Remote/Local Sensors with Overtemperature Alarms <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6646 <https://www.maximintegrated.com/MAX6646>`__
-  `MAX6647: +145°C Precision SMBus-Compatible Remote/Local Sensors with Overtemperature Alarms <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6647 <https://www.maximintegrated.com/MAX6647>`__
-  `MAX6648: Precision SMBus-Compatible Remote/Local Temperature Sensors with Overtemperature Alarms <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX648 <https://www.maximintegrated.com/MAX648>`__
-  `MAX6649: +145°C Precision SMBus-Compatible Remote/Local Sensors with Overtemperature Alarms <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6649 <https://www.maximintegrated.com/MAX6649>`__
-  `MAX6650: Fan-Speed Regulators and Monitors with SMBus/I²C-Compatible Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6650.c>`__ `MAX6650 <https://www.maximintegrated.com/MAX6650>`__
-  `MAX6651: Fan-Speed Regulators and Monitors with SMBus/I²C-Compatible Interface and up to Four Tachometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6650.c>`__ `MAX6651 <https://www.maximintegrated.com/MAX6651>`__
-  `MAX6654: 1°C Accurate Remote/Local Temperature Sensor with SMBus Serial Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6654 <https://www.maximintegrated.com/MAX6654>`__
-  `MAX6657: ±1°C, SMBus-Compatible Remote/Local Temperature Sensors with Overtemperature Alarms <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6657 <https://www.maximintegrated.com/MAX6657>`__
-  `MAX6658: ±1°C, SMBus-Compatible Remote/Local Temperature Sensors with Overtemperature Alarms <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6658 <https://www.maximintegrated.com/MAX6658>`__
-  `MAX6659: ±1°C, SMBus-Compatible Remote/Local Temperature Sensors with Overtemperature Alarms <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6659 <https://www.maximintegrated.com/MAX6659>`__
-  `MAX6680: ±1°C Fail-Safe Remote/Local Temperature Sensors with SMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6680 <https://www.maximintegrated.com/MAX6680>`__
-  `MAX6681: ±1°C Fail-Safe Remote/Local Temperature Sensors with SMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6681 <https://www.maximintegrated.com/MAX6681>`__
-  `MAX6689: 7-Channel Precision Temperature Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6689 <https://www.maximintegrated.com/MAX6689>`__
-  `MAX6692: Precision SMBus-Compatible Remote/Local Temperature Sensors with Overtemperature Alarms <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6692 <https://www.maximintegrated.com/MAX6692>`__
-  `MAX6693: 7-Channel Precision Temperature Monitor with Beta Compensation <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6693 <https://www.maximintegrated.com/MAX6693>`__
-  `MAX6694: 5-Channel Precision Temperature Monitor with Beta Compensation <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6694 <https://www.maximintegrated.com/MAX6694>`__
-  `MAX6695: Dual Remote/Local Temperature Sensors with SMBus Serial Interfaces <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6695 <https://www.maximintegrated.com/MAX6695>`__
-  `MAX6696: Dual Remote/Local Temperature Sensors with SMBus Serial Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/lm90.c>`__ `MAX6696 <https://www.maximintegrated.com/MAX6696>`__
-  `MAX6697: 7-Channel Precision Temperature Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6697 <https://www.maximintegrated.com/MAX6697>`__
-  `MAX6698: 5-Channel Precision Temperature Monitor with Beta Compensation <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6698 <https://www.maximintegrated.com/MAX6698>`__
-  `MAX6699: 7-Channel Precision Remote-Diode, Thermistor, and Local Temperature Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6697.c>`__ `MAX6699 <https://www.maximintegrated.com/MAX6699>`__
-  `MAX6874: EEPROM-Programmable, Hex/Quad, Power-Supply Sequencers/Supervisors <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/misc/eeprom/max6875.c>`__ `MAX6874 <https://www.maximintegrated.com/MAX6874>`__
-  `MAX6875: EEPROM-Programmable, Hex/Quad, Power-Supply Sequencers/Supervisors <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/misc/eeprom/max6875.c>`__ `MAX6875 <https://www.maximintegrated.com/MAX6875>`__
-  `MAX6639: 2-Channel Temperature Monitor with Dual, Automatic, PWM Fan-Speed Controller <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/max6639.c>`__ `MAX6639 <https://www.maximintegrated.com/MAX6639>`__

PMbus
^^^^^

-  `ADM1075: −48 V Hot Swap Controller and Digital Power Monitor with PMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/adm1275.c>`__ :adi:`ADM1075`
-  `ADM1272: High Voltage Positive Hot Swap Controller and Digital Power Monitor with PMBus <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/adm1275.c>`__ :adi:`ADM1272`
-  `ADM1275: Hot Swap Controller and Digital Power Monitor with PMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/adm1275.c>`__ :adi:`ADM1275`
-  `ADM1276: Hot Swap Controller and Digital Power and Energy Monitoringwith PMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/adm1275.c>`__ :adi:`ADM1276`
-  `ADM1278: Hot Swap Controller and Digital Power and Energy Monitor with PMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/adm1275.c>`__ :adi:`ADM1278`
-  `ADM1293: Digital Power Monitor with PMbus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/adm1275.c>`__ :adi:`ADM1293`
-  `ADM1294: Digital Power Monitor with PMbus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/adm1275.c>`__ :adi:`ADM1294`
-  `ADP1050: Digital Controller for Isolated Power Supply with PMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/adp1050.c>`__ :adi:`ADP1050`
-  `LTC2972: 2-Channel PMBus Power System Manager Featuring Accurate Output Current Measurement <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC2972`
-  `LTC2974: 4-Channel PMBus Power System Manager Featuring Accurate Output Current Measurement <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC2974`
-  `LTC2975: 4-Channel PMBus Power System Manager Featuring Accurate Input Current and Energy Measurement <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC2975`
-  `LTC2977: 8-Channel PMBus Power System Manager Featuring Accurate Output Voltage Measurement <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC2977`
-  `LTC2978: Octal Digital Power Supply Manager with EEPROM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC2978`
-  `LTC2979: 16-Channel PMBus Low-Voltage Power System Manager <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC2979`
-  `LTC2980: 16-Channel PMBus Power System Manager <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC2980`
-  `LTC3815: 6A Monolithic Synchronous DC/DC Step-Down Converter with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc3815.c>`__ :adi:`LTC3815`
-  `LTC3880: Dual Output PolyPhase Step-Down DC/DC Controller with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC3880`
-  `LTC3882: Dual Output PolyPhase Step-Down DC/DC Voltage Mode Controller with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC3882`
-  `LTC3883: Single Phase Step-Down DC/DC Controller with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC3883`
-  `LTC3884: Dual Output PolyPhase Step-Down Controller with Sub-Milliohm DCR Sensing and Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC3884`
-  `LTC3886: 60V Dual Output Step-Down Controller with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC3886`
-  `LTC3887: Dual Output PolyPhase Step-Down DC/DC Controller with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC3887`
-  `LTC3889: 60V Dual Output Step-Down Controller with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC3889`
-  `LTC7880: 60V Dual Output Step-Up Controller with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTC7880`
-  `LTM2987: 16-Channel μModule PMBus Power System Manager <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM2987`
-  `LTM4644: Quad DC/DC μModule (Power Module) Regulator with Configurable 4A Output Array <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM4644`
-  `LTM4664: 54VIN Dual 25A, Single 50A µModule Regulator with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM4664`
-  `LTM4675: Dual 9A or Single 18A μModule Regulator with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM4675`
-  `LTM4676A: Dual 13A or Single 26A μModule (Power Module) Regulator with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM4676A`
-  `LTM4676: Dual 13A or Single 26A μModule (Power Module) Regulator with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`Obsolete <LTM4676>`
-  `LTM4677: Dual 18A or Single 36A μModule (Power Module) Regulator with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM4677`
-  `LTM4678: Dual 25A or Single 50A µModule Regulator with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM4678`
-  `LTM4680: Dual 30A or Single 60A µModule Regulator with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM4680`
-  `LTM4686: Ultrathin Dual 10A or Single 20A μModule Regulator with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM4686`
-  `LTM4700: Dual 50A or Single 100A µModule Regulator with Digital Power System Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/ltc2978.c>`__ :adi:`LTM4700`
-  `MAX15301: InTune Automatically Compensated Digital PoL Controller with Driver and PMBus Telemetry <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max15301.c>`__ `MAX15301 <https://www.maximintegrated.com/MAX15301>`__
-  `MAX16064: Quad, Power-Supply Controller with Active-Voltage Output Control and PMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max16064.c>`__ `MAX16064 <https://www.maximintegrated.com/MAX16064>`__
-  `MAX20710: Integrated, Step-Down Switching Regulator with PMBus <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max20730.c>`__ `MAX20710 <https://www.maximintegrated.com/MAX20710>`__
-  `MAX20730: Integrated, Step-Down Switching Regulator with PMBus <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max20730.c>`__ `MAX20730 <https://www.maximintegrated.com/MAX20730>`__
-  `MAX20734: Integrated, Step-Down Switching Regulator with PMBus <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max20730.c>`__ `MAX20734 <https://www.maximintegrated.com/MAX20734>`__
-  `MAX20743: Integrated, Step-Down Switching Regulator with PMBus <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max20730.c>`__ `MAX20743 <https://www.maximintegrated.com/MAX20743>`__
-  `MAX20751: Multiphase Master with PMBus Interface and Internal Buck Converter <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max20751.c>`__ `MAX20751 <https://www.maximintegrated.com/MAX20751>`__
-  `MAX20796: Dual-Phase Scalable Integrated Voltage Regulator with PMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/pmbus.c>`__ `MAX20796 <https://www.maximintegrated.com/MAX20796>`__
-  `MAX31785: 6-Channel Intelligent Fan Controller <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max31785.c>`__ `MAX31785 <https://www.maximintegrated.com/MAX31785>`__
-  `MAX34440: PMBus 6-Channel Power-Supply Manager <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max34440.c>`__ `MAX34440 <https://www.maximintegrated.com/MAX34440>`__
-  `MAX34441: PMBus 5-Channel Power-Supply Manager and Intelligent Fan Controller <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max34440.c>`__ `MAX34441 <https://www.maximintegrated.com/MAX34441>`__
-  `MAX34446: PMBus Power-Supply Data Logger <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max34440.c>`__ `MAX34446 <https://www.maximintegrated.com/MAX34446>`__
-  `MAX34451: PMBus 16-Channel V/I Monitor and 12-Channel Sequencer/Marginer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max34440.c>`__ `MAX34451 <https://www.maximintegrated.com/MAX34451>`__
-  `MAX34460: PMBus 12-Channel Voltage Monitor and Sequencer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max34440.c>`__ `MAX34460 <https://www.maximintegrated.com/MAX34460>`__
-  `MAX34461: PMBus 16-Channel Voltage Monitor and Sequencer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max34440.c>`__ `MAX34461 <https://www.maximintegrated.com/MAX34461>`__
-  `MAX8688: Digital Power-Supply Controller/Monitor with PMBus Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/hwmon/pmbus/max8688.c>`__ `MAX8688 <https://www.maximintegrated.com/MAX8688>`__

Ethernet PHY
~~~~~~~~~~~~

-  :doc:`ADIN1100 - Robust, Industrial, Low Power 10BASE-T1L Ethernet PHY </wiki-migration/resources/tools-software/linux-drivers/net-phy/adin1100>`
-  :doc:`ADIN1200 - Robust, Industrial, Low Power 10/100 Ethernet PHY </wiki-migration/resources/tools-software/linux-drivers/net-phy/adin>`
-  :doc:`ADIN1300 - Robust, Industrial, Low Latency 10/100/1000 Gigabit Ethernet PHY </wiki-migration/resources/tools-software/linux-drivers/net-phy/adin>`

Ethernet MAC-PHY
~~~~~~~~~~~~~~~~

-  :doc:`ADIN1110 - Robust, Industrial, Low Power 10BASE-T1L Ethernet MAC-PHY </wiki-migration/resources/tools-software/linux-drivers/net-mac-phy/adin1110>`
-  :doc:`ADIN2111 - Low Complexity, 2-Port Ethernet Switch with Integrated 10BASE-T1L PHYs </wiki-migration/resources/tools-software/linux-drivers/net-mac-phy/adin2111>`
-  :doc:`Open Alliance - 10BASE-T1x MAC-PHY Serial Interface </wiki-migration/resources/tools-software/linux-drivers/net-mac-phy/open_alliance>`

I2C Mux
~~~~~~~

-  `LTC4306: 4-Channel, 2-Wire Bus Multiplexer with Capacitance Buffering <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/i2c/muxes/i2c-mux-ltc4306.c>`__ :adi:`LTC4306`
-  `LTC4305: 2-Channel, 2-Wire Bus Multiplexer with Capacitance Buffering <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/i2c/muxes/i2c-mux-ltc4306.c>`__ :adi:`LTC4305`
-  `MAX9286: Quad 1.5Gbps GMSL Deserializer with Coax or STP Input and CSI-2 Output <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/max9286.c>`__ `MAX9286 <https://www.maximintegrated.com/MAX9286>`__
-  `MAX9271: 16-Bit GMSL Serializer with Coax or STP Cable Drive <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/max9271.c>`__ `MAX9271 <https://www.maximintegrated.com/MAX9271>`__

IIO - Accelerometers
~~~~~~~~~~~~~~~~~~~~

-  :doc:`ADXL312, ADXL313, ADXL314: Low Noise, Low Drift, Low Power, 3-Axis MEMS Accelerometers </wiki-migration/resources/tools-software/linux-drivers/iio-accelerometer/adxl313>`
-  :doc:`ADXL345: 3-Axis, ±2 g/±4 g/±8 g/±16 g Digital Accelerometer </wiki-migration/resources/tools-software/linux-drivers/input-misc/adxl345>`
-  :doc:`ADXL346: 3-Axis, ±2 g/±4 g/±8 g/±16 g Ultralow Power Digital Accelerometer </wiki-migration/resources/tools-software/linux-drivers/input-misc/adxl345>`
-  :doc:`ADXL355: Low Noise, Low Drift, Low Power, 3-Axis MEMS Accelerometers </wiki-migration/resources/tools-software/linux-drivers/iio-accelerometer/adxl355>`
-  :doc:`ADXL362: Micropower 3-Axis MEMS Accelerometer, Programmable Digital Output, ±2/±4/±8 g Range </wiki-migration/resources/tools-software/linux-drivers/input-misc/adxl362>`
-  :doc:`ADXL367: Micropower 3-Axis MEMS Accelerometer, Programmable Digital Output, ±2 g/±4 g/±8 g Range </wiki-migration/resources/tools-software/linux-drivers/iio-accelerometer/adxl367>`
-  :doc:`ADXL372: Micropower 3-Axis MEMS Accelerometer, Programmable Digital Output, ±200 g Range </wiki-migration/resources/tools-software/linux-drivers/iio-accelerometer/adxl372>`
-  :doc:`ADXL375: 3-Axis, ±200 g Digital Accelerometer </wiki-migration/resources/tools-software/linux-drivers/input-misc/adxl345>`
-  :doc:`ADIS16201: Programmable Dual-Axis Inclinometer / Accelerometer </wiki-migration/resources/tools-software/linux-drivers/iio-accelerometer/adis16201>`
-  :doc:`ADIS16203: Programmable 360° Inclinometer </wiki-migration/resources/tools-software/linux-drivers/iio-accelerometer/adis16203>`
-  :doc:`ADIS16209: High Accuracy, Dual-Axis Digital Inclinometer and Accelerometer </wiki-migration/resources/tools-software/linux-drivers/iio-accelerometer/adis16209>`
-  :doc:`ADIS16240: Low Power Programmable Impact Sensor and Recorder </wiki-migration/resources/tools-software/linux-drivers/iio-accelerometer/adis16240>`

IIO - Amplifiers
~~~~~~~~~~~~~~~~

-  :doc:`AD8366: DC to 600 MHz, Dual-Digital Variable Gain Amplifiers </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`ADA4961: Low Distortion, 3.2 GHz, RF DGA </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`ADL5240: 100 MHz TO 4000 MHz RF/IF Digitally Controlled VGA </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`ADRF5720: 0.5 dB LSB, 6-Bit, Silicon Digital Attenuator, 9 kHz to 40 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`ADRF5730: 0.5 dB LSB, 6-Bit, Silicon Digital Attenuator, 100 MHz to 40 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`ADRF5731: 2 dB LSB, 4-Bit, Silicon Digital Attenuator, 100 MHz to 40 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`HMC271A: 1dB LSB 5-Bit Digital Attenuator SMT, 0.7 - 3.7 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`ADA4250 Programmable Gain Instrumentation Amplifier Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ada4250>`
-  :doc:`HMC425: 0.5 dB LSB, GaAs MMIC, 6-BIT DIGITAL POSITIVE CONTROL ATTENUATOR, 2.2 - 8.0 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/hmc425a>` :adi:`Obsolete <HMC425>`
-  :doc:`HMC425A: 0.5 dB LSB, GaAs MMIC, 6-BIT DIGITAL POSITIVE CONTROL ATTENUATOR, 2.2 - 8.0 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/hmc425a>` :adi:`HMC425A`
-  :doc:`HMC540S: 1 dB LSB Silicon MMIC 4-Bit Digital Positive Control Attenuator 0.1 - 8 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/hmc425a>`
-  :doc:`HMC1018A: 1.0 dB LSB GaAs MMIC 5-BIT DIGITAL ATTENUATOR, 0.1 - 30 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`HMC1019A: 0.5 dB LSB GaAs MMIC 5-BIT DIGITAL ATTENUATOR, 0.1 - 30 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`HMC1119: 0.25 dB LSB, 7-Bit, Silicon Digital Attenuator, 0.1 GHz to 6.0 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`

IIO - Analog to Digital Converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD4000: 16-Bit, 2 MSPS, Pseudo Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4001: 16-Bit, 2 MSPS, Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4002: 18-Bit, 2 MSPS, Pseudo Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4003: 18-Bit, 2 MSPS, Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4004: 16-Bit, 1 MSPS, Pseudo Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4005: 16-Bit, 1 MSPS, Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4006: 18-Bit, 1 MSPS, Pseudo Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4007: 18-Bit, 1 MSPS, Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4008: 16-Bit, 500 kSPS, Pseudo Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4010: 18-Bit, 500 kSPS, Pseudo Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4011: 18-Bit, 500 kSPS, Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4020: 20-bit, 1.8 MSPS, Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4021: 20-bit, 1 MSPS, Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4022: 20-bit, 500 kSPS, Differential SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`AD4030-24: 24-Bit, 2 MSPS/500 kSPS, SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad4630>`
-  :doc:`AD4111: Single Supply, 24-Bit, Sigma-Delta ADC with ±10 V and 0 mA to 20 mA Inputs, Open Wire Detection </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD4112: Single Supply, 24-Bit, Sigma-Delta ADC with ±10 V and 0 mA to 20 mA Inputs </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD4114: Single Supply, Multichannel, 31.25 kSPS, 24-Bit, Sigma-Delta ADC with ±10 V Inputs </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD4115: Single-Supply, Multichannel, 125 kSPS, 24-Bit, Sigma-Delta ADC with ±10 V Inputs </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD4116: Single Supply, 24-Bit, Sigma-Delta ADC with ±10 V, 10 MΩ Inputs and Buffered Low Level Inputs </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  `AD4130: 32 μA, Ultra Low Power, 24-Bit Sigma-Delta ADC with Integrated PGA and FIFO <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad4130.c>`__ :adi:`AD4130`
-  :doc:`AD4630-16: 24-Bit, 2 MSPS/500 kSPS, Dual Channel SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad4630>`
-  :doc:`AD4630-24: 24-Bit, 2 MSPS/500 kSPS, Dual Channel SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad4630>`
-  :doc:`AD4695: 16-Bit, 16-Channel, 500 kSPS, Easy Drive Multiplexed SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad4695>`
-  :doc:`AD4696: 16-Bit, 16-Channel, 1 MSPS, Easy Drive Multiplexed SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad4695>`
-  :doc:`AD4697: 16-Bit, 8-Channel, 500 kSPS, Easy Drive Multiplexed SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad4695>`
-  :doc:`AD4698: 16-Bit, 8-Channel, 1 MSPS, Easy Drive Multiplexed SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad4695>`
-  :doc:`AD6684: 135 MHz Quad IF Receiver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9208>`
-  :doc:`AD6688: RF Diversity and 1.2GHz BW Observation Receiver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9208>`
-  :doc:`AD7091: 1 MSPS, Ultralow Power 12-Bit ADC in 8-Lead LFCSP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7091R: 1 MSPS, ultra low power 12-Bit ADC in 10 LEAD LFCSP and MSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7091R-5: 4-Channel, 12-bit Ultra Low Power ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7091r5>`
-  :doc:`AD7091R-8: 8-Channel, 12-bit Ultra Low Power ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7091r8>`
-  :doc:`AD7124: 24-Bit Low Power Sigma-Delta ADC with PGA and Reference </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7124>`
-  :doc:`AD7124-4: 4-Channel, Low Noise, Low Power, 24-Bit, Sigma-Delta ADC with PGA and Reference </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7124>`
-  :doc:`AD7124-8: 8-Channel, Low Noise, Low Power, 24-Bit, Sigma-Delta ADC with PGA and Reference </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7124>`
-  :doc:`AD7170: 12-Bit Low Power Sigma-Delta ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7780>`
-  :doc:`AD7171: 16-Bit Low Power Sigma-Delta ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7780>`
-  :doc:`AD7172-2: Low Power, 24-Bit, 31.25 kSPS, Sigma-Delta ADC with True Rail-to-Rail Buffers </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD7172-4: Low Power, 4-/8-channel, 31.25 kSPS, 24-bit, Sigma-Delta ADC with True Rail-to-Rail Buffers </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD7173-8: Low Power, 8-/16-Channel, 31.25 kSPS, 24-Bit, Highly Integrated Sigma-Delta ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD7175-2: 24-Bit, 250 kSPS, Sigma-Delta ADC with 20 µs Settling and True Rail-to-Rail Buffers </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD7175-8: 24-Bit, 8-/16-Channel, 250 kSPS, Sigma-Delta ADC with True Rail-to-Rail Buffers </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD7176-2: 24-Bit, 250 kSPS Sigma Delta ADC with 20 µs Settling </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD7177-2: 32-Bit, 10 kSPS, Sigma-Delta ADC with 100 µs Settling and True Rail-to-Rail Buffers </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7173>`
-  :doc:`AD7190: 4.8 kHz Ultra-Low Noise 24-Bit Sigma-Delta ADC with PGA </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7192>`
-  :doc:`AD7192: 4.8 kHz Ultra-Low Noise 24-Bit Sigma-Delta ADC with PGA </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7192>`
-  :doc:`AD7193: 4-Channel, 4.8 kHz Ultra-Low Noise 24-Bit Sigma-Delta ADC with PGA </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7192>`
-  :doc:`AD7194: 8-Channel, 4.8 kHz, Ultralow Noise, 24-Bit Sigma-Delta ADC with PGA </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7192>`
-  :doc:`AD7195: 4.8 kHz, Ultralow Noise, 24-Bit Sigma-Delta ADC with PGA and AC Excitation </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7192>`
-  :doc:`AD7265: Differential/Single-Ended Input, Dual 1 MSPS, 12-Bit, 3-Channel SAR A/D Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7266>`
-  :doc:`AD7266: Differential/Single-Ended Input, Dual, Simultaneous Sampling, 2 MSPS, 12-Bit, 3-Channel SAR A/D Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7266>`
-  :doc:`AD7273: 3 MSPS 10-Bit ADC in TSOT and MSOP Packages </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7274: 3 MSPS 12-Bit A/D Converter in TSOT and MSOP Packages </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7276: 3 MSPS 12-Bit ADC in 8-Lead MSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7277: 3 MSPS 10-Bit ADC in 8-Lead MSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7278: 3 MSPS 8-Bit ADC in 8-Lead MSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7280A: Lithium Ion Battery Monitoring System </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7280a>`
-  :doc:`AD7291: 8-Channel, I2C, 12-Bit SAR ADC with Temperature Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7291>`
-  `AD7292: 10-Bit Monitor & Control System with ADC, DACs, Temperature Sensor and GPIOs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7292.c>`__ :adi:`AD7292`
-  :doc:`AD7298: 8-Channel, 1MSPS, 12-Bit SAR ADC with Temperature Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7298>`
-  :doc:`AD7380: 4 MSPS Dual Simultaneous Sampling, 16-BIT SAR ADC, Differential Input </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7381: 4 MSPS Dual Simultaneous Sampling, 14-BIT SAR ADC, Differential Input </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7383: 4 MSPS Dual Simultaneous Sampling, 16-BIT SAR ADC, Pseudo Differential Input </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7384: 4 MSPS Dual Simultaneous Sampling, 14-BIT SAR ADC, Pseudo Differential Input </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7386: 4-Channel, 4 MSPS, 16-Bit Dual Simultaneous Sampling SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7387: 4-Channel, 4 MSPS, 14-Bit, Dual, Simultaneous Sampling SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7388: 4-Channel, 4 MSPS, 12-Bit, Dual, Simultaneous Sampling SAR ADCs </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7380-4: Differential Input, Quad, External Reference Simultaneous Sampling, 16-BIT, SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7381-4: Differential Input, Quad, 14-Bit, Simultaneous Sampling, SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7383-4: Pseudo Differential Input, Quad, 4 MSPS Simultaneous Sampling, 16-Bit, SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7384-4: Pseudo Differential Input, Quad, 4 MSPS Simultaneous Sampling, 14-Bit, SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7386-4: Single-Ended Input, Quad, Simultaneous Sampling, 16-Bit, SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7387-4: Single-Ended Input, Quad, Simultaneous Sampling, 14-Bit, SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7388-4: Single-Ended Input, Quad, Simultaneous Sampling, 12-Bit, SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7389-4: Differential Input, Quad, Internal Reference, Simultaneous Sampling, 16-Bit SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`AD7466: 1.6 V Micro-Power 12-Bit ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7467: 1.6 V Micro-Power 10-Bit ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7468: 1.6 V Micro-Power 8-Bit ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7475: 1 MSPS, 12-Bit A/D Converter in MSOP-8 or SOIC-8 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7476: 1MSPS, 12-Bit ADC in 6 Lead SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7476A: 12-Bit, 1 MSPS, Low-Power A/D Converter in SC70 and MSOP Packages </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7477: 1MSPS, 10-Bit ADC in 6 Lead SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7477A: 10-Bit, 1 MSPS, Low-Power A/D Converter in SC70 and MSOP Packages </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7478: 8-Bit, 1 MSPS, Low Power Successive Approximation ADC Which Operates From A Single 2.35 V to 5.25 V Power Supply </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7478A: 8-Bit, 1 MSPS, Low-Power A/D Converter in SC70 and MSOP Packages </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7495: 1 MSPS, 12-Bit A/D Converter in MSOP-8 or SOIC-8 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7605-4: 4-Channel DAS with 16-Bit, Bipolar, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7606-4: 4-Channel DAS with 16-Bit, Bipolar, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7606-6: 6-Channel DAS with 16-Bit, Bipolar, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7606: 8-Channel DAS with 16-Bit, Bipolar, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7606B: 8-Channel DAS with 16-Bit, 800 kSPS Bipolar Input, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7606C-16: 8-Channel DAS with 16-Bit, 1 MSPS Bipolar Input, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7606C-18: 8-Channel DAS with 18-Bit, 1 MSPS Bipolar Input, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7607: 8-Channel DAS with 14-Bit, 200 kSPS Bipolar Input, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7608: 8-Channel DAS with 18-Bit, 200 kSPS Bipolar Input, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7609: 8-Channel Differential DAS with 18-Bit, 200 kSPS Bipolar Input, Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7616: 16-Channel DAS with 16-Bit, Bipolar Input, Dual Simultaneous Sampling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7606>`
-  :doc:`AD7625: 16-Bit, 6 MSPS PulSAR Differential ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7625>`
-  :doc:`AD7626: 16-Bit, 10 MSPS, PulSAR Differential ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7625>`
-  :doc:`AD7680: 3 mW, 100 kSPS, 16-Bit ADC in 6 Lead SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7682: 16-Bit, 4-Channel, 250 kSPS PulSAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7683: 100 kSPS 16-Bit PulSAR® A/D Converter in µSOIC/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7684: 16-Bit, 100 kSPS PulSAR®, Differential ADC in MSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7685: 16-Bit, 250 kSPS PulSAR® ADC in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7686: 500 kSPS 16-BIT PulSAR® A/D Converter in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7687: 16-Bit, 1.5 LSB INL, 250 kSPS PulSAR® Differential ADC in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7688: 500 kSPS 16- BIT Differential PulSAR® A/D Converter in µSOIC/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  `AD7689: 16-Bit, 8-Channel, 250 kSPS PulSAR® ADC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7949.c>`__ :adi:`AD7689`
-  :doc:`AD7690: 18-Bit, 1.5 LSB INL, 400 kSPS PulSAR® Differential ADC in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7691: 18-Bit, 1.5 LSB INL, 250 kSPS PulSAR® Differential ADC in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7693: 16-Bit, ±0.5 LSB, 500 kSPS PulSAR® Differential A/D Converter in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7694: 250 kSPS 16-BIT PulSAR® A/D Converter in µSOIC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7766-1: 24-Bit, 8.5 mW, 109 dB, 64 kSPS ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7766>`
-  :doc:`AD7766-2: 24-Bit, 8.5 mW, 109 dB, 32 kSPS ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7766>`
-  :doc:`AD7766: 24-Bit, 8.5 mW, 109 dB, 128 kSPS ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7766>`
-  :doc:`AD7767-1: 24-Bit, 8.5 mW, 109 dB, 64 kSPS ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7766>`
-  :doc:`AD7767-2: 24-Bit, 8.5 mW, 109 dB, 32 kSPS ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7766>`
-  :doc:`AD7767: 24-Bit, 8.5 mW, 109 dB, 128 kSPS ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7766>`
-  :doc:`AD7768-1: 24-Bit, Power Scaling, Sigma-Delta ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7768-1>`
-  :doc:`AD7768: 24-Bit, Simultaneous Sampling, Power Scaling ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7768>`
-  :doc:`AD7780: 24-Bit Pin-Programmable Low Power Sigma-Delta ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7780>`
-  :doc:`AD7781: 20-Bit, Pin-Programmable, Ultralow Power Sigma-Delta ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7780>`
-  :doc:`AD7785: 3-Channel, Low Noise, Low Power, 20-Bit Σ-Δ ADC with On-Chip In-Amp and Reference </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7793>`
-  :doc:`AD7787: Low Power, 2-Channel 24-Bit Sigma-Delta ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7791>`
-  :doc:`AD7788: 16-Bit, Single-Channel, Ultra Low Power, Sigma-Delta A/D Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7791>`
-  :doc:`AD7789: 24-Bit, Single-Channel, Ultra Low Power, Sigma-Delta A/D Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7791>`
-  :doc:`AD7790: 16-Bit, Single-Channel, Ultra Low Power, Sigma-Delta A/D Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7791>`
-  :doc:`AD7791: 24-Bit, Single-Channel, Ultra Low Power, Sigma-Delta A/D Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7791>`
-  :doc:`AD7792: 3-Channel, Low Noise, Low Power, 16-Bit Sigma Delta ADC with On-Chip In-Amp and Reference </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7793>`
-  :doc:`AD7793: 3-Channel, Low Noise, Low Power, 24-Bit Sigma Delta ADC with On-Chip In-Amp and Reference </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7793>`
-  :doc:`AD7794: 6-Channel, Low Noise, Low Power, 24-Bit Sigma Delta ADC with On-Chip In-Amp and Reference </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7793>`
-  :doc:`AD7795: 6-Channel, Low Noise, Low Power, 16-Bit Sigma Delta ADC with On-Chip In-Amp and Reference </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7793>`
-  :doc:`AD7796: Low Power 16-Bit Sigma-Delta A/D Converter for Bridge Sensors </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7793>`
-  :doc:`AD7797: Low Power 24-Bit Sigma-Delta A/D Converter for Bridge Sensors </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7793>`
-  :doc:`AD7798: 3-Channel, Low Noise, Low Power, 16-Bit, Sigma Delta ADC with On-Chip In-Amp </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7793>`
-  :doc:`AD7799: 3-Channel, Low Noise, Low Power, 24-Bit, Sigma Delta ADC with On-Chip In-Amp </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7793>`
-  `AD7816:Temperature Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/staging/iio/adc/ad7816.c>`__ :adi:`Obsolete <AD7816>`
-  `AD7817:Temperature Sensor (On Chip) 4-Channel, 9 µs, 10-Bit ADC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/staging/iio/adc/ad7816.c>`__ :adi:`AD7817`
-  `AD7818:Temperature Sensor (On Chip) 1-Channel, 9 µs, 10-Bit ADC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/staging/iio/adc/ad7816.c>`__ :adi:`AD7818`
-  :doc:`AD7887: 2.7 V to 5.25 V, Micropower, 2-Channel, 125 kSPS, 12-Bit ADC in 8-Lead MSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7887>`
-  `AD7904: 4-Channel, 1 MSPS, 8-Bit A/D Converter with Sequencer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7923.c>`__ :adi:`AD7904`
-  `AD7908: 8-Channel, 1 MSPS, 8-Bit ADC with Sequencer in 20-Lead TSSOP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7923.c>`__ :adi:`AD7908`
-  :doc:`AD7910: 250 KSPS, 10-Bit ADC in 6 Lead SC70 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  `AD7914: 4-Channel, 1 MSPS, 10-Bit A/D Converter with Sequencer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7923.c>`__ :adi:`AD7914`
-  `AD7918: 8-Channel, 1 MSPS, 10-Bit ADC with Sequencer in 20-Lead TSSOP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7923.c>`__ :adi:`AD7918`
-  :doc:`AD7920: 250 KSPS, 12-Bit ADC in 6 Lead SC70 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  `AD7923: 4-Channel 200 kSPS, 12-Bit A/D Converter with Sequencer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7923.c>`__ :adi:`AD7923`
-  `AD7924: 4-Channel, 1 MSPS, 12-Bit A/D Converter with Sequencer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7923.c>`__ :adi:`AD7924`
-  `AD7928: 8-Channel, 1 MSPS, 12-Bit A/D Converter with Sequencer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7923.c>`__ :adi:`AD7928`
-  :doc:`AD7940: AD7940: 3 MW, 100 KSPS, 14-Bit ADC in 6-Lead SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7942: 14-Bit, 250 kSPS PulSAR®, Pseudo Differential ADC in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7944: 14-Bit, 2.5 MSPS, PulSAR 15.5 mW ADC in LFCSP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7944>` :adi:`AD7944`
-  :doc:`AD7946: 14-Bit, 500 kSPS PulSAR® ADC in MSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  `AD7949: 14-Bit, 8-Channel, 250 kSPS PulSAR ADC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ad7949.c>`__ :adi:`AD7949`
-  :doc:`AD7960: 18-Bit, 5 MSPS PULSAR® Differential ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7625>`
-  :doc:`AD7961: 16-Bit, 5 MSPS PULSAR® Differential ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7625>`
-  :doc:`AD7980: 16-Bit, 1 MSPS PulSAR® ADC in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7982: 18-Bit, 1 MSPS PulSAR® 7.0 mW ADC in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7984: 18-Bit, 1.33 MSPS PulSAR® 10.5 mW ADC in MSOP/QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7985: 16-Bit, 2.5 MSPS PulSAR 11 mW ADC in QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7944>` :adi:`AD7985`
-  :doc:`AD7986: 14-Bit, 18-Bit, 2 MSPS PulSAR 15 mW ADC in QFN </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7944>` :adi:`AD7986`
-  :doc:`AD7988-1: 16-Bit, 100 kSPS, Ultra Low Power 16-Bit SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7988-5: 16-Bit, 500 kSPS, Ultra Low Power 16-Bit SAR ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>`
-  :doc:`AD7991: 4-Channel, 12-Bit ADC with I2C Compatible Interface in 8-Lead SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7998>`
-  :doc:`AD7992: 2-Channel, 12-Bit ADC with I2C Compatible Interface in 10-Lead MSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7998>`
-  :doc:`AD7993: 4-Channel, 10-Bit ADC with I2C Compatible Interface in 16-Lead TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7998>`
-  :doc:`AD7994: 4 Channel, 12-Bit ADC with I2C Compatible Interface in 16-Lead TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7998>`
-  :doc:`AD7995: 4-Channel, 10-Bit ADC with I2C Compatible Interface in 8-Lead SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7998>`
-  :doc:`AD7997: 8-Channel, 10-Bit ADC with I2C Compatible Interface in 20-Lead TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7998>`
-  :doc:`AD7998: 8-Channel, 12-Bit ADC with I2C Compatible Interface in 20-Lead TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7998>`
-  :doc:`AD7999: 4-Channel, 8-Bit ADC with I2C Compatible Interface in 8-Lead SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7998>`
-  :doc:`AD9083 16-Channel, 125 MHz Bandwidth, JESD204B Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9083>`
-  :doc:`AD9207 12-Bit, 6 GSPS, JESD204B/JESD204C Dual ADC </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  :doc:`AD9208: 14-Bit, 3GSPS, JESD204B, Dual Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9208>`
-  :doc:`AD9209 12-Bit, 4GSPS, JESD204B/C, Quad Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  :doc:`AD9234: 12-Bit, 1 GSPS JESD204B, Dual Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9250: 14-Bit, 170 MSPS/250 MSPS, JESD204B, Dual Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9265: 16-Bit, 125 MSPS/105 MSPS/80 MSPS, 1.8 V Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9434: 12-BIT, 370 MSPS/500 MSPS, 1.8 V ANALOG-TO-DIGITAL CONVERTER </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9467: 16-Bit, 200 MSPS/250 MSPS Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9625: 12-BIT, 2.0/2.5 GSPS, 1.3 V/2.5 V ANALOG-TO-DIGITAL CONVERTER </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9643: 14-Bit, 170/210/250 MSPS, 1.8 V Dual Analog-to-Digital Converter (ADC) </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9649: 14-Bit, 20/40/65/80 MSPS, 1.8 V Analog-to-Digital Converter (ADC) </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9652: 16-bit, 310 MSPS, 3.3/1.8 V Dual Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9680: 14-Bit, 1000 MSPS JESD204B, Dual Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9683: 14-BIT, 170 MSPS/250 MSPS, JESD204B, ANALOG-TO-DIGITAL CONVERTER </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9684: 14-Bit, 500 MSPS LVDS, Dual Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9689: 14-Bit, 2.0 GSPS/2.6 GSPS, JESD204B, Dual Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9208>`
-  :doc:`AD9694: Quad 14-Bit, 500 MSPS, 1.2 V/2.5 V Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9208>`
-  :doc:`AD9695: 14-Bit, 1300 MSPS/625 MSPS, JESD204B, Dual Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9208>`
-  :doc:`AD9697: 14-Bit, 1300 MSPS, JESD204B, Analog-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9208>`
-  :doc:`ADAQ4003: 18-Bit 2 MSPS μModule Data Acquisition System in BGA </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad400x>`
-  :doc:`ADAQ4224: 24-Bit, 2 MSPS μModule Data Acquisition Solution </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad4630>`
-  :doc:`ADAQ4370-4: Quad, 16-Bit, 2 MSPS, Simultaneous Sampling, μModule Data-Acquisition Solution </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`ADAQ4380-4: Quad, 16-Bit, 4 MSPS, Simultaneous Sampling, μModule Data Acquisition Solution </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`ADAQ4381-4: Quad, 14-Bit, 4 MSPS, Simultaneous Sampling, μModule Data Acquisition Solution </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad738x>`
-  :doc:`ADAQ8092: 14-Bit, 105 MSPS, μModule </wiki-migration/resources/tools-software/linux-drivers/iio-adc/adaq8092>`
-  :doc:`ADAS1000: Low Power, 5-ELECTRODE ELECTROCARDIOGRAM (ECG) ANALOG FRONT END (AFE) </wiki-migration/resources/tools-software/linux-drivers/iio-adc/adas1000>`
-  `ADT7516: SPI/I2C Compatible,Temperature Sensor, 4-Channel ADC and Quad Voltage Output <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/staging/iio/addac/adt7316.c>`__ :adi:`ADT7516`
-  `ADT7517: SPI-/I2C-Compatible, Temperature Sensor, 4-Channel ADC and Quad Voltage Output <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/staging/iio/addac/adt7316.c>`__ :adi:`ADT7517`
-  `ADT7519: SPI-/I2C-Compatible, Temperature Sensor, 4-Channel ADC and Quad Voltage Output <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/staging/iio/addac/adt7316.c>`__ :adi:`Obsolete <ADT7519>`
-  :doc:`LTC2314-14: 14-Bit, 4.5Msps Serial Sampling ADC in TSOT </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7476a>` :adi:`LTC2314-14`
-  `LTC2471: Selectable 208sps/833sps, 16-Bit I2C ΔΣ ADCs with 10ppm/°C Max Precision Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ltc2471.c>`__ :adi:`LTC2471`
-  `LTC2473: Selectable 208sps/833sps, 16-Bit I2C ΔΣ ADCs with 10ppm/°C Max Precision Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ltc2471.c>`__ :adi:`LTC2473`
-  `LTC2485: 24-Bit ΔΣ ADC with Easy Drive Input Current Cancellation and I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ltc2485.c>`__ :adi:`LTC2485`
-  `LTC2488: 16-Bit 2-/4-Channel ΔΣ ADC with Easy Drive Input Current Cancellation <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/spi/spidev.c>`__ :adi:`LTC2488`
-  `LTC2496: 16-Bit 8-/16-Channel ΔΣ ADC with Easy Drive Input Current Cancellation <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ltc2497.c>`__ :adi:`LTC2496`
-  `LTC2497: 16-Bit 8-/16-Channel ΔΣ ADC with Easy Drive Input Current Cancellation and I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ltc2497.c>`__ :adi:`LTC2497`
-  `LTC2499: 24-Bit 8-/16-Channel ΔΣ ADC with Easy Drive Input Current Cancellation and I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/ltc2497.c>`__ :adi:`LTC2499`
-  `MAX1027: 10-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1027.c>`__ `MAX1027 <https://www.maximintegrated.com/MAX1027>`__
-  `MAX1029: 10-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1027.c>`__ `MAX1029 <https://www.maximintegrated.com/MAX1029>`__
-  `MAX1031: 10-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1027.c>`__ `MAX1031 <https://www.maximintegrated.com/MAX1031>`__
-  `MAX1036: 2.7V to 5.5V, Low-Power, 4-/12-Channel 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1036 <https://www.maximintegrated.com/MAX1036>`__
-  `MAX1037: 2.7V to 5.5V, Low-Power, 4-/12-Channel 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1037 <https://www.maximintegrated.com/MAX1037>`__
-  `MAX1038: 2.7V to 5.5V, Low-Power, 4-/12-Channel 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1038 <https://www.maximintegrated.com/MAX1038>`__
-  `MAX1039: 2.7V to 5.5V, Low-Power, 4-/12-Channel 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1039 <https://www.maximintegrated.com/MAX1039>`__
-  `MAX11100: 16-Bit, +5V, 200ksps ADC with 10µA Shutdown <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max11100.c>`__ `MAX11100 <https://www.maximintegrated.com/MAX11100>`__
-  `MAX1117: Single-Supply, Low-Power, 2-Channel, Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1118.c>`__ `MAX1117 <https://www.maximintegrated.com/MAX1117>`__
-  `MAX1118: Single-Supply, Low-Power, 2-Channel, Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1118.c>`__ `MAX1118 <https://www.maximintegrated.com/MAX1118>`__
-  `MAX1119: Single-Supply, Low-Power, 2-Channel, Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1118.c>`__ `MAX1119 <https://www.maximintegrated.com/MAX1119>`__
-  :doc:`MAX11205 16-Bit, Single-Channel, Ultra-Low Power, Delta-Sigma ADC with 2-Wire Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-adc/max11205>`
-  `MAX1136: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel, 2-Wire Serial 10-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1136 <https://www.maximintegrated.com/MAX1136>`__
-  `MAX1137: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel, 2-Wire Serial 10-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1137 <https://www.maximintegrated.com/MAX1137>`__
-  `MAX1138: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel, 2-Wire Serial 10-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1138 <https://www.maximintegrated.com/MAX1138>`__
-  `MAX1139: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel, 2-Wire Serial 10-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1139 <https://www.maximintegrated.com/MAX1139>`__
-  `MAX11600: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/8-/12-Channel, 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11600 <https://www.maximintegrated.com/MAX11600>`__
-  `MAX11601: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/8-/12-Channel, 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11601 <https://www.maximintegrated.com/MAX11601>`__
-  `MAX11602: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/8-/12-Channel, 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11602 <https://www.maximintegrated.com/MAX11602>`__
-  `MAX11603: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/8-/12-Channel, 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11603 <https://www.maximintegrated.com/MAX11603>`__
-  `MAX11604: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/8-/12-Channel, 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11604 <https://www.maximintegrated.com/MAX11604>`__
-  `MAX11605: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/8-/12-Channel, 2-Wire Serial 8-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11605 <https://www.maximintegrated.com/MAX11605>`__
-  `MAX11606: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11606 <https://www.maximintegrated.com/MAX11606>`__
-  `MAX11607: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11607 <https://www.maximintegrated.com/MAX11607>`__
-  `MAX11608: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11608 <https://www.maximintegrated.com/MAX11608>`__
-  `MAX11609: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11609 <https://www.maximintegrated.com/MAX11609>`__
-  `MAX11610: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11610 <https://www.maximintegrated.com/MAX11610>`__
-  `MAX11611: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11611 <https://www.maximintegrated.com/MAX11611>`__
-  `MAX11612: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11612 <https://www.maximintegrated.com/MAX11612>`__
-  `MAX11613: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11613 <https://www.maximintegrated.com/MAX11613>`__
-  `MAX11614: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11614 <https://www.maximintegrated.com/MAX11614>`__
-  `MAX11615: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11615 <https://www.maximintegrated.com/MAX11615>`__
-  `MAX11616: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11616 <https://www.maximintegrated.com/MAX11616>`__
-  `MAX11617: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in Ultra-Small Packages <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11617 <https://www.maximintegrated.com/MAX11617>`__
-  `MAX11644: Low-Power, 1-/2-Channel, I²C, 12-Bit ADCs in Ultra-Tiny 1.9mm x 2.2mm Package <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11644 <https://www.maximintegrated.com/MAX11644>`__
-  `MAX11645: Low-Power, 1-/2-Channel, I²C, 12-Bit ADCs in Ultra-Tiny 1.9mm x 2.2mm Package <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11645 <https://www.maximintegrated.com/MAX11645>`__
-  `MAX11646: Low-Power, 1-/2-Channel, I²C, 10-Bit ADCs in Ultra-Tiny 1.9mm x 2.2mm Package <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11646 <https://www.maximintegrated.com/MAX11646>`__
-  `MAX11647: Low-Power, 1-/2-Channel, I²C, 10-Bit ADCs in Ultra-Tiny 1.9mm x 2.2mm Package <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX11647 <https://www.maximintegrated.com/MAX11647>`__
-  `MAX1227: 12-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1027.c>`__ `MAX1227 <https://www.maximintegrated.com/MAX1227>`__
-  `MAX1229: 12-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1027.c>`__ `MAX1229 <https://www.maximintegrated.com/MAX1229>`__
-  `MAX1231: 12-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1027.c>`__ `MAX1231 <https://www.maximintegrated.com/MAX1231>`__
-  `MAX1236: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel, 2-Wire Serial, 12-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1236 <https://www.maximintegrated.com/MAX1236>`__
-  `MAX1237: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel, 2-Wire Serial, 12-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1237 <https://www.maximintegrated.com/MAX1237>`__
-  `MAX1238: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel, 2-Wire Serial, 12-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1238 <https://www.maximintegrated.com/MAX1238>`__
-  `MAX1239: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel, 2-Wire Serial, 12-Bit ADCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1239 <https://www.maximintegrated.com/MAX1239>`__
-  `MAX1240: +2.7V, Low-Power, 12-Bit Serial ADCs in 8-Pin SO <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1241.c>`__ `MAX1240 <https://www.maximintegrated.com/MAX1240>`__
-  `MAX1241: +2.7V, Low-Power, 12-Bit Serial ADCs in 8-Pin SO <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1241.c>`__ `MAX1241 <https://www.maximintegrated.com/MAX1241>`__
-  `MAX1361: 250ksps, +3V, 8-/4-Channel, 12-Bit ADCs with +2.5V Reference and Parallel Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1361 <https://www.maximintegrated.com/MAX1361>`__
-  `MAX1362: 400ksps, +5V, 8-/4-Channel, 12-Bit ADCs with +2.5V Reference and Parallel Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1362 <https://www.maximintegrated.com/MAX1362>`__
-  `MAX1363: 250ksps, +3V, 8-/4-Channel, 12-Bit ADCs with +2.5V Reference and Parallel Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1363 <https://www.maximintegrated.com/MAX1363>`__
-  `MAX1364: 400ksps, +5V, 8-/4-Channel, 12-Bit ADCs with +2.5V Reference and Parallel Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1364 <https://www.maximintegrated.com/MAX1364>`__
-  `MAX1368: Microcontroller-Interface, 4.5-/3.5-Digit Panel Meters with 4-20mA Output <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max1363.c>`__ `MAX1368 <https://www.maximintegrated.com/MAX1368>`__
-  :doc:`MAX14001/MAX14002: isolated, single-channel, 10-bit ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/max14001>`
-  :doc:`MAX22530/MAX22531/MAX22532: galvanically isolated, 4-channel, multiplexed, 12-bit ADC </wiki-migration/resources/tools-software/linux-drivers/iio-adc/max22531>`
-  `MAX9611: High-Side, Inverting Current-Sense Amplifiers with12-Bit ADC and Op Amp/Comparator <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max9611.c>`__ `MAX9611 <https://www.maximintegrated.com/MAX9611>`__
-  `MAX9612: High-Side, Noninverting Current-Sense Amplifiers with12-Bit ADC and Op Amp/Comparator <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/adc/max9611.c>`__ `MAX9612 <https://www.maximintegrated.com/MAX9612>`__

IIO - Beamformers
~~~~~~~~~~~~~~~~~

-  :doc:`ADAR1000: 8 GHz to 16 GHz, 4-Channel, X Band and Ku Band Beamformer </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adar1000>`

IIO - Capacitance to Digital Converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD7152: 2-Channel, 12-Bit Capacitance to Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-cdc/ad7152>`
-  :doc:`AD7153: 1-Channel, 12-Bit Capacitance to Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-cdc/ad7152>`
-  :doc:`AD7150: Ultra-Low Power, 2-Channel, Capacitance Converter for Proximity Sensing </wiki-migration/resources/tools-software/linux-drivers/iio-cdc/ad7150>`
-  :doc:`AD7151: Ultra-Low Power, 1-Channel, Capacitance Converter for Proximity Sensing </wiki-migration/resources/tools-software/linux-drivers/iio-cdc/ad7150>`
-  :doc:`AD7156: Ultra-Low Power, 1.8 V, 3 mm × 3 mm, 2-Channel, Capacitance Converter </wiki-migration/resources/tools-software/linux-drivers/iio-cdc/ad7150>`
-  :doc:`AD7745: 24-bit, 1 Channel Capacitance to Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-cdc/ad7745>`
-  :doc:`AD7746: 24-bit, 2 Channel Capacitance to Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-cdc/ad7745>`
-  :doc:`AD7747: 24-Bit Capacitance-to-Digital Converter with Temperature Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-cdc/ad7745>`

IIO - Combined Analog to Digital and Digital to Analog converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD74412R: Quad-Channel, Software Configurable Input and Output </wiki-migration/resources/tools-software/linux-drivers/iio-addac/ad74413r>` :adi:`AD74412R`
-  :doc:`AD74413R: Quad-Channel, Software Configurable Input and Output </wiki-migration/resources/tools-software/linux-drivers/iio-addac/ad74413r>` :adi:`AD74413R`
-  `AD74115H: Single-Channel, Software Configurable Input and Output with HART Modem <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/addac/ad74115.c>`__ :adi:`AD74115H`

IIO - Digital to Analog Converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD3552R: Dual Channel, 16-Bit, 33 MUPS, Multispan, Multi-IO SPI DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/axi-ad3552r>`
-  :doc:`AD5024: Fully Accurate 12-Bit VOUT nanoDAC® Quad, SPI Interface, 4.5 V to 5.5 V in TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5025: Fully Accurate 12-Bit VOUT nanoDAC® SPI Interface 2.7 V TO 5.5 V IN A TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5044: Fully Accurate 14-Bit VOUT nanoDAC® Quad, SPI Interface, 4.5 V to 5.5 V in TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5045: Fully Accurate 14-Bit VOUT nanoDAC® SPI Interface 2.7 V TO 5.5 V IN A TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5064-1: Fully Accurate 16-Bit VOUT nanoDAC® Quad, SPI Interface, 4.5 V to 5.5 V in TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5064: Fully Accurate 16-Bit VOUT nanoDAC® Quad, SPI Interface, 4.5 V to 5.5 V in TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5065: Fully Accurate 16-Bit VOUT nanoDAC® SPI Interface 2.7 V TO 5.5 V IN A TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5300: 2.7V to 5.5V, 140 ΜA, Rail-to-Rail Voltage-Output 8-Bit DAC in SOT-23 AND MICROSOIC Packages </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5301: 2.5V to 5.5V, 120 ΜA, 2-Wire Interface, Voltage-Output 8-Bit DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5310: 2.7V to 5.5V, 140 ΜA, Rail-to-Rail Voltage-Output 10-Bit DAC in SOT-23 AND MICROSOIC Packages </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5310R: Single, 10-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5311: 2.5V to 5.5V, 120 ΜA, 2-Wire Interface, Voltage-Output 10-Bit DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5311R: Single, 10-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5320: 2.7V to 5.5V, 140 ΜA, Rail-to-Rail Voltage-Output 12-Bit DAC in SOT-23 AND MICROSOIC Packages </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5321: 2.5V to 5.5V, 120 ΜA, 2-Wire Interface, Voltage-Output 12-Bit DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5338: 2.5 V to 5.5 V, 250 µA, 2-Wire Interface, Dual Voltage Output, 10-Bit DACs </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5338R: Dual 10-Bit nanoDAC® with 2 ppm/°C Reference, I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5360: 16-Channel, 16-Bit, Serial Input, Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5360>`
-  :doc:`AD5361: 16-Channel, 14-Bit, Serial Input, Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5360>`
-  :doc:`AD5362: 8-Channel, 16-Bit, Serial Input, Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5360>`
-  :doc:`AD5363: 8-Channel, 14-Bit, Serial Input, Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5360>`
-  :doc:`AD5370: 40-Channel, 16-Bit, Serial Input, Voltage-Output DACs </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5360>`
-  :doc:`AD5371: 40-Channel, 14-Bit, Serial Input, Voltage-Output DACs </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5360>`
-  :doc:`AD5372: 32-Channel, 16-Bit, Serial Input, Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5360>`
-  :doc:`AD5373: 40-Channel, 14-Bit, Serial Input, Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5360>`
-  :doc:`AD5380: 40-Channel 14-Bit 3 V/5 V Single-Supply Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5380>`
-  :doc:`AD5381: 40-Channel 12-Bit 3 V/5 V Single-Supply Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5380>`
-  :doc:`AD5382: 32-Channel 14-Bit 3 V/5 V Single-Supply Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5380>`
-  :doc:`AD5383: 32-Channel 12-Bit 3 V/5 V Single-Supply Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5380>`
-  :doc:`AD5384: 40-Channel, 3 V/5 V Single Supply,14-Bit, Serial Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5380>`
-  :doc:`AD5390: 16-Channel 14-Bit 3 V/5 V Single-Supply Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5380>`
-  :doc:`AD5391: 16-Channel 12-Bit 3 V/5 V Single-Supply Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5380>`
-  :doc:`AD5392: 8-Channel 14-Bit 3 V/5 V Single-Supply Voltage-Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5380>`
-  :doc:`AD5415: Dual 12-Bit, High Bandwidth, Multiplying DAC with 4-Quadrant Resistors and Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5449>`
-  :doc:`AD5421: 16-Bit, Serial Input, Loop-Powered, 4mA to 20mA DA </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5421>`
-  :doc:`AD5426: 8-Bit, High Bandwidth, Multiplying DACs with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5449>`
-  :doc:`AD5429: Dual 8-Bit, High Bandwidth, Multiplying DACs with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5449>`
-  :doc:`AD5432: 10-Bit, High Bandwidth, Multiplying DACs with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5449>`
-  :doc:`AD5439: Dual 10-Bit, High Bandwidth, Multiplying DACs with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5449>`
-  :doc:`AD5443: 12-Bit, High Bandwidth, Multiplying DACs with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5449>`
-  :doc:`AD5444: 12-Bit High Bandwidth Multiplying DAC with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5446: 14-Bit High Bandwidth Multiplying DAC with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5449: Dual 12-Bit, High Bandwidth, Multiplying DACs with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5449>`
-  :doc:`AD5450: 8-BIT High Bandwidth Multiplying DAC with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5451: 10-BIT High Bandwidth Multiplying DAC with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5452: 12-BIT High Bandwidth Multiplying DAC with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5453: 14-BIT High Bandwidth Multiplying DAC with Serial Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5501: High Voltage, 12-Bit Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5504>` :adi:`Obsolete <ad5501>`
-  :doc:`AD5504: High Voltage, Quad Channel 12-Bit Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5504>`
-  :doc:`AD5512A: 2.7 V to 5.5 V, Serial-Input, Voltage-Output, 16-/12-Bit nanoDAC® in 16-lead 3 mm × 3 mm LFCSP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5541A: 2.7 V to 5.5 V, Serial-Input, Voltage-Output, 16-/12-Bit nanoDAC® in 8-lead 3 mm × 3 mm LFCSP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5542A: 2.7 V to 5.5 V, Serial-Input, Voltage-Output, 16-/12-Bit nanoDAC® in 16-lead 3 mm × 3 mm LFCSP & 16-lead TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5542: 2.7 V to 5.5 V, Serial-Input, Voltage-Output, 16-Bit DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5543: 16-Bit DAC in µSOIC-8 Package </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5553: 14-Bit DAC in µSOIC-8 Package </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5592R: 8 Channel, 12-Bit, Configurable ADC/DAC with on-chip Reference, SPI interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5592r>`
-  :doc:`AD5593R: 8 Channel, 12-Bit, Configurable ADC/DAC with on-chip Reference, I2C interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5593r>`
-  :doc:`AD5600: High Temperature, 16-Bit, Unbuffered Voltage Output DAC, SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  `AD5601: 2.7V to 5.5V, <100 uA, 8-Bit nanoDAC®, SPI Interface in SC70 Package </resources/tools-software/linux-drivers/iio-dac/ad5446>`__
-  `AD5602: 2.7V to 5.5V, <100 ΜA, 8-Bit nanoDAC® with I2C compatible Interface, tiny SC70 Package </resources/tools-software/linux-drivers/iio-dac/ad5446>`__
-  `AD5611: 2.7V to 5.5V, <100 uA, 10-Bit nanoDAC®, SPI Interface in SC70 Package </resources/tools-software/linux-drivers/iio-dac/ad5446>`__
-  `AD5612: 2.7V to 5.5V, <100 ΜA, 10-Bit nanoDAC® with I2C compatible Interface, tiny SC70 Package </resources/tools-software/linux-drivers/iio-dac/ad5446>`__
-  :doc:`AD5620-1: Single, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference in SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5620-2: Single, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference in SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5620-3: Single, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference in SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5620: Single, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference in SOT-23 </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  `AD5621: 2.7V to 5.5V, <100 uA, 12-Bit nanoDAC®, SPI Interface in SC70 Package </resources/tools-software/linux-drivers/iio-dac/ad5446>`__
-  `AD5622: 2.7V to 5.5V, <100 ΜA, 12-Bit nanoDAC® with I2C compatible Interface, tiny SC70 Package </resources/tools-software/linux-drivers/iio-dac/ad5446>`__
-  :doc:`AD5624: 2.7 V to 5.5 V, 450 µA, Rail-to-Rail Output, Quad, 12-Bit nano DAC® </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5624r>`
-  :doc:`AD5624R: Quad, 12-Bit nanoDAC® with 5ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5624r>`
-  :doc:`AD5625: Quad, 12-Bit nanoDAC®, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5625R: Quad, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5626R: Dual, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5626R: Quad, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5627: Dual, 12-Bit nanoDAC®, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5627R: Dual, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5628-1: Octal, 12-Bit, SPI Voltage-Output denseDAC with 1.25 V 5 ppm/°C reference, </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5628-2: Octal, 12-Bit, SPI Voltage-Output denseDAC with 2.5 V 5 ppm/°C reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5628: Octal, 12-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5629R: OCTAL, 12-BIT, I2C Voltage Output denseDAC with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5640-1: Single, 14-Bit nanoDAC® Converter with 5 ppm/°C On-Chip Reference in S0T-23 </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5640-2: Single, 14-Bit nanoDAC® Converter with 5 ppm/°C On-Chip Reference in S0T-23 </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5640-3: Single, 14-Bit nanoDAC® Converter with 5 ppm/°C On-Chip Reference in S0T-23 </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5640: Single, 14-Bit nanoDAC® Converter with 5 ppm/°C On-Chip Reference in S0T-23 </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  `AD5641: 2.7V to 5.5V, <100 mA, 14-Bit nanoDAC®, SPI interface in LFCSP and SC70 </resources/tools-software/linux-drivers/iio-dac/ad5446>`__
-  :doc:`AD5644R: Quad, 14-Bit nanoDAC® with 5ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5624r>`
-  :doc:`AD5645R: Quad, 14-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5647R: Dual, 14-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5648: Octal, 14-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5648-1: Octal, 14-Bit, SPI Voltage-Output denseDAC with a 1.25 V 5 ppm/°C reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5648-2: Octal, 14-Bit, SPI Voltage-Output denseDAC with 2.5 V 5 ppm/°C reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5048-1: Octal, 14-Bit, SPI Voltage-Output denseDAC with 1.25 V 5 ppm/°C reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5048-2: Octal, 14-Bit, SPI Voltage-Output denseDAC with 2.5 V 5 ppm/°C reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5660-1: Single, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5660-2: Single, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5660-3: Single, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5660: Single, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5662: 2.7-5.5V, 16-Bit nanoDAC® Converter in a Sot-23 </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5446>`
-  :doc:`AD5664R: Quad, 16-Bit nanoDAC® with 5ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5624r>`
-  :doc:`AD5665: Quad, 16-Bit nanoDAC®, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5665R: Quad, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5666: Quad, 16-Bit D/A Converter with 10ppm/°C max On-Chip Reference in 14-lead TSSOP </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5667: Dual, 16-Bit nanoDAC®, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5667R: Dual, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C® Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5668: Octal, 16-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5668-1: Octal, 16-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5668-2: Octal, 16-Bit, SPI Voltage-Output denseDAC with 2.5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5668-3: Octal, 16-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5669R: OCTAL, 16-BIT, I2C Voltage-Output denseDAC with 5 ppm/°C On-Chip Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5064>`
-  :doc:`AD5671R: Octal, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5672R: Octal, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5673R: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage Reference TC, I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5674R: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage Reference Temperature Coefficient, SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5675R: Octal, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5676: Octal, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5676R: Octal, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5677R: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage Reference, I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5679: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage Reference Temperature Coefficient, SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5679R: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage Reference Temperature Coefficient, SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5681R: Single, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5682R: Single, 14-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5683R: Single, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5683: Single, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5684: Quad, 12-Bit nanoDAC+ with SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5686>`
-  :doc:`AD5684R: Quad, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5686>`
-  :doc:`AD5685R: Quad, 14-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5686>`
-  :doc:`AD5686R: Quad, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5686>`
-  :doc:`AD5691R: Single, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5692R: Single, 14-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5693R: Single, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5693: Single, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5694: Quad, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5694R: Quad, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5695R: Quad, 14-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5696: Quad, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  :doc:`AD5696R: Quad, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and I2C Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5676>`
-  `AD5721: Multiple Range, 12-Bit, Unipolar, Voltage Output DACs <https://github.com/torvalds/linux/blob/master/drivers/iio/dac/ad5761.c>`__ :adi:`AD5721`
-  `AD5721R: Multiple Range, 12-Bit, Unipolar Voltage Output DACs with 2 PPM/⁰C Reference <https://github.com/torvalds/linux/blob/master/drivers/iio/dac/ad5761.c>`__ :adi:`AD5721R`
-  :doc:`AD5735: Quad Channel, 12-Bit, Serial Input, 4-20 mA & Voltage Output DAC with Dynamic Power Control </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5755>`
-  :doc:`AD5737: Quad Channel, 12-Bit, Serial Input, 4-20 mA Output DAC with Dynamic Power Control and HART Connectivity </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5755>`
-  :doc:`AD5744: Complete Quad, 14-Bit, High Accuracy, Serial Input, Bipolar Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5764>` :adi:`Obsolete <ad5744>`
-  :doc:`AD5744R: Complete Quad, 14-Bit, High Accuracy, Serial Input, Bipolar Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5764>`
-  :doc:`AD5755-1: Quad Channel, 16-Bit, Serial Input, 4-20 mA & Voltage Output DAC, Dynamic Power Control, HART Connectivity </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5755>`
-  :doc:`AD5755: Quad Channel, 16-Bit, Serial Input, 4 mA to 20 mA and Voltage Output DAC, Dynamic Power Control </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5755>`
-  :doc:`AD5757: Quad Channel, 16-Bit, Serial Input, 4-20 mA Output DAC, Dynamic Power Control, HART Connectivity </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5755>`
-  :doc:`AD5758: Single Channel, 16-Bit, Current/Voltage Output DAC, Dynamic Power Control, HART Connectivity </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5758>`
-  :doc:`AD5760: ULTRA STABLE 16-BIT ±0.5 LSB INL, Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5791>`
-  `AD5761: Multiple Range, 16-Bit, Bipolar, Voltage Output DACs <https://github.com/torvalds/linux/blob/master/drivers/iio/dac/ad5761.c>`__ :adi:`AD5761`
-  `AD5761R: Multiple Range, 16-Bit, Bipolar Voltage Output DACs with 2 PPM/⁰C Reference <https://github.com/torvalds/linux/blob/master/drivers/iio/dac/ad5761.c>`__ :adi:`AD5761R`
-  :doc:`AD5764: Complete Quad, 16-Bit, High Accuracy, Serial Input, Bipolar Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5764>`
-  :doc:`AD5764R: Complete Quad, 16-Bit, High Accuracy, Serial Input, Bipolar Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5764>`
-  `AD5766: 16-Channel, 16-Bit Voltage Output denseDAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5766.c>`__ :adi:`AD5766`
-  `AD5767: 16-Channel, 12-Bit Voltage Output denseDAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5766.c>`__ :adi:`AD5767`
-  :doc:`AD5770R: 6-Channel, 14-Bit, Current Output DAC with On-Chip Reference, SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5770r>`
-  :doc:`AD5780: SYSTEM READY, 18-BIT ±1 LSB INL, Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5764>`
-  :doc:`AD5781: True 18-Bit, Voltage Output DAC ±0.5 LSB INL, ±0.5 LSB DNL </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5791>`
-  :doc:`AD5790: System Ready 20-Bit, +-/ 2 LSB INL, Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5791>`
-  :doc:`AD5791: 1 ppm 20-Bit, ±1 LSB INL, Voltage Output DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5791>`
-  :doc:`AD7303: +2.7 V TO +5.5 V, Serial Input, Dual Voltage Output 8-Bit DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad7303>`
-  :doc:`AD7293: 12-Bit Power Amplifier Current Controller with ADC, DACs, Temperature and Current Sensors </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad7293>`
-  :doc:`AD8460: 110 V High Voltage, 1 A High Current, Arbitrary Waveform Generator with Integrated 14-Bit High Speed DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad8460>`\ :adi:`AD8460`
-  `AD8801: Octal 8-Bit TrimDAC with Power Shutdown & Mid-Scale Preset <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad8801.c>`__ :adi:`AD8801`
-  `AD8803: Octal 8-Bit TrimDAC with Power Shutdown & Mid-Scale Preset <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad8801.c>`__ :adi:`AD8803`
-  :doc:`AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  :doc:`AD9136: Dual, 16-Bit, 2.8 GSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  :doc:`AD9144: Quad, 16-Bit, 2.8 GSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  :doc:`AD9152: Dual, 16-Bit, 2.25 GSPS, TxDAC+ Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  :doc:`AD9154: Quad, 16-Bit, 2.4 GSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  :doc:`AD9162: 16-Bit, 12 GSPS, RF Digital-to-Analog Converters </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  :doc:`AD9171: Dual, 16-Bit, 6.2 GSPS RF DAC with Single Channelizer </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9172>`
-  :doc:`AD9172: Dual, 16-Bit, 12.6 GSPS RF DAC with Channelizers </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9172>`
-  :doc:`AD9173: Dual, 16-Bit, 12.6 GSPS RF DAC with Channelizers </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9172>`
-  :doc:`AD9174: Dual, 16-Bit, 12.6 GSPS RF DAC and Direct Digital Synthesizer </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9172>`
-  :doc:`AD9175: Dual, 11-Bit/16-Bit, 12.6 GSPS RF DAC with Wideband Channelizers </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9172>`
-  :doc:`AD9176: Dual, 16-Bit, 12.6 GSPS RF DAC with Wideband Channelizers </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9172>`
-  :doc:`AD9177 Quad, 16-Bit, 12 GSPS RF DAC with Wideband Channelizers </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  :doc:`AD9739A: 14-Bit, 2.5 GSPS, RF D/A Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  `ADT7316 ±0.5°C Accurate Digital Temperature Sensor and Quad Voltage Output 12-Bit DAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/staging/iio/addac/adt7316.c>`__ :adi:`ADT7316`
-  `ADT7317 ±0.5°C Accurate Digital Temperature Sensor and Quad Voltage Output 10-Bit DAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/staging/iio/addac/adt7316.c>`__ :adi:`ADT7317`
-  `ADT7318 ±0.5°C Accurate Digital Temperature Sensor and Quad Voltage Output 8-Bit DACs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/staging/iio/addac/adt7316.c>`__ :adi:`ADT7318`
-  `LTC1660: Micropower Octal 10-Bit DACs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ltc1660.c>`__ :adi:`LTC1660`
-  `LTC1660: Micropower Octal 8-Bit DACs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ltc1660.c>`__ :adi:`LTC1660`
-  `LTC1665: Micropower Octal 8-Bit DACs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ltc1660.c>`__ :adi:`LTC1665`
-  `LTC2606: 16-Bit Rail-to-Rail DACs with I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2606`
-  `LTC2607: 16-Bit Dual Rail-to-Rail DACs with I²C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2607`
-  `LTC2609: Quad 16-/14-/12-Bit Rail-to-Rail DACs with I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2609`
-  `LTC2616: 14-Bit Rail-to-Rail DACs with I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2616`
-  `LTC2617: 14-Bit Dual Rail-to-Rail DAC with I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2617`
-  `LTC2619: Quad 16-/14-/12-Bit Rail-to-Rail DACs with I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2619`
-  `LTC2626: 12-Bit Rail-to-Rail DACs with I2C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2626`
-  `LTC2627: 12-Bit Dual Rail-to-Rail with I²C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2627`
-  `LTC2629: Quad 16-/14-/12-Bit Rail-to-Rail DACs with I²C Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2629`
-  `LTC2631: Single 12-/10-/8-Bit I2C VOUT DACs with 10ppm/°C Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2631`
-  `LTC2632: Dual 12-/10-/8-Bit SPI VOUT DACs with 10ppm/°C Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ltc2632.c>`__ :adi:`LTC2632`
-  `LTC2634: Quad 12-/10-/8-Bit Rail-to-Rail DACs with 10ppm/°C Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ltc2632.c>`__ :adi:`LTC2634`
-  `LTC2636: Octal 12-/10-/8-Bit SPI VOUT DACs with 10ppm/°C Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ltc2632.c>`__ :adi:`LTC2636`
-  `LTC2633: Dual 12-/10-/8-Bit I2C VOUT DACs with 10ppm/°C Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2633`
-  `LTC2635: Quad 12-/10-/8-Bit I2C VOUT DACs with 10ppm/°C Reference <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad5064.c>`__ :adi:`LTC2635`
-  :doc:`LTC2664: Quad 16-Bit/12-Bit ±10V VOUT SoftSpan DACs with 10ppm/°C Max Reference </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ltc2664>`
-  :doc:`LTC2672: 5-Channel, 300mA, 12-/16-Bit Current Source Output SoftSpan DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ltc2672>`
-  `LTC2688: 16-Channel, 12-/16-Bit Voltage Output SoftSpan DAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ltc2688.c>`__ :adi:`LTC2688`
-  `MAX5821: Dual, 10-Bit, Low-Power, 2-Wire, Serial Voltage-Output DAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/max5821.c>`__ `MAX5821 <https://www.maximintegrated.com/MAX5821>`__
-  `MAX517: 2-Wire Serial 8-Bit DACs withRail-to-Rail Outputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/max517.c>`__ `MAX517 <https://www.maximintegrated.com/MAX517>`__
-  `MAX518: 2-Wire Serial 8-Bit DACs withRail-to-Rail Outputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/max517.c>`__ `MAX518 <https://www.maximintegrated.com/MAX518>`__
-  `MAX519: 2-Wire Serial 8-Bit DACs withRail-to-Rail Outputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/max517.c>`__ `MAX519 <https://www.maximintegrated.com/MAX519>`__
-  `MAX520: Quad/Octal, 2-Wire Serial 8-Bit DACs with Rail-to-Rail Outputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/max517.c>`__ `MAX520 <https://www.maximintegrated.com/MAX520>`__
-  `MAX521: Quad/Octal, 2-Wire Serial 8-Bit DACs with Rail-to-Rail Outputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/max517.c>`__ `MAX521 <https://www.maximintegrated.com/MAX521>`__
-  `DS4422: Two-/Four-Channel, I²C, 7-Bit Sink/Source Current DAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/DS4424.c>`__ `DS4422 <https://www.maximintegrated.com/DS4422>`__
-  `DS4424: Two-/Four-Channel, I²C, 7-Bit Sink/Source Current DAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/DS4424.c>`__ `DS4424 <https://www.maximintegrated.com/DS4424>`__

IIO - Direct Digital Synthesis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD9832: 25 MHz Serial Interface DDS With On-Chip 10-Bit DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9832>`
-  :doc:`AD9833: Low Power, 12.65 mW, 2.3 V to +5.5 V, Programmable Waveform Generator </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9834>`
-  :doc:`AD9834: 20 mW Power, 2.3 V to 5.5 V, 75 MHz Complete DDS </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9834>`
-  :doc:`AD9835: Complete DDS With 10-Bit On-Chip DAC </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9832>`
-  :doc:`AD9837: Low Power, 8.5 mW, 2.3 V to 5.5 V, Programmable Waveform Generator </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9834>`
-  :doc:`AD9838: 11 mW Power, 2.3 V to 5.5 V, Complete DDS </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9834>`
-  :doc:`AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  :doc:`AD9144: Quad, 16-Bit, 2.8 GSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
-  :doc:`AD9739A: 14-Bit, 2.5 GSPS, RF D/A Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

IIO - Filters
~~~~~~~~~~~~~

-  :doc:`ADMV8818: 2 GHz to 18 GHz, Digitally Tunable, High-Pass and Low-Pass Filter </wiki-migration/resources/tools-software/linux-drivers/iio-filter/admv8818>`

IIO - Frequency Synthesizers / Phase-Locked Loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD9161: 11-Bit/16-Bit, 12 GSPS, RF Digital-to-Analog Converters </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9162>`
-  :doc:`AD9162: 11-Bit/16-Bit, 12 GSPS, RF Digital-to-Analog Converters </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9162>`
-  :doc:`AD9163: 16-Bit, 12 GSPS, RF DAC and Digital Upconverter </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9162>`
-  :doc:`AD9164: 16-Bit, 12 GSPS, RF DAC and Direct Digital Synthesizer </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9162>`
-  :doc:`AD9166: DC to 9 GHz Vector Signal Generator </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9162>`
-  :doc:`AD9508: 1.65 GHz Clock Fanout Buffer with Output Dividers and Delay Adjust </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9508>`
-  :doc:`AD9516-0: 14-Output Clock Generator with Integrated 2.8 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9516-1: 14-Output Clock Generator with Integrated 2.5 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9516-2: 14-Output Clock Generator with Integrated 2.2 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9516-3: 14-Output Clock Generator with Integrated 2.0 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9516-4: 14-Output Clock Generator with Integrated 1.6 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9516-5: 14-Output Clock Generator </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9517-0: 12-Output Clock Generator with Integrated 2.8 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9517-1: 12-Output Clock Generator with Integrated 2.5 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9517-2: 12-Output Clock Generator with Integrated 2.2 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9517-3: 12-Output Clock Generator with Integrated 2.0 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9517-4: 12-Output Clock Generator with Integrated 1.6 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9518-0: 6-Output Clock Generator with Integrated 2.8 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9518-1: 6-Output Clock Generator with Integrated 2.5 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9518-2: 6-Output Clock Generator with Integrated 2.2 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9518-3: 6-Output Clock Generator with Integrated 2.0 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9518-4: 6-Output Clock Generator with Integrated 1.6 GHz VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9517>`
-  :doc:`AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29 LVCMOS Outputs </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9523>`
-  :doc:`AD9528: JESD204B Clock Generator with 14 LVDS/HSTL Outputs </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9528>`
-  :doc:`ADF4159: Direct Modulation/Fast Waveform Generating, 13 GHz, Fractional-N Frequency Synthesizer </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4159>`
-  :doc:`ADF4169: Direct Modulation/Fast Waveform Generating, 13.5 GHz, Fractional-N Frequency Synthesizer </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4159>`
-  :doc:`ADF4350: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
-  :doc:`ADF4351: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
-  :doc:`ADF4360-0: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4360-1: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4360-2: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4360-3: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4360-4: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4360-5: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4360-6: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4360-7: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4360-8: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4360-9: Clock Generator PLL with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4360>`
-  :doc:`ADF4371: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4371>`
-  :doc:`ADF4372: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4371>`
-  :doc:`ADF4377: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4377>`
-  :doc:`ADF4355: Microwave Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf5355>`
-  :doc:`ADF4355-2: Microwave Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf5355>`
-  :doc:`ADF4355-3: Microwave Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf5355>`
-  :doc:`ADF5355: Microwave Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf5355>`
-  :doc:`ADF5356: Microwave Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf5355>`
-  :doc:`ADMV1013: 24 GHz to 44 GHz, Wideband, Microwave Upconverter </wiki-migration/resources/tools-software/linux-drivers/iio-pll/admv1013>`
-  :doc:`ADMV1014: 24 GHz to 44 GHz, Wideband, Microwave Downconverter </wiki-migration/resources/tools-software/linux-drivers/iio-pll/admv1014>`
-  :doc:`ADRF6780: 5.9 GHz to 23.6 GHz, Wideband, Microwave Upconverter </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adrf6780>`
-  :doc:`HMC7044: Clock Jitter Attenuator with JESD204B </wiki-migration/resources/tools-software/linux-drivers/iio-pll/hmc7044>`
-  :doc:`HMC7043: High Performance, 3.2 GHz, 14-Output Fanout Buffer </wiki-migration/resources/tools-software/linux-drivers/iio-pll/hmc7044>`
-  :doc:`LTC6952: Ultralow Jitter, 4.5GHz PLL, JESD204B/JESD204C </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ltc6952>`
-  :doc:`LTC6953: Ultralow Jitter, 4.5GHz Clock Distributor with 11 Outputs, JESD204B/JESD204C </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ltc6952>`

IIO - Gyroscopes
~~~~~~~~~~~~~~~~

-  :doc:`ADIS16060: Wide Bandwidth Yaw Rate Gyroscope with SPI </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16060>`
-  :doc:`ADIS16080: ±80°/sec Yaw Rate Gyro with SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16080>` :adi:`Obsolete <ADIS16080>`
-  :doc:`ADIS16100: ±300°/sec Yaw Rate Gyro with SPI Interface </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16080>` :adi:`Obsolete <adis16100>`
-  :doc:`ADIS16130: Digital Output, High-Precision Angular Rate Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16130>` :adi:`Obsolete <adis16130>`
-  :doc:`ADIS16133: ±1200°/sec Precision Angular Rate Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16136>` :adi:`Obsolete <adis16133>`
-  :doc:`ADIS16135: ±300°/sec Precision Angular Rate Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16136>`
-  :doc:`ADIS16136: ±450°/sec Precision Angular Rate Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16136>`
-  :doc:`ADIS16137: ±1000°/Sec Precision Angular Rate Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16136>`
-  :doc:`ADIS16251: Programmable Low Power Gyroscope </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16260>` :adi:`Obsolete <adis16251>`
-  :doc:`ADIS16250: Programmable Low Power Gyroscope </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16260>` :adi:`Obsolete <adis16250>`
-  :doc:`ADIS16255: Programmable Low Power Gyroscope </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16260>` :adi:`Obsolete <adis16255>`
-  :doc:`ADIS16260: Programmable Low Power Gyroscope </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16260>`
-  :doc:`ADIS16265: Programmable Digital Gyroscope Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16260>`
-  :doc:`ADIS16266: ±14,000°/sec Digital Gyroscope Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adis16260>`\ :adi:`Obsolete <adis16266>`
-  `ADXRS290: Ultralow noise, dual-axis MEMS Gyroscope for Stabilization Applications <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/gyro/adxrs290.c>`__ :adi:`ADXRS290`
-  :doc:`ADXRS450: ±300°/sec High Vibration Immunity Digital Gyro </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adxrs450>`
-  :doc:`ADXRS453: High Performance, Digital Output Gyroscope </wiki-migration/resources/tools-software/linux-drivers/iio-gyroscope/adxrs450>`

IIO - Heart-Rate
~~~~~~~~~~~~~~~~

-  `MAX30100: Pulse Oximeter and Heart-Rate Sensor IC for Wearable Health <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/health/max30100.c>`__ `MAX30100 <https://www.maximintegrated.com/MAX30100>`__
-  `MAX30102: High-Sensitivity Pulse Oximeter and Heart-Rate Sensor for Wearable Health <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/health/max30102.c>`__ `MAX30102 <https://www.maximintegrated.com/MAX30102>`__

IIO - Impedance Converters and Network Analyzers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD5933: 1 MSPS, 12 Bit Impedance Converter Network Analyzer </wiki-migration/resources/tools-software/linux-drivers/iio-impedance-analyzer/ad5933>`
-  :doc:`AD5934: 250 kSPS 12-Bit Impedance Converter Network Analyzer </wiki-migration/resources/tools-software/linux-drivers/iio-impedance-analyzer/ad5933>`

IIO - Inertial Measurement Units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`ADIS16300: Four Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>` :adi:`Obsolete <adis16300>`
-  :doc:`ADIS16305: Precision Four Degrees of Freedom Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>` :adi:`Obsolete <adis16305>`
-  :doc:`ADIS16334: Low-Profile Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>`
-  :doc:`ADIS16350: High Precision Tri-Axis Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>` :adi:`Obsolete <adis16350>`
-  :doc:`ADIS16354: High Precision Tri-Axis Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>` :adi:`Obsolete <adis16354>`
-  :doc:`ADIS16355: High-Precision Tri-Axis Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>` :adi:`Obsolete <adis16355>`
-  :doc:`ADIS16360: Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>` :adi:`Obsolete <adis16360>`
-  :doc:`ADIS16362: Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>`
-  :doc:`ADIS16364: High Precision Tri-Axis Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>`
-  :doc:`ADIS16365: Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>`
-  :doc:`ADIS16367: Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>` :adi:`Obsolete <adis16367>`
-  :doc:`ADIS16375: Low Profile, Low Noise Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16480>`
-  :doc:`ADIS16400: High Precision Tri-Axis Inertial Sensor Gyroscope, Magnetometer, Accelerometer </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>` :adi:`Obsolete <adis16400>`
-  :doc:`ADIS16405: High Precision Tri-Axis Gyroscope, Accelerometer, Magnetometer </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>` :adi:`Obsolete <adis16405>`
-  :doc:`ADIS16445: Compact, Precision Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>`
-  :doc:`ADIS16448: Low Noise, High Stability Ten Degree of Freedom MEMS Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16400>`
-  :doc:`ADIS16460: Compact, Precision, Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16475>`
-  :doc:`ADIS16465: Precision MEMS IMU Module </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16475>`
-  :doc:`ADIS16467: Precision MEMS IMU Module </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16475>`
-  :doc:`ADIS16470: Wide Dynamic Range, Miniature MEMs IMU </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16475>`
-  :doc:`ADIS16475: Precision, Miniature MEMs IMU </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16475>`
-  :doc:`ADIS16477: Precision, Miniature MEMs IMU </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16475>`
-  :doc:`ADIS16480: Ten Degrees of Freedom MEMS Inertial Sensor with Dynamic Orientation Outputs </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16480>`
-  :doc:`ADIS16485: Tactical Grade Six Degrees of Freedom MEMS Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16480>`
-  :doc:`ADIS16488: Low Profile, Low Noise Ten Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16480>` :adi:`Obsolete <adis16488>`
-  :doc:`ADIS16490: Tactical Grade, Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16480>`
-  :doc:`ADIS16495: Tactical Grade, Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16480>`
-  :doc:`ADIS16497: Tactical Grade, Six Degrees of Freedom Inertial Sensor </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16480>`
-  :doc:`ADIS16500: Precision, Miniature MEMs IMU </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16475>`
-  :doc:`ADIS16505: Precision, Miniature MEMs IMU </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16475>`
-  :doc:`ADIS16507: Precision, Miniature MEMs IMU </wiki-migration/resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis16475>`

IIO - Light
~~~~~~~~~~~

-  `MAX44000: Ambient and Infrared Proximity Sensor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/light/max44000.c>`__ `MAX44000 <https://www.maximintegrated.com/MAX44000>`__
-  `MAX44009: Industry's Lowest-Power Ambient Light Sensor with ADC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/light/max44009.c>`__ `MAX44009 <https://www.maximintegrated.com/MAX44009>`__

IIO - Mixed Signal Front Ends (MxFE)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD9081 MxFE® Quad, 16-Bit, 12 GSPS RF DAC and Quad, 12-Bit, 4 GSPS RF ADC </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  :doc:`AD9082 MxFE® Quad, 16-Bit, 12 GSPS RF DAC and Dual, 12-Bit, 6 GSPS RF ADC </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  :doc:`AD9088 MxFE® 4T4R Direct RF Transmitter and Observation Receiver </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  :doc:`AD9086 MxFE® 4T2R Direct RF Transmitter and Observation Receiver </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

IIO - Potentiometers
~~~~~~~~~~~~~~~~~~~~

-  `MAX5487: Dual, 256-Tap, Nonvolatile, SPI-Interface, Linear-Taper Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5487.c>`__ `MAX5487 <https://www.maximintegrated.com/MAX5487>`__
-  `MAX5488: Dual, 256-Tap, Nonvolatile, SPI-Interface, Linear-Taper Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5487.c>`__ `MAX5488 <https://www.maximintegrated.com/MAX5488>`__
-  `MAX5489: Dual, 256-Tap, Nonvolatile, SPI-Interface, Linear-Taper Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5487.c>`__ `MAX5489 <https://www.maximintegrated.com/MAX5489>`__
-  `MAX5481: 10-Bit, Nonvolatile, Linear-Taper Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5481.c>`__ `MAX5481 <https://www.maximintegrated.com/MAX5481>`__
-  `MAX5482: 10-Bit, Nonvolatile, Linear-Taper Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5481.c>`__ `MAX5482 <https://www.maximintegrated.com/MAX5482>`__
-  `MAX5483: 10-Bit, Nonvolatile, Linear-Taper Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5481.c>`__ `MAX5483 <https://www.maximintegrated.com/MAX5483>`__
-  `MAX5484: 10-Bit, Nonvolatile, Linear-Taper Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5481.c>`__ `MAX5484 <https://www.maximintegrated.com/MAX5484>`__
-  `MAX5432: 32-Tap, Nonvolatile, I2C, Linear, Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5432.c>`__ `MAX5432 <https://www.maximintegrated.com/MAX5432>`__
-  `MAX5433: 32-Tap, Nonvolatile, I2C, Linear, Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5433.c>`__ `MAX5433 <https://www.maximintegrated.com/MAX5433>`__
-  `MAX5434: 32-Tap, Nonvolatile, I2C, Linear, Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5432.c>`__ `MAX5434 <https://www.maximintegrated.com/MAX5434>`__
-  `MAX5435: 32-Tap, Nonvolatile, I2C, Linear, Digital Potentiometers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/max5432.c>`__ `MAX5435 <https://www.maximintegrated.com/MAX5435>`__
-  `DS1803: Addressable Dual Digital Potentiometer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/ds1803.c>`__ `DS1803 <https://www.maximintegrated.com/DS1803>`__
-  `AD5110: Single Channel, 128-Position, I2C, ±8% Resistor Tolerance, Nonvolatile Digital Potentiometer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/ad5110.c>`__ :adi:`AD5110`
-  `AD5112: Single Channel, 64-Position, I2C, ±8% Resistor Tolerance, Nonvolatile Digital Potentiometer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/ad5110.c>`__ :adi:`AD5112`
-  `AD5114: Single Channel, 32-Position, I2C, ±8% Resistor Tolerance, Nonvolatile Digital Potentiometer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/potentiometer/ad5110.c>`__ :adi:`AD5114`

IIO - Resolvers
~~~~~~~~~~~~~~~

-  :doc:`AD2S90: Low Cost, Complete 12-Bit Resolver-to-Digital Converter </wiki-migration/resources/tools-software/linux-drivers/iio-resolver/ad2s90>`
-  :doc:`AD2S1200: 12-Bit R/D Converter with Reference Oscillator </wiki-migration/resources/tools-software/linux-drivers/iio-resolver/ad2s1200>`
-  :doc:`AD2S1205: 12-Bit R/D Converter with Reference Oscillator </wiki-migration/resources/tools-software/linux-drivers/iio-resolver/ad2s1200>`
-  :doc:`AD2S1210: Variable Resolution, 10-Bit to 16-Bit R/D Converter with Reference Oscillator </wiki-migration/resources/tools-software/linux-drivers/iio-resolver/ad2s1210>`

IIO - Receivers
~~~~~~~~~~~~~~~

-  :doc:`AD6676: Wideband IF Receiver Subsystem </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad6676>`

IIO - Transceivers
~~~~~~~~~~~~~~~~~~

-  :doc:`AD9361: RF Agile Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  :doc:`AD9363: RF Agile Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  :doc:`AD9364: RF Agile Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  :doc:`AD9371: RF Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9371>`
-  :doc:`AD9375: RF Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9371>`
-  :doc:`ADRV9002: RF Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`
-  :doc:`ADRV9008-1: RF Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`
-  :doc:`ADRV9008-2: RF Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`
-  :doc:`ADRV9009: RF Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`
-  :doc:`ADRV9009-ZU11EG: RF System on Module </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`
-  :doc:`ADRV9361-Z7035: RF System on Module </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  :doc:`ADRV9364-Z7020: RF System on Module </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

IIO - Temperature
~~~~~~~~~~~~~~~~~

-  :doc:`LTC2983: Multi-Sensor Digital Temperature Measurement System </wiki-migration/resources/tools-software/linux-drivers/iio-temperature/ltc2983>` :adi:`LTC2983`
-  :doc:`LTC2984: Multi-Sensor Digital Temperature Measurement System </wiki-migration/resources/tools-software/linux-drivers/iio-temperature/ltc2983>` :adi:`LTC2984`
-  :doc:`LTC2986: Multi-Sensor Digital Temperature Measurement System </wiki-migration/resources/tools-software/linux-drivers/iio-temperature/ltc2983>` :adi:`LTC2986`
-  :doc:`LTM2985: Multi-Sensor Digital Temperature Measurement System </wiki-migration/resources/tools-software/linux-drivers/iio-temperature/ltc2983>` :adi:`LTM2985`
-  `MAX31856: Precision Thermocouple to Digital Converter with Linearization <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/temperature/max31856.c>`__ `MAX31856 <https://www.maximintegrated.com/MAX31856>`__
-  `MAX31855: Cold-Junction Compensated Thermocouple-to-Digital Converter <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/temperature/maxim_thermocouple.c>`__ `MAX31855 <https://www.maximintegrated.com/MAX31855>`__
-  `MAX6675: Cold-Junction-Compensated K-Thermocouple-to-Digital Converter (0°C to +1024°C) <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/temperature/maxim_thermocouple.c>`__ `MAX6675 <https://www.maximintegrated.com/MAX6675>`__

IIO - Vector Power Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`ADL5960: 10 MHz to 20 GHz, Integrated Vector Network Analyzer Front-End </wiki-migration/resources/tools-software/linux-drivers/iio-vector-power/adl5960>` :adi:`ADL5960`

Input - Keyboard
~~~~~~~~~~~~~~~~

-  :doc:`ADP5520: Backlight Driver with I/O Expander </wiki-migration/resources/tools-software/linux-drivers/multifunction-device/adp5520>`
-  :doc:`ADP5585: Keypad Decoder and I/O Expansion </wiki-migration/resources/tools-software/linux-drivers/input-keyboard/adp5589>`
-  :doc:`ADP5587: Mobile I/O Expander and QWERTY Keypad Controller </wiki-migration/resources/tools-software/linux-drivers/input-keyboard/adp5588>`
-  :doc:`ADP5588: Mobile I/O Expander and QWERTY Keypad Controller </wiki-migration/resources/tools-software/linux-drivers/input-keyboard/adp5588>`
-  :doc:`ADP5589: Keypad Decoder and I/O Expansion </wiki-migration/resources/tools-software/linux-drivers/input-keyboard/adp5589>`
-  `MAX7359: 2-Wire Interfaced Low-EMI Key Switch Controller/GPO <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/input/keyboard/max7359_keypad.c>`__ `MAX7359 <https://www.maximintegrated.com/MAX7359>`__

Input - Misc
~~~~~~~~~~~~

-  :doc:`AD7142: Programmable Controller for Capacitance Touch Sensors </wiki-migration/resources/tools-software/linux-drivers/input-misc/ad714x>`
-  :doc:`AD7143: Programmable Controller for Capacitance Touch Sensors </wiki-migration/resources/tools-software/linux-drivers/input-misc/ad714x>`
-  :doc:`AD7147: CapTouch® Programmable Controller for Single-Electrode Capacitance Sensors </wiki-migration/resources/tools-software/linux-drivers/input-misc/ad714x>`
-  :doc:`AD7147A: CapTouch® Programmable Controller for Single-Electrode Capacitance Sensors </wiki-migration/resources/tools-software/linux-drivers/input-misc/ad714x>`
-  :doc:`AD7148: CapTouch® Programmable Controller for Single-Electrode Capacitance Sensors </wiki-migration/resources/tools-software/linux-drivers/input-misc/ad714x>` :adi:`Obsolete <ad7148>`

Input - Touchscreens
~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD7873: Touch Screen Digitizer </wiki-migration/resources/tools-software/linux-drivers/input-touchscreen/ad7873>`
-  :doc:`AD7843: Touch Screen Digitizer </wiki-migration/resources/tools-software/linux-drivers/input-touchscreen/ad7873>`
-  :doc:`AD7877: Touch Screen Controller </wiki-migration/resources/tools-software/linux-drivers/input-touchscreen/ad7877>`
-  :doc:`AD7879: Low Voltage Controller for Touch Screens (SPI) </wiki-migration/resources/tools-software/linux-drivers/input-touchscreen/ad7879>`
-  :doc:`AD7879-1: Low Voltage Controller for Touch Screens (I2C) </wiki-migration/resources/tools-software/linux-drivers/input-touchscreen/ad7879>`
-  :doc:`AD7889: Low Voltage Controller for Touch Screens (SPI) </wiki-migration/resources/tools-software/linux-drivers/input-touchscreen/ad7879>`
-  :doc:`AD7889-1: Low Voltage Controller for Touch Screens (I2C) </wiki-migration/resources/tools-software/linux-drivers/input-touchscreen/ad7879>`
-  `MAX11800: Low-Power, Ultra-Small Resistive Touch-Screen Controllers with I²C/SPI Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/input/touchscreen/max11801_ts.c>`__ `MAX11800 <https://www.maximintegrated.com/MAX11800>`__
-  `MAX11801: Low-Power, Ultra-Small Resistive Touch-Screen Controllers with I²C/SPI Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/input/touchscreen/max11801_ts.c>`__ `MAX11801 <https://www.maximintegrated.com/MAX11801>`__
-  `MAX11802: Low-Power, Ultra-Small Resistive Touch-Screen Controllers with I²C/SPI Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/input/touchscreen/max11801_ts.c>`__ `MAX11802 <https://www.maximintegrated.com/MAX11802>`__
-  `MAX11803: Low-Power, Ultra-Small Resistive Touch-Screen Controllers with I²C/SPI Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/input/touchscreen/max11801_ts.c>`__ `MAX11803 <https://www.maximintegrated.com/MAX11803>`__

LED
~~~

-  :doc:`ADP1650: 1.5 A LED Flash Driver with I2C-Compatible Interface </wiki-migration/resources/tools-software/linux-drivers/leds/adp1650>`
-  `ADP1653: Compact, High Efficiency, High Power, Flash/Torch LED Driver with Dual Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adp1653.c>`__ :adi:`ADP1653`
-  :doc:`ADP5501: Programmable Current Backlight Driver with Ambient Light Sensor Input </wiki-migration/resources/tools-software/linux-drivers/multifunction-device/adp5520>`
-  :doc:`ADP5520: Backlight Driver with I/O Expander </wiki-migration/resources/tools-software/linux-drivers/multifunction-device/adp5520>`
-  :doc:`ADP8860: Charge Pump, 7-Channel Smart LED Driver with I2C Interface </wiki-migration/resources/tools-software/linux-drivers/backlight/adp8860>`
-  :doc:`ADP8861: Charge Pump, 7-Channel Smart LED Driver with I2C Interface </wiki-migration/resources/tools-software/linux-drivers/backlight/adp8860>`
-  :doc:`ADP8863: Charge Pump, 7-Channel Fun Lighting LED Driver </wiki-migration/resources/tools-software/linux-drivers/backlight/adp8860>`
-  :doc:`ADP8870: Charge Pump Parallel Backlight Driver with Image Content PWM Input </wiki-migration/resources/tools-software/linux-drivers/backlight/adp8870>`

Miscellaneous
~~~~~~~~~~~~~

-  :doc:`AD5160: 256 Position SPI Compatible Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5161: 256 Position SPI/I2C Selectable Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5162: 256-Position Dual Channel SPI Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>` :adi:`AD5162`
-  :doc:`AD5165: 256-Position, Ultralow Power 1.8 V Logic-Level Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5170: 256-Position, Two-Time Programmable, I2C Compatible Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5171: 64 Position OTP Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5172: 256-Position, One-Time Programmable, Dual Channel, I2C Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5173: 256-Position, One-Time Programmable, Dual Channel, I2C Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5200: 256-Position Digital Potentiometers </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5201: 33-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5203: 4-Channel, 64-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5204: 4-Channel Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5206: 6-Channel, 256-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5207: Dual, 256 Position, Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5231: Nonvolatile Memory, 1024-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5232: Nonvolatile Memory, Dual, 256-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5233: Nonvolatile, Quad, 64-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5235: Nonvolatile Memory, Dual 1024-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5241: I2C® Compatible Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5242: Dual-Channel, I2C® Compatible, 256 Position, Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5243: 256-Position Dual Channel I2C Compatible Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5245: 256 Position I2C Compatible Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5246: 128 Position I2C Compatible Programmable Resistor in SC70 Package </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5247: 128-Position I2C®-Compatible Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5248: 256-Position Dual Channel I2C Compatible Digital Resistor </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5251: I2C, Nonvolatile Memory, Dual 64-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5252: I2C, Nonvolatile Memory, Dual 256-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5253: Quad 64-Position I2C Nonvolatile Memory Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5254: Quad 256-Position I2C Nonvolatile Memory, Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5255: 3-Channel, Dual 512- and Single 128-Position I2C Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>` :adi:`Obsolete <ad5255>`
-  :doc:`AD5258: Nonvolatile, I2C®-Compatible 64-Position, Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5259: Nonvolatile, I2C Compatible 256-Position, Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5260: +15 V or ±5 V, Single-Channel, SPI Compatible, 256 Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5262: +15 V or ±5 V, Dual-Channel, SPI Compatible, 256 Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5263: Quad, 15 V, 256-Position Digital Potentiometer with Pin-Selectable SPI/I2C </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5270: 1024-Position, 1% Resistor Tolerance Error, SPI Interface and 50-TP Memory Digital Rheostat </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5271: 256-Position, 1% Resistor Tolerance Error, SPI Interface and 50-TP Memory Digital Rheostat </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5272: 1024-Position, 1% Resistor Tolerance Error, Single Channel I2C Interface and 50-TP Memory Digital Rheostat </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5273: 64-Position, One-Time-Programmable (OTP) Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5274: 256-Position, 1% Resistor Tolerance Error, I2C Interface and 50-TP Memory Digital Rheostat </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5280: Single/Dual, +15 V/±5 V, 256-Position, I2C-Compatible Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5282: Single/Dual, +15 V/±5 V, 256-Position, I2C-Compatible Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5290: Compact +30 V / ±15 V 256-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5291: Single Channel, 256-Position, 1% R-Tol, Digital Potentiometer with 20-Times Programmable Memory </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5292: Single Channel, 1024-Position, 1% R-Tol, Digital Potentiometer with 20-Times Programmable Memory </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD5293: Single Channel, 1024-Position, 1% R-Tol, Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD7376: +30 V/±15 V Operation 128-Position Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD8400: Single-Channel Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD8402: 2-Channel Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`AD8403: 4-Channel Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`ADN2850: Nonvolatile Memory, Dual 1024-Position Digital Resistor </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>`
-  :doc:`ADN2860: 3-Channel, Dual 512- and Single 128-Position I²C Digital Potentiometer </wiki-migration/resources/tools-software/linux-drivers/misc/dpot>` :adi:`Obsolete <adn2860>`
-  `DS1620: Digital Thermometer and Thermostat <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/./drivers/char/ds1620.c>`__ `DS1620 <https://www.maximintegrated.com/DS1620>`__

Multifunction Device
~~~~~~~~~~~~~~~~~~~~

-  :doc:`ADP5520: Backlight Driver with I/O Expander </wiki-migration/resources/tools-software/linux-drivers/multifunction-device/adp5520>`
-  :doc:`ADP5501: Programmable Current Backlight Driver with Ambient Light Sensor Input </wiki-migration/resources/tools-software/linux-drivers/multifunction-device/adp5520>`

Multiplexers
~~~~~~~~~~~~

-  :doc:`ADGS1408: Multiplexer driver </wiki-migration/resources/tools-software/linux-drivers/mux/adgs1408>`
-  :doc:`ADGS1409: Multiplexer driver </wiki-migration/resources/tools-software/linux-drivers/mux/adgs1408>`

Networking - MAC802154
~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`ADF7241: Low Power IEEE 802.15.4 Zero-IF 2.4 GHz Transceiver IC </wiki-migration/resources/tools-software/linux-drivers/networking-mac802154/adf7242>`
-  :doc:`ADF7242: Low Power IEEE 802.15.4/Proprietary GFSK/FSK Zero-IF 2.4 GHz Transceiver IC </wiki-migration/resources/tools-software/linux-drivers/networking-mac802154/adf7242>`

Precision Synchronizer
~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`ADF4030: 10-Channel Precision Synchronizer </wiki-migration/resources/tools-software/linux-drivers/iio-synchronizer/adf4030>`

Real Time Clocks
~~~~~~~~~~~~~~~~

-  `DS1216B: SmartWatch RAM (16K/64K) <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1216.c>`__ `DS1216B <https://www.maximintegrated.com/DS1216>`__
-  `DS1216C: SmartWatch RAM (64K/256K) <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1216.c>`__ `DS1216C <https://www.maximintegrated.com/DS1216>`__
-  `DS1216D: SmartWatch RAM (256K/1M) <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1216.c>`__ `DS1216D <https://www.maximintegrated.com/DS1216>`__
-  `DS1216E: SmartWatch ROM (64K/256K) <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1216.c>`__ `DS1216E <https://www.maximintegrated.com/DS1216>`__
-  `DS1216F: SmartWatch ROM (65K/256k/1M) <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1216.c>`__ `DS1216F <https://www.maximintegrated.com/DS1216>`__
-  `DS1216H: SmartWatch RAM (1M/4M) <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1216.c>`__ `DS1216H <https://www.maximintegrated.com/DS1216>`__
-  `DS1286: Watchdog Timekeepers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1286.c>`__ `DS1286 <https://www.maximintegrated.com/DS1286>`__
-  `DS12887: PC Real Time Clock <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-cmos.c>`__ `DS12887 <https://www.maximintegrated.com/DS12887>`__
-  `DS1302: Trickle-Charge Timekeeping Chip <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1302.c>`__ `DS1302 <https://www.maximintegrated.com/DS1302>`__
-  `DS1305: Serial Alarm Real-Time Clock <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1305.c>`__ `DS1305 <https://www.maximintegrated.com/DS1305>`__
-  `DS1306: Serial Alarm Real-Time Clock <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1305.c>`__ `DS1306 <https://www.maximintegrated.com/DS1306>`__
-  `DS1307: 64 x 8, Serial, I²C Real-Time Clock <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1307.c>`__ `DS1307 <https://www.maximintegrated.com/DS1307>`__
-  `DS1308: Low-Current I²C RTC with 56-Byte NV RAM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1307.c>`__ `DS1308 <https://www.maximintegrated.com/DS1308>`__
-  `DS1337: I²C Serial Real-Time Clock <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1307.c>`__ `DS1337 <https://www.maximintegrated.com/DS1337>`__
-  `DS1338: I²C RTC with 56-Byte NV RAM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1307.c>`__ `DS1338 <https://www.maximintegrated.com/DS1338>`__
-  `DS1339: I²C Serial Real-Time Clock <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1307.c>`__ `DS1339 <https://www.maximintegrated.com/DS1339>`__
-  `DS1340: I²C RTC with Trickle Charger <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1307.c>`__ `DS1340 <https://www.maximintegrated.com/DS1340>`__
-  `DS1341: Low-Current I²C RTCs for High-ESR Crystals <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1307.c>`__ `DS1341 <https://www.maximintegrated.com/DS1341>`__
-  `DS1343: Low-Current SPI/3-Wire RTCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1343.c>`__ `DS1343 <https://www.maximintegrated.com/DS1343>`__
-  `DS1344: Low-Current SPI/3-Wire RTCs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1343.c>`__ `DS1344 <https://www.maximintegrated.com/DS1344>`__
-  `DS1347: Low-Current, SPI-Compatible Real-Time Clock <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1347.c>`__ `DS1347 <https://www.maximintegrated.com/DS1347>`__
-  `DS1374: I²C, 32-Bit Binary Counter Watchdog RTC with Trickle Charger and Reset Input/Output <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1374.c>`__ `DS1374 <https://www.maximintegrated.com/DS1374>`__
-  `DS1388: I²C RTC/Supervisor with Trickle Charger and 512 Bytes EEPROM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1307.c>`__ `DS1388 <https://www.maximintegrated.com/DS1388>`__
-  `DS1390: Low-Voltage SPI/3-Wire RTCs with Trickle Charger <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1390.c>`__ `DS1390 <https://www.maximintegrated.com/DS1390>`__
-  `DS1393: Low-Voltage SPI/3-Wire RTCs with Trickle Charger <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1390.c>`__ `DS1393 <https://www.maximintegrated.com/DS1393>`__
-  `DS1394: Low-Voltage SPI/3-Wire RTCs with Trickle Charger <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1390.c>`__ `DS1394 <https://www.maximintegrated.com/DS1394>`__
-  `DS1511: Y2K-Compliant Watchdog Real-Time Clocks <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1511.c>`__ `DS1511 <https://www.maximintegrated.com/DS1511>`__
-  `DS1553: 64kB, Nonvolatile, Year-2000-Compliant Timekeeping RAM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1553.c>`__ `DS1553 <https://www.maximintegrated.com/DS1553>`__
-  `DS1672: I²C 32-Bit Binary Counter RTC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1672.c>`__ `DS1672 <https://www.maximintegrated.com/DS1672>`__
-  `DS1682: Total-Elapsed-Time Recorder with Alarm <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/misc/ds1682>`__ `DS1682 <https://www.maximintegrated.com/DS1682>`__
-  `DS1685: 3V/5V Real-Time Clock <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS1685 <https://www.maximintegrated.com/DS1685>`__
-  `DS1687: 3V/5V Real-Time Clock <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS1687 <https://www.maximintegrated.com/DS1687>`__
-  `DS1688: 3 Volt/5 Volt Serialized Real-Time Clock with NV RAM Control <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS1688 <https://www.maximintegrated.com/DS1688>`__
-  `DS1689: 3 Volt/5 Volt Serialized Real Time Clock with NV RAM Control <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS1689 <https://www.maximintegrated.com/DS1689>`__
-  `DS1691: 3 Volt/5 Volt Serialized Real-Time Clock with NV RAM Control <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS1691 <https://www.maximintegrated.com/DS1691>`__
-  `DS1693: 3 Volt/5 Volt Serialized Real Time Clock with NV RAM Control <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS1693 <https://www.maximintegrated.com/DS1693>`__
-  `DS17285: 3V/5V Real-Time Clocks <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS17285 <https://www.maximintegrated.com/DS17285>`__
-  `DS17287: 3V/5V Real-Time Clocks <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS17287 <https://www.maximintegrated.com/DS17287>`__
-  `DS1742: Y2KC Nonvolatile Timekeeping RAM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1742.c>`__ `DS1742 <https://www.maximintegrated.com/DS1742>`__
-  `DS1743: Y2KC Nonvolatile Timekeeping RAMs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1742.c>`__ `DS1743 <https://www.maximintegrated.com/DS1743>`__
-  `DS17485: 3V/5V Real-Time Clocks <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS17485 <https://www.maximintegrated.com/DS17485>`__
-  `DS17487: 3V/5V Real-Time Clocks <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS17487 <https://www.maximintegrated.com/DS17487>`__
-  `DS17885: 3V/5V Real-Time Clocks <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c>`__ `DS17885 <https://www.maximintegrated.com/DS17885>`__
-  `DS17887: 3V/5V Real-Time Clocks <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1685.c/>`__ `DS17887 <https://www.maximintegrated.com/DS17887>`__
-  `DS2404: EconoRAM Time Chip <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds2404.c>`__ `DS2404 <https://www.maximintegrated.com/DS2404>`__
-  `DS3231: Extremely Accurate I²C-Integrated RTC/TCXO/Crystal <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds1307.c>`__ `DS3231 <https://www.maximintegrated.com/DS3231>`__
-  `DS3232: Extremely Accurate I²C RTC with Integrated Crystal and SRAM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds3232.c>`__ `DS3232 <https://www.maximintegrated.com/DS3232>`__
-  `DS3234: Extremely Accurate SPI Bus RTC with Integrated Crystal and SRAM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-ds3232.c>`__ `DS3234 <https://www.maximintegrated.com/DS3234>`__
-  `MAX6900: I²C-Compatible RTC in a TDFN <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-max6900.c>`__ `MAX6900 <https://www.maximintegrated.com/MAX6900>`__
-  `MAX6902: SPI-Compatible RTC in a TDFN <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-max6902.c>`__ `MAX6902 <https://www.maximintegrated.com/MAX6902>`__
-  `MAX6916: SPI-Compatible RTC with Microprocessor Supervisor, Alarm, and NV RAM Controller <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/rtc/rtc-max6916.c>`__ `MAX6916 <https://www.maximintegrated.com/MAX6916>`__
-  `MAX6369: Pin-Selectable Watchdog Timers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/watchdog/max63xx_wdt.c>`__ `MAX6369 <https://www.maximintegrated.com/MAX6369>`__
-  `MAX6370: Pin-Selectable Watchdog Timers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/watchdog/max63xx_wdt.c>`__ `MAX6370 <https://www.maximintegrated.com/MAX6370>`__
-  `MAX6371: Pin-Selectable Watchdog Timers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/watchdog/max63xx_wdt.c>`__ `MAX6371 <https://www.maximintegrated.com/MAX6371>`__
-  `MAX6372: Pin-Selectable Watchdog Timers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/watchdog/max63xx_wdt.c>`__ `MAX6372 <https://www.maximintegrated.com/MAX6372>`__
-  `MAX6373: Pin-Selectable Watchdog Timers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/watchdog/max63xx_wdt.c>`__ `MAX6373 <https://www.maximintegrated.com/MAX6373>`__
-  `MAX6374: Pin-Selectable Watchdog Timers <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/watchdog/max63xx_wdt.c>`__ `MAX6374 <https://www.maximintegrated.com/MAX6374>`__

Regulators
~~~~~~~~~~

-  :doc:`ADP122: 5.5 V Input, 300 mA, Low Quiescent Current, CMOS Linear Regulator, Fixed Output Voltage </wiki-migration/resources/tools-software/linux-drivers/regulator/adp150>`
-  :doc:`ADP123: 5.5 V Input, 300 mA, Low Quiescent Current, CMOS Linear Regulator, Adjustable Output Voltage </wiki-migration/resources/tools-software/linux-drivers/regulator/adp150>`
-  :doc:`ADP124: 5.5V Input, 500 mA, Low Quiescent Current, CMOS Linear Regulator w/31 Fixed-output Voltages </wiki-migration/resources/tools-software/linux-drivers/regulator/adp150>`
-  :doc:`ADP125: 5.5V Input, 500 mA, Low Quiescent Current, CMOS Linear Regulator w/External Voltage Divider </wiki-migration/resources/tools-software/linux-drivers/regulator/adp150>`
-  :doc:`ADP150: Ultralow Noise, 150 mA CMOS Linear Regulator </wiki-migration/resources/tools-software/linux-drivers/regulator/adp150>`
-  :doc:`ADP5022: Dual 3 MHz, 600 mA Buck Regulator with 150 mA LDO </wiki-migration/resources/tools-software/linux-drivers/regulator/adp150>`
-  :doc:`AD5398: 120 mA, Current Sinking, 10-Bit, I2C D/A Converter </wiki-migration/resources/tools-software/linux-drivers/regulator/ad5398>`
-  :doc:`AD5821: 120 mA, Current Sinking, 10-Bit, I2C® DAC </wiki-migration/resources/tools-software/linux-drivers/regulator/ad5398>`
-  `LTC3589: 8-Output Regulator with Sequencing and I2C <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/ltc3589.c>`__ :adi:`LTC3589`
-  `LTC3676: Power Management Solution for Application Processors <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/ltc3676.c>`__ :adi:`LTC3676`
-  `MAX8952: 2.5A Step-Down Regulator with Remote Sense in 2mm x 2mm WLP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/max8952.c>`__ `MAX8952 <https://www.maximintegrated.com/MAX8952>`__
-  `MAX8660: High-Efficiency, Low-IQ, PMICs with Dynamic Voltage Management for Mobile Applications <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/max8660.c>`__ `MAX8660 <https://www.maximintegrated.com/MAX8660>`__
-  `MAX8649: 1.8A Step-Down Regulator with Remote Sense in 2mm x 2mm WLP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/max8649.c>`__ `MAX8649 <https://www.maximintegrated.com/MAX8649>`__
-  `MAX77826: Highly Integrated PMIC for Camera and Peripherals in 3mm x 3mm WLP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/max77826-regulator.c>`__ `MAX77826 <https://www.maximintegrated.com/MAX77826>`__
-  `MAX1586: High-Efficiency, Low-IQ PMICs with Dynamic Core for PDAs and Smart Phones <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/max1586.c>`__ `MAX1586 <https://www.maximintegrated.com/MAX1586>`__
-  `MAX1587A : High-Efficiency, Low-IQ PMICs with Dynamic Core for PDAs and Smartphones <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/arch/arm/mach-pxa/hx4700.c>`__ `MAX1587A <https://www.maximintegrated.com/MAX1587A>`__
-  `MAX8893A: µPMICs for Multimedia Application Processors in a 3.0mm x 2.5mm WLP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/max8893.c>`__ `MAX8893A <https://www.maximintegrated.com/MAX8893A>`__
-  `MAX8893B: µPMICs for Multimedia Application Processors in a 3.0mm x 2.5mm WLP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/max8893.c>`__ `MAX8893B <https://www.maximintegrated.com/MAX8893B>`__
-  `MAX8893C: µPMICs for Multimedia Application Processors in a 3.0mm x 2.5mm WLP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/max8893.c>`__ `MAX8893C <https://www.maximintegrated.com/MAX8893C>`__
-  `MAX8973A: 9A, Three-Phase Step-Down Switching Regulator <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/regulator/max8973-regulator.c>`__ `MAX8973A <https://www.maximintegrated.com/MAX8973A>`__

Power-Off
^^^^^^^^^

-  `LTC2952: Pushbutton PowerPath Controller with Supervisor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/power/reset/ltc2952-poweroff.c>`__ :adi:`LTC2952`

Serial
~~~~~~

-  `MAX3100: SPI/MICROWIRE-Compatible UART in QSOP-16 <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/tty/serial/max3100.c>`__ `MAX3100 <https://www.maximintegrated.com/MAX3100>`__
-  :doc:`MAX3107: SPI/I²C UART with 128-Word FIFOs </wiki-migration/resources/tools-software/linux-drivers/serial/max310x>`
-  :doc:`MAX3108: SPI/I²C UART with 128-Word FIFOs in WLP </wiki-migration/resources/tools-software/linux-drivers/serial/max310x>`
-  :doc:`MAX3109: Dual Serial UART with 128-Word FIFOs </wiki-migration/resources/tools-software/linux-drivers/serial/max310x>`
-  :doc:`MAX14830: Quad Serial UART with 128-Word FIFOs </wiki-migration/resources/tools-software/linux-drivers/serial/max310x>`

Sound
~~~~~

-  `AD1815: SoundPort® Controller <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/isa/ad1816a/ad1816a.c>`__ :adi:`Obsolete <ad1815>`
-  `AD1816: SoundPort® Controller <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/isa/ad1816a/ad1816a.c>`__ :adi:`Obsolete <ad1816>`
-  `AD1819: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1819>`
-  `AD1835: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/ad1836.c>`__ :adi:`Obsolete <ad1835>`
-  :doc:`AD1835A: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1835a>`
-  `AD1836: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/ad1836.c>`__ :adi:`Obsolete <ad1836>`
-  :doc:`AD1836A: Multichannel 96 kHz Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1835a>`
-  `AD1837: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/ad1836.c>`__ :adi:`Obsolete <ad1837>`
-  :doc:`AD1837A: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta CODEC </wiki-migration/resources/tools-software/linux-drivers/sound/ad1835a>` :adi:`Obsolete <AD1837A>`
-  :doc:`AD1838: 2 ADC, 6 DAC 96 kHz, 24-Bit Sigma Delta Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1835a>` :adi:`Obsolete <AD1838>`
-  :doc:`AD1838A: 2 ADC, 6 DAC 96 kHz, 24-Bit Sigma Delta Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1835a>` :adi:`Obsolete <AD1838A>`
-  `AD1839: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/ad1836.c>`__ :adi:`Obsolete <ad1839>`
-  :doc:`AD1839A: 2 ADC, 6 DAC 96 kHz, 24-Bit Sigma Delta Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1835a>` :adi:`Obsolete <ad1839a>`
-  `AD1843: Serial-Port 16-Bit SoundComm Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/mips/ad1843.c>`__ :adi:`Obsolete <ad1843>`
-  `AD1845: Parallel-Port 16-Bit SoundPort® Stereo Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/isa/sscape.c>`__ :adi:`Obsolete <ad1845>`
-  `AD1847: Serial-Port 16-Bit SoundPort Stereo Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/isa/wss/wss_lib.c>`__ :adi:`Obsolete <ad1847>`
-  `AD1848: Parallel-Port 16-Bit SoundPort Stereo Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/isa/ad1848/ad1848.c>`__ :adi:`Obsolete <ad1848>`
-  `AD1852: Stereo, 24-Bit, 192 kHz, Multibit Sigma Delta DAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/rme96.c>`__ :adi:`ad1852`
-  `AD1855: Stereo, 96 kHz, Multibit Sigma Delta <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/rme96.c>`__ :adi:`Obsolete <ad1855>`
-  `AD1881A: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1881a>`
-  `AD1881: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1881>`
-  `AD1884: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1884>`
-  `AD1885: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1885>`
-  `AD1886A: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1886a>`
-  `AD1887: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1887>`
-  `AD1888: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1888>`
-  :doc:`AD1933: 8 DAC with PLL, 192 kHz, 24-Bit Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1936>`
-  :doc:`AD1934: 8 DAC with PLL, 192 kHz, 24-Bit Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1936>`
-  :doc:`AD1936: 4 ADC/8 DAC, 192 kHz, 24-Bit CODEC with PLL, Single-Ended Output, I2C Control </wiki-migration/resources/tools-software/linux-drivers/sound/ad1936>` :adi:`Obsolete <ad1936>`
-  :doc:`AD1937: Four ADCs/Eight DACs with PLL, 192 kHz, 24-Bit Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1936>`
-  :doc:`AD1938: 4 ADC/8 DAC with PLL, 192 kHz, 24-Bit CODEC </wiki-migration/resources/tools-software/linux-drivers/sound/ad1936>`
-  :doc:`AD1939: 4 ADC/8 DAC with PLL, 192 kHz, 24-Bit Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1936>`
-  `AD1980: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1980>`
-  `AD1981A: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1981a>`
-  `AD1981B: AC’97 SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/ac97/ac97_codec.c>`__ :adi:`Obsolete <ad1981B>`
-  `AD1983: HD Audio SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/hda/patch_analog.c>`__ :adi:`Obsolete <ad1983>`
-  `AD1984B: HD Audio SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/hda/patch_analog.c>`__ :adi:`Obsolete <ad1984b>`
-  `AD1984: HD Audio SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/hda/patch_analog.c>`__ :adi:`Obsolete <ad1984>`
-  `AD1985: HD Audio SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/hda/patch_analog.c>`__ :adi:`Obsolete <ad1985>`
-  `AD1986A: HD Audio SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/hda/patch_analog.c>`__ :adi:`Obsolete <ad1986a>`
-  `AD1986: HD Audio SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/hda/patch_analog.c>`__ :adi:`Obsolete <ad1986>`
-  `AD1988A: HD Audio SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/hda/patch_analog.c>`__ :adi:`Obsolete <ad1988A>`
-  `AD1988B: HD Audio SoundMAX® Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/pci/hda/patch_analog.c>`__ :adi:`Obsolete <ad1988B>`
-  :doc:`AD73311: Single Voiceband Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad73322>`
-  :doc:`AD73322: Dual Voiceband Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad73322>`
-  :doc:`AD73322L: Dual-Channel, 3 V Front-End Processor for General Purpose Applications Including Speech and Telephony </wiki-migration/resources/tools-software/linux-drivers/sound/ad73322>`
-  :doc:`ADAU1328: 2 ADC/8 DAC with PLL, 192 kHz, 24-Bit Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ad1936>`
-  :doc:`ADAU1361: Stereo, Low Power, 96 kHz, 24-Bit Audio Codec with Integrated PLL </wiki-migration/resources/tools-software/linux-drivers/sound/adau1361>`
-  :doc:`ADAU1372: Quad ADC, Dual DAC, Low Latency, Low Power Codec </wiki-migration/resources/tools-software/linux-drivers/sound/adau1372>`
-  :doc:`ADAU1373: Low Power Codec with Speaker and Headphone Amplifier </wiki-migration/resources/tools-software/linux-drivers/sound/adau1373>` :adi:`Obsolete <adau1373>`
-  :doc:`ADAU1381: Low-noise Stereo Codec with Enhanced Recording and Playback Processing </wiki-migration/resources/tools-software/linux-drivers/sound/adau1381>` :adi:`Obsolete <adau1381>`
-  :doc:`ADAU1401A: SigmaDSP® 28/56-Bit Audio Processor with Two ADCs and Four DACs </wiki-migration/resources/tools-software/linux-drivers/sound/adau1701>`
-  :doc:`ADAU1401: SigmaDSP® 28/56-Bit Audio Processor with Two ADCs and Four DACs </wiki-migration/resources/tools-software/linux-drivers/sound/adau1701>`
-  :doc:`ADAU1461: SigmaDSP Stereo, Automotive Low Power, 96 kHz, 24-Bit Audio Codec with Integrated PLL </wiki-migration/resources/tools-software/linux-drivers/sound/adau1361>` :adi:`Obsolete <adau1461>`
-  :doc:`ADAU1701: SigmaDSP® 28/56-Bit Audio Processor with Two ADCs and Four DACs </wiki-migration/resources/tools-software/linux-drivers/sound/adau1701>`
-  :doc:`ADAU1702: SigmaDSP® 28/56-Bit Audio Processor with Two ADCs and Four DACs </wiki-migration/resources/tools-software/linux-drivers/sound/adau1701>`
-  :doc:`ADAU1761: SigmaDSP® Stereo, Low Power, 96 kHz, 24-Bit Audio Codec with Integrated PLL </wiki-migration/resources/tools-software/linux-drivers/sound/adau1361>`
-  :doc:`ADAU1781: SigmaDSP Low-noise Stereo Audio Codec for Portable Applications </wiki-migration/resources/tools-software/linux-drivers/sound/adau1381>` :adi:`Obsolete <adau1781>`
-  :doc:`ADAU1961: Automotive Stereo, Low Power, 96 kHz, 24-Bit Audio Codec with Integrated PLL </wiki-migration/resources/tools-software/linux-drivers/sound/adau1361>`
-  :doc:`ADAU1977: Quad ADC with Diagnostics (10V Input) </wiki-migration/resources/tools-software/linux-drivers/sound/adau1977>`
-  :doc:`ADAU1978: Quad ADC (2V Input) </wiki-migration/resources/tools-software/linux-drivers/sound/adau1977>`
-  :doc:`ADAU1979: Quad ADC (4.5V Input) </wiki-migration/resources/tools-software/linux-drivers/sound/adau1977>`
-  :doc:`ADAU7002: Stereo PDM to I2S or TDM Conversion IC </wiki-migration/resources/tools-software/linux-drivers/sound/adau7002>`
-  :doc:`ADAU7118: 8 Channel, PDM to I2S or TDM Conversion IC </wiki-migration/resources/tools-software/linux-drivers/sound/adau7118>`
-  :doc:`ADAV801: Audio Codec for Recordable DVD </wiki-migration/resources/tools-software/linux-drivers/sound/adav801>`
-  :doc:`ADAV803: Audio Codec for Recordable DVD </wiki-migration/resources/tools-software/linux-drivers/sound/adav801>`
-  `MAX2165: Single-Conversion DVB-H Tuner <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/tuners/max2165.c>`__ `MAX2165 <https://www.maximintegrated.com/MAX2165>`__
-  `MAX2175: RF to Bits Automotive Radio Tuner <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/i2c/max2175.c>`__ `MAX2175 <https://www.maximintegrated.com/MAX2175>`__
-  `MAX9759: 3.2W, High-Efficiency, Low-EMI, Filterless, Class D Audio Amplifier <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max9759.c>`__ `MAX9759 <https://www.maximintegrated.com/MAX9759>`__
-  `MAX9768: 10W Mono Class D Speaker Amplifier with Volume Control <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/max9768.c>`__ `MAX9768 <https://www.maximintegrated.com/MAX9768>`__
-  `MAX98088: Stereo Audio Codec with FlexSound Technology <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max98088.c>`__ `MAX98088 <https://www.maximintegrated.com/MAX98088>`__
-  `MAX98089: Stereo Audio Codec with FlexSound Technology <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max98088.c>`__ `MAX98089 <https://www.maximintegrated.com/MAX98089>`__
-  `MAX98090: Ultra-Low Power Stereo Audio Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/max98090.c>`__ `MAX98090 <https://www.maximintegrated.com/MAX98090>`__
-  `MAX98095: Audio Hub with FlexSound Processor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max98095.c>`__ `MAX98095 <https://www.maximintegrated.com/MAX98095>`__
-  `MAX98357A: Tiny, Low-Cost, PCM Class D Amplifier with Class AB Performance <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/max98357a.c>`__ `MAX98357A <https://www.maximintegrated.com/MAX98357A>`__
-  `MAX98360A: Tiny, Cost-Effective, Plug-and-Play Digital Class-D Amplifier <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/intel/boards/sof_da7219_max98373.c>`__ `MAX98360A <https://www.maximintegrated.com/MAX98360A>`__
-  `MAX98371: Digital Input Class D Speaker Amplifier with Dynamic Headroom Tracking <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max98371.c>`__ `MAX98371 <https://www.maximintegrated.com/MAX98371>`__
-  `MAX98390: Boosted Class-D Amplifier with Integrated Dynamic Speaker Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max98390.c>`__ `MAX98390 <https://www.maximintegrated.com/MAX98390>`__
-  `MAX9850: Stereo Audio DAC with DirectDrive® Headphone Amplifier <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max9850.c>`__ `MAX9850 <https://www.maximintegrated.com/MAX9850>`__
-  `MAX9860: 16-Bit Mono Audio Voice Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max9860.c>`__ `MAX9860 <https://www.maximintegrated.com/MAX9860>`__
-  `MAX9867: Low-Power, Stereo Audio Codec <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max9867.c>`__ `MAX9867 <https://www.maximintegrated.com/MAX9867>`__
-  `MAX9877: Low RF Susceptibility Mono Audio Subsystem with DirectDrive Headphone Amplifier <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//sound/soc/codecs/max9877.c>`__ `Obsolete <https://www.maximintegrated.com/MAX9877>`__
-  `SSM2305: Filterless, High Efficiency, Mono 2.8 W, Class-D Audio Amplifier <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/ssm2305.c>`__ :adi:`SSM2305`
-  :doc:`SSM2518: Digital Input Stereo, 2 W, Class-D Audio Power Amplifier </wiki-migration/resources/tools-software/linux-drivers/sound/ssm2518>`
-  :doc:`SSM2602: Low Power Audio Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ssm2602>`
-  :doc:`SSM2603: Low Power Audio Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ssm2602>`
-  :doc:`SSM2604: Low Power Audio Codec </wiki-migration/resources/tools-software/linux-drivers/sound/ssm2602>`
-  :doc:`SSM4567: Digital 2.5 W, 5.1 V, Boost Class-D Audio Amplifier with Output Sensing </wiki-migration/resources/tools-software/linux-drivers/sound/ssm4567>`

Transceiver
~~~~~~~~~~~

-  `DS26522: Dual T1/E1/J1 Transceiver <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/net/wan/slic_ds26522.c>`__ `DS26522 <https://www.maximintegrated.com/DS26522>`__

USB
~~~

-  `MAX3420E: USB Peripheral Controller with SPI Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/usb/gadget/udc/max3420_udc.c>`__ `MAX3420E <https://www.maximintegrated.com/MAX3420E>`__
-  `MAX3421E: USB Peripheral/Host Controller with SPI Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/usb/host/max3421-hcd.c>`__ `MAX3421E <https://www.maximintegrated.com/MAX3421E>`__
-  `MAX3355E: ±15kV ESD-Protected USB On-the-Go Charge Pump and Comparators in UCSP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/extcon/extcon-max3355.c>`__ `MAX3355E <https://www.maximintegrated.com/MAX3355E>`__
-  `MAX9490: USB to 1-Wire/iButton Adapter <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/masters/ds2490.c>`__ `DS9490 <https://www.maximintegrated.com/DS9490>`__

Video
~~~~~

-  `AD9389B: High Performance HDMI®/DVI Transmitter <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/ad9389b.c>`__ :adi:`AD9389B`
-  `AD9889B: High Performance HDMI®/DVI Transmitter <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/ad9389b.c>`__ :adi:`AD9889B`
-  `ADV7123: CMOS, 330 MHz Triple 10-Bit High Speed Video DAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpu/drm/bridge/simple-bridge.c>`__ :adi:`ADV7123`
-  `ADV7170: CMOS, 330 MHz Triple 10-Bit High Speed Video DAC <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7170.c>`__ :adi:`Obsolete <ADV7170>`
-  `ADV7171: Digital PAL/NTSC Video Encoder with 10-Bit SSAF™ and Advanced Power Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7170.c>`__ :adi:`ADV7171`
-  `ADV7175: Digital PAL/NTSC Video Encoder with 10-Bit SSAF™ and Advanced Power Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7175.c>`__ :adi:`Obsolete <ADV7175>`
-  `ADV7175A: Digital PAL/NTSC Video Encoder with 10-Bit SSAF™ and Advanced Power Management <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7175.c>`__ :adi:`Obsolete <ADV7175A>`
-  `ADV7176: Integrated Digital CCIR-601 YCrCb to PAL/NTSC Video Encoder <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7170.c>`__ :adi:`ADV7176`
-  `ADV7180: 10-Bit, 4× Oversampling SDTV Video Decoder <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7180.c>`__ :adi:`ADV7180`
-  `ADV7182: 10-Bit, SDTV Video Decoder with Differential Inputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/i2c/adv7180.c>`__ :adi:`ADV7182`
-  `ADV7182A: 10-Bit, SDTV Video Decoder with Differential Inputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/i2c/adv7180.c>`__ :adi:`ADV7182A`
-  `ADV7183: Advanced Video Decoder with 9-Bit ADC, & Component Input Support <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7183.c>`__ :adi:`Obsolete <ADV7183>`
-  `ADV7280: 10-Bit, 4× Oversampled SDTV Video Decoder with Deinterlacer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/i2c/adv7180.c>`__ :adi:`ADV7280`
-  `ADV7280A: 10-Bit, 4× Oversampled SDTV Video Decoder with Deinterlacer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/i2c/adv7180.c>`__ :adi:`ADV7280A`
-  `ADV7281: 10-Bit, 4× Oversampled SDTV Video Decoder with Differential Inputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/i2c/adv7180.c>`__ :adi:`ADV7281`
-  `ADV7281A: 10-Bit, 4× Oversampled SDTV Video Decoder with Differential Inputs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/i2c/adv7180.c>`__ :adi:`ADV7281A`
-  `ADV7282: 10-Bit, 4× Oversampled SDTV Video Decoder with Differential Inputs and Deinterlacer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/i2c/adv7180.c>`__ :adi:`ADV7282`
-  `ADV7282A: 10-Bit, 4× Oversampled SDTV Video Decoder with Differential Inputs and Deinterlacer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree//drivers/media/i2c/adv7180.c>`__ :adi:`ADV7282A`
-  `ADV7481: Integrated Video Decoder and Dual-Mode HDMI/MHL Receiver <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv748x/adv748x-core.c>`__ :adi:`ADV7481`
-  `ADV7482: Integrated Video Decoder and HDMI Receiver <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv748x/adv748x-core.c>`__ :adi:`ADV7482`
-  `ADV7343: Multiformat Video Encoder with Six, 11-Bit, 297 MHz DACs <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7343.c>`__ :adi:`ADV7343`
-  `ADV7393: Low Power, Chip Scale 10-Bit SD/HD Video Encoder <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7393.c>`__ :adi:`ADV7393`
-  `ADV7604: 12-Bit, Deep Color HDMI v1.3 Receiver with Analog Interface <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7604.c>`__ :adi:`ADV7604`
-  `ADV7611: Low Power 165 MHz HDMI Receiver <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7604.c>`__ :adi:`ADV7611`
-  `ADV7612: Dual Port, Xpressview, 225 MHz HDMI Receiver <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7604.c>`__ :adi:`ADV7612`
-  `AD9389B: High Performance HDMI®/DVI Transmitter <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/ad9389b.c>`__ :adi:`AD9389B`
-  `ADV7842: Dual HDMI 1.4 Fast Switching Receiver with 12-Bit, 170 MHz Video and Graphics Digitizer and 3D Comb Filter Decoder <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7842.c>`__ :adi:`ADV7842`
-  `ADV7844: Quad HDMI 1.4 Fast Switching Receiver with 12-Bit, 170 MHz Video and Graphics Digitizer and 3D Comb Filter Decoder <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/media/i2c/adv7842.c>`__ :adi:`ADV7844`
-  :doc:`ADV7511: 225 MHZ, HIGH PERFORMANCE HDMI® TRANSMITTER WITH ARC </wiki-migration/resources/tools-software/linux-drivers/drm/adv7511>`
-  :doc:`ADV7511W: 165 MHZ HIGH PERFORMANCE HDMI TRANSMITTER </wiki-migration/resources/tools-software/linux-drivers/drm/adv7511>`
-  :doc:`ADV7513: 165 MHZ HIGH PERFORMANCE HDMI TRANSMITTER </wiki-migration/resources/tools-software/linux-drivers/drm/adv7511>`
-  :doc:`ADV7533: MIPI/DSI Receiver with HDMI Transmitter </wiki-migration/resources/tools-software/linux-drivers/drm/adv7511>`
-  :doc:`ADV7535: MIPI/DSI Receiver with HDMI Transmitter </wiki-migration/resources/tools-software/linux-drivers/drm/adv7511>`

1-Wire Controller
~~~~~~~~~~~~~~~~~

-  `DS9490: USB to 1-Wire/iButton Adapter <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/masters/ds2490.c>`__ `DS9490 <https://www.maximintegrated.com/DS9490>`__
-  `DS2490: USB to 1-Wire Bridge Chip <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/masters/ds2490.c>`__ `DS2490 <https://www.maximintegrated.com/DS2490>`__
-  `DS2482-100: Single-Channel 1-Wire Master <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/masters/ds2482.c>`__ `DS2482-100 <https://www.maximintegrated.com/DS2482-100>`__
-  `DS2482-800: 8-Channel 1-Wire Master <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/masters/ds2482.c>`__ `DS2482-800 <https://www.maximintegrated.com/DS2482-800>`__

1-Wire Peripheral
~~~~~~~~~~~~~~~~~

-  `DS28E17: 1-Wire®-to-I2C Master Bridge <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds28e17.c>`__ `DS28E17 <https://www.maximintegrated.com/DS28E17>`__
-  `DS28E04-100: 4096-Bit Addressable 1-Wire EEPROM with PIO <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds28e04.c>`__ `DS28E04-100 <https://www.maximintegrated.com/DS28E04-100>`__
-  `DS28E05: 1-Wire EEPROM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds2805.c>`__ `DS28E05 <https://www.maximintegrated.com/DS28E05>`__
-  `DS2438: Smart Battery Monitor <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds2438.c>`__ `DS2438 <https://www.maximintegrated.com/DS2438>`__
-  `DS2433: 4Kb 1-Wire EEPROM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds2433.c>`__ `DS2433 <https://www.maximintegrated.com/DS2433>`__
-  `DS2431: 1024-Bit 1-Wire EEPROM <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds2431.c>`__ `DS2431 <https://www.maximintegrated.com/DS2431>`__
-  `DS2423: 4kbit 1-Wire RAM with Counter <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds2423.c>`__ `DS2423 <https://www.maximintegrated.com/DS2423>`__
-  `DS2413: 1-Wire Dual Channel Addressable Switch <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds2413.c>`__ `DS2413 <https://www.maximintegrated.com/DS2413>`__
-  `DS2411: Silicon Serial Number with VCC Input <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_smem.c>`__ `DS2411 <https://www.maximintegrated.com/DS2411>`__
-  `DS2405: Addressable Switch <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds2405.c>`__ `DS2405 <https://www.maximintegrated.com/DS2405>`__
-  `DS2406: Dual Addressable Switch Plus 1Kb Memory <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds2406.c>`__ `DS2406 <https://www.maximintegrated.com/DS2406>`__
-  `DS2408: 1-Wire 8-Channel Addressable Switch <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds2408.c>`__ `DS2408 <https://www.maximintegrated.com/DS2408>`__
-  `DS2401: Silicon Serial Number <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_smem.c>`__ `DS2401 <https://www.maximintegrated.com/DS2401>`__
-  `DS1990A: iButton Serial Number <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_smem.c>`__ `DS1990A <https://www.maximintegrated.com/DS1990A>`__
-  `DS2502: 1Kb Add-Only Memory <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds250x.c>`__ `DS2502 <https://www.maximintegrated.com/DS2502>`__
-  `DS2505: 16Kb Add-Only Memory <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds250x.c>`__ `DS2505 <https://www.maximintegrated.com/DS2505>`__
-  `DS1822: Econo 1-Wire Digital Thermometer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_therm.c>`__ `ds1822 <https://www.maximintegrated.com/ds1822>`__
-  `DS1825: Programmable Resolution 1-Wire Digital Thermometer With 4-Bit ID <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_therm.c>`__ `DS1825 <https://www.maximintegrated.com/DS1825>`__
-  `DS18S20: 1-Wire Parasite-Power Digital Thermometer <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_therm.c>`__ `DS18S20 <https://www.maximintegrated.com/DS18S20>`__
-  `DS28EA00: 1-Wire Digital Thermometer with Sequence Detect and PIO <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_therm.c>`__ `DS28EA00 <https://www.maximintegrated.com/DS28EA00>`__
-  `DS28E04-100: 4096-Bit Addressable 1-Wire EEPROM with PIO <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/w1/slaves/w1_ds28e04.c>`__ `DS28E04-100 <https://www.maximintegrated.com/DS28E04-100>`__

.. [1]
   IDC study/survey from over 5000 developers in 116 countries. Open Source in Global Software: Market Impact, Disruption, and Business Models. 2006.
