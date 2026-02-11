.. _videos:

Videos
------

.. screenshot:: http://localhost:5173/video
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302

The videos page gives detailed access to all your video data. On the main page you will see three main sections:

* A zone where you can drop new videos.
* A filter and bul action section. Here you can filter videos on dates, do bulk selection for downloading, synchronizing
  and deleting video records, or do downloads and deletes on selected items in the video list
* A list with video records, including their status, associated time series (if any). and a number of actions.

Uploading new videos
++++++++++++++++++++
You can manually upload a video. Just drop a file in the zone or click to select one. After selecting a video file,
enter the date and time and click "Upload". That's it! A new fresh record will appear in the list at the associated date.
If you don't see it, it could be that it has a relatively old date compared to other videos. You can scroll down,
go to next pages, or filter out specific dates to find it.

During uploading, the time stamp provided will be compared against time stamps of available water level records.
If you have already :ref:`setup a water level query <water_level>` and the timestamp of the video is close enough to a
recorded water level sample timestamp, then the water level will be automatically matched against the video. You will
then see this water level appear in the "Time series" field in the table.

.. _videos_bulk_action:

Filtering and bulk actions
++++++++++++++++++++++++++

At some point, you may need to perform many times the same action on a large amount of videos. For this, we designed
"bulk actions". It works as follows: click on the desired actions, "Download", "Synchronize" or "Delete". A pop-up
will appear requesting a start and end date. Select these and click on "Confirm <action>". This will execute the
selected action. Consider for instance the following use cases:

* ORC-OS is installed on a station, which has been offline for a while due to lack of data in a 4G bundle. After
  resupplying data, synchronize those records that have been missed in a designated time interval with just one command.
* A station is installed at a remote site with no internet connection. You may drive by the location, connect a laptop
  and simply download all video records interactively once every week to keep track of the data collection.
* A station is taken down and reinstalled at another location. You may want to delete a large amount of old records,
  that have already been downloaded or synchronized with a LiveORC server.

Downloading and deleting can also be done on selected records.

.. note::

   when choosing a bulk action for a large period, indexation may take a while and may cause the web interface to not
   respond for a while. Once indexation is done, all processing occurs in a separate thread and the web interface
   should be available again.

.. warning::

   Deleting a record means that all data is deleted from disk. This includes the video file itself, thumbnail, and any
   associated files created during processing, such as NetCDF files and log files. This cannot be reversed! The
   associated time series record will remain available.

Video list
++++++++++
Videos are by default ordered on the Timestamp field. This ensures that the latest video in terms of the associated
time stamp is always at the top the table. At the bottom of the table, you can select the amount of records to display
in one page, and browse through the pages.

A few important remarks should be made about the records:

* each record may have an associated "Time series" field, which in turn may contain water level, discharge, and surface
  and bulk velocity estimates. As mentioned above, this time series field may also only contain a water level if no
  processing has been performed yet, or nothing at all if no close (in time) water level record was found, or water
  levels are not available at all.
* each record has several "Actions" available: these include a "Play" button for displaying the video and results of
  the analysis, a "Sync" button for interactive syncing of an individual record, a "Edit" button, with which you can
  supply a new or modify an existing water level with a video in case the water level is not available or inaccurate,
  a "Delete" button for removing an individual record, a "log file" button, bringing up a log file for the specific
  analysis, and a "video configuration" button which can have different icons and color codes dependent on its state.

Below we briefly describe the less obvious buttons. For the "video configuration" button, we refer to the section on
:ref:`video configuration <video_conf_intro>`.

.. _videos_edit:

Displaying your video
+++++++++++++++++++++
Click the play button to see your video, an analysis augmented reality view of results and the time series and status.
If the file is synced to a LiveORC server, you will also get a direct link to the LiveORC record. The augmented reality
result image and time series are only available when processing to water levels, velocities, and discharge has been
performed on the video. Otherwise the associated fields are left empty with a ``-`` sign.

Editing your video's water level
++++++++++++++++++++++++++++++++
.. screenshot:: http://localhost:5173/video
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // Find the elements by their IDs, change values
    // Disable animations for deterministic screenshots
    const style = document.createElement('style');
    style.innerHTML = `
      * {
        transition: none !important;
        animation: none !important;
      }
    `;
    document.head.appendChild(style);
    const table = document.querySelectorAll('[class="table table-bordered table-striped"]')[0];
    const content = table.children[1];
    const row = content.children[0];
    const buttonEdit = row.children[9].children[0];
    const clickButton = async () => {
      buttonEdit.click();
      // Force React + layout flush
      document.body.offsetHeight;
      // Small sync delay (now safe)
    }
    await clickButton();
    const end = Date.now() + 2000;
    while (Date.now() < end) {}


if (buttonEdit) {
  const rect = buttonEdit.getBoundingClientRect();
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
  buttonEdit.click();
  // Force React + layout flush
  document.body.offsetHeight;

  // buttonEdit.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
  // Wait 2000ms for the menu animation to complete
  // Synchronous delay using a busy-wait loop (2000ms)
}

Click the edit button to bring up a side view of the cross section and the associated water level (if any).
In this view you can now start editing the water level with a slider. If there is no water level asscoaited yet, create
a new record by clicking on "Add water level". Once you are satisfied, click on "submit video with water level" to
process it. You may also decide to let ORC estimate the water level for you. Click on "Submit and estimate level
optically" to use this option.

