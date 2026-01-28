.. _first_use:

First use
---------

ORC-OS works with a web front end. If this is for instance installed on a raspberry pi device using our
images, then this front end is accessible by connecting a computer or laptop to the same network
as your raspberry pi, and then typing the IP-address of the pi in the address
bar of a browser. You can also type in ``http://`` followed by the hostname of the device if this is known to you.

.. tip::

   Usually you can find the IP-address and hostnames of network connected devices on your router's administration pages.
   Dependent on your network router, if you use the hostname to login, you may have to type
   a suffix in the address bar. This is mostly ``.local`` or ``.home``. Assuming your device is called
   ``myorcdevice`` the address (with ``.local`` as suffix) would then be ``http://myorcdevice.local``.

The first time that you use ORC-OS, you will need to setup a password. It is important
to remember this or store it in a password vault, as you can only change it by resetting it in
the back-end, for which you will need a system administrator. Once logged in, you can change the password.

After this, each time you access the ORC-OS page, you will find a page where you have to type your password as
shown below.

.. tip::

   With our annual support packages, you will also receive remote access options to devices that are installed in the field
   with a remote internet connection, such as 4G or starlink. Contact us at info@rainbowsensing.com for the available
   options.


.. screenshot:: http://localhost:5173/login
  :browser: chromium
  :viewport-width: 1024
  :viewport-height: 720
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // Find the elements by their IDs, change values
    const pw = document.querySelectorAll('[type="password"]')[0];
    if (pw) {
        pw.value = 'my_password';
    }




