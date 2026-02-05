.. _log:

Log file
--------
Go to this page to check real-time what the ORC-OS backend is working on. It will show real-time information such as
new water levels coming in, disk cleanup checks and activities and detailed information at INFO and DEBUG level
of currently running videos and what is done with these. If anything goes wrong, check this log page to find out
more details about your issue.

.. tip::

    Typical problems with video processing you may encounter:

    - Syncing failed because a LiveORC server is down
    - Water level could not be optically estimated. In this case you will find an error hinting this, and you can still
      :ref:`assign a water level yourself <videos_edit>` with a nice user friendly slider and reprocess.
    - Unrealistic water levels are used found that are below the lowest or above the highest level of the assigned cross
      section. Check if your water level settings in the :ref:`video configuration <vc_water_level>` are set to the
      right levels and datums. This often goes wrong, and is very essential to understand the horizontal plane
      of the water in the field of view, and to estimate the wetted cross section.

