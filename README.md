# selenium-practice @ automationpractice.com
An automation testing project with Python Selenium Webdriver & Page Object Model

## Prerequisites
- firefox
- geckodriver
- python3
- pip3
- make

## Dependecies
- selenium
- faker
- html-testRunner

Command *make deps* will do it for you, however you can install them manually.

## Default webdriver settings
Default setting of webdriver is headless option - for githubactions.

Under **/tests/base_configuration_test.py** at lines: [#[7 - 16]](https://github.com/rpodsiadly/selenium-practice/blob/2eaf906a13a7c301f6d7799c222410cb13c7be8d/tests/base_configuration_test.py#L7-L16)  and [#[28 - 37]](https://github.com/rpodsiadly/selenium-practice/blob/2eaf906a13a7c301f6d7799c222410cb13c7be8d/tests/base_configuration_test.py#L28-L37) you can set up *visual environment*

## How to run this project
- clone repository
- to install dependencies execute:
  ```bash
  make deps
  ```
  <details><summary>or do it manually:</summary>

    ```bash
    pip3 install selenium
    pip3 install faker
    pip3 install html-testRunner
  ```

  </details>
  
- to run tests, execute:
  ```bash
  make test
  ```
  or type in terminal:
  ```bash
  PYTHONPATH=. python3 tests/test_suite.py
  ```
  

## Test cases 

> Environment: Ubuntu 20.04.4 LTS | Firefox Browser 99.0 (64bit)

> Preconditions: user not logged in, browser running
<details><summary>Main page tests</summary>
  
  - loading main page
  - passing to *WOMEN* subpage
  - passing to *DRESSES* subpage
  - passing to *T-SHIRTS* subpage
  - passing to authentication page
  - adding to cart a product with certian value from *DRESSES* subpage
</details>
<details><summary>Authentication page tests - registration</summary>
  
  - new user registration with email already taken - negative
  - new user registration with incorrect date of birth - negative
  - new user registration with incorrect password - negative
</details>
<details><summary>Authentication page tests - logining</summary>
  
  - logining negative
  - logining positive
</details>
<details><summary>Docs in Polish</summary>

[click](https://drive.google.com/file/d/1_BCPqebHNRKxu0r-sFxfOmt79Oa9JPaa/view?usp=share_link)
</details>

## Tests result preview
[UnitTest Result preview](https://htmlpreview.github.io/?https://github.com/rpodsiadly/selenium-practice/blob/de4b75133a5c9b842cb73e9a1c1664673a5b10d1/reports/unittestresult_2022-05-30_21-24-43.html)
