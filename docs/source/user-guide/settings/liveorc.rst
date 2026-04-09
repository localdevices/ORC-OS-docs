.. _liveorc:

Setting up LiveORC API
----------------------
.. screenshot:: http://localhost:5173/callback_url
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // Find the elements by their IDs, change values
    const url = document.getElementById('url');
    if (url) {
        url.value = 'https://liveorc.my-organisation.me/';
    }
    const user = document.getElementById('user');
    if (user) {
        user.value = 'john.doe@my-organisation.me';
    }
    const password = document.getElementById('password');
    if (password) {
        password.value = 'myp@ssw0rd';
    }
    const refresh = document.getElementById('tokenRefresh');
    if (refresh) {
        refresh.value = '';
    }
    const access = document.getElementById('tokenAccess');
    if (access) {
        access.value = '';
    }

  The LiveORC API settings page. Here you can set up server url and credentials for synchronizing data with a LiveORC
  server.



If you are running or have (write) access to a LiveOpenRiverCam server, you can set up a connection here.
Just fill out url, username and password and submit these. The username and password will be replaced by an
access and refresh token. The refresh token will be automatically used to regenerate access codes once the access
token is expired (after 6 hours).

In addition you may set:

- a "Site id". This is the id number belonging to a geographical site location as set up in LiveORC. Once you have
  made a site in LiveORC, write down its ID number and provide it here to automatically post incoming and processed
  videos when you have established :ref:`Daemon settings <daemon_settings>`. This site number is a requirement for the
  Daemon settings.
- an amount of time to retry syncing data with the set LiveORC server in case connectivity is limited. This setting
  is important in case your device may suffer from interruptions in connectivity, or connectivity is delayed because a
  modem takes time to come online after power cycling your device. This is the case e.g. with Starlink modems that
  typically require 1 to 2 minutes of time before they provide connectivity.

Once you have a valid url, user name and password, you will also see the online status of the set LiveORC
server at the bottom of the page. This will also be shown at the front page of ORC-OS.