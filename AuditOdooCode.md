# Guía para el uso de Pre-Commit + Pylint Odoo + Flake8 en proyectos de Odoo

Este README proporciona una breve descripción de las herramientas **Pylint**, **Flake8** y **Pre-commit**, junto con sus configuraciones recomendadas para usarlas en proyectos Odoo. Estas herramientas ayudan a mejorar la calidad del código al asegurar que se sigan las mejores prácticas de codificación, evitar errores comunes, y garantizar que el código se ajuste a las guías de estilo específicas de Odoo.

Además, te explicamos cómo aplicar reglas y estilos personalizados de Odoo mediante **Pylint-Odoo** y **odoo-pre-commit-hooks**, que son complementos de las librerías oficiales de Pylint y Pre-commit, pero con reglas y guías específicas para el desarrollo de módulos Odoo.

---

## ¿Por qué usar estas herramientas?

Si eres desarrollador de Odoo, usar estas herramientas tiene varias ventajas:
- **Garantiza la calidad del código**: Detecta errores comunes, problemas de estilo y malas prácticas antes de que se hagan commits en el repositorio.
- **Facilita el trabajo en equipo**: Asegura que todo el equipo siga las mismas convenciones de estilo y mejores prácticas.
- **Cumple con las guías de Odoo**: Los plugins como **Pylint-Odoo** y **odoo-pre-commit-hooks** integran reglas específicas para el ecosistema de Odoo.
- **Auditabilidad**: Mantén el código de tu proyecto auditado, facilitando su mantenimiento y asegurando su escalabilidad.

---

