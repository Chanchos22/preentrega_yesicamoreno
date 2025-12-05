from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:
    # Selectores
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
        
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def obtener_nombre_producto_carrito(self):
        # visibility_of_all_elements_located devuelve una LISTA de elementos web.
        nombres_productos = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEM_NAME))
        
        # Corrección de lógica para acceder al texto del primer elemento ([0])
        return nombres_productos[0].text
    
    # He eliminado la segunda definición incompleta que causaba el error de sintaxis/duplicación.
        