.. _quickstart:

Quickstart
==========

We here offer a very quick introduction of ORC-OS. We assume that ORC-OS is already installed on a device, that you
wish to keep running in the field, and which processes incoming videos automatically and send results to a central
server. We start with an empty database and gradually fill the first parts.

Some critical settings
----------------------
All settings are available through the right-side menu at the ... icon. Just hover over the icon to show the Settings
context menu.

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
    


We first make sure that the internal drive of the device always has some space.

LOREM IPSUM

We also set up a connection with a LiveORC server and a specific measurement site, pre-configured in LiveORC, so that
incoming videos can be reported.

.. note::

  For this step, you do need a functional LiveORC server with username and password running, accessible over the
  internet. Replace your server url and login details by your own details above.

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

Fill out the url (without suffix ``api/`` and your user email address and password in the relevant fields. Click
submit to check the details. Your username and password will disappear and a access and refresh token will appear.
You will see that your server is online also.

Let's now continue to uploading a sample video.

Video configuration
-------------------
Before going through the next steps, download our sample videos from this link. Navigate to ``Videos`` in the left
menu.

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


You can drag and drop a video in the indicated box.