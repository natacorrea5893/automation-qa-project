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
  E ingreso correctamente
```

```gherkin
Feature: Iniciar sesión en la Tienda
  Como usuario
  Quiero acceder a la Página Principal
  E ingreso correctamente
```


### Detalles

**Autor**:
_Natanael Correa_

**Contacto**:
_nata_444@live.com.ar_
