# Proyecto Final: Curso de QA Automation con Selenium y Pytest-BDD


## Resumen

Este proyecto tiene el objetivo de realizar pruebas automatizadas sobre una página web, utilizando _Python_, _Selenium_ y _Pytest-BDD_.


## Prerrequisitos

Con el gestor de paquetes [pip](https://pip.pypa.io/en/stable/) asegurarse de correr los siguientes comandos:

```bash
python -m pip install selenium
pip install pytest
pip install pytest-bdd
```

Para generar los reportes utilizaremos el siguiente paquete:
```bash
pip install pytest-html-reporter
```

También estarán listados todos los paquetes instalados en el archivo _**requirements.txt**_ para utilizarse de la siguiente forma:

```bash
pip install -r requirements.txt
```

Instalar la extensión de Chrome [Ranorex Selocity](https://chrome.google.com/webstore/detail/ranorex-selocity/ocgghcnnjekfpbmafindjmijdpopafoe)
que usaremos para crear los locators.

Descargar los WebDrivers
[Gecko Driver](https://github.com/mozilla/geckodriver/releases) y
[Chrome Driver](https://chromedriver.chromium.org/downloads). Pegar los archivos .exe en el directorio
del intérprete (también se recomienda tenerlos en el proyecto, dentro de una carpeta _**Drivers**_ ).


## Pruebas

```gherkin
Feature: Iniciar sesión en la Tienda
  Como usuario
  Quiero acceder a la Página Principal
  Entonces ingreso correctamente
```

```gherkin
Feature: Gestionar la Libreta de Direcciones
  Como usuario
  Quiero gestionar la Libreta de Direcciones
  Entonces edito correctamente la/s dirección/es
```

## Correr Pruebas con Pytest

Para correr TODOS los tests:
```bash
python -m pytest
```

Para correr todos los test dentro de un módulo:
```bash
python -m pytest tests/step_defs/test_service_steps.py
```

El comando para correr los test que posean un tag específico (ej. regression) es:
```bash
python -m pytest -k “regression”
```

Para las tags, se puede emplear cualquier comando:
```bash
python -m pytest -k “regression and Login”
python -m pytest -k “regression or service”
python -m pytest -k “not service”
```

## Generar Reportes

Al correr cualquier test se generará el reporte en la carpeta raíz del proyecto.
En su lugar usaremos el siguiente comando para usar la carpeta **_Reports_**:
```bash
python -m pytest -k test_all_steps --html-report=Reports/report.html
```

## Detalles

**Autor**:
_Natanael Correa_

**Contacto**:
_nata_444@live.com.ar_
