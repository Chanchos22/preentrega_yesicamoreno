from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from utils import is_element_present
from utils import login
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import time

@pytest.mark.parametrize("usuario, password", [("standard_user", "secret_sauce")])
def test_cart2(login_in_driver, usuario, password):
    driver = login_in_driver

    try:
        inventory_page = InventoryPage(driver)

        # Agregar al carrito el primer producto
        inventory_page.agregar_primer_producto()
        time.sleep(1)

        # Abrir el carrito
        inventory_page.abrir_carrito()
        time.sleep(1)

        # Validar el producto
        cart_page = CartPage(driver)
        time.sleep(1)

        producto_nombre = cart_page.obtener_nombre_producto_carrito()
        assert isinstance(producto_nombre, str) and len(producto_nombre) > 0

    except Exception as e:
        print(f"Error en test_cart2: {e}")
        raise

    finally:
        driver.quit()
