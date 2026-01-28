.. _menus:

Navigation menus
================

Main menu
---------

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

  Main menu

On the top-left side, you can find a large menu button, which
expands a menu providing access to the datasets and functionalities around those datasets
such as videos, time series, logs and functionalities to aim the camera manage the datasets,
and set up calibrations for use in automated video processing.

Settings menu
-------------

.. screenshot:: http://localhost:5173
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // Find the elements by their IDs, change values
    const wrappers = document.querySelectorAll('.user-menu-wrapper');
    if (wrappers.length > 0) {
      const menu = wrappers[0];
      const rect = menu.getBoundingClientRect();
      const overlay = document.createElement('div');
      Object.assign(overlay.style, {
        position: 'absolute',
        top: (rect.top + window.scrollY - 10) + 'px',
        left: (rect.left + window.scrollX - 10) + 'px',
        width: (rect.width + 20) + 'px',
        height: (rect.height + 20) + 'px',
        border: '5px solid red',
        borderRadius: '6px',
        zIndex: '999999',
        pointerEvents: 'none',
        boxSizing: 'border-box'
      });
      document.body.appendChild(overlay);
      const hoverEvent = new MouseEvent('mouseover', {
        bubbles: true,
        cancelable: true,
        view: window
      });
      menu.dispatchEvent(hoverEvent);
    }

  Settings menu

The settings menu provides more general settings to keep the device running the way you want.
Here you setup connectivity with your own LiveORC webserver, manage the devices disk space and setup
automated processing. The individual settings are further described under :ref:`Settings <ug_general>`


User menu
---------
.. screenshot:: http://localhost:5173
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // Find the elements by their IDs, change values
    const wrappers = document.querySelectorAll('.user-menu-wrapper');
    if (wrappers.length > 1) {
      const menu = wrappers[1];
      const rect = menu.getBoundingClientRect();
      const overlay = document.createElement('div');
      Object.assign(overlay.style, {
        position: 'absolute',
        top: (rect.top + window.scrollY - 10) + 'px',
        left: (rect.left + window.scrollX - 10) + 'px',
        width: (rect.width + 20) + 'px',
        height: (rect.height + 20) + 'px',
        border: '5px solid red',
        borderRadius: '6px',
        zIndex: '999999',
        pointerEvents: 'none',
        boxSizing: 'border-box'
      });
      document.body.appendChild(overlay);
      const hoverEvent = new MouseEvent('mouseover', {
        bubbles: true,
        cancelable: true,
        view: window
      });
      menu.dispatchEvent(hoverEvent);
    }

  User menu