# FashionDays testing with unittest library

In this project I will be testing certain aspects of FashionDays web page using unittest library.

Site tested: https://www.fashiondays.ro/

Project structure:
- package called main;
- file in main package called 'main_page' which contains tests regarding the main site page;
- file in main package called 'authentication_page' which contains tests regarding the authentication page;
- file in main package called 'newsletter_page' which contains tests regarding the subscription to the newsletter;
- file in main package called 'suites', it's role is to run the whole project

Libraries and packages used:
- unittest;
- selenium;
- webdriver_manager;
- pytest;
- time;
- HtmlTestRunner. ***This one might not work to pip install, if that's the case, the search for 'html-testRunner' in python packages then install it***

How to run the project:
- in 'suites' file, press the green arrow on the side of the class to run the whole project;
- righ click on package name, copy path / reference -> Absolute Path, then in your terminal write 'cd <paste the Absolute Path>', press enter, then write  'pytest code_itself.py', enter again;  ****** YOU ALSO NEED TO PIP INSTALL PYTEST FOR THIS ONE ******
- press the green arrow on the side of any method to only run that specific test.
  
  # !! REMINDER !!
  Some tests are run on certain timed campaigns and promotions, so when they expire the test will automatically enter 'except'.
  I provided those tests with the @unittest.skip , if you uncomment said decorators those respective tests will be skipped.

