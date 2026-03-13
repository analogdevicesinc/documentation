Short Parameter Name support for Export file (PARAM.h)
======================================================

Parameter names(#defines) in the PARAM.h export file is too long sometimes. The
following example shows an long export name.

#define MOD\_<<Heirarchy Board Names separated by \_>>\_<<Module
Label>>_ALG<<Algorithm
Index>>\_<<AlgorithmInternalName>><AlgorithmInstanceNumber>>\_<<ParameterName>>_ADDR

When the short parameter name is enabled the parameter will be shortened as
follows. #define ADDR\_<<Module Label>>\_<<ParameterName>>

(e.g) **Original Name:** #define MOD_BOARD1_COMPRESSOR1_ALG0_TWOCHANRMSNOPOSTGAINS300FULLRANGE1POINTS0_ADDR

**Short Name:** #define ADDR_COMPRESSOR1_POINTS0

This option available under Action Menu.

|image1|

.. important::

   Parameter names in export may not be unique when 'Short Parameter Name for
   Export' option is enabled in the following cases. 1. Same module label is
   used across multiple hierarchy boards in the schematic.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/action.jpg
