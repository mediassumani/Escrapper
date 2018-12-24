# Escrapper
A lightweight, simple, and easy-to-use web scrapper package tool built in Python.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

## Installing

Install this package with pip:

```python
pip install Escrapper

```

## How is it used?

  - import the Escrapper module
    - ```python
      import Escrapper
      ```
  - Create an object of the Escrapper class
    - ```python
      scrapper = Escrapper(past_website_url_here)
      ```

  - Get raw/uncleaned data
    - ```python
      raw_data = scrapper.download_data()
      ```
  - Get cleaned up data
    - ```python
      clean_data = scrapper.clean_up_data()
      ```

  - Write data's content into a textfile
  - ```python
      scrapper.write_in_file("filename.txt")
    ```

## Contributing


## License
This project is open sourced and under the <a href="https://github.com/MediBoss/Escrapper/blob/master/LICENSE">MIT</a> license.
