Proyecto de Talento Tech
Proposito del proyecto

Este proyecto tiene como objetivo automatizar pruebas de UI y API para el sitio SauceDemo, aplicando buenas prácticas como:

Page Object Model (POM)

Manejo de datos externos

Generación de reportes HTML

Logging centralizado

Captura automática de pantallas para pruebas fallidas

Tecnologías utilizadas

Python 3.x

Pytest

Selenium WebDriver

Requests

Logging

Faker

CSV / JSON

Estructura del Proyecto
preentrega-yesica-moreno-10/
│
├── datos/
│   ├── data_login.csv
│   └── productos.json
│
├── logs/
│   └── suite.log
│
├── pages/
│   ├── base_page.py
│   ├── inventory_page.py
│   ├── login_page.py
│   ├── cart_page.py
│   └── api_page.py
│
├── reports/
│   └── screens/   (capturas de pantalla de tests fallidos)
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_api.py
│
├── run_test.py
└── README.md

Reportes y Logs

El proyecto genera tres tipos de resultados durante la ejecución:

📄 1. Reporte HTML

Se genera automáticamente con el nombre:

reporte.html


Ubicación: carpeta raíz del proyecto.

Incluye:

Lista completa de tests ejecutados

Estado de cada prueba

Duración total y por test

Capturas de pantalla de pruebas fallidas

📝 2. Logs de ejecución

Ubicación:

logs/suite.log


Contiene:

Inicio y fin de la suite

Pasos ejecutados

Errores detectados

Información útil para depuración

📸 3. Capturas de pantalla

Se generan solo cuando un test falla.

Ubicación:

reports/screens/

Cómo ejecutar las pruebas
▶️ Ejecutar TODAS las pruebas usando el script principal
python -m run_test.py

▶️ Ejecutar con Pytest directamente
Todas las pruebas:
pytest -v

Un archivo específico:
pytest -v tests/test_login.py

Con reporte HTML:
pytest --html=reporte.html --self-contained-html

¿Cómo interpretar los reportes?

Al finalizar la ejecución:

Se genera reporte.html en la raíz

Se actualiza logs/suite.log

Se guardan capturas de pantalla en reports/screens/

El reporte HTML muestra:

Estado de las pruebas

Tiempo por test

Errores y traceback

Capturas de fallos

Pruebas incluidas
🔐 Login

Login exitoso

Login fallido

Login usando Faker

📦 Inventario

Validación de productos

Agregar productos al carrito

Verificaciones de UI en inventario

🛒 Carrito

Agregar y remover productos

Validaciones de cantidades

Flujo de compra parcial

🌐 API – Reqres.in

GET /users

POST /users

DELETE /users/{id}

Validaciones:

Códigos HTTP

Estructura JSON

Campos obligatorios

Manejo de datos de prueba

Ubicados en la carpeta datos/:

Archivo	Uso
data_login.csv	Usuarios válidos e inválidos para login test
productos.json	Información de productos para validaciones
Conclusión

Este proyecto ofrece una arquitectura ordenada, escalable y profesional, aplicando buenas prácticas de automatización con Python y Pytest.

Incluye:

Flujo de ejecución simple (run_test.py)

Reportes HTML automáticos

Logging centralizado

Screenshots

Page Object Model

Pruebas UI y API

La estructura permite agregar nuevas pruebas y funciones sin modificar el núcleo del proyecto, asegurando mantenibilidad y crecimiento en el tiempo.
