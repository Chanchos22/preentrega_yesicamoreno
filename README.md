Pre-Entrega de Proyecto: Automatización en SauceDemo
🎯 Propósito del Proyecto

Este proyecto tiene como objetivo automatizar el flujo crítico de un usuario en el sitio web de demostración de e-commerce SauceDemo.

La automatización verifica los siguientes casos de prueba obligatorios:

Login Exitoso: Navegación, ingreso de credenciales válidas y validación de la redirección al inventario.

Verificación del Catálogo: Validación de la presencia de productos y listado de sus detalles (nombre y precio).

Interacción con Carrito: Adición de un producto al carrito y verificación de su aparición en la vista final del carrito.

💻 Tecnologías Utilizadas
Tecnología	Descripción
Python	Lenguaje de programación principal.
Pytest	Framework para la estructura, gestión y ejecución de pruebas.
Selenium WebDriver	Herramienta para la automatización de la interfaz del navegador.
webdriver-manager	Gestiona y descarga automáticamente el driver de Chrome.
Git & GitHub	Control de versiones y alojamiento del repositorio.

1- 🛠️ Instalación de Dependencias

Para ejecutar las pruebas, se recomienda instalar las librerías necesarias mediante pip:
py -m pip install pytest

2- Instalar Selenium, WebDriver Manager y Pytest-HTML:
py -m pip install selenium webdriver-manager pytest-html

🚀 Cómo Ejecutar las Pruebas

3- Ejecutar la suite completa de pruebas y generar el reporte final desde la carpeta principal del proyecto (Entrega-automation-proyecto):
pytest --html=reports/reporte.html --self-contained-html -v

4- Detalles del comando:

-v : Muestra el nombre de cada prueba mientras se ejecuta (Verbose).

--html=... : Genera un reporte HTML y especifica la ruta donde guardarlo.

Pytest buscará automáticamente todos los archivos de prueba que comiencen con test_ dentro de la carpeta tests/.

Archivo de prueba específico :
Si se desea ejecutar un archivo en particular:
pytest -v --html=reports/reporte.html tests/test_saucedemo.py

5- 📄 Generación de Reporte en HTML

El reporte con los resultados detallados de la ejecución se generará automáticamente al finalizar las pruebas y estará disponible en:
reports/reporte.html

