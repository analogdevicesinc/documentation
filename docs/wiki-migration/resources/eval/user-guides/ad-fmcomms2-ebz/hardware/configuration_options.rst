Configuration Options for AD9361/AD9364 boards
==============================================

By default, the `AD-FMCOMMS2-EBZ <https://wiki.analog.com/..>`__, :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` and `ARRADIO <https://wiki.analog.com/../../arradio>`__ board includes the Johanson Technology's `2450BL15B050E <http://www.johansontechnology.com/datasheets/baluns/JTI_Balun-2450BL15B050_12-03.pdf>`__ 2.45 GHz Balun. This balun is rated for a operating frequency of 2400~2500 MHz. If you want to evaluate the part outside of this frequency range, an alternative balun should be installed. A list of alternative baluns are below:

Receive Balun
-------------

============ =============== =============== ========= ===========
Manufacturer Frequency (MHz) Balun number    Impedance AC coupling
============ =============== =============== ========= ===========
TDK          350             HHM1591D1       50/100    100pF
TDK          900             HHM1564A4       50/200    100pF
Johanson     1450            1450BL15A200E   50/200    20pF
Johanson     1600            1600BL15B050E   50/50     20pf
Anaren       1631            BD1631J50100A00 50/100    18pF
Johanson     2450            2450BL15B200E   50/200    9pF
Johanson     2450            2450BL15B050E   50/50     18pF
Hitachi      3000            ESLT-S370KBI    50/50     10pF
Johanson     5400            5400BL15K050E   50/50     10pF
Hitachi      5000            ESLT_S540E      50/50     10pF
============ =============== =============== ========= ===========

Transmit Balun
--------------

============ =============== ============= =========
Manufacturer Frequency (MHz) Balun number  Impedance
============ =============== ============= =========
TDK          350             HHM1591D1     50/100
Johanson     900             0900BL15C050E 50/50
Johanson     1600            1600BL15B050E 50/50
Johanson     1600            1600BL15B050E 50/50
Johanson     1850            1850BL15B050E 50/50
Johanson     2450            2450BL15B050E 50/50
Johanson     3700            3700BL15B050E 50/50
Johanson     5400            5400BL15K050E 50/50
Johanson     5400            5400BL15K050E 50/50
============ =============== ============= =========
