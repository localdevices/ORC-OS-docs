.. _daemon_settings:

Daemon settings
---------------

.. screenshot:: http://localhost:5173/settings
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302

The Daemon settings are at the heart of edge-processing of ORC-OS. When you run ORC-OS on an edge device, you likely
want to automatically run videos, as they come in. The principle is as follows:

- ORC-OS scans a pre-defined folder for incoming video files.
- If a file comes in, the file name will be compared against a user-define file name or file name pattern (including
  a time string format).
- If the incoming file follows this pattern, the time stamp will be read from the file, and the video file will be
  stored in the database, with the time stamp.
- If a time series record with the same, or nearly the same timestamp is found in the database, this record (with water
  level value) will be associated with the video file. This water level will then be used during processing.
- Once a full :ref:`video configuration <video_conf_intro>` is available and selected, the video will be automatically
  processed into velocity fields, discharge estimates over the cross section, and an analysis image.
  The video configuration contains information to orthorectify the video, a cross section, and settings how to
  (pre- and post-)process the video.
- In a final step, if a LiveORC API server is configured, the video record with all its information (time series record
  and video configuration) will be synchronized with the server on the set Site ID.

This form allows you to set up the Daemon settings. Important explanations of the different fields are provided below.

- Expected video filename template: this is the file naming convention used to recognize new incoming files.
- The "Parse time from the video file name" setting, if selected, extracts the time stamp of the video from the file
  name following the set template. If you unselect, the time stamp will be derived from the last moment of write to
  the file.
- Allowed time difference between video and water level time stamps. The amount of seconds allowed between a water
  level in the database and a video in the database. Every time a
  video is added to the database, ORC-OS will check if a "free" water level is available and not already linked
  to another video, that has a timestamp within the amount of seconds set here.
- Shutdown device after an automated task. You should only use this if you have a power cycling logic that ensures
  the device switches on after a set interval. It may save power in case a video processing took a brief time. A 15
  second time window is always available after processing to allow a user to login to the back end and switch off the
  service for maintenance.
- Reboot device after some time. This allows for a reboot at a set interval. Usually this should be at least one hour.
  The reboot can be used to ensure the device stays healthy. In case for some reason the device crashes and does not
  give access to the front end, this setting can result in a fresh reboot after a set interval and bring back the
  device without having to go into the field to reboot it.
- Video configurations: here, you select a completed video configuration. This configuration will be used to treat
  any incoming video. Only entirely finalized configurations will be shown here. Read more about setting up
  :ref:`Video configurations <video_conf_intro>`.
- LiveORC settings: here you select what data to synchronize. You may decide to only send resulting time series if
  band width is very limited. With larger band width you may send the analysis augmented reality image produced with
  each video, and/or the entire video. The latter is particularly useful for situational awareness for people that
  only see the LiveORC server-side, or for reprocessing on server-side e.g. in case the water level was poorly
  estimated or different settings should be applied for a good result.
- Activate the daemon runner: when settings are complete you can activate or interrupt the daemon service with this
  switch.

The most important setting is the :ref:`Video configurations <video_conf_intro>`. This part requires most attention and
needs to be performed on one video with all :ref:`field survey <field_survey>` measurements in place.
