🧪 Proyecto de Automatización – SauceDemo

Automatización de pruebas UI y API utilizando Python, Pytest y Selenium, aplicando buenas prácticas como Page Object Model (POM), manejo de datos externos, reportes HTML, logs y captura automática de pantallas.

🎯 Propósito del Proyecto

Este proyecto tiene como objetivo automatizar el flujo crítico de un usuario en el e-commerce de demostración SauceDemo, validando funcionalidades esenciales y asegurando la calidad del sistema.

Incluye pruebas obligatorias como:

🔐 Login exitoso y fallido

🔐 Login usando datos Faker (datos aleatorios)

📦 Validación del catálogo de productos (presencia, nombre, precio)

🛒 Interacción con el carrito (agregar productos + verificación final)

🌐 Pruebas API (Reqres):

GET Users

POST Create User

DELETE User

Validación de códigos HTTP

Validación de estructura JSON

💻 Tecnologías Utilizadas
Tecnología	Descripción
Python 3.x	Lenguaje de programación principal
Pytest	Ejecución y estructura de pruebas
Selenium WebDriver	Automatización UI del navegador
WebDriver Manager	Descarga automática de drivers
Faker	Generación de datos aleatorios
CSV / JSON	Datos externos para pruebas
Requests	Automatización de API
Git & GitHub	Control de versiones
📁 Estructura del Proyecto
preentrega_yesicamoreno/
│── datos/
│   ├── data_login.csv
│   └── productos.json
│── logs/
│   └── suite.log
│── reports/
│   └── screens/  (screenshots de fallas)
│── tests/
│── pages/
│── run_test.py
│── README.md

📝 Reportes y Logs Generados
📄 Reporte HTML

Se genera automáticamente al ejecutar la suite.
📍 Ubicación: reports/reporte.html

Incluye:

Lista de pruebas ejecutadas

Estado (passed / failed)

Duración

Capturas de pantalla (para fallas)

🖼️ Capturas de pantalla

Se guardan al fallar una prueba.
📍 Ubicación: reports/screens/

📜 Logs de ejecución

📍 Ubicación: logs/suite.log
Contiene detalle completo de cada acción ejecutada.

⚙️ Instalación de Dependencias

Ejecutar:

py -m pip install pytest
py -m pip install selenium webdriver-manager pytest-html
py -m pip install faker requests

🚀 Cómo Ejecutar Todas las Pruebas
✔️ Opción 1 — Ejecutar con archivo principal

Desde la carpeta raíz:

python -m run_test.py

✔️ Opción 2 — Ejecutar usando Pytest + generación de reporte
pytest --html=reports/reporte.html --self-contained-html -v

Detalles del comando:

-v → modo verbose (muestra cada test)

--html= → genera reporte HTML

Pytest detecta automáticamente todos los archivos test_ dentro de /tests

✔️ Ejecutar un test específico

Ejemplo:

pytest -v --html=reports/reporte.html tests/test_saucedemo.py

📦 Manejo de Datos Externos

El proyecto utiliza datos para pruebas desde:

CSV → usuarios válidos/ inválidos (data_login.csv)

JSON → productos para validar (productos.json)

Esto permite escalar el proyecto sin modificar el código principal.

🧠 Conclusión

Este proyecto está diseñado con una arquitectura escalable y mantenible, utilizando buenas prácticas de automatización:

✅ Page Object Model
✅ Datos externos
✅ Reportes HTML
✅ Logs
✅ Captura automática de pantallas
✅ Flujo de ejecución simple con run_test.py

Permite agregar nuevos casos de prueba sin alterar la estructura base.
