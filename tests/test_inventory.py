from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from utils import is_element_present  # Asegurate de tener esta función en utils.py
from utils import login

@pytest.fixture
def driver():
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    chrome_opt.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_opt)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        # Validar título de la página
        assert driver.title == "Swag Labs", f"❌ Título incorrecto: {driver.title}"

        # Validar existencia de productos
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "❌ No hay productos visibles en la pagina"

        # Validar existencia de menú y filtros
        assert is_element_present(driver, By.CLASS_NAME, "product_sort_container"), "❌ Filtro de productos no visible"
        assert is_element_present(driver, By.ID, "header_container"), "❌ Menú superior no visible"

        # Validar nombre y precio del primer ítem de la lista
        first_item = products[0]
        item_name = first_item.find_element(By.CLASS_NAME, "inventory_item_name").text
        item_price = first_item.find_element(By.CLASS_NAME, "inventory_item_price").text
        assert item_name != "", "❌ El primer producto no tiene nombre"
        assert item_price != "", "❌ El primer producto no tiene precio"

    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()

