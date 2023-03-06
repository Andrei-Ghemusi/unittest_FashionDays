# FashionDays testing with unittest library

In this project I will be testing certain aspects of FashionDays web page using unittest library.

Site tested: https://www.fashiondays.ro/

Project structure:
- package called main;
- file in main package called 'code_itself' which contains all of the tests;
- in the 'code_itself' file you will find the libraries used, a class called 'FashionDaysTest' and several methods which test certain functionalities of the page.

Libraries and packages used:
- unittest;
- selenium;
- webdriver_manager;
- pytest;
- time.

How to run the project:
- if you want to run the whole project, right click then click 'Run';
- press 'Ctrl' + 'Shift" + 'F10" to also run the whole project;
- righ click on package name, copy path / reference -> Absolute Path, then in your terminal write 'cd <paste the Absolute Path>', press enter, then write  'pytest code_itself.py', enter again;  ****** YOU ALSO NEED TO PIP INSTALL PYTEST FOR THIS ONE ******
- press the green arrow on the side of any method to only run that specific test.

