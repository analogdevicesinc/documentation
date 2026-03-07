Schematic Version Control (ADAU145X)
====================================

| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| Schematic version control allows the users to maintain version numbers for a particular schematic. This feature is disabled by default. It can be enabled by using write click context menu on the IC as shown below. This is currently supported only for ADAU145X Sigma DSPs.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/schematicversion.jpg
   :align: center

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/versioncontrol.jpg
   :align: center

There are 2 version numbers, one is major and another minor. The minor can be incremented manually. The major version is incremented whenever there is a change in the schematic (code change) and the compilation is done. The major version can also be overridden by the user.

There is an extra field for "Customer ID" which can be enabled optionally. This is updated manually by the users. The Last three memory locations of DM1 memory are used to maintain these version numbers.