## Pylint-Odoo
**[Pylint-Odoo](https://github.com/OCA/pylint-odoo/tree/main)** es una extensión del analizador estático de código **Pylint** que agrega reglas específicas para el desarrollo en Odoo.

### Función:
- **Detecta errores de sintaxis y semántica** en el código Python de Odoo, como errores de importación o variables no usadas.
- **Verifica las convenciones de Odoo**: Asegura que el código siga las guías de estilo de Odoo, como el uso adecuado de nombres, convenciones de estructuras, y las mejores prácticas del marco de trabajo.
- **Emite recomendaciones** sobre cómo mejorar la legibilidad y la estructura del código para que se alinee con las mejores prácticas de Odoo.

### Configuración:
Para integrar **Pylint-Odoo** en tu proyecto, puedes seguir las instrucciones del repositorio de [Pylint-Odoo](https://github.com/OCA/pylint-odoo/tree/main) y adaptarlo a tus necesidades.

---

## Flake8
**[Flake8](https://github.com/PyCQA/flake8/tree/main)** es una herramienta de análisis estático que comprueba el estilo y la calidad del código Python, basada en los estándares PEP8.

### Función:
- **Verifica el estilo de codificación**: Asegura que el código siga las reglas establecidas en **PEP8**, el cual es el estándar de estilo de código en Python.
- **Detecta errores y advertencias**: Incluye advertencias sobre líneas demasiado largas, el uso inconsistente de comillas, espacios innecesarios, entre otros.

### Configuración:
Para agregar **Flake8** a tu proyecto, consulta la documentación oficial de [Flake8](https://github.com/PyCQA/flake8/tree/main) y configura las reglas personalizadas que desees.

---

## Pre-Commit
**[Pre-commit](https://pre-commit.com/#advanced)** es una herramienta que permite ejecutar hooks automáticamente antes de realizar un commit. Esto asegura que el código pase las pruebas de estilo y calidad antes de ser añadido al repositorio.

### Función:
- **Automatiza la ejecución de Pylint y Flake8**: Antes de hacer un commit, se ejecutan automáticamente estas herramientas para garantizar que el código sigue las guías de estilo y no tiene errores.
- **Prevenir errores comunes**: Asegura que el código cumpla con las reglas preestablecidas antes de ser compartido en el repositorio, lo que facilita la colaboración y evita problemas en el código de producción.

### Configuración:
Para configurar **Pre-commit** en tu proyecto, sigue los pasos en la [documentación oficial de Pre-commit](https://pre-commit.com/#advanced). Debes agregar los hooks de Pylint y Flake8 a tu archivo `.pre-commit-config.yaml`.

En el caso de proyectos Odoo, se recomienda usar los hooks de **[odoo-pre-commit-hooks](https://github.com/OCA/odoo-pre-commit-hooks/tree/main)**, que incluyen configuraciones específicas de Odoo. Estos hooks aseguran que el código siga las mejores prácticas y guías de estilo de Odoo.

### Ejemplo de integración con OCA
Si deseas ver una integración real usando **Pre-commit** en el ecosistema Odoo, puedes consultar un proyecto de OCA, como **OCA/web**. En este caso, ellos ya aplican estas librerías como parte de su flujo de trabajo CI/CD. Puedes copiar su configuración para tu propio proyecto:

- [**.pylintrc**](https://github.com/OCA/web/blob/18.0/.pylintrc)
- [**.pylintrc-mandatory**](https://github.com/OCA/web/blob/18.0/.pylintrc-mandatory)
- [**.pre-commit-config.yaml**](https://github.com/OCA/web/blob/18.0/.pre-commit-config.yaml)

Estos archivos contienen las configuraciones necesarias para que las herramientas trabajen conforme a las mejores prácticas de Odoo.

---

## Integración de las herramientas

Para integrar y configurar estas herramientas en tu proyecto, sigue estos pasos:

1. **Instalar pre-commit**:
   Instala la herramienta **Pre-commit** con pip:
   ```bash
   # creamos primero un entorno python
   python3 -m venv venv
   source venv/bin/activate

   pip install -U pip setuptools wheel pre-commit

2. **Crear los ficheros clave para pre-commit**:
    Es necesario crear los siguientes ficheros en tu repositorio, puedes usar como base cualquier repositorio de OCA por ejemplo OCA/web

    [**.pylintrc**](https://github.com/OCA/web/blob/18.0/.pylintrc)
    
    [**.pylintrc-mandatory**](https://github.com/OCA/web/blob/18.0/.pylintrc-mandatory)
    
    [**.pre-commit-config.yaml**](https://github.com/OCA/web/blob/18.0/.pre-commit-config.yaml) 

3. **Ejecutar analisis pre-commit en un terminal**:
    ```bash
    pre-commit run --all-files --show-diff-on-failure --color=always

4. **Guardar los cambios**:
    Cuando ya hayas lintado y depurado tu repositorio puedes hacer commits y subir los cambios a remoto.

5. **CI/DI pre-commit**:
    Si deseas integrar GitHub Actions en el repositorio para que se ejecute automaticamente pre-commit puedes usar el mismo ejemplo del repositorio oca/web que ya esta listo pasa usar y testeado por toda la comunidad
    [Ejemplo WorkFlow](https://github.com/OCA/web/blob/18.0/.github/workflows/pre-commit.yml).

### Fichero pre-commit listo para integrar: 
```bash
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v2.4.1
    hooks:
      - id: prettier
        # https://github.com/prettier/prettier/issues/12143
        exclude: "}$"
  - repo: https://github.com/OCA/odoo-pre-commit-hooks
    rev: v0.0.33
    hooks:
      - id: oca-checks-odoo-module
        args:
          - --fix
        #  - --disable=xml-dangerous-qweb-replace-low-priority
      - id: oca-checks-po
        args:
          - --disable=po-pretty-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
        # exclude autogenerated files
        exclude: /README\.rst$|\.pot?$
      - id: end-of-file-fixer
        # exclude autogenerated files
        exclude: /README\.rst$|\.pot?$
      - id: debug-statements
      - id: fix-encoding-pragma
        args: ["--remove"]
      - id: check-case-conflict
      - id: check-docstring-first
      - id: check-executables-have-shebangs
      - id: check-merge-conflict
        # exclude files where underlines are not distinguishable from merge conflicts
        exclude: /README\.rst$|^docs/.*\.rst$
      - id: check-symlinks
      - id: check-xml
      - id: mixed-line-ending
        args: ["--fix=lf"]
  - repo: https://github.com/OCA/pylint-odoo
    rev: v9.1.3
    hooks:
      - id: pylint_odoo
        name: pylint-odoo with checks
        args:
          - --rcfile=.pylintrc
          - --exit-zero
        verbose: true
  - repo: https://github.com/PyCQA/flake8
    rev: 7.1.2
    hooks:
      - id: flake8
        name: flake8 checks
        args:
          - --config=.flake8
          - --exit-zero
          - --color=always
          - -v
        verbose: true
```

### Fichero .flake8
```bash
[flake8]
# lineas de logitud maxima 79 en python
max-line-length = 79
max-complexity = 17
exclude =
    .git,
    __pycache__,
    .venv,
    venv
ignore = E203,W503,W504,C901
# ignora import not used error F401 en ficheros init 
per-file-ignores=
    __init__.py:F401
```

## Links usados en este manual

Aquí tienes una lista de repositorios y recursos importantes para integrar herramientas de calidad de código en proyectos Odoo, como **Pylint**, **Flake8**, y **Pre-commit**.

1. **[OCA/web - Odoo Community Association (OCA) Web Module](https://github.com/OCA/web/tree/18.0)**
   - Este repositorio de OCA contiene apps y configuraciones de calidad de código ya integradas, ideales para seguir buenas prácticas en proyectos Odoo. Puedes revisar su configuración de CI/CD y cómo integran herramientas como **Pylint** y **Pre-commit**.

2. **[odoo-pre-commit-hooks - Pre-commit Hooks para Odoo](https://github.com/OCA/odoo-pre-commit-hooks/tree/main)**
   - Este repositorio ofrece hooks de **Pre-commit** específicos para proyectos Odoo. Permite integrar herramientas como **Pylint** y **Flake8**, asegurando que el código cumpla con las guías de estilo de Odoo antes de hacer un commit.

3. **[Pre-commit - Documentación Oficial](https://pre-commit.com/#advanced)**
   - **Pre-commit** es una herramienta que facilita la ejecución automática de hooks de calidad de código antes de cada commit. Esta página ofrece información detallada sobre cómo usarla y configurarla en tus proyectos.

4. **[Pylint-Odoo - Plugin Pylint para Odoo](https://github.com/OCA/pylint-odoo/tree/main)**
   - Este repositorio extiende **Pylint**, un analizador estático de código Python, con reglas específicas para proyectos Odoo. Ayuda a asegurar que el código siga las guías de estilo y mejores prácticas de Odoo.

5. **[Flake8 - Herramienta de Análisis de Código Python](https://github.com/PyCQA/flake8/tree/main)**
   - **Flake8** es una herramienta para verificar el estilo de codificación en proyectos Python, basándose en las reglas **PEP8**. Este repositorio proporciona la versión oficial de **Flake8**.

6. **[OCA Addons Repo Template - Plantilla para Repositorios de Addons OCA](https://github.com/OCA/oca-addons-repo-template/tree/master)**
   - Este repositorio ofrece una plantilla base para crear nuevos módulos Odoo bajo el estándar de OCA. Incluye configuraciones recomendadas y ejemplos de cómo organizar un proyecto Odoo siguiendo las mejores prácticas.
