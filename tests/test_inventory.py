# test_inventory.py
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
    
def test_inventory(login_in_driver):
    try:
        driver = login_in_driver
        assert driver.title == "Swag Labs"

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()

