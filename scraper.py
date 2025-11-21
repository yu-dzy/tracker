import time
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# URL to screenshot
URL = "https://polymarket.com/event/elon-musk-of-tweets-november-18-november-25?tid=1763763629223"


def take_screenshot():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # In GitHub Actions, Chrome is already installed in the environment
    driver = webdriver.Chrome(options=chrome_options)

    try:
        print("Loading page...")
        driver.get(URL)
        time.sleep(10) # Wait for load

        # Set size for full page
        total_width = driver.execute_script("return document.body.parentNode.scrollWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        driver.set_window_size(total_width, total_height)
        time.sleep(2)

        # Create filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        # We save it to a folder called 'screenshots'
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
            
        filename = f"screenshots/polymarket_{timestamp}.png"
        driver.save_screenshot(filename)
        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    take_screenshot()
