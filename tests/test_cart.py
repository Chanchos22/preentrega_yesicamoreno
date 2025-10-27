import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # Esperar un poco más para asegurar carga visual (mantengo el tuyo)
    time.sleep(1.5)

    # Localizar el botón del producto "Sauce Labs Backpack"
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )

    # Desplazar hasta el botón
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
    time.sleep(1.5)  # Lo bajo a 1.5 para un efecto más natural

    try:
        add_button.click()
        print("🖱️ Click normal exitoso")
    except Exception:
        driver.execute_script("arguments[0].click();", add_button)
        print("⚡ Click con JavaScript ejecutado")

    # Esperar para que se vea el cambio visual al agregar al carrito
    time.sleep(2)

    # --- VALIDAR CARRITO ---
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1", f"❌ Esperado: 1, obtenido: {cart_badge.text}"

    # Pausa extra para observar el badge
    time.sleep(1.5)

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Pausa para ver la transición
    time.sleep(1.5)

    # Validar que el producto esté en el carrito
    cart_item = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    assert cart_item.is_displayed(), "❌ El producto no aparece en el carrito"

    print("✅ Test completado correctamente: producto agregado y visible en el carrito.")


