# test_login.py
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    chrome_opt.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_opt)
    driver.maximize_window()  # ✅ Maximiza la ventana
    yield driver
    driver.quit()

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()





