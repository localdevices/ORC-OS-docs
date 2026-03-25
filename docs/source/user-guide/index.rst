.. _user-guide:

User guide
==========

This user guide describes the ORC-OS software and is intended for field hydrologists that wish 
to configure ORC-OS for use in the field. It does not treat hardware and surveying aspects.
These are described in the :ref:`hardware <prerequisites>` and the :ref:`field survey <field_survey>`
documentation. In summary, this software user guide runs through:

* Who or for what the software can be used.
* How to use the software through the web interface, focussing on general settings, entering field survey information,
  and handling of data and data synchronization with a LiveOpenRiverCam server.
* How to control the hardware through background services, i.e. additional bespoke components that are developed
  for your specific hardware setup. 
* How to modify the software interface by adding additional background services, specific to your requirements
  and setup. This is intended for developers and requires some python and/or bash scripting skills. It may also be of
  interest to users that wish to understand how the software works and how to modify it.

.. tip::

    Rainbow Sensing offers training and support for the ORC-OS software and for setup and maintenance of the 
    central server component `LiveORC`_. If you are interested in this, please
    go to https://openrivercam.org or contact us at info@rainbowsensing.com

    We also provide ready-to-flash images for a very attractive price. Support packages include:

    * Ready-to-flash image for Raspberry Pi 5 devices.
    * 8 hours of support and guaranteed software updates within one year after acquisition.
    * Several back-end services pre-programmed, including power management, relay management and remote access management.
    * Username and password for remote access to your device.

.. screenshot:: http://localhost:5173
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302

  The ORC-OS front page.

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: General

    First use <general/first_use>
    Menus <general/menus>

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: App pages

    Home <app/home>
    Videos <app/videos>
    Time series <app/timeseries>
    Device Information <app/device>
    Log file <app/log>
    Aim your camera <app/aim>
    Recipes <app/recipes>
    Cross sections <app/cross_sections>


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Settings

    General <settings/general>
    Disk management <settings/disk_management>
    Automated water level retrieval <settings/water_level_settings>
    Setting up LiveORC link <settings/liveorc>
    Over-The-Air Updates <settings/updates>
    Daemon for automated processing <settings/daemon>
    Background services <settings/services>

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Video configuration

    What is a video configuration? <video_conf/intro>
    Field preparations <video_conf/preparations>
    Camera calibration <video_conf/camera_calib>
    Water level and cross sections <video_conf/cross_sections>
    Processing options <video_conf/processing>

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Developers

    What can a developer do? <developers/intro>
    Console and virtual environment <developers/backend>
    Creating background services <developers/services>
    Example service: relay management <developers/relay>
    Command-line interface <developers/cli>



.. _LiveORC: https://github.com/localdevices/LiveORC

