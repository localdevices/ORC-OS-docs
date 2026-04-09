.. _disk_management:

Disk management
---------------
.. screenshot:: http://localhost:5173/disk_management
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302

Under disk management, you can set:

- Minimum space [GB] below which cleanup will take place
- Critical space [GB] below which service will be turned off.
- Frequency [s] for checking space and performing cleanup.

The first amount determines when disk cleanup should take place. Disk cleanup will be done checking only files
related to OpenRiverCam. The oldest records will be cleaned first. Only files are removed. The records containing
the original filename, timestamps, and time series information will remain in the database.

.. note::

    The second amount (critical space) is not yet in use, but may be used in the future to shut down the OpenRiverCam
    service if the amount of available storage goes under the set storage threshold. This is to prevent that
    the storage runs entirely full and causes operating system level problems.

The last input determines how often ORC-OS checks if there is still sufficient storage and do cleanup actions.
You can see disk space checks and cleanup activities in the log.

.. warning::

    If your device runs operationally, we highly recommend setting up disk management to prevent getting locked out
    of your device. Typically we advice to keep a 5 GB free space.

