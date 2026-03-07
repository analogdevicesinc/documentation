Building Scopy on OSX
=====================

Using existing DMG Installers
-----------------------------

| Scopy DMG Installers for OSX are available for each release.
| The oldest supported OSX version is 10.11.

.. admonition:: Download
   :class: download

   
   -  Download: :git-scopy:`OSX installer <releases/latest>`
   


Installing the dependencies
---------------------------

You can also build Scopy from source, instead of using the provided installer. Before building Scopy on OSX systems, you need to make sure all the requirements are installed.

| 
| **Setup Python**

::

        **export PYTHONPATH=$(brew --prefix)/lib/python2.7/site-packages
        export PATH=$PATH:$(brew --prefix)/share/python**

| 
| **Get pip**

::

        **curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
        sudo python get-pip.py**

| 
| **Install dependencies using Homebrew**

::

        **brew install brew-pip cmake gettext swig fftw bison autoconf automake libtool libzip glibmm doxygen python3 wget qt5 libusb
        sudo pip install --ignore-installed six
        brew pip mako
        brew pip cheetah**

| 
| **Get the latest release of libiio from** :git-libiio:`here <releases>`

| 
| **Build and install Boost**

::

       **cd ~
       wget https://netcologne.dl.sourceforge.net/project/boost/boost/1.63.0/boost_1_63_0.tar.gz
       tar -xzvf boost_1_63_0.tar.gz
       cd boost_1_63_0
       ./bootstrap.sh --with-libraries=date_time,filesystem,program_options,regex,system,test,thread
       ./b2
       sudo ./b2 install**

| 
| **Build and install Markdown**

::

       **cd ~
       wget 
       https://pypi.python.org/packages/1d/25/3f6d2cb31ec42ca5bd3bfbea99b63892b735d76e26f20dd2dcc34ffe4f0d/Markdown-2.6.8.tar.gz
       tar -xzvf Markdown-2.6.8.tar.gz
       cd Markdown-2.6.8
       ./setup.py build
       sudo ./setup.py install**

| 
| **Build and install Cheetah**

::

       **cd ~
       wget https://pypi.python.org/packages/cd/b0/c2d700252fc251e91c08639ff41a8a5203b627f4e0a2ae18a6b662ab32ea/Cheetah-2.4.4.tar.gz
       tar -xzvf Cheetah-2.4.4.tar.gz
       cd Cheetah-2.4.4
       ./setup.py build
       sudo ./setup.py install**

| 
| **Build and install Volk**

::

       **cd ~
       wget http://libvolk.org/releases/volk-1.3.tar.gz
       tar -xzvf volk-1.3.tar.gz
       cd volk-1.3
       mkdir build && cd build
       cmake ..
       make
       sudo make install**

| 
| **Build and install GNU Radio**

::

       **cd ~
       git clone https://github.com/analogdevicesinc/gnuradio
       cd gnuradio
       git checkout scopy
       mkdir build && cd build
       cmake -DENABLE_INTERNAL_VOLK:BOOL=OFF -DENABLE_GR_FEC:BOOL=OFF -DENABLE_GR_DIGITAL:BOOL=OFF -DENABLE_GR_DTV:BOOL=OFF -DENABLE_GR_ATSC:BOOL=OFF -DENABLE_GR_AUDIO:BOOL=OFF -DENABLE_GR_CHANNELS:BOOL=OFF -DENABLE_GR_NOAA:BOOL=OFF -DENABLE_GR_PAGER:BOOL=OFF -DENABLE_GR_TRELLIS:BOOL=OFF -DENABLE_GR_VOCODER:BOOL=OFF ..
       make
       sudo make install**

| 
| **Build and install libsigrok**

::

       **cd ~
       git clone https://github.com/sigrokproject/libsigrok/
       mkdir -p libsigrok/build
       cd libsigrok/build
       ../autogen.sh
       ../configure --disable-all-drivers --enable-bindings --enable-cxx
       make -j4 install**

| 
| **Build and install libsigrokdecode**

::

       **cd ~
       mkdir -p libsigrokdecode-0.4.1/build
       wget http://sigrok.org/download/source/libsigrokdecode/libsigrokdecode-0.4.1.tar.gz
       tar -xzvf libsigrokdecode-0.4.1.tar.gz
       cd libsigrokdecode-0.4.1/build
       ../configure --enable-shared --disable-static
       make -j4 install**

| 
| **Build and install Qwt**

Before building Qwt, you need to check out your version of qmake.

Please make sure you are using Qt 5. For the next steps, use the full path to qmake.

Now we can build and install Qwt:

::

       **cd ~
       git clone https://github.com/osakared/qwt -b qwt-6.1-multiaxes
       cd qwt
       curl https://raw.githubusercontent.com/analogdevicesinc/scopy-snap/master/qwt-6.1-multiaxes.patch

       | patch -p1
       # Use full path to qmake
       qmake qwt.pro
       make -j4
       sudo make install**

|

| **Build and install Qwt Polar**

::

       **cd ~
       curl -L https://downloads.sourceforge.net/project/qwtpolar/qwtpolar/1.1.1/qwtpolar-1.1.1.tar.bz2 | tar -xj
       cd qwtpolar-1.1.1
       curl https://raw.githubusercontent.com/analogdevicesinc/scopy-snap/master/qwtpolar-qwt-6.1-compat.patch |patch -p1**

| Change QWT_POLAR_INSTALL_PREFIX to /usr/local and remove the following lines:
| QWT_POLAR_CONFIG += QwtPolarExamples
| QWT_POLAR_CONFIG += QwtPolarDesigner
| QWT_POLAR_CONFIG += QwtPolarFramework
| QWT_POLAR_INSTALL_FEATURES =

  .. math::

     {QWT_POLAR_INSTALL_PREFIX}/features \\
     After that, change QWT_POLAR_INSTALL_PREFIX to /usr/local and QWT_POLAR_INSTALL_HEADERS to 

  \ {QWT_POLAR_INSTALL_PREFIX}/include/qwt


  | ``**# Use full path to qmake
      qmake LIBS+="-L/usr/local/lib -lqwt" INCLUDEPATH+="/usr/local/include/qwt" qwtpolar.pro
      make -j4
      sudo make install**``

|

| **Install libad9361**

::

       **cd ~
       git clone https://github.com/analogdevicesinc/libad9361-iio
       cd libad9361-iio
       mkdir build && cd build
       cmake ..
       make
       sudo make install**

| 
| **Build and install the IIO blocks for GNU Radio**

::

       **cd ~
       git clone https://github.com/analogdevicesinc/gr-iio
       cd gr-iio
       mkdir build && cd build
       cmake ..
       make
       sudo make install**

| 
| ===== Building Scopy =====

::

       **git clone https://github.com/analogdevicesinc/scopy.git**

This will fetch the latest sources from GitHub to a "scopy" directory.

::

       **cd scopy
       mkdir build && cd build
       cmake ..**

If everything goes well, the output should be "Configuring done" and "Generating done".

Now build the project:

::

       **make**

And run Scopy:

::

       **./scopy**

**Return to** :doc:`Scopy Main Page </wiki-migration/university/tools/m2k/scopy>`
