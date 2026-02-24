.. _libm2k m2kcli:

Command line utility
""""""""""""""""""""

m2kcli is a command-line frontend for libm2k.

m2kcli is composed from many commands, each representing a major functionality
of the ADALM-2000:

- analog-in: oscilloscope and voltmeter
- analog-out: signal generator
- digital: logic analyzer and pattern generator
- power-supply

m2kcli offers an easy way to communicate with other devices using digital
protocols such as:

- SPI
- I²C
- UART
- UART Terminal

How to install it?
==================

Windows
-------

In the *Select Additional Tasks* window, select *Install libm2k tools* option.

How to build it?
================

Build and install libm2k. Instruction can be found
:ref:`here <libm2k>`. Make sure to enable tools
option.

Enable tools on Linux or OSX
----------------------------

.. shell::

   ~/libm2k/build
   $cmake -DENABLE_TOOLS=ON ../

Enable tools on Windows
-----------------------

Check the *ENABLE_TOOLS* box in CMake GUI.

Commands
========

All commands require an URI. URI describes the context location.

* auto - establish an USB connection detecting the available USB
* usb:XX.XX.X
* ip: XXX.XXX.XXX.XXX - standard ip address 192.168.2.1
* serial:/dev/ttyAMA0,115200n8
* local:

Options:

| **help**
| Show the help message and exit.

| **quiet**
| Return the result only.

analog-in
---------

synopsis
~~~~~~~~

.. code:: bash

   m2kcli analog-in <uri>
                    [-h | --help]
                    [-q | --quiet]
                    [-C | --calibrate]
                    [-v | --voltage channel=<index>,... raw=<value>]
                    [-c | --capture channel=<index>,... buffer_size=<size> raw=<value> [nb_samples=<value>] [format=<type>]]
                    [-g | --get <attribute>...]
                    [-G | --get-channel channel=<index>,... <attribute>...]
                    [-s | --set <attribute>=<value>...]
                    [-S | --set-channel channel=<index> <attribute>=<value>...]


description
~~~~~~~~~~~

analog-in command controls the analogical input component, having two main
functions: oscilloscope and voltmeter. The available channels for analog in are
channel 0 and channel 1.

Pinout:

| ▤ ▥ □ □ □ □ □ □ □ □ □ □ □ □ □
| ▤ ▥ □ □ □ □ □ □ □ □ □ □ □ □ □

Options:

**calibrate**

Calibrate the ADC.

**voltage**

Return the voltage of the given channels. The result is printed to standard
output.

Mandatory arguments:

* channel - one or both indexes are possible to be specified
* raw - 0 = processed values, 1 = raw values

Examples:

Retrieve the average voltage of both channels as raw values:

.. shell::

   $m2kcli analog-in auto -v channel=0,1 raw=1

Retrieve only the processed voltage for the first channel:

.. shell::

   $m2kcli analog-in auto --voltage channel=0 raw=0 -q

--------------

**capture**

Return a specific number of samples. The result is printed to standard output.

Mandatory arguments:

* channel - one or both indexes are possible to be specified
* buffer_size - the number of samples into one iio_buffer
* raw - 0 = processed values, 1 = raw values

Optional arguments:

* nb_samples – integer value that represents the number of samples to be
  captured.
  Default value is 0, continuously capturing samples until the process is force stopped
* format – csv/binary. The way the samples will be printed. Default type is csv

Examples:

Capture 2048 unprocessed samples from both channels using a buffer of length
1024 and save them into a binary file:

.. shell::

   $m2kcli analog-in auto --capture channel=0,1 buffer_size=1024 \
   $    nb_samples=2048 raw=1 format=binary > file.bin

Continuous samples capturing:

.. shell::

   $m2kcli analog-in ip:192.168.2.1 -c channel=1 buffer_size=1024 raw=0

--------------

**get**

Return the value of the global attributes. Enumerate the attributes with a space
between them.

Attributes:

* sampling_frequency
* oversampling_ratio
* trigger_source
* trigger_delay

