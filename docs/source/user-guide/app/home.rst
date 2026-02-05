.. _home:

Home page
---------

.. screenshot:: http://localhost:5173
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302

Welcome to ORC-OS! The home page is where you see the most prominent information about your device's current status.
The page is subdivided in two parts:

- on the left side you see the latest (in timestamp) processed video. For real-time operating devices, this gives a very quick
  idea of the latest state, whether the video was processed and synchronized successfully, and what the output
  looks like in terms of the water level, bulk and surface velocity and discharge.
- on the right side you see statistics of processed videos and synced video statuses as well as important device
  statuses for real-time use. It shows what settings are available for the :ref:`real-time daemon <daemon_settings>`
  (or what seems lacking) as well as the status of the :ref:`LiveORC server <liveorc>` if this is set up.

.. tip::

   Have a close look at this page to see if things seem to be ok. Things to check are typically

   - What was the timestamp of the last video processed? This may hint towards malfunctioning camera hardware or
     lost connection between the camera device and your device with ORC-OS.
   - Did the processing go ok? If not, check the :ref:`logs <log>` to see details. If you estimate water level optically
     random failures are often due to poor visibility of the water level. Check if the bottom line cross section
     over which the water level is estimated is still clear from vegetation, debris or other things that might obscure
     it.
   - Did syncing to LiveORC work? If not, then also check if the connection with LiveORC is all on green on the device
     status subpage.

