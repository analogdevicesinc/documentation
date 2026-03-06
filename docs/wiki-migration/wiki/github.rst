Github at Analog Devices
========================

Analog Devices uses `GitHub <https://github.com/analogdevicesinc>`__ to distribute source code (and text files that resemble source code) which needed to be maintained.

InterWiki Links
---------------

There are a few `Interwiki link <https://wiki.analog.com/syntax>`__ shortcuts which can be used to quickly link to specific files in github. These are used to move the wiki reader to the actual code. It's not meant to provide downloads.

Link to the mainline linux kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``[[:git-linux:`path|path]]``` translates to ``http://github.com/analogdevicesinc/linux/blob/{branch}/{path}``

   -  Example: ``[[:git-linux:`arch/arm/boot/dts/zynq-adrv9361-z7035-fmc-rfcard-tdd`.dts|device tree]]`` makes :git-linux:`device tree <arch/arm/boot/dts/zynq-adrv9361-z7035-fmc-rfcard-tdd.dts>` in the wiki.

Link to a repo on github
~~~~~~~~~~~~~~~~~~~~~~~~

-  ``[[https://github.com/analogdevicesinc/repository|repository]]`` translates to ``http://github.com/analogdevicesinc/{repository}``

   -  Example: ``[[https://github.com/analogdevicesinc/HighSpeedConverterToolbox|HighSpeedConverterToolbox]]`` makes :git-HighSpeedConverterToolbox>`__ in the wiki.

Link to a specific file on github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``[[https::`HighSpeedConverterToolbox </github.com/repository?branch/path|path]]`` translates to ``http://github.com/analogdevicesinc/{repository}/blob/{branch/path}``

   -  Example: ``[[https://github.com/hdl?hdl_2016_r2/projects/pluto| Files]]`` creates this link : `Files <https://github.com/hdl?hdl_2016_r2/projects/pluto>`

Downloads
---------

We try not to distribute random zip file on the wiki, but use a on-line service from `DownGit <https://analogdevicesinc.github.io/DownGit/#/home>`__ by `Minhas Kamal <https://github.com/MinhasKamal>`__ to create links in the wiki, that point to github, and allow you to post "live" code as zip file in the wiki. ADI created a custom fork of this project since this was running into `issues <https://github.com/MinhasKamal/DownGit/issues/31>`__ for many people.

Just go to the `DownGit <https://analogdevicesinc.github.io/DownGit/#/home>`__ page, and paste the repository (including sub directory) you want to provide, and it will provide a link you can use.

Example
~~~~~~~

For example, ADI provides a javascript engine in it's scopy application, and maintain :git-scopy:`examples <js>` in the scopy repository, so it can maintained by the software team, and tested on every release. We also make sure that packaging/installers includes them as examples.

On the wiki – for things that are in sub directories of repositories, where you want to provide a zip file for end users, but not have them download the entire repository - just paste the url of the directory - in this case - ``:git-scopy:`js``` into Downgit. This will create a url:

``https://analogdevicesinc.github.io/DownGit/#/home?url=:git-scopy:`js```

which can be used in the wiki, like `here <https://analogdevicesinc.github.io/DownGit/#/home?url=:git-scopy:`js>`__` that way – end users still get the zip file, but the code is maintained in github.

There is also a shortlink for this ``[[:git-repo:`path/|]]``` which means in the wiki, you can do ``[[:git-scopy:`js|zipfile]]``` like :git-scopy:`zipfile <js>`, and it will zip up the file, and download it.

If it is just a single file (like the examples), we can just point to the top level directory, and people can download from github what they want.
