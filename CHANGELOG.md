
# Change Log

## [v0.4.1] - 2023-04-06

- changing parameter name from 'db_creds' to 'conn_str' in function 
*assemble_models()*.
- Typing hints.
- refactoring the code,
- Updating README.md.

## [v0.4.0]  - 2023-03-17

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
