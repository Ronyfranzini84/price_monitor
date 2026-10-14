from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Website URL
url = "https://www.magazineluiza.com.br/busca/computador-c-monitor-teclado-e-mouse/"

# Configure Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Start browser
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open website
    driver.get(url)

    # Display page information
    print(f"Page title: {driver.title}")
    print(f"Current URL: {driver.current_url}")

    input("\nPress Enter to close the browser...")

finally:
    # Close browser
    driver.quit()