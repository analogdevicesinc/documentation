Short Parameter Name support for Export file (PARAM.h)
======================================================

Parameter names(#defines) in the PARAM.h export file is too long sometimes. The following example shows an long export name.

#define MOD\_<fc #ff0000><<Heirarchy Board Names separated by \_>></fc>\_<fc #800080><<Module Label>></fc>_ALG<fc #008080><<Algorithm Index>></fc>\_<fc #6495ed><<AlgorithmInternalName>></fc><AlgorithmInstanceNumber>>\_<fc #800000><<ParameterName>></fc>_ADDR

| When the short parameter name is enabled the parameter will be shortened as follows.
| #define ADDR\_<fc #4682b4><<Module Label>></fc>\_<fc #008000><<ParameterName>></fc>

| (e.g) **Original Name:**
| #define MOD\_<fc #ff0000>BOARD1</fc>\_<fc #800080>COMPRESSOR1</fc>_ALG<fc #008080>0</fc>\_<fc #4682b4>TWOCHANRMSNOPOSTGAINS300FULLRANGE</fc>1<fc #800000>POINTS0</fc>_ADDR

| **Short Name:**
| #define ADDR\_<fc #6495ed>COMPRESSOR1</fc>\_<fc #008000>POINTS0</fc>

This option available under Action Menu.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/action.jpg
   :align: center

|

.. important::

   Parameter names in export may not be unique when 'Short Parameter Name for Export' option is enabled in the following cases.


   | 1. Same module label is used across multiple hierarchy boards in the schematic.
   |
