"""Screenshot maker for ORC-OS documentation.

This script uses playwright and allows for longer wait times for slow pages.
"""

from playwright.sync_api import sync_playwright
import time
from pathlib import Path



def capture_screenshot(page, config):
    """Capture a single screenshot with given configuration."""
    print(f"📸 Capturing: {config['description']}")
    print(f"   URL: {config['url']}")
    
    try:
        # Navigate to page
        page.goto(config["url"], wait_until="domcontentloaded", timeout=60000)
        
        # Wait for network to be idle
        try:
            page.wait_for_load_state("networkidle", timeout=30000)
        except:
            print("   ⚠️  Network didn't fully idle, continuing anyway...")
        
        # Wait additional time for dynamic content
        page.wait_for_timeout(config.get("wait_time", 5000))
        
        # Optional: Scroll to trigger lazy loading
        page.evaluate("""
            () => {
                window.scrollTo(0, 100);
                setTimeout(() => window.scrollTo(0, 0), 100);
            }
        """)
        page.wait_for_timeout(1000)
        
        # Take screenshot
        output_path = config["filename"]
        page.screenshot(path=str(output_path), full_page=False)
        
        print(f"   ✅ Saved to: {output_path}")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def make_screenshots(screenshots):
    """Main function to capture all configured screenshots."""
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        
        success_count = 0
        fail_count = 0
        
        for config in screenshots:
            # Create context with specified settings
            context = browser.new_context(
                viewport=config.get("viewport", {"width": 1920, "height": 1080}),
                color_scheme=config.get("color_scheme", "dark"),
            )
            
            page = context.new_page()
            
            if capture_screenshot(page, config):
                success_count += 1
            else:
                fail_count += 1
            
            page.close()
            context.close()
            print()  # Blank line between screenshots
        
        browser.close()
    
    print("=" * 60)
    print(f"✨ Complete! {success_count} succeeded, {fail_count} failed")
    
    if fail_count > 0:
        print("\n⚠️  Some screenshots failed. Make sure:")
        print("   - FastAPI backend server is running at http://localhost:5000")
        print("   - React dev server is running at http://localhost:5173")
        return 1
    
    return 0