Examples:

Display all global attributes

.. shell::

   $m2kcli analog-in auto --get all

Get the sampling frequency and the oversampling ratio

.. shell::

   $m2kcli analog-in auto -g sampling_frequency oversampling_ratio

--------------

**get-channel**

Return the value of the attributes corresponding the the given channels.

Mandatory arguments:

* channel - one or both indexes are possible to be specified

Attributes:

* range
* trigger_level
* trigger_condition
* trigger_mode
* trigger_hysteresis

Examples:

Get all attributes of both channels

.. shell::

   $m2kcli analog-in --get-channel channel=0,1 all

Get the triggering condition of the second channel

.. shell::

   $m2kcli analog-in -G channel=1 trigger_condition

--------------

**set**

Set the value of the global attributes.

Attributes:

* sampling_frequency - {1000 | 10000 | 100000 | 1000000 | 10000000 | 100000000}
* oversampling_ratio - integer
* trigger_source - {channel_1 | channel_2 | channel_1_or_channel_2 | channel_1_and_channel_2 | channel_1_xor_channel_2}
* trigger_delay - integer
* kernel_buffers - integer

Examples:

Set sampling_frequency and trigger_source

.. shell::

   $m2kcli analog-in auto --set sampling_frequency=100000 trigger_source=channel_1

--------------

**set-channel**

Set the value of the attributes corresponding to the given channels.

Mandatory arguments:

* channel - one or both indexes are possible to be specified

Attributes:

* range - {high | low}
* trigger_level - integer
* trigger_condition - {rising_edge | falling_edge | low_level | high_level}
* trigger_mode - {always | analog | digital | digital_or_analog | digital_and_analog | digital_xor_analog | n_digital_or_analog | n_digital_and_analog | n_digital_xor_analog}
* trigger_hysteresis - double (volts)

Examples:

Set the range and the trigger_mode

.. shell::

   $m2kcli analog-in auto --set-channel channel=1 range=high trigger_mode=analog

--------------

analog-out
----------

synopsis
~~~~~~~~

::

    m2kcli analog-out <uri>
                      [-h | --help]
                      [-q | --quiet]
                      [-C | --calibrate]
                      [-9 | --generate channel=<index>,... cyclic=<value> raw=<value> [buffer_size=<size>] [format=<type>]]
                      [-G | --get-channel channel=<index> <attribute>...]
                      [-S | --set-channel channel=<index> <attribute>=<value>...]

description
~~~~~~~~~~~

analog-out command controls the analogical output component, having the main
functions of a signal generator. The available channels for analog out are
channel 0 and channel 1.

Pinout:

| □ □ □ □ ▤ □ □ □ □ □ □ □ □ □ □
| □ □ □ □ ▥ □ □ □ □ □ □ □ □ □ □

Options:

| **calibrate**
| Calibrate both DACs.

| **generate**
| Generate signals for the specified channels. The samples are read from the
  standard input.

Mandatory arguments:

* channel - one or both indexes are possible to be specified
* cyclic - 0 = non-cyclic mode, 1 = cyclic mode
* raw - 0 = processed values, 1 = raw values

Optional arguments:

* buffer_size - size of the output buffer; default value is 256
* format - csv/binary. The way the samples will be read. Default type is csv

Examples:

Generate a cyclic signal based on the samples located in file.csv

.. shell::

   $m2kcli analog-out auto --generate channel=0 \
   $    cyclic=1 raw=0 buffer_size=1024 < file.csv

--------------

**get-channel**

Return the value of the attributes corresponding to the given channel.

Mandatory arguments:

* channel - one or both indexes are possible to be specified

Attributes:

* sampling_frequency
* oversampling_ratio

Examples:

Get all attributes of the first channel

.. shell::

   $m2kcli analog-out auto -G channel=0 all

--------------

**set-channel**

Set the value of the attributes corresponding to the given channel.

Mandatory arguments:

* channel - one or both indexes are possible to be specified

Attributes:

