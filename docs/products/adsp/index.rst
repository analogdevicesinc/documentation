.. _adsp:

Digital Signal Processors (ADSP)
================================

.. toctree::
   :hidden:
   :glob:

   *

ADI has a large portfolio of :adi:`Digital Signal Processors <en/product-category/dsp.html>`
(see :adi:`Selection Table for Digital Signal Processors <en/parametricsearch/3020#/>`).
A subset of those processors include ARM Cortex cores and are prefixed with SC
for "SHARC Connect". They can run baremetal applications, an RTOS or Linux.
Cortex-M33 models are appropriate for a baremetal application or an RTOS, while
Cortex-A5 and Cortex-A55 can also run 32-bit or 64-bit Linux respectively.

.. list-table:: ADSP SHARC Connect SoCs
   :header-rows: 1

   * - Cortex-M33
     - Cortex-A5
     - Cortex-A55
   * - :adi:`ADSP-SC834 <en/products/ADSP-SC834.html>`
     - :adi:`ADSP-SC570 <en/products/ADSP-SC570.html>`
     - :adi:`ADSP-SC596 <en/products/ADSP-SC596.html>`
   * - :adi:`ADSP-SC835 <en/products/ADSP-SC835.html>`
     - :adi:`ADSP-SC571 <en/products/ADSP-SC571.html>`
     - :adi:`ADSP-SC598 <en/products/ADSP-SC598.html>`
   * -
     - :adi:`ADSP-SC572 <en/products/ADSP-SC572.html>`
     -
   * -
     - :adi:`ADSP-SC573 <en/products/ADSP-SC573.html>`
     -
   * -
     - :adi:`ADSP-SC582 <en/products/ADSP-SC582.html>`
     -
   * -
     - :adi:`ADSP-SC583 <en/products/ADSP-SC583.html>`
     -
   * -
     - :adi:`ADSP-SC584 <en/products/ADSP-SC584.html>`
     -
   * -
     - :adi:`ADSP-SC587 <en/products/ADSP-SC587.html>`
     -
   * -
     - :adi:`ADSP-SC589 <en/products/ADSP-SC589.html>`
     -
   * -
     - :adi:`ADSP-SC592 <en/products/ADSP-SC592.html>`
     -
   * -
     - :adi:`ADSP-SC594 <en/products/ADSP-SC594.html>`
     -

Linux support
-------------

ADI supports running Linux on all ADSP SoCs with Cortex-A5 and A55 cores.
That includes the following repositories. New features are tracked in the
`ADSP Github Project <https://github.com/orgs/analogdevicesinc/projects/20/views/1>`__
and coordinated with the community during weekly public office hours at 17:00 CET
on Thursdays using a
`Jitsi meeting <https://meet.jit.si/AnalogDevicesIncDigitalSignalProcessingOfficeHours>`__.

Upstream forks
--------------

The ADSP Linux team maintains branches based on upstream releases. Changes made
to support ADI hardware is upstreamed as quickly as possible. Until those
changes have been accepted upstream, they are maintained in the following ADI
forks.

Release versions include the upstream version and a ADI specific release number
(e.g.  ``1``, ``2``, ...).

- :git-linux:`+`:
    - v6.12.0:
      :git-linux:`Commits <commits/adsp-6.12.0-y+>`
      :git-linux:`Release 1 <releases/tag/adsp-6.12.0-1+>`
    - v6.12.38:
      :git-linux:`Commits <commits/adsp-6.12.38-y+>`
- :git-u-boot:`+`
    - v2025.07:
      :git-u-boot:`Commits <commits/adi-u-boot-2025.07.y+>`
      :git-u-boot:`Release 1 <releases/tag/v2025.07-1+>`
    - v2025.10:
      :git-u-boot:`Commits <commits/adi-u-boot-2025.10.y+>`
- :git-buildroot:`+`
    - v2025.05:
      :git-buildroot:`Commits <commits/adi-2025.05.x+>`
- :git-trusted-firmware-a:`+`
- :git-optee_os:`+`
- :git-openocd:`+`

ADI repositories
----------------

- :git-adsp-ldr:`+`
    - :git-adsp-ldr:`v1.0.0 <releases/tag/v1.0.0+>`
      :git-adsp-ldr:`v1.0.1 <releases/tag/v1.0.1+>`
      :git-adsp-ldr:`v1.0.2 <releases/tag/v1.0.2+>`
- :git-lnxdsp-repo-manifest:`+`
- :git-br2-external:`+`
