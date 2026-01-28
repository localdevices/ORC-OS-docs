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
  a datetime string format).
- If the incoming file follows this pattern, the datetime stamp will be read from the file, and the file will be stored
  in the database, with the timestamp.
- If a timeseries record with the same, or nearly the same timestamp is found in the database, this record (with water
  level value) will be associated with the video file. This water level will then be used during processing.
- If a full video configuration is available and selected (including information to orthorectify the video, a cross
  section, and settings how to process the video), the video will be automatically processed into velocity fields,
  discharge estimates over the cross section, and an analysis image.
- In a final step, if a LiveORC API server is configured, the video record with all its information (time series record
  and video configuration) will (if available) be synchronized with the server on the set Site ID.

This form allows you to set up the Daemon settings. Important explanations of the different fields are provided below.

- Expected video filename template: this is the file naming convention used to recognize new incoming files.
- The "Parse dates from the video file name" settings, if selected, extracts the datetime stamp of the video.
  If you unselect, the datetime stamp will be derived from the last moment of write to the file.
- Allowed time difference between video and water level time stamps. The amount of seconds allowed between a water
  level in the database and a video in the database. Every time a
  video is added to the database, ORC-OS will check if a "free" water level is available and not already linked
  to another video, that has a timestamp within the amount of seconds set here.
- Shutdown device after an automated task. You should only use this if you have a power cycling logic that ensures
  the devive switches on also after a while. It may save power in case a video processing took a brief time. A 15 second
  time window is always available after processing to allow a user to login to the back end and switch off the service
  for maintenance.