* sampling_frequency - {750 | 7500 | 75000 | 750000 | 7500000 | 75000000}
* oversampling_ratio - integer

Examples:

Set the sampling frequency of both channel to 7500

.. shell::

   $m2kcli analog-out auto -S channel=0,1 sampling_frequency=7500

--------------

digital
-------

synopsis
~~~~~~~~

::

    m2kcli digital <uri>
                    [-h | --help]
                    [-q | --quiet]
                    [-c | --capture buffer_size=<size> [nb_samples=<value>] [format=<type>]]
                    [-9 | --generate channel=<index>,... cyclic=<value> [buffer_size=<size>] [format=<type>]]
                    [-g | --get <attribute>...]
                    [-G | --get-channel channel=<index>,... <attribute>...]
                    [-s | --set <attribute>=<value>...]
                    [-S | --set-channel channel=<index>,... <attribute>=<value>...]

.. _description-2:

description
~~~~~~~~~~~

digital command controls the digital input and output component, having two main
functions: logic analyzer and pattern generator. The available channels for
digital are between 0 and 15.

Pinout:

| □ □ □ □ □ □ □ ■ ■ ■ ■ ■ ■ ■ ■
| □ □ □ □ □ □ □ ■ ■ ■ ■ ■ ■ ■ ■

Options:

| **capture**
| Return a specific number of samples. The result is printed to standard output.

Mandatory arguments:

* buffer_size - the number of samples into one iio_buffer

Optional arguments:

* nb_samples - integer value that represents the number of samples to be captured.
  Default value is 0 , continuously capturing samples until the program is force
  stopped
* format - csv/binary. The way the samples will be printed. Default type is csv

Examples:

Capture 100 samples

.. shell::

   $m2kcli digital auto -c buffer_size=60 nb_samples=100

Capture samples continuously, binary format

.. shell::

   $m2kcli digital auto -c buffer_size=1000 format=binary

--------------

**generate**

Generate digital signals for the specified channels.The samples are read from
the standard input.

Mandatory arguments:

* channel - one or more indexes are possible to be specified
* cyclic - 0 = non-cyclic mode, 1 = cyclic mode

Optional arguments:

* buffer_size - size of the output buffer; default value is 256
* format - csv/binary. The way the samples will be read. Default type is csv

Examples:

Generate a cyclic signal for the given channels based on the samples located in file.csv

.. shell::

   $m2kcli digital auto -9 channel=0,1,4,5,14 cyclic=1 < file.csv

--------------

**get**

Return the value of the global attributes.

Attributes:

* sampling_frequency_in
* sampling_frequency_out
* trigger_delay
* trigger_mode

Examples:

Get all attributes

.. shell::

   $m2kcli digital auto -g all

--------------

**get-channel**

Return the value of the attributes corresponding the the given channels.

Mandatory arguments:

::

    channel - one or more indexes are possible to be specified

Attributes:

* value
* output_mode
* trigger_condition

Examples:

Get all attributes for the given channels

.. shell::

   $m2kcli digital auto --get-channel channel=0,1,2,3,4 all

--------------

**set**

Set the value of the global attributes.

Attributes:

* sampling_frequency_in - double
* sampling_frequency_out - double
* trigger_delay - integer
* trigger_mode - {or | and}

Examples:

Set the trigger mode to 'or'

.. shell::

   $m2kcli digital auto -s trigger_mode=or

--------------

**set-channel**

Set the value of the attributes corresponding to the given channels.

Mandatory attributes:

* channel - one or more indexes are possible to be specified

Attributes:

* value - {0 | 1}
* output_mode - {open_drain | push_pull}
* trigger_condition - {rising_edge | falling_edge | low_level | high_level | any_edge | no_trigger}

Examples:

Set for the 7th channel the triggering condition to rising edge

.. shell::

   $m2kcli digital auto -S channel=7 trigger_condition=rising_edge

--------------

power-supply
------------

synopsis
~~~~~~~~

