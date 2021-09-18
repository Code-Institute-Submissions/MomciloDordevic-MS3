<h1 align="center">Pizza Lovers</h1>

![Responsive]()

[View Live Site Here](http://pizza-lovers-moma.herokuapp.com/get_pizzas)

## Table of Contents

> - [UX](#ux)
> - [User Stories](#user-stories)
> - [Design](#design)
> - [Data Schema](#data-schema)
> - [Wireframes](#wireframes)
> - [Features](#features)
> - [Existing Features](#existing-features)
> - [Technologies Used](#technologies-used)
> - [Testing](#testing)
> - [Deployment](#deployment)
> - [Credits](#credits)
> - [Resources](#resources)
> - [Acknowledgements](#acknowledgements)

## UX

### Project Goals

The primary goal of **Pizza Lovers** is to allow the users to create, save, search, and view their favorite pizza recipes in one place using  HTML5, CSS3, JavaScript, Python, Flask, and MongoDB.

### User Goals
The user is looking for a web-based application where they can:
- Use the CRUD conventions to:
    - Create a recipe
    - Read recipe
    - Update(Edit) recipe
    - Delete recipe they created
- Be able to search the database for recipes with keywords that query Recipe Names, Ingredients and Alergens.


## User Stories
**As a first-time visitor, I want to be able to:**
- Easily find recipes stored in the database.
- View full recipes and get valuable information.
- Create an Account.

**As a returning visitor, I want to be able to:**
- Log into my account and have access to all features of the application.
- Add/Create recipes and store them in the database.
- View my and other users recipes.
- Edit my recipe.
- Delete a recipe that I have Added/Created.

**As an Admin user of the site, I want to be able to:**
- Add new categories.
- Edit all recipes.
- Delete all recipes.

### Strategy

- For this project, the targeted audiences would be:
    - Pizza/Food Lovers
    - People who are passionate about cooking
    - People of all ages searching for information
    
- The website enables the user to:
    - Register an account
    - Log In to their account
    - View Recipes
    - Search Recipes, by recipe name, ingredients or alergens
    - Create their own recipes and upload them to the database
    - View the full recipe they have created, or that someone else has created
    - Edit recipes they  have created
    - Delete a recipe created by them
    - Subscribe to a Newsletter (Fictional)

### Scope

- What the user will look for in this web application:
    - Easy navigation
    - Welcoming Design
    - Searching the database for recipes
    - Adding their recipes
    - Managing recipes (Edit or Delete)
    - Viewing the Full Recipe
    - Able to Register and Login

[ back to top ](#table-of-contents)

## Design

### Colors

- Colors used for text and background:
    - #f9a825
    - #bb0000
    - Red
    - #fff
    - rgb(0, 185, 0)
    - #fff9ea

### Typography

- The primary font used is **Fira Sans**, and **Sans Serif** is used as a default backup font.

## Data Schema
[MongoDB](https://www.mongodb.com/) was used for this project and the schema design was created. See below:

![Schema Design]()

[ back to top ](#table-of-contents)

### Users Collection
- Upon regisering, the user will be required to provide the following:
    - Username
    - Password

### Recipes Collection
- When creating a new recipe the user will provide the following:
    - Category Name (Required)
    - Recipe Name (Required)
    - Recipe Image URL (Required)
    - Ingredients (Required)
    - Alergens (Required)
    - Baking Time (Required)
    - Recipe Description (Not Required)