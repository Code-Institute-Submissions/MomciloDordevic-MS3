<h1 align="center">Testing</h1>

---

## Index 

- <a href="#validators">1. Code validators</a>
- <a href="#responsiveness">2. Responsiveness</a>
- <a href="#browser-compatibility">3. Browser compability</a>
- <a href="#user-stories">4. Testing user stories </a>
- <a href="#defensive-design">5. Defensive design</a>
- <a href="#bugs">5. Bugs</a>

---

<span id="validators"></span>

## 1. Code validators
 - **[HTML Validator](https://validator.w3.org/):** No errors to show.
    - With testing the HTML code, I had some syntax issues on all pages I build with jinja templating.
    - I tested the HTML code by running my server locally and used view page source. This code I passed through the validator.
    - There is one warning on every page saying: Section lacks heading. Consider using h2-h6 elements to add identifying heading to all sections. I have got this warning because I have put my flash messages between sections.

    ![warning](readme_img/testing/warning-section.png)

- **[CSS Validator](https://jigsaw.w3.org/css-validator/):** No errors found.
![CSS Validator](readme_img/testing/css-validator.png)

- **[JS Hint](https://jshint.com/):** No errors found, two warnings, one undefined variable 
    - 2 warnings consist the notification: 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    - 1 undefined variable: $

- **[Python validator | PEP8](http://pep8online.com/):** No errors found

![python validator](readme_img/testing/python-validator.png)

---
