"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Create a new instance of the Chrome driver
options = Options()
options.add_argument("start-maximized")  # Start Chrome in maximized window
options.add_argument("disable-infobars")  # Disable infobars
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("--load-extension=/path/to/DAWN%20Validator.crx")  # Load DAWN Validator extension

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Keep the browser running for 1 hour
print("Browser is now running. Accumulating points...")
time.sleep(3600)  # 1 hour in seconds

# Close the browser
driver.quit()
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Create a new instance of the Chrome driver
options = Options()
options.add_argument("start-maximized")  # Start Chrome in maximized window
options.add_argument("disable-infobars")  # Disable infobars
options.add_argument("--enable-extensions")  # Enable extensions
options.add_extension("chrome://extensions/?id=fpdkjdnhkakefebpekbdhillbhonfjjp")  # Load DAWN Validator extension

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Keep the browser running for 1 hour
print("Browser is now running. Accumulating points...")
#time.sleep(1000)  # 2 hours in seconds
# Close the browser
driver.quit()