::

    m2kcli power-supply <uri>
                        [-h | --help]
                        [-q | --quiet]
                        [-C | --calibrate]
                        [-c | --capture channel=<index>...]
                        [-9 | --generate channel=<index>,... value=<value>]

description
~~~~~~~~~~~

power-supply command controls the power supply. The available channels for power
supply are channel 0 and channel 1.

Pinout:

| □ □ □ ▤ □ □ □ □ □ □ □ □ □ □ □
| □ □ □ ▥ □ □ □ □ □ □ □ □ □ □ □

Options:

| **calibrate**
| Calibrate the ADC.

| **capture**
| Return the value, read by the power supply. The result is printed to standard
  output.

Mandatory arguments:

* channel - one or both indexes are possible to be specified

Examples:

Get the voltage of both channels

.. shell::

   $m2kcli power-supply auto --capture channel=0,1

--------------

generate

Generate the specified value for the given channels.

Mandatory arguments:

* channel - one or both indexes are possible to be specified
* value - double value, representing the voltage

Examples:

Generate 4V on both channels

.. shell::

   $m2kcli power-supply auto --generate channel=0,1 value=4

--------------

spi
---

synopsis
~~~~~~~~

::

    m2kcli spi <uri>
                [-h | --help]
                [-i | --init [frequency=<value> clk=<value> mosi=<index> [miso=<index>] cs=<index> mode=<value> bit_numbering=<value>]
                [-w | --write data=<value>,...]

description
~~~~~~~~~~~

spi command communicates with an SPI device.

Options:

| **init**
| Initialize all channels used by the protocol to communicate.

Mandatory arguments:

* frequency - integer
* clk - index of any digital pin
* mosi - index of any digital pin
* cs - index of any digital pin
* mode - {0 | 1 | 2 | 3}
* bit_numbering - {MSB | LSB}

Optional arguments:

* miso - index of any digital pin; if miso is absent, write only mode will be activated

--------------

**write**

Write the given data and display back the read data. Before writing, the SPI
protocol must be initialized.

Mandatory arguments:

* data - list of bytes, comma separated values

Examples:

Electronics Lab 14 on our wiki page can be found
:dokuwiki:`here </university/courses/electronics/electronics-lab-14>`.
Configure the connections for 'Unipolar output operation' mode:

.. shell::

   $m2kcli spi auto -i frequency=1000000 clk=1 mosi=2 miso=7 bit_numbering=MSB \
   $    cs=0 mode=3 -w data=0x09,0xC4

--------------

i2c
---

synopsis
~~~~~~~~

::

    m2kcli i2c <uri>
                [-h | --help]
                [-i | --init frequency=<value> address=<value> scl=<index> sda=<index> [write_only=<value>]]
                [-w | --write data=<value>,... option=<value> [write_only=<value>]]
                [-r | --read bytes_number=<value> option=<value>]

description
~~~~~~~~~~~

i2c command communicates with an I²C device.

Options:

| **init**
| Initialize all channels used by the protocol to communicate.

Mandatory arguments:

* frequency - integer
* address - 7/10 bit address
* scl - index of any digital pin
* sda - index of any digital pin

Optional arguments:

* write_only - In normal mode, i2c command tries to acknowledge the message, by
  checking the ACK/NACK bits. In this case any other front-end cannot be used
  for processing the output message. So the purpose of write_only argument is
  to provide the possibility of combining m2kcli write mode with other front-end,
  for example sigrok-cli, that can decode the message.

  * write_only=0: disable write only mode
  * write_only=1: enable write only mode
  * default value: 0

--------------

**write**

Write the given data. Before writing, the I²C protocol must be initialized.

Mandatory arguments:

* data - list of bytes, comma separated values
* option - 3-bit number; only one addressing bit must be set; repeated start is optional

  * bit 0 - 7-bit addressing
  * bit 1 - repeated start
  * bit 2 - 10-bit addressing

--------------

**read**

Read a given number of bytes. Before reading, the I²C protocol must be
initialized.

Mandatory arguments:

* bytes_number - integer
* option - 3-bit number; only one addressing bit must be set; repeated start is optional

  * bit 0 - 7-bit addressing
  * bit 1 - repeated start
  * bit 2 - 10-bit addressing

Examples:

This example uses EVAL-ADT7420-PMDZ as a slave. Hardware configuration:

* (ADALM2000) DIO_0 <--> Pin 1 (ADT7420) <-->  10 kilohms resistor <- V+ (ADALM2000)
* (ADALM2000) DIO_1 <--> Pin 3 (ADT7420) <--> 10 kilohms resistor <- V+ (ADALM2000)
* (ADALM2000) GND <--> Pin 5 (ADT7420)
* (ADALM2000) V+ -> Pin 7 (ADT7420)

.. shell::

   $m2kcli i2c ip:192.168.2.1 -i frequency=100000 address=0x48 scl=0 sda=1 -w data=0x0B option=3
   $m2kcli i2c ip:192.168.2.1 -i frequency=100000 address=0x48 scl=0 sda=1 -r bytes_number=1 option=1
   $m2kcli i2c ip:192.168.2.1 -i frequency=100000 address=0x48 scl=0 sda=1 -w data=0 option=3
   $m2kcli i2c ip:192.168.2.1 -i frequency=100000 address=0x48 scl=0 sda=1 -r bytes_number=2 option=1

--------------

uart
----

synopsis
~~~~~~~~

::

    m2kcli uart <uri>
                 [-h | --help]
                 [-i | --init device=<index> baud_rate=<value> parity=<value> bits_number=<value> stop_bits=<value>]
                 [-w | --write data=<value>,...]
                 [-r | --read bytes_number=<value> format=<value>]

description
~~~~~~~~~~~

uart command communicates with an UART device.

Options:

| **init**
| Initialize all channels used by the protocol to communicate.

Mandatory arguments:

* device - index of any digital pin
* baud_rate - integer
* parity - {none | odd | even | mark | space}
* bits_number - {5 | 6 | 7 | 8}
* stop_bits - {1 | 1.5 | 2}

--------------

**write**

Write the given data. Before writing, the UART protocol must be initialized.

Mandatory arguments:

* data - list of bytes, comma separated values

--------------

**read**

Read a given number of bytes. Before reading, the UART protocol must be
initialized.

Mandatory arguments:

* bytes_number - integer
* format - {text | number}; default type text

Examples:

Replicate the example found :dokuwiki:`here </university/courses/electronics/m2k-uart-debug>`

First terminal

.. shell::

   $m2kcli uart ip:192.168.2.1 -i device=1 baud_rate=9600 parity=none \
   $    bits_number=8 stop_bits=1 -r bytes_number=3 format=text

Second terminal

.. shell::

   $m2kcli uart ip:192.168.2.1 -i device=0 baud_rate=9600 parity=none \
   $    bits_number=8 stop_bits=1 -w data=ADI

--------------

uart-terminal
-------------

synopsis
~~~~~~~~

::

    m2kcli uart-terminal <uri>
                         [-h | --help]
                         [-i | --init rx=<index> tx=<index> baud_rate=<value> parity=<value> bits_number=<value> stop_bits=<value>]

description
~~~~~~~~~~~

uart-terminal command continuously communicates with an UART device, simulating
a terminal.

Options:

| **init**
| Initialize the UART communication.

Mandatory arguments:

* rx - index of any digital pin
* tx - index of any digital pin
* baud_rate - integer
* parity - {none | odd | even | mark | space}
* bits_number - {5 | 6 | 7 | 8}
* stop_bits - {1 | 1.5 | 2}

Examples:

Connect ADALM-2000 to an UART device

.. shell::

   $m2kcli uart-terminal auto -i baud_rate=115200 rx=15 tx=7 stop_bits=1 \
   $    parity=none bits_number=8

--------------

USB to Serial UART adapter script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The script can be found
:git-libm2k:`here <tools/m2kcli/examples/m2k_tty.sh>`.

It creates an UART-Terminal using an ADALM2000 board and connects it to a
`PTY <https://linux.die.net/man/7/pty>`__ (pseudoterminal interfaces). This
enables connection to a Serial Terminal Emulator (like GTKTerm, Picocom,
Minicom, Tera Term).

To use the script, run it in a terminal and keep it running, after that, from
another terminal connect to the PTY using a terminal emulator and the settings
displayed on screen. When you want to close the connection just press ENTER
inside the terminal from where the script was ran.

Example of usage, connect a Raspberry Pi to PC using a M2K board:

First terminal

.. shell::

   $./m2k_tty.sh
    M2K configurations:
        URI: ip:192.168.2.1
        RX pin: 7
        TX pin: 15
    Sample details for UART:
        Baud rate: 115200
        Number of data bits: 8
        Parity: none
        Stop bits: 1
    Checking uart-terminal...

    m2kcli uart-terminal: 43847 is running
    Done, connect to **/dev/pts/3** to access the uart terminal

    Press any key to close the connection

In a second terminal connect using a terminal emulator to the previous displayed
path and the corresponding UART settings.

Second terminal

.. shell::

   $picocom -b 115200 -r -l /dev/pts/3

    port is        : /dev/pts/3
    flowcontrol    : none
    baudrate is    : 115200
    parity is      : none
    databits are   : 8
    stopbits are   : 1

    Terminal ready

    Raspbian GNU/Linux 10 analog ttyS0

    analog login:
    analog login: root
    Last login: Fri Sep  2 17:17:21 BST 2022 on ttyS0
    Linux analog 5.10.63-v7l+ #2 SMP Fri Jun 24 15:44:30 EEST 2022 armv7l

    root@analog:~#

And the connection will stay active as long as the first terminal will stay
active. To close the connection, just press a key inside the first terminal.

::

   m2kcli uart-terminal: 43847 is running
   Done, connect to /dev/pts/3 to access the uart terminal

   Press any key to close the connection

   -Killed m2kcli uart-terminal
   -Killed socat
   --Connection closed

Requirements:

-  `socat <https://linux.die.net/man/1/socat>`__
-  :ref:`libiio <libiio build>`
-  libm2k with :ref:`m2kcli <m2kcli build>`

It uses the socat command to create two connected
`PTYs <https://linux.die.net/man/7/pty>`__ and using the m2kcli uart-terminal
command makes the connection between a PTY and our UART-Terminal. After all of
that is done, the user can connect to the other PTY using a Serial Port Terminal
Emulator (like GTKTerm, Picocom, Minicom, Tera Term).

--------------

m2kcli and sigrok-cli
=====================

Sigrok is a portable, cross-platform, free open source signal analysis software.
sigrok-cli is a command-line frontend for sigrok. A a much wider documentation
about sigrok-cli can be found on this wiki
`page <https://sigrok.org/wiki/Sigrok-cli>`__.

sigrok-cli can be used for decoding digital signals. m2kcli does not have the
functionality of continuously decoding SPI or I²C signals. Using sigrok-cli for
decoding the data and m2kcli for capturing the data, we can simulate this
functionality.

**How to get sigrok-cli?**

Sigrok offers two main possibilities of getting the cli. Building from source or
downloading the packages. All the steps are well described on their wiki page.
For building sigrok-cli have a look at this
`page <https://sigrok.org/wiki/Building>`__, while for downloading the binaries
and the distribution packages have a
look\ `here <https://sigrok.org/wiki/Downloads#Binaries_and_distribution_packages>`__.

**Example:**

In the following example ADALM-2000 is connected to an I²C device and we are
using a Linux AppImage binary for sigrok-cli.

.. shell::

   $m2kcli digital auto -s sampling_frequency_in=1000000
   $m2kcli digital auto -c buffer_size=1000 format=binary | \
   $    sigrok-cli -i - -I binary:numchannels=16:samplerate=1mhz -P \
   $        i2c:scl=15:sda=7 -A i2c=address-read:address-write:data-read:data-write
