import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
<<<<<<< HEAD:run_tests.py
    "test_login.py",
    "test_inventory.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]
=======
    "tests/test_login.py",
    "tests/test_inventory.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]
>>>>>>> 491e526 (cambios):preentrega-yesica-moreno-10/run_tests.py

pytest.main(pytest_args)



