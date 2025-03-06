# Guide for Using Pre-Commit + Pylint Odoo + Flake8 in Odoo Projects

This README provides a brief description of the tools **Pylint**, **Flake8**, and **Pre-commit**, along with their recommended configurations for use in Odoo projects. These tools help improve code quality by ensuring that best coding practices are followed, avoiding common errors, and ensuring that the code adheres to Odoo-specific style guidelines.

Additionally, we explain how to apply custom Odoo rules and styles using **Pylint-Odoo** and **odoo-pre-commit-hooks**, which are extensions of the official Pylint and Pre-commit libraries but with rules and guidelines specific to Odoo module development.

---

## Why Use These Tools?

If you are an Odoo developer, using these tools offers several advantages:

- **Ensures Code Quality**: Detects common errors, style issues, and bad practices before code is committed to the repository.
- **Facilitates Teamwork**: Ensures that the entire team follows the same style conventions and best practices.
- **Complies with Odoo Guidelines**: Plugins like **Pylint-Odoo** and **odoo-pre-commit-hooks** integrate rules specific to the Odoo ecosystem.
- **Auditability**: Keeps your project's code audited, making maintenance easier and ensuring scalability.

---

## Pylint-Odoo

**[Pylint-Odoo](https://github.com/OCA/pylint-odoo/tree/main)** is an extension of the **Pylint** static code analyzer that adds rules specific to Odoo development.

### Functionality:

- **Detects syntax and semantic errors** in Odoo Python code, such as import errors or unused variables.
- **Verifies Odoo Conventions**: Ensures that the code follows Odoo style guidelines, such as proper naming conventions, structure conventions, and best practices within the framework.
- **Provides Recommendations**: Offers suggestions on how to improve code readability and structure to align with Odoo best practices.

### Configuration:

To integrate **Pylint-Odoo** into your project, you can follow the instructions in the [Pylint-Odoo repository](https://github.com/OCA/pylint-odoo/tree/main) and adapt it to your needs.

---

## Flake8

**[Flake8](https://github.com/PyCQA/flake8/tree/main)** is a static analysis tool that checks Python code style and quality, based on PEP8 standards.

### Functionality:

- **Verifies Coding Style**: Ensures that the code follows the rules established in **PEP8**, the Python code style standard.
- **Detects Errors and Warnings**: Includes warnings about lines that are too long, inconsistent use of quotes, unnecessary spaces, and more.

### Configuration:

To add **Flake8** to your project, consult the official [Flake8 documentation](https://github.com/PyCQA/flake8/tree/main) and configure the custom rules you desire.

---

## Pre-Commit

**[Pre-commit](https://pre-commit.com/#intro)** is a tool that allows you to automatically run hooks before making a commit. This ensures that the code passes style and quality checks before being added to the repository.

### Functionality:

- **Automates Pylint and Flake8 Execution**: Before committing, these tools are automatically run to ensure that the code follows style guidelines and is error-free.
- **Prevents Common Errors**: Ensures that the code meets predefined rules before being shared in the repository, facilitating collaboration and avoiding issues in production code.

### Configuration:

To configure **Pre-commit** in your project, follow the steps in the [official Pre-commit documentation](https://pre-commit.com/#advanced). You need to add the Pylint and Flake8 hooks to your `.pre-commit-config.yaml` file.

For Odoo projects, it is recommended to use the hooks from **[odoo-pre-commit-hooks](https://github.com/OCA/odoo-pre-commit-hooks/tree/main)**, which include Odoo-specific configurations. These hooks ensure that the code follows Odoo best practices and style guidelines.

### Example Integration with OCA

If you want to see a real-world integration using **Pre-commit** in the Odoo ecosystem, you can check out an OCA project like **OCA/web**. In this case, they already apply these libraries as part of their CI/CD workflow. You can copy their configuration for your own project:

- [**.pylintrc**](https://github.com/OCA/web/blob/18.0/.pylintrc)
- [**.pylintrc-mandatory**](https://github.com/OCA/web/blob/18.0/.pylintrc-mandatory)
- [**.pre-commit-config.yaml**](https://github.com/OCA/web/blob/18.0/.pre-commit-config.yaml)

These files contain the necessary configurations for the tools to work according to Odoo best practices.

---

## Integration of the Tools

To integrate and configure these tools in your project, follow these steps:

1. **Install pre-commit**:
   Install the **Pre-commit** tool with pip:

   ```bash
   # First, create a Python environment
   python3 -m venv venv
   source venv/bin/activate

   pip install -U pip setuptools wheel pre-commit
   ```

2. **Create Key Files for Pre-commit**:
   You need to create the following files within your repository. You can use any OCA repository, such as OCA/web, as a base to copy the files.

   [**.pylintrc**](https://github.com/OCA/web/blob/18.0/.pylintrc)

   [**.pylintrc-mandatory**](https://github.com/OCA/web/blob/18.0/.pylintrc-mandatory)

   [**.pre-commit-config.yaml**](https://github.com/OCA/web/blob/18.0/.pre-commit-config.yaml)

3. **Run Pre-commit Analysis in a Terminal**:

   ```bash
   # Navigate to your repository (very important!)
   pre-commit run --all-files --show-diff-on-failure --color=always
   ```

4. **Save Changes**:
   Once you have linted and debugged your repository, you can commit and push the changes to the remote.

5. **CI/CD Pre-commit**:
   If you want to integrate GitHub Actions into the repository to automatically run pre-commit, you can use the same example from the OCA/web repository, which is ready to use and tested by the community:
   [Example Workflow](https://github.com/OCA/web/blob/18.0/.github/workflows/pre-commit.yml).

### Ready-to-Integrate Pre-commit File:

```yaml
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

### .flake8 File

```ini
[flake8]
# maximum line length of 79 in Python
max-line-length = 79
max-complexity = 17
exclude =
    .git,
    __pycache__,
    .venv,
    venv
ignore = E203,W503,W504,C901
# ignore F401 (import not used) error in __init__.py files
per-file-ignores=
    __init__.py:F401
```

## Links Used in This Guide

Here is a list of repositories and important resources for integrating code quality tools in Odoo projects, such as **Pylint**, **Flake8**, and **Pre-commit**.

1. **[OCA/web - Odoo Community Association (OCA) Web Module](https://github.com/OCA/web/tree/18.0)**

   - This OCA repository contains apps and code quality configurations already integrated, ideal for following best practices in Odoo projects. You can review their CI/CD configuration and how they integrate tools like **Pylint** and **Pre-commit**.

2. **[odoo-pre-commit-hooks - Pre-commit Hooks for Odoo](https://github.com/OCA/odoo-pre-commit-hooks/tree/main)**

   - This repository offers **Pre-commit** hooks specific to Odoo projects. It allows integrating tools like **Pylint** and **Flake8**, ensuring that the code complies with Odoo style guidelines before committing.

3. **[Pre-commit - Official Documentation](https://pre-commit.com/#intro)**

   - **Pre-commit** is a tool that facilitates the automatic execution of code quality hooks before each commit. This page provides detailed information on how to use and configure it in your projects.

4. **[Pylint-Odoo - Pylint Plugin for Odoo](https://github.com/OCA/pylint-odoo/tree/main)**

   - This repository extends **Pylint**, a static code analyzer for Python, with rules specific to Odoo projects. It helps ensure that the code follows Odoo style guidelines and best practices.

5. **[Flake8 - Python Code Analysis Tool](https://github.com/PyCQA/flake8/tree/main)**

   - **Flake8** is a tool for verifying coding style in Python projects, based on **PEP8** rules. This repository provides the official version of **Flake8**.

6. **[OCA Addons Repo Template - Template for OCA Addons Repositories](https://github.com/OCA/oca-addons-repo-template/tree/master)**
   - This repository offers a base template for creating new Odoo modules under the OCA standard. It includes recommended configurations and examples of how to organize an Odoo project following best practices.
