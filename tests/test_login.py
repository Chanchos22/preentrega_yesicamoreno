from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.datos import leer_csv_login
from utils.logger import logger   # ✅ IMPORTACIÓN CORRECTA

# --- FIXTURE ---

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

# --- PRUEBA ---

@pytest.mark.parametrize("usuario,password,debe_funcionar", leer_csv_login("datos/data_login.csv"))
def test_login_validation(driver, usuario, password, debe_funcionar):
    """Prueba la funcionalidad de login usando datos de un CSV."""

    # 1. Ejecutar Login
    logger.info(f"Completando con los datos del usuario: {usuario}")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # 2. Validación
    if debe_funcionar == 'True':
        logger.info("Verificando redireccionamiento dentro de la página")
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        logger.info("Test de login exitoso")

    elif debe_funcionar == 'False':
        logger.info("Verificando mensaje de error para login fallido")
        mensaje_error = LoginPage(driver).obtener_error()
        assert "Epic sadface" in mensaje_error, "El mensaje de error no se está mostrando correctamente"
        logger.info("Test de login fallido completado")




