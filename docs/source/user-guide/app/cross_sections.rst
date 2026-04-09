.. _cross_sections:

Cross sections
--------------

.. screenshot:: http://localhost:5173/cross_section
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302
  :interactions:
    // Find the elements by their IDs, change values
    const table = document.querySelectorAll('[class="table table-bordered table-striped"]')[0];
    const content = table.children[1];
    const row = content.children[0];
    const buttonEdit = row.children[3].children[0];
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
    }


This page is only meant to administrate cross section records. You can here delete obsolete cross sections if you wish.
They are not large to store, so it is usually not needed to delete them. You can also conveniently store the cross
section data as GeoJSON files. Note that these do not have a coordinate reference system (CRS) if the original uploaded
files do not contain a coordinate reference system. If you load the saved GeoJSON in QGIS you can manually assign a CRS.

