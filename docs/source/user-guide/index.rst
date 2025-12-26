.. _user-guide:

User guide
==========

This user guide is intended for field hydrologists that wish to configure ORC-OS for use in the field. In summary, it
runs through:

* who or for what the software can be used.
* prerequisites, needed materials, site conditions and required hydrology and surveying skills.
* How to use the software through the web interface, focussing on general settings, entering field survey information,
  and handling of data and data synchronization with a LiveOpenRiverCam server.

.. screenshot:: http://localhost:5173
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302

  The ORC-OS front page.


:interactions:
  // Find the element by its CSS selector
  const el = document.querySelector('.custom-logo-link');
  if (el) {
      const rect = el.getBoundingClientRect();
      const overlay = document.createElement('div');
      Object.assign(overlay.style, {
        position: 'absolute',
        top: (rect.top + window.scrollY - 30) + 'px',
        left: (rect.left + window.scrollX - 20) + 'px',
        width: (rect.width + 40) + 'px',
        height: (rect.height + 60) + 'px',
        border: '10px solid red',
        borderRadius: '5px',
        zIndex: '999999',
        pointerEvents: 'none',
        boxSizing: 'border-box'
      });
      document.body.appendChild(overlay);
  }

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: How to use ORC-OS

    What and for whom is ORC-OS? <general/whom>
    How to obtain ORC-OS <general/getting_orcos>
    Prerequisites for using ORC-OS <general/prerequisites>
    Suitable site conditions <general/site_conditions>
    Required field survey measurements <general/field_survey>


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Settings

    General <settings/general>
    Disk management <settings/disk_management>
    Automated water level retrieval <settings/water_level_settings>
    Setting up LiveORC link <settings/liveorc>
    Over-The-Air Updates <settings/updates>


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: App pages

    Home <app/home>
    Videos <app/videos>
    Device Information <app/device>
    Log file <app/log>
    Aim your camera <app/aim>
    Recipes <app/recipes>
    Cross sections <app/cross_sections>

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Video configuration

    What is a video configuration for? <video_conf/intro>
    Selecting a sample video <video_conf/sample_video>
    Camera calibration <video_conf/camera_calib>
    Selecting an area of interest <video_conf/aoi>
    Selecting cross sections <video_conf/cross_sections>
    Processing options <video_conf/processing>

