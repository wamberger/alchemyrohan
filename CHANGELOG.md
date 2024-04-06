
# Change Log

## [v0.4.1] - 2024-04-06

- Adding an option to execute it in command-line: *arohan*.
- Changing parameter name from 'db_creds' to 'conn_str' in function 
*assemble_models()*.
- Changing parameter name from 'abs_path_to_models' to 'path' in function 
*assemble_models()*.
- Changing parameter name from 'py_path_to_model' to 'py_path' in function 
*assemble_models()*.
- Removed function *is_model()*.
- Removed function *reload_module()*.
- Removed function *is_module()*.
- Updated typing hints.
- Refactoring the code.
- Updated README.md.
- Bug fixing in sqlite.py - relationship between tables.
- In models, the name of the method '__post_init__' changed to 'validate'.

## [v0.4.0]  - 2024-03-17

Main Update! Not compatible with previous versions.

- Function name changed from *assemble_model()* to *assemble_models()*.
- Updated parameters of the *assemble_models()* function.
- Revised code structure of the *assemble_models()* function.
    - Loop through list
    - path check
- Adjusted naming or added text in *utils.py*, *wizard.py* and *__init__py*.
    - wizard.py: 'from sqlalchemy.orm import declarative_base' from 
    from sqlalchemy.ext.declarative import declarative_base
    - utils.py: text and naming of optional functions
    - __init__.py: text
- Updated README.md file

## [v0.3.2] - 2023

text fixing and adding third party licenses

## [v0.3.1] - 2023

bug fixing

## [v0.3.0] - 2023

added additional functions

## [v0.2.0] - 2023

tested with Oracle database

## [v0.1.0] - 2023

creation of the initial code and tested with SqLite database
