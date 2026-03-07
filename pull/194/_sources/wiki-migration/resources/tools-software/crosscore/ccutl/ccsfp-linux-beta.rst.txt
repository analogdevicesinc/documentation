CrossCore Utilities Serial Flash Programmer for Linux
=====================================================

Introduction
------------

This is a beta version of the CrossCore Utilites Serial Flash Programmer for Linux host machines. This utility may be used to program flash memory on ADSP-SC5xx, ADSP-215xx and ADI Cortex-M based processors using a command line interface. The package is available from `here <https://download.analog.com/tools/CrossCoreUtils/Releases/Release_1.7.1/adi-CrossCoreUtilities-linux-amd64-1.7.1.deb>`_.

.. important::

   This product is still in beta development.


Installation
------------

Install the package either by double-clicking the downloaded .deb package or running ``sudo apt install /path/to/adi-CrossCoreUtilities-linux-amd64-1.7.1.deb`` and following the on-screen prompts. The package will be installed to ``/opt/analog/ccutl/1.7.1``.

Usage
-----

Connect the target board to the host via USB, this will be via the socket labelled USB-to-UART on EZ-KITS / SOMs or via the USB-C socket on later revisions of the ADSP-SC598 SOM.

To ensure the target is connected, run the command ``dmesg | grep tty``, and ensure the USB serial device is listed. The port number must be specified when invoking CrossCore Serial Flash Programmer.

To invoke, run: ``/opt/analog/ccutl/1.7.1/bin/ccsfp [options] [file]``

The options available are:

+----------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| Switch         | Arguments                | Description                                                                                         |
+================+==========================+=====================================================================================================+
| -a \| -auto    |                          | Enable unattended mode. Always enabled on Linux host.                                               |
+----------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| -b \| -baud    | <number>                 | Select standard baud rate. Only 115200 is supported on Linux hosts and will be selected by default. |
+----------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| -k \| -key     | <key>                    | Provide 32-digit hexadecimal unlock key (used for Cortex-M processors).                             |
+----------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| -p \| -port    | <name>                   | Select serial port (e.g. /dev/ttyUSB0).                                                             |
+----------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| -t \| -target  | <name>                   | Select target (as defined in ADIChip.ini).                                                          |
+----------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| -x \| -action  | program \| erase \| load | Select action. Defaults to 'program'.                                                               |
+----------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| -v \| -version |                          | Print version information.                                                                          |
+----------------+--------------------------+-----------------------------------------------------------------------------------------------------+
| -h \| -help    |                          | Print the help message.                                                                             |
+----------------+--------------------------+-----------------------------------------------------------------------------------------------------+

Example ldr files are provided in the folder ``/opt/analog/ccutl/1.7.1/etc/ccsfp/examples/`` which may be used to verify CrossCore Serial Flash Programmer is working correctly. When booted, these examples will make one of the push buttons on the development board toggle an LED when pressed. For example, to flash the example application to an ADSP-SC589 EZ-KIT, run: ``/opt/analog/ccutl/1.7.1/bin/ccsfp -t 'ADSP-SC589 EZ-KIT' -x program -p /dev/ttyUSB0 /opt/analog/ccutl/1.7.1/etc/ccsfp/examples/ADSP-SC589-Button.ldr``

For more information refer to the CrossCore Serial Flash Programmer User's Guide, available at ``/opt/analog/ccutl/1.7.1/Docs/CrossCoreSerialFlashProgrammer_UsersGuide.pdf``.

Targets
-------

Targets supported by the '-t' switch are as follows:

+---------------------------+


| ADSP-CM40x                |

+---------------------------+

| ADSP-CM41x                |

+---------------------------+

| ADuCM302x                 |

+---------------------------+

| ADuCM4x50                 |

+---------------------------+

| ADSP-21562 ALEAS          |

+---------------------------+

| ADSP-21569 EZ-KIT         |

+---------------------------+

| ADSP-21569 SOM            |

+---------------------------+

| ADSP-21569 CRR OSPI       |

+---------------------------+

| ADSP-SC573 EZ-KIT         |

+---------------------------+

| ADSP-SC584 EZ-KIT         |

+---------------------------+

| ADSP-SC589 EZ-KIT         |

+---------------------------+

| ADSP-21593 SOM            |

+---------------------------+

| ADSP-21593 CRR OSPI       |

+---------------------------+

| ADSP-SC594 SOM            |

+---------------------------+

| ADSP-SC594 CRR OSPI       |

+---------------------------+

| ADSP-SC598 SOM            |

+---------------------------+

| ADSP-SC598 CRR OSPI       |

+---------------------------+

| ADSP-SC598 eMMC USER AREA |

+---------------------------+

| ADSP-SC598 eMMC BOOT AREA |

+---------------------------+

| SHARC Audio Module        |

+---------------------------+

Modification
------------

In order to support flashing of custom targets, additional entries may be added to ``/opt/analog/ccutl/1.7.1/etc/ccsfp/ADIChip.ini``.

This will require the creation of a second-stage kernel ldr, to be used for communication with CrossCore Serial Flash Programmer while writing to the target. For more information on this, please refer to the CrossCore Serial Flash Programmer User's Guide, available at ``/opt/analog/ccutl/1.7.1/Docs/CrossCoreSerialFlashProgrammer_UsersGuide.pdf``.
