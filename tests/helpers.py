from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_login(driver, username, password):
    """
    Inicia sesión en SauceDemo con las credenciales proporcionadas.
    """
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Esperar hasta que cargue el inventario
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

def is_element_present(driver, by, locator, timeout=5):
    """
    Verifica si un elemento está presente en la página dentro del tiempo dado.
    Retorna True si se encuentra, False si no.
    """
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        return True
    except:
        return False
