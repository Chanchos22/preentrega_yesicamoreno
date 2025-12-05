from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def perform_login(driver, username, password):
    driver.get("https://www.saucedemo.com/")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    # Completar campos
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 5)

    # 1) Intentar login exitoso → URL debe contener inventory.html
    try:
        wait.until(EC.url_contains("inventory.html"))
        return True  # Login OK

    except TimeoutException:
        # 2) Si no se pudo loguear, buscar mensaje de error
        try:
            error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
            return False  # Login inválido
        except:
            raise Exception(
                "El login falló pero no apareció mensaje de error ni cambió la URL."
            )


def is_element_present(driver, by, locator, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        return True
    except:
        return False


def login(driver, usuario, password):
    return perform_login(driver, usuario, password)

