Building Scopy on Linux
=======================

Installing the dependencies
---------------------------

Before building Scopy on Linux system, you need to make sure all the requirements are installed.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 
| **Install a Qt 5 version (>5.12) using an online or offline installer from the official Qt downloads page.**

| 
| **Install dependencies**

::

       **git clone https://github.com/analogdevicesinc/scopy.git**

This will fetch the latest sources from GitHub to a "scopy" directory.

This following command will use system Qt version

::

       **scopy/CI/appveyor/install_ubuntu_deps.sh**

or if you want to use a custom version of Qt (the one you just installed) - scopy/CI/appveyor/install_ubuntu_deps.sh <path_to_qt\_> for example:

::

       **scopy/CI/appveyor/install_ubuntu_deps.sh /home/Adi/Qt/5.15.0/gcc_64**
       

This should install all of the dependencies required to build Scopy.

Building Scopy
--------------

If you are using a custom Qt version set -DCMAKE_PREFIX_PATH to the <Qt installation folder>/lib/cmake. If you are using the system version don't set the -DCMAKE_PREFIX_PATH.

::

       **cd scopy
       mkdir build && cd build
       cmake -DCMAKE_PREFIX_PATH=/home/adi/Qt/5.15.0/gcc_64/lib/cmake ../**

If everything goes well, the output should be "Configuring done" and "Generating done".

Now build the project:

::

       **make**

And run Scopy:

::

       **./scopy**

Alternatively you can open QtCreator from the Qt folder. Open, configure and build the project.

**Return to** :doc:`Scopy Main Page </wiki-migration/university/tools/m2k/scopy>`
