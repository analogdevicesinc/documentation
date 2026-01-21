:orphan:

.. _help-and-support:

Help and Support for ADI FMC Cards & RF SoMs
===============================================================================

If you have any questions regarding the:

- ADI FMC Boards: AD-FMCOMMS2-EBZ, AD-FMCOMMS3-EBZ, AD-FMCOMMS4-EBZ,
  AD-FMCOMMS5-EBZ AD-FMCOMMS11-EBZ
- Arrow ARRADIO board or
- ADI RF SoM (ADRV9364-Z7020, ADRV9361-Z7035 or ADRV9009-ZU11EG)

or are experiencing any problems while using the board or following the user
guides, feel free to ask us a question.

Questions can be asked on our :ez:`/` support community.

.. important::

   Calling on the phone, emailing someone directly or writing private messages
   to employees on :ez:`EngineerZone </>`, will only cause things to get
   answered in much much slower manner.

Why EngineerZone?
-------------------------------------------------------------------------------

Why can't I get one-on-one email/phone support on the AD9361?

The AD9361 is a very complex part - it has over one thousand (1000) different
registers with little way to understand (other than experience, and staring at
things a long time) what is going on inside the part. The working system
crosses many domains (RF, FIR Filter Design, driver software, HDL, user
applications). One single person can't understand the entire thing, so a single
email, which is forwarded around to multiple places actually takes longer to
get questions answered (and has a higher chance of getting lost), than posting
them on EngineerZone (**where things are tracked, and closed**). Having experts in
the field monitor the EngineerZone is a better use of everyone's time, and
questions are actually answered faster for those asking. Please use it.

When asking a question please take the time to give a detailed description of
your problem. Always include on which carrier platform (ZC706? ZC702? Zed,
SocKit, FMC carrier, breakout (for SoMs). etc) you are currently using the
card. If you are experiencing a problem please state the steps you have
executed, the result you expected you would get and the result you actually
got. By doing so you enable us to provide you precise and detailed answers in a
timely manner.

Before asking questions, **please also take the time to check if somebody else
already asked the same question and already got an answer**. Please make sure you
ask in these forums. EngineerZone is a big place, with lots of places to post
questions, and it's possible to ask a question in the wrong place, where no one
familiar with these boards/parts/software monitors things, and it will go
unanswered forever. Don't get mad if this happens. The problem is between the
chair and the keyboard (you). If you are posting in the right place, and the
question is unanswered for a few working days, please bump the thread
(we, humans, are replying to the threads after all, and sometimes miss things).

HDL / Hardware Questions
-------------------------------------------------------------------------------

For questions regarding the AD-FMCOMMS2-EBZ, AD-FMCOMMS3-EBZ or AD-FMCOMMS4-EBZ
hardware or the HDL reference design please state them in the
:ez:`FPGA Reference Designs <fpga>` sub-community.
If you have questions about the tools, please go ask the tools vendors:

- `AMD Xilinx Forums <https://support.xilinx.com/s>`_
- `Intel Altera Forums <https://community.intel.com/t5/FPGA/ct-p/fpga>`_

Linux Driver or Application Questions
-------------------------------------------------------------------------------

For questions regarding the the ADI Linux distribution (which is based
`Linaro <https://www.linaro.org/>`_ with `Xfce <https://www.xfce.org/>`_ desktop),
the Linux drivers, or the device trees for the AD9361 or
AD9364 based platforms, please use the
:ez:`Linux Software Drivers <linux-software-drivers>` sub-community.

If you have generic userspace questions (how do I use a standard linux tool),
we should suggest to use your favorite `search tool <https://google.com>`_ to find
that  tool/utility/application support method (some use email, some use web).
If you think you have found a bug specific to ARM, please report this upstream.

No-OS Questions
-------------------------------------------------------------------------------

For questions regarding the no-OS drivers for AD9361 or AD9364, please use the
:ez:`Linux Software Drivers <linux-software-drivers>`
sub-community.

General AD9361 Questions
-------------------------------------------------------------------------------

Questions about the AD9361 or AD9364, please use the
:ez:`AD9361 <wide-band-rf-transceivers/design-support>` sub-community.

Detailed documentation on the AD9361 device can be found at:
:adi:`AD9361 Design support package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`

AD9361/4 FIR Filter Wizard
-------------------------------------------------------------------------------

Questions about the
:dokuwiki:`AD936x FIR Filter Wizard <resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`
can be asked on
:ez:`Linux Software Drivers <linux-software-drivers>` sub-community.

MATLAB/Simulink/SimRF Questions
-------------------------------------------------------------------------------

Questions about the MathWorks provided AD9361 simRF model, or the FMCOMMS2/3/4/5
Hardware support package can be asked either:

- :mw:`MathWorks information page <products/connections/product_detail/adi-rf-transceivers.html>`
- :mw:`MathWorks Hardware Support <hardware-support/request-hardware-support.html>`

Questions about the Analog Devices provided Filter Wizard, or streaming system object,
or Board Support Package can be asked:

- :ez:`MATLAB/Simulink support <sw-interface-tools>`

GNU Radio
-------------------------------------------------------------------------------

Questions about using the FMCOMMSx boards and GNU Radio either on a host or on
the ARM target, can be asked on :ez:`Software Interface Tools <sw-interface-tools>`
sub-community.
Generic questions about GNU Radio should be asked on their
`mailing list <https://wiki.gnuradio.org/index.php/MailingLists>`_.

Bugs / Feature Requests
-------------------------------------------------------------------------------

If you think you have a bug to report, the best place to to this is the :ez:`/`.
This way we can discuss if the bug is a bug, or a feature request, or just missing
documentation.

If you think you have a real bug, where you have developed a real fix (first - thanks),
feel free to:

- Post something on EngineerZone.
- Post something on the GitHub issue tracker.
- Fork the GitHub repository, and fix it, and then send a pull request.

Either is OK with us.

More info
-------------------------------------------------------------------------------

For more information also check:

- `VITA's FMC info <http://www.vita.com/fmc>`_
- :adi:`AD-FMCOMMS2-EBZ`
- :adi:`AD-FMCOMMS3-EBZ`
- :adi:`AD-FMCOMMS4-EBZ`
- :adi:`AD-FMCOMMS5-EBZ`
- :dokuwiki:`Arradio <resources/eval/user-guides/arradio>`
