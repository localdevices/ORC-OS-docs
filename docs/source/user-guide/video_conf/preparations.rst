.. _sample_video:

Field preparations
------------------

When you are in the field, you will set up a camera and collect field measurements.
Follow as carefully as possible our :ref:`Field Guide <field_guide>` while doing this. Below, we assume
you have:

* set up and aimed a camera at a satisfactory height, overlooking as carefully as possible the measured cross section
  without seeing any sky.
* spread out "ground control points" over both left and right bank (and middle if possible) in view of the camera
  objective.
* measured the 3-D coordinates of the control points, cross-section and water level in one common coordinate system
  using one of the suggested methods. Again, precision within a few cm is very important, so use precise measurement
  instruments only.

Selecting a sample video
^^^^^^^^^^^^^^^^^^^^^^^^
Once you are satisfied with the aim, record a sample video of a few seconds, and store this on your own laptop
computer. Once stored, check if the quality is good and image is sharp, and once satisfied, go to the
:ref:`video page <videos>`. Upload the video, following the instructions. Choose a time stamp close to the moment
of taking the video.

.. screenshot:: http://localhost:5173/video
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    const dropZone = document.querySelectorAll('[role="presentation"]')[0];
    if (dropZone) {
      const rect = dropZone.getBoundingClientRect();
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
    }

  Upload the video here

Once uploaded, click on the red blinking video configuration icon next to the video, and select "Edit" to create a new
video configuration belonging to the uploaded video. A new window will open.

The video configuration screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the video configuration screen, you will see 3 major fields:

* The left-side shows the ``Camera view``  and ``Top view``. Using the two tabs, you can change between one or the
  other. The Top view does not show any information yet, as that only displays your measurement data and camera
  location.
* The top-right shows several tabs to manage the video configuration, with tabs for ``Name + details``, ``Camera pose``,
  ``Cross sections``, and ``Processing``. You must go through all tabs to get to a completed video configuration.
* The bottom-right shows side views of selected cross-sections and set water levels. This starts empty as well as
  you must first upload and select cross-sections.

.. tip::

  Under the ``Processing`` tab, you can change the first frame to process. This will also change the displayed frame
  in the ``Camera view`` to the one selected here.

.. figure:: ../../_images/_screenshots/video_config_start.png
   :align: center
   :alt: video configuration overview

   Start page of the video configuration screen. 

