.. _liveorc:

Setting up LiveORC link
-----------------------
If you are running or have (write) access to a LiveOpenRiverCam server, you can set up a connection here.
Just fill out url, username and password and an access and refresh token will be provided.

In addition you may set
- a ``site id``. This is the id number belonging to a geographical site location as set up in LiveORC. Once you have
  made a site in LiveORC, write down this number and provide it here to automatically post incoming and processed videos
  when you have established :ref:`Daemon settings <daemon_settings>`
- an amount of time to retry syncing data with the set LiveORC server in case connectivity is limited. This setting
  is important in case your device may suffer from interruptions in connectivity, or connectivity is delayed because a
  modem takes time to come online after power cycling your device. This is the case e.g. with Starlink modems that
  typically require 1 to 2 minutes of time before they provide connectivity.

Once you have a valid url, user name and password, you will also see the online status of the set LiveORC
server at the bottom of the page. This will also be shown at the front page of ORC-OS.