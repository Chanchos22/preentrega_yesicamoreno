import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.inventory_page import InventoryPage


@pytest.fixture
def driver():
    """Configura y devuelve la instancia del WebDriver."""
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    chrome_opt.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_opt)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_cart_flow(driver):
    """Prueba el flujo de login, añadir un producto y verificar el carrito."""

    # --- LOGIN ---
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # --- INVENTORY PAGE ---
    inventory = InventoryPage(driver)
    inventory.agregar_primer_producto()    # <--- Método correcto de tu clase
    inventory.abrir_carrito()              # <--- Método correcto de tu clase

    # Verificar que el carrito tiene 1 producto
    assert inventory.obtener_conteo_carrito() == 1

    # Verifico que haya un ítem en el carrito
    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items) == 1

    time.sleep(2)
