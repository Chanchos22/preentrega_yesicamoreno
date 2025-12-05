import pytest

test_files = [
<<<<<<< HEAD
    "tests/test_login.py",
    "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_cart2.py",
    "tests/test_cart_json.py",
=======
<<<<<<< HEAD:run_tests.py
    "test_login.py",
    "test_inventory.py"
>>>>>>> a2c65a09c0961e3609ab7da98c0dc36e458a7f9c
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
