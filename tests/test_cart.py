import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from utils import perform_login, is_element_present
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

def test_cart_flow(driver):
    driver.get("https://www.saucedemo.com/")

    # --- LOGIN ---
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # --- INVENTARIO ---
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    time.sleep(1.5)

    # Localizar el botón del producto "Sauce Labs Backpack"
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
    time.sleep(1.5)

    try:
        add_button.click()
        print("🖱️ Click normal exitoso")
    except Exception:
        driver.execute_script("arguments[0].click();", add_button)
        print("⚡ Click con JavaScript ejecutado")

    time.sleep(2)

    # --- VALIDAR CARRITO ---
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1", f"❌ Esperado: 1, obtenido: {cart_badge.text}"
    time.sleep(1.5)

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1.5)

    # Validar que el producto esté en el carrito
    cart_item = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    assert cart_item.is_displayed(), "❌ El producto no aparece en el carrito"

    # Validar nombre del item
    cart_item_name = cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item_name == "Sauce Labs Backpack", f"❌ Nombre del producto incorrecto: {cart_item_name}"

    # Validar precio del item
    cart_item_price = cart_item.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert cart_item_price == "$29.99", f"❌ Precio del producto incorrecto: {cart_item_price}"

    print("✅ Test completado correctamente: producto agregado y visible en el carrito.")

