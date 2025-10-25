Pre-Entrega de Proyecto: Automatización en SauceDemo

🎯 Propósito del Proyecto Este proyecto tiene como objetivo automatizar el flujo crítico de un usuario en el sitio web de demostración de e-commerce SauceDemo.

La automatización verifica los siguientes casos de prueba obligatorios:

Login Exitoso: Navegación, ingreso de credenciales válidas, y validación de la redirección al inventario.

Verificación del Catálogo: Validación de la presencia de productos y listado de sus detalles.

Interacción con Carrito: Adición de un producto al carrito y verificación de su aparición en la vista final del carrito.

💻 Tecnologías Utilizadas Tecnología Descripción Python Lenguaje de programación principal. Pytest Framework para la estructura, gestión y ejecución de las pruebas. Selenium WebDriver Herramienta para la automatización de la interfaz del navegador. webdriver-manager Utilizado para gestionar y descargar automáticamente el driver de Chrome. Git & GitHub Usado para control de versiones y alojamiento del repositorio.

🛠️ Cómo Instalar las Dependencias Para ejecutar las pruebas, debes usar el método de instalación de paquetes de Python (pip) para asegurar que todas las librerías necesarias estén disponibles.

1- Instalar Pytest: py -m pip install pytest

2- Instalar Selenium, WebDriver Manager, y Pytest-HTML: py -m pip install selenium webdriver-manager pytest-html

3- Cómo Ejecutar las Pruebas Para ejecutar la suite completa de pruebas y generar el reporte final, usa el siguiente comando. Este comando le indica a Pytest que debe buscar los tests en la carpeta y archivo especificados.

4- Ejecutar los Tests y Generar Reporte Ejecuta el comando desde la carpeta principal (Entrega-automation-proyecto): py -m pytest -v --html=pre-entrega/reports/reporte.html pre-entrega/tests/test_saucedemo.py

5- Detalles del Comando -v: (Verbose) Muestra el nombre de cada prueba mientras se ejecuta. --html=...: Genera el reporte HTML y especifica la ruta donde guardarlo. pre-entrega/tests/test_saucedemo.py: Ruta del archivo de prueba a ejecutar.

6- Generar Reporte en HTML El reporte con los resultados detallados de la ejecución se generará automáticamente tras correr el comando anterior y estará disponible en la siguiente ubicación: Ubicación del Archivo: pre-entrega/reports/reporte.html py -m pytest -v --html=pre-entrega/reports/reporte.html pre-entrega/tests/test_saucedemo.py
