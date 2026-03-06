About
=====

The ACE Plug-in Manager uses an external package source in order to retrieve the latest available ACE plug-ins, allowing users to install plug-ins to evaluate new products, or get the latest updates available for a plug-in which is already installed.

Ideally, the user never needs to interact with this, but unfortunately there is always the possibility of downtime, and since we are using a 3rd party hosting provider, we have limited control over the timing and length of outages when they occur.

In order to ensure availability of new plug-ins and updates for users in the event of an outage, we have mirrored our package feed to other externally-hosted sources, which are available below. The following steps describe how users can add these sources in ACE to access plug-in feeds in case of an outage on the main feed.

Sources
=======

.. note::

   Note that the Azure DevOps Plug-in Feed is only compatible with ACE V1.28.3258.1431+


-  MyGet Master Plug-in Feed: `https:www.myget.org/F/adiaceplugins/api/v3/index.json]] \* Azure DevOps Plug-in Feed: [[https:\ pkgs.dev.azure.com/ADI-ACE/AdiAcePlugins/\_packaging/AzurePlugins/nuget/v3/index.json|https://pkgs.dev.azure.com/ADI-ACE/AdiAcePlugins/\_packaging/AzurePlugins/nuget/v3/index.json <https://www.myget.org/F/adiaceplugins/api/v3/index.json>`__

Steps
=====

In ACE, open the Settings menu and navigate to the Plug-ins tab.

Under the Custom Plug-in Sources dropdown, click the **+** button to add a new Custom Plug-in Source. Add an appropriate name and the link to the selected plug-in source above in the relevant textboxes.

Ensure that the Enabled checkbox on the source is checked and click Ok to save changes.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/custompackagesources.jpg
   :align: center
   :width: 500px

Navigate to the Plug-in Manager and you should now see the new package source available under the Available Packages and Available Updates tabs.

Select the new source to browse and install plug-in packages and updates from the new source.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/custompackagesourcespluginmanager.jpg
   :align: center
   :width: 200px
