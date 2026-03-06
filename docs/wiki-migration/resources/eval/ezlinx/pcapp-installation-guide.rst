.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



| 
| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`

ezLINX™ Sample PC Application Installation Guide
================================================

Online Installation
-------------------

Windows XP / Vista / 7
~~~~~~~~~~~~~~~~~~~~~~

| **Step 1:**
| Download the Sample PC Application install files from the :doc:`ezLINX Development Environment page </wiki-migration/resources/eval/ezlinx>` (Figure 1 below).

.. image:: https://wiki.analog.com/_media/ezlinx/pc_install_fig1_xp_v2.jpg
   :align: center
   :width: 600px

| **Step 2:**
| Right click on *ezLINXPCApp.zip* and extract it.

| **Step 3 (Windows XP Only):**
| If you already have v4 or higher of the .NET Framework or Windows Imaging Component already installed on your machine, skip this step. Windows Imaging Component is required to install and use the Microsoft .NET Framework. This can be downloaded from http://www.microsoft.com/en-us/download/details.aspx?id=32 (Figure 2 below). For the English installer the file *wic_x86_enu.exe* should be downloaded and ran. This will install Windows Imaging Component on your machine.

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/pc_install_fig2_xp_v3.jpg
   :alt: Figure 2.
   :align: center
   :width: 600px

| **Step 4:**
| Run *setup.exe* found in the extracted *ez*\ LINXPCApp archive. Windows will warn that the software publisher can not be verified (Figure 3 below). Ignore this and select “Install”.

.. image:: https://wiki.analog.com/_media/ezlinx/pc_install_fig3_xp.jpg
   :alt: Figure 3.
   :align: center
   :width: 400px

| **Step 5:**
| The installer will then check that you have the necessary software on your machine to install the application. If you do not have the necessary software you will be prompted to accept the license agreement for the .NET Framework v4 and/or Windows Installer 3.1 (See Figure 4. below). Accept these license agreements and the required software will be downloaded and installed.

.. image:: https://wiki.analog.com/_media/ezlinx/license_agreement_1.jpg
   :alt: Figure 4.
   :align: center
   :width: 400px

| **Step 6:**
| The *ez*\ LINX Sample PC Application will be installed (Figure 5 below). When the installer is finished the Sample PC Application will launch automatically.

.. image:: https://wiki.analog.com/_media/ezlinx/pc_install_fig4_xp.jpg
   :alt: Figure 5.
   :align: center
   :width: 400px

Offline Installation
--------------------

Windows Vista / Windows 7
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Step 1:**
| To install the *ez*\ LINX Sample PC Application you must have v4 or later of the Microsoft .NET Framework installed. If this is already installed skip down to step 2. If not, run the application *dotNetFx40_Full_x86_x64.exe* found on the disk provided. Accept the license agreement (Figure 6. below) and the .NET Framework will be installed on your machine, this will take a few minutes. If using Windows 7, at this point you will be prompted to restart your machine. This must be done before the ezLINX Sample PC Application can be installed.

.. image:: https://wiki.analog.com/_media/ezlinx/license_agreement_2.jpg
   :alt: Figure 6.
   :align: center

| **Step 2:**
| Run setup.exe provided on the disk. Windows will warn that the software publisher can not be verified. Ignore this and select “Install”. The Sample PC Application will be installed. When the installer is finished the Sample PC Application will launch automatically.

Windows XP
~~~~~~~~~~

| **Step 1:**
| To install the ezLINX Sample PC Application you must have v4 or later of the Microsoft .NET Framework installed. If this is already installed skip down to step 3. Both Windows Installer v3.1 or higher and Microsoft Imaging Component (WIC) are required to install the .NET Framework. If both of these are already installed skip to step 2. These files are provided on the distributed disk. To install Windows Installer v3.1 run the file *WindowsInstaller-KB893803-v2-x86.exe*. To install the Windows Imaging Component run the *file wic_x86_enu.exe*.

| **Step 2:**
| To install the .NET Framework you must run the application *dotNetFx40_Full_x86_x64.exe* found on the disk provided. Ignore the security warnings (Figure 7) and accept the license agreement (Figure 8). The .NET Framework will be installed on your machine, this will take a few minutes.

.. image:: https://wiki.analog.com/_media/ezlinx/pc_install_fig5_xp.jpg
   :alt: Figure 7.
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/ezlinx/pc_install_fig6_xp.jpg
   :alt: Figure 8.
   :align: center
   :width: 400px

| **Step 3:**
| Run *setup.exe* provided on the disk. Windows will warn that the software publisher can not be verified. Ignore this and select “Install”. The *ez*\ LINX Sample PC Application will be installed. When the installer is finished the Sample PC Application will start automatically.

| 
| Once the Sample PC Application has been installed, the USB device must be configured for use with the *ez*\ LINX Development Platform hardware. Click :doc:`here </wiki-migration/resources/eval/ezlinx/usb-ip-config>` for a guide to installing and configuring this device driver.
