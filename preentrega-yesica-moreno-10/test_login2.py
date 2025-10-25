import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

@pytest.fixture
def driver():
    # 1. Configuración del driver (correcta)
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile': {
            'password_manager_enabled': False
        }
    })
    
    # 2. Inicialización
    driver = webdriver.Chrome(options=options)
    
    # 3. Entrega a la prueba
    yield driver
    
    # 4. Limpieza (Teardown)
    driver.quit()
    
# ----------------------------------------------------------------------

# Función de Prueba (Corregida)
def test_login(driver): 
    
    try:
        # Abre la página
        driver.get("https://www.saucedemo.com/")
        
        time.sleep(2) 

        # Ingresa credenciales
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        # Hace clic en el botón de login
        driver.find_element(By.ID, "login-button").click()
        
        time.sleep(3) 
        
        # Aserción
        assert "/inventory.html" in driver.current_url, "No se redirigio directamente al inventario"
        
        print("✅ Login exitoso y validado correctamente")

    except Exception as e:
        # Captura errores de Selenium o Aserciones
        print(f"❌ Error en test_login: {e}")
        raise 

    # ❌ BLOQUE FINALLY ELIMINADO: La fixture se encarga de driver.quit()
