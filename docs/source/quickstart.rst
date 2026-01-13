.. _quickstart:

Quickstart
==========

We here offer a very quick introduction of ORC-OS. We assume that ORC-OS is already installed on a device, that you
wish to keep running in the field, and which processes incoming videos automatically and send results to a central
server. We start with an empty database and gradually fill the first parts.

Some critical settings
----------------------
All settings are available through the right-side menu at the  icon. Just hover over the |settings_icon| icon to show
the Settings context menu.

.. screenshot:: http://localhost:5173
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // find element of menu, and hover over it.
    const settingsMenu = document.querySelectorAll('[class="user-menu-wrapper"]')[0];
    if (settingsMenu) {
      settingsMenu.dispatchEvent(new MouseEvent('mouseover', { bubbles: true, cancelable: true }));
    }
    const menuItem = document.querySelectorAll('[class="user-menu-item"]')[1];
    if (menuItem) {
      // hover!
      // menuItem.dispatchEvent(new MouseEvent('hoverover', { bubbles: true, cancelable: true }));
      // menuItem.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true, cancelable: true }));
      // Apply the hover styles directly:
      menuItem.style.backgroundColor = '#495057';
    }
    // Wait for animation
    const end = Date.now() + 300;
    while (Date.now() < end) {}


We first make sure that the internal drive of the device always has some space. Click on ``Disk management``.

.. screenshot:: http://localhost:5173/disk_management
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // Find the elements by their IDs, change values
    const field1 = document.getElementById('min_free_space');
    if (field1) {
        field1.value = 5;
    }
    const field2 = document.getElementById('critical_space');
    if (field2) {
        field2.value = 2;
    }
    const field3 = document.getElementById('frequency');
    if (field3) {
        field3.value = 3600;
    }

Insert the values indicated. This will ensure that disk space remains above 5 GB. The critical space value is not yet
used but may get a role in a future update. The application will check every 3600 seconds (one hour) if space needs
to be freed up, and will do so by removing the oldest video data and analyses first.

Let's also set up a LiveORC connection if you have a LiveORC server running. If not skip the next step.

.. note::

  For this step, you do need a functional LiveORC server with username and password running, accessible over the
  internet. Replace your server url and login details by your own details above.

Go to the settings menu and select ``LiveORC API``.

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

Fill out your own url (without suffix ``api/`` and your user email address and password in the relevant fields. Click
submit to check the details. Your username and password will disappear and a access and refresh token will appear.
You will see that your server is online also.

Let's now continue to uploading a sample video.

Video configuration
-------------------
Before going through the next steps, download our sample videos from this link. Navigate to the  ``Videos`` in the left
menu.


.. screenshot:: http://localhost:5173
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // find element of main menu, and click on it.
    const mainMenu = document.querySelectorAll('[class="navbar-toggler-icon"]')[0];
    if (mainMenu) {
      mainMenu.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
    }
    // Find element of video menu
    const el = document.querySelectorAll('[href="video"]')[0];
    if (el) {
      // hover!
      el.dispatchEvent(new MouseEvent('hoverover', { bubbles: true, cancelable: true }));
    }
    // Wait 300ms for the menu animation to complete
    // Synchronous delay using a busy-wait loop (300ms)
    const end = Date.now() + 300;
    while (Date.now() < end) {}

  Location of the video menu in ORC-OS.

.. screenshot:: http://localhost:5173/video
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // Find the element by its CSS selector
    const el = document.querySelectorAll('[role="presentation"]')[0];
    if (el) {
      const rect = el.getBoundingClientRect();
      const overlay = document.createElement('div');
      Object.assign(overlay.style, {
        position: 'absolute',
        top: (rect.top + window.scrollY - 10) + 'px',
        left: (rect.left + window.scrollX - 20) + 'px',
        width: (rect.width + 40) + 'px',
        height: (rect.height + 25) + 'px',
        border: '5px solid red',
        borderRadius: '3px',
        zIndex: '999999',
        pointerEvents: 'none',
        boxSizing: 'border-box'
      });
      document.body.appendChild(overlay);
    }

  Drag-and-drop window for new videos.

You can drag and drop a video in the indicated box. Drag and drop it into the window. You can also click on
the drag-and-drop zone to find the video file in your file browser.



.. |settings_icon| raw:: html

   <i class="fa-solid fa-gear" aria-hidden="true"></i>
