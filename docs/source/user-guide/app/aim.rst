.. _aim:

Aim your camera
---------------
This page should only be used in the field. It is meant to capture a live view from your connected camera system
so that you can aim the camera. In case you have at least one Raspberry Pi camera connected to the device, the
page shows specific options for Raspberry Pi camera's.

Use with a camera with an IP or other remote address
++++++++++++++++++++++++++++++++++++++++++++++++++++
Make sure that you have a camera that is set up to broadcast live over a IP-address, or public web address.
Simply fill out the address including prefix (such as ``rtsp://``) over which the camera broadcasts live footage
to bring up the camera's live view. You can then go ahead and aim

Setting up LiveORC API
----------------------
.. screenshot:: http://localhost:5173/camera_aim
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


Raspberry Pi camera's
+++++++++++++++++++++
If you have one or more Raspberry Pi camera's connected that you wish to use, you will get specific options for these
camera's. First, if you have more than one camera installed, you can select which camera you wish to use. You can
then choose a resolution and framerate and preview the camera with a switch. There is also a little red record
button. After aiming, set a time in seconds and click on this button to record a sample video immediately. You can then
immediately use this sample video for setting up your :ref:`video configuration <video_conf_intro>`.

