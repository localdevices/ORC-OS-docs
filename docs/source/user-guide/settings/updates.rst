.. _updates:

Over the air updates
--------------------

Setting up LiveORC API
----------------------

.. screenshot:: http://localhost:5173/updates
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302

ORC-OS has its own Over the air (OTA) update system. If an update is available, at this page you will see
- your current ORC-OS version
- whether an update is available (with the version number)
- a description of the changes and improvements provided by the selected update

By default, the last available update is shown, but you can also select to update to a specific version.
This allows you to e.g. update to a previous version in case you cannot directly go to the last version. 
The OTA system checks if your system fulfills the right requirements for the selected update. It checks e.g.:

- Minimum previous version of ORC-OS (sometimes you first need to update to a minimum version before you can update
  to the last version)
- Minimum python version required
- Minimum available packages (with indication that these should first be installed)

If one of the minimum requirements is not met, you cannot update. A remedy for the found issues will be shown. 

.. warning:: 

   Make sure that the device has stable internet, enough data, and enough power supply. Also ensure that any services
   that interrupt power such as power cycling services are stopped AND disabled. The update process can take a few 
   minutes, and if interrupted, it may cause issues with the device or the updated code will never compile in time
   before a next restart. 

To update to the selected version, just click on the update button and check the progress on the page. Do not refresh 
during this process. If the update is finished the device will reboot automatically. After that, we recommend to
perform a full refresh of the web interface by pressing ``Ctrl+Shift+R``. Sometimes the restart takes a few minutes,
especially when the update includes a change in code that needs to be compiled. Normally this should not take more than
3 minutes.

You cannot revert to an older version.

