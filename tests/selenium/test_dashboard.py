import os, time, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = os.getenv("DASHBOARD_URL", "https://wazuh.example.com")

def new_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=opts)

def test_dashboard_https_and_login_form():
    driver = new_driver()
    try:
        driver.set_page_load_timeout(30)
        driver.get(URL)
        # Title should mention Wazuh (may vary slightly by version)
        assert "Wazuh" in driver.title or "Dashboard" in driver.title
        # A login form should be present
        inputs = driver.find_elements(By.TAG_NAME, "input")
        assert any("user" in (i.get_attribute("name") or "").lower() for i in inputs)
        assert any("pass" in (i.get_attribute("name") or "").lower() for i in inputs)
    finally:
        driver.quit()
