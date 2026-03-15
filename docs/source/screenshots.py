from pathlib import Path

screenshots = [
    {
        "url": "http://localhost:5173/video?editVideoId=38",
        "filename": Path(__file__).parent / "_images" / "_screenshots" / "video_edit_water_level.png",
        "viewport": {"width": 1920, "height": 1280},
        "wait_time": 15000,  # milliseconds
        "color_scheme": "dark",
        "description": "Video editing page with water level editor",
    },
    {
        "url": "http://localhost:5173/video_config/42",
        "filename": Path(__file__).parent / "_images" / "_screenshots" / "video_config_start.png",
        "viewport": {"width": 1280, "height": 960},
        "wait_time": 3000,
        "color_scheme": "dark",
        "description": "Video config start page",
        "interactions": """
async () => {
    const nameField = document.querySelector('input[id="name"]');
    await new Promise(resolve => setTimeout(resolve, 2000));
    if (nameField) {
        nameField.value = 'A brand new video configuration';
    }
}
"""
    },  

    # Add more screenshots as needed
    {
        "url": "http://localhost:5173/video_config/42",
        "filename": Path(__file__).parent / "_images" / "_screenshots" / "video_config_water_level.png",
        "viewport": {"width": 1280, "height": 960},
        # "wait_time": 3000,
        "color_scheme": "dark",
        "description": "Video config water level settings",
        "interactions": """
async () => {
    const configTabs = document.querySelectorAll('.tabs-row')[1];
    if (configTabs.children.length > 0) {
        configTabs.children[3].dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
        // Wait for Vue/React to re-render the tab
        await new Promise(resolve => setTimeout(resolve, 500));
        const mb3Items = [...document.querySelectorAll('.mb-3.mt-3')];
        if (mb3Items.length > 4) {
          const z0Item = [...mb3Items].filter(div => {
            const label = div.querySelector('label');
            return label?.getAttribute('for') == 'z_0';
          })[0];
          const hRefItem = [...mb3Items].filter(div => {
            const label = div.querySelector('label');
            return label?.getAttribute('for') == 'h_ref';
          })[0];
          const rect1 = z0Item.getBoundingClientRect();
          const overlay1 = document.createElement('div');
          Object.assign(overlay1.style, {
            position: 'absolute',
            top: (rect1.top + window.scrollY - 6) + 'px',
            left: (rect1.left + window.scrollX - 10) + 'px',
            width: (rect1.width + 20) + 'px',
            height: (rect1.height + 12) + 'px',
            border: '5px solid #494949',
            borderRadius: '6px',
            zIndex: '999999',
            pointerEvents: 'none',
            boxSizing: 'border-box'
          });
          document.body.appendChild(overlay1);
          const rect2 = hRefItem.getBoundingClientRect();
          const overlay2 = document.createElement('div');
          Object.assign(overlay2.style, {
            position: 'absolute',
            top: (rect2.top + window.scrollY - 6) + 'px',
            left: (rect2.left + window.scrollX - 10) + 'px',
            width: (rect2.width + 20) + 'px',
            height: (rect2.height + 12) + 'px',
            border: '5px solid #0E981C',
            borderRadius: '6px',
            zIndex: '999999',
            pointerEvents: 'none',
            boxSizing: 'border-box'
          });
          document.body.appendChild(overlay2);
        }
      }
    }
"""
    },
    {
        "url": "http://localhost:5173/video_config/42",
        "filename": Path(__file__).parent / "_images" / "_screenshots" / "video_config_upload_cs.png",
        "viewport": {"width": 1280, "height": 960},
        # "wait_time": 3000,
        "color_scheme": "dark",
        "description": "Video config upload cross section",
        "interactions": """
async () => {
    const configTabs = document.querySelectorAll('.tabs-row')[1];
    if (configTabs.children.length > 0) {
        configTabs.children[3].dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
        // Wait for Vue/React to re-render the tab
        await new Promise(resolve => setTimeout(resolve, 500));
        const btns = document.querySelectorAll('.btn.btn-primary');
        if (btns.length > 0) {
          const btn = [...btns].filter(div => {
            return div?.textContent?.trim() == "Upload new";
          })[0];
          btn.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
          await new Promise(resolve => setTimeout(resolve, 500));
        }
    }
}
"""
    },
]
