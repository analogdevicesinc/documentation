GNU Radio
=========

|https://wiki.gnuradio.org/images/2/2f/Gnuradio_logo_icon.png|\ `GNU Radio <http://gnuradio.org>`_ is a free software (as in freedom) development toolkit that provides signal processing blocks to implement software-defined radios and signal-processing systems. It can be used with a wide variety of external RF hardware to create software-defined radios, or without hardware in a simulation-like environment. It is widely used in hobbyist, academic, and commercial environments to support both wireless communications research and real-world radio systems. GNU Radio uses a thread-per-block scheduler, so the signal processing speed scales based on model design (how many blocks), and the number of cores (number of resources to run threads) available.

In GNU Radio, a variety of C++ libraries modeling different digital communications and digital signal processing algorithms are integrated together using Python and SWIG (a software development tool that connects programs written in C and C++ with a variety of high-level programming languages including Python). These libraries are produced by the open source community, and freely shared with everyone. This extends past the basic signal processing libraries with external frameworks, standard based wireless implementations, and examples that share the open source philosophy, maintained by the community.

Analog Devices supports the interface to GNU Radio, but does not support GNU Radio itself. If you are having problems installing the ADI provided portions, please ask. If you are having difficulty with the core pieces of GNU Radio, you might get pointed to the mailine `GNU Radio mailing lists <https://wiki.gnuradio.org/index.php/MailingLists>`_.

Windows
-------

Windows is not a primary platform for GNU Radio development by the core GNU Radio Development team, and is not thoroughly tested by anyone. Support from both ADI and the GNU Radio community is limited on Windows. it is recommended use GNU Radio on a Linux based system. For those that want to try, ADI does provide a limited support Windows build, which can be found :doc:`here </wiki-migration/resources/tools-software/linux-software/gnuradio_windows>`.

Linux
-----

Linux is the GNU Radio defacto standard for development. All core developers, and ADI developers use Linux as their primary development and test system. More information can be found at: :doc:`gnuradio </wiki-migration/resources/tools-software/linux-software/gnuradio>`

.. |https://wiki.gnuradio.org/images/2/2f/Gnuradio_logo_icon.png| image:: https://wiki.gnuradio.org/images/2/2f/Gnuradio_logo_icon.png
