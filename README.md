# [RECIPE BASE](https://boderg-recipe-base-6a6e035e0009.herokuapp.com "Click to view the deployed site")

- Recipe Base is a recipe sharing database where users can add their recipes, view, edit and delete their recipes.
- Recipe Base is for anyone who wants an online space to save their recipes instead of cluttering up their kitchen with lots of books or bits of paper stuffed in folders.
- Recipe Base is for anyone who wishes to share their recipes with others.
- Recipe Base is for anyone who wants to find new and exciting recipes saved by others.
- All recipes on the site can be categorised and searched for by category or by ingredient.
- All recipes can be viewed by anyone, however, you must be logged in as a signed up user to view the full recipe with instructions.
- Signed in users can only edit their own recipes and profiles, so users can be sure their recipes won't be deleted by others.
- Non registered users are restricted to only ingredients for recipes and have no access to full recipes, categories or profiles.

## Mockup Screenshot

Here is a mockup of the Recipe Base site using the Am I Responsive website.

![screenshot](documentation/mockups/mockup.png)

## UX

Here is the process behind the design of the Recipe Base site.

- The design for Recipe Base started as a series of wireframes covering mobile, tablet and desktop formats to determine the initial design and layout of the site.
- A flowchart and database ERD were then designed to work out the flow of the site.
- Recipe Base was designed with registered users in mind offering a safe storage of their saved recipes.
- A classy look and feel was given to the site to help it stand out but also be easy on the eye.

### Colour Scheme

The colours chosen for the site where as follows;

- `#e7e9bb and #403b4a` used for main body background, border and button gradients.
- `#f8ebff and #80c3b2` used for cards and panel background gradients.
- `#403b4a` used for main text and icons.
- `#0076662` used for text hover.
- `#e7e9bb` used for icon hover.
- `#ffffff` used for button text,
- `#333333` used for button text shadows.
- `#ff0000` used for delete button text.

[cssgradient.io](https://cssgradient.io/gradient-backgrounds/) was used for colour and gradient choices.

- cssgradient.io was used to style the buttons on the Recipe Base site. The gradient chosen gives a kind of metallic look to the buttons.
- The colours used for the buttons were translated to the borders and gradients on the Recipe Base site.
- The remaining colours were then chosen by eye to fit with the aesthetic of the site as they worked well with the borders and button colours.

Here are screenshots of the button choice that influenced the colour direction of the Recipe Base site.

| Button chosen | Button site |
| :---: | :---: |
| ![screenshot](documentation/ux/colour-scheme/button.png) | ![screenshot](documentation/ux/colour-scheme/css-gradient-buttons.png) |

CSS `:root` variables were used to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    --transparent: #00000000;
    --white: #ffffffff;
    --text-main: #403b4aff;
    --text-hover: #007662ff;
    --sidenav-hover-bg: #00000033;
    --icons: #403b4a;
    --icons-hover: #e7e9bb;
    --input-active: #f8ebff;
    --footer: #00000014;
    --modal-footer: #80c3b277;
    --delete: #ff0000;
    --body-gradient: linear-gradient(to top, #e7e9bb77, #403b4a77 100%);
    --card-reveal: linear-gradient( #f8ebff 10%, #80c3b2 100%);
    --card-panel: linear-gradient( #f8ebff 10%, #80c3b2 100%) padding-box,
                linear-gradient(135deg, #e7e9bb 10%, #403b4a 100%) border-box;
    --border-gradient: linear-gradient(var(--white), var(--white)) padding-box,
                linear-gradient(135deg, #e7e9bb 10%, #403b4a 100%) border-box;
    --button-gradient: linear-gradient(135deg, #403b4a 0%, #e7e9bb  51%, #403b4a  100%);
}
```

### Typography

Fontjoy was used for font pairing and selection for the Recipe Base site.

| Light background | Dark background |
| :---: | :---: |
| ![screenshot](documentation/ux/typeography/fontjoy-pairing-light.png) | ![screenshot](documentation/ux/typeography/fontjoy-pairing-dark.png) |

Here are screenshots of the font selection:

Three fonts were decided upon and implemented as follows:

- [Cairo](https://fonts.google.com/specimen/Cairo) was used for the primary headers, navigation and buttons.

- [Cormorant Infant](https://fonts.google.com/specimen/Cormorant-Infant) was used for all titles.

- [Karma](https://fonts.google.com/specimen/Karma) was used for all paragraphs and standard text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer, button icons and form icons.

## User Stories

Here are some of the user stories for the Recipe Base site.

### New Site Users

- As a new site user, I would like to view recipes, so that I can get some inspiration for different meals.
- As a new site user, I would like to have an option to sign up easily, so that I can actively join a community.
- As a new site user, I would like to be able to search for different ingredients , so that I can change up my mealtime variety.
- As a new site user, I would like to be able to search for recipes with similar ingredients, so that I can see variations of of a meal.
- As a new site user, I would like to see what the site is about, so that I can so that I can make an informed choice as to whether I should sign up or not.

### Returning Site Users

- As a returning site user, I would like to be able to log in, so that I can access features available to signed up users.
- As a returning site user, I would like to have a place to save my own recipes, so that I can retrieve them when I need to.
- As a returning site user, I would like to have a place to save my recipes, so that I can share my creations with others.
- As a returning site user, I would like to be able to view recipes by food type, so that I can find variations for a particular food type.
- As a returning site user, I would like to be able to edit a recipe, so that I can adjust any changes I have made to my recipe.

### Site Admin

- As a site administrator, I should be able to access the site, so that I can make changes to food categories.
- As a site administrator, I should be able to access, so that I can create new food categories.
- As a site administrator, I should be able to access the site, so that I can categorise recipes that have not been categorised by the owner, making them more easily accessible in searches.
- As a site administrator, I should be able to access the site, so that I can delete fake entries (if created).
- As a site administrator, I should be able to access the site, so that I can remove fake or malicious accounts.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design the Recipe Base site wireframes.

<details>
<summary>Click here to view the wireframes for the Recipe Base site.</summary>

### Home Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/home.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/home.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/home.png) |

### Registration Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/register.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/register.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/register.png) |

### Log In Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/log-in.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/log-in.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/log-in.png) |

### Recipes Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/recipes.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/recipes.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/recipes.png) |

### Recipe Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/recipe.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/recipe.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/recipe.png) |

### Categories Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/categories.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/categories.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/categories.png) |

### Category Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/category.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/category.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/category.png) |

### Profile Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/profile.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/profile.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/profile.png) |

### Add Recipe Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/add-recipe.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/add-recipe.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/add-recipe.png) |

### Add Category Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/add-category.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/add-category.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/add-category.png) |

### Edit Recipe Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/edit-recipe.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/edit-recipe.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/edit-recipe.png) |

### Edit Category Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/edit-category.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/edit-category.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/edit-category.png) |

### Edit Profile Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/edit-profile.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/edit-profile.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/edit-profile.png) |

### Flash Messages Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/flash-banner.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/flash-baner.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/flash-banner.png) |

### Delete Modal (Page Bottom) Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/delete-modal.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/delete-modal.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/delete-modal.png) |

### Side Navigation Wireframes

| Mobile | Tablet |
| :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/side-navigation.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/side-navigation.png) |

### Error 404 Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/404.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/404.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/404.png) |

### Error 500 Page Wireframes

| Mobile | Tablet | Desktop |
| :---: | :---: | :---: |
| ![screenshot](documentation/wireframes/recipe-base-mobile/500.png) | ![screenshot](documentation/wireframes/recipe-base-tablet%20/500.png) | ![screenshot](documentation/wireframes/recipe-base-desktop/500.png) |

</details>

## Features

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you should go over the different parts of your project,
and describe each in a sentence or so.

You will need to explain what value each of the features provides for the user,
focusing on who this website is for, what it is that they want to achieve,
and how your project is the best way to help them achieve these things.

For some/all of your features, you may choose to reference the specific project files that implement them.

IMPORTANT: Remember to always include a screenshot of each individual feature!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Existing Features

- **Title for feature #1**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature01.png)

- **Title for feature #2**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature02.png)

- **Title for feature #3**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature03.png)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Repeat as necessary for as many features as your site contains.

Hint: the more, the merrier!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Future Features

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Do you have additional ideas that you'd like to include on your project in the future?
Fantastic! List them here!
It's always great to have plans for future improvements!
Consider adding any helpful links or notes to help remind you in the future, if you revisit the project in a couple years.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- Title for future feature #1
    - Any additional notes about this feature.
- Title for future feature #2
    - Any additional notes about this feature.
- Title for future feature #3
    - Any additional notes about this feature.

## Tools & Technologies Used

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you should explain the various tools and technologies used to develop the project.
Make sure to put a link (where applicable) to the source, and explain what each was used for.
Some examples have been provided, but this is just a sample only, your project might've used others.
Feel free to delete any unused items below as necessary.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for an enhanced responsive layout.
- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Codeanywhere](https://codeanywhere.com) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Materialize](https://materializecss.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Flask](https://flask.palletsprojects.com) used as the Python framework for the site.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [MongoDB](https://www.mongodb.com) used as the non-relational database management with Flask.
- [SQLAlchemy](https://www.sqlalchemy.org) used as the relational database management with Flask.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.

## Database Design

My project uses a non-relational database with MongoDB, and therefore the database architecture
doesn't have actual relationships like a relational database would.

My database is called **task_manager**.

It contains 3 collections:

- **categories**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | category_name | String | |

- **tasks**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | category_name | String | selected from *categories* collection |
    | task_name | String | |
    | task_description | String | |
    | is_urgent | String | |
    | due_date | String | |
    | created_by | String | selected from the *users* collection |

- **users**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | username | String | |
    | password | String | uses Secure Hash Algorithm (SHA) |

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**IMPORTANT:**

- Be sure to remove all instances of ElephantSQL/PostgreSQL/Flask-Migrate if you've only used a non-relational database with MongoDB
- Be sure to remove all instances of MongoDB if you've only used a relational database with ElephantSQL/PostgreSQL
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

The live deployed application can be found deployed on [Heroku](https://boderg-recipe-base-6a6e035e0009.herokuapp.com).

### ElephantSQL Relational Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: PLACEHOLDER-NAME).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### MongoDB Non-Relational Database

This project uses [MongoDB](https://www.mongodb.com) for the Non-Relational Database.

To obtain your own MongoDB Database URI, sign-up on their site, then follow these steps:

- The name of the database on MongoDB should be called **insert-your-database-name-here**.
- The collection(s) needed for this database should be **insert-your-collection-names-here**.
- Click on the **Cluster** name created for the project.
- Click on the **Connect** button.
- Click **Connect Your Application**.
- Copy the connection string, and replace `password` with your own password (also remove the angle-brackets).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `IP` | 0.0.0.0 |
| `MONGO_DBNAME` | user's own value |
| `MONGO_URI` | user's own value |
| `PORT` | 5000 |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: python app.py > Procfile`
- *replace **app.py** with the name of your primary Flask app name; the one at the root-level*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If you are using SQLAlchemy for your project, you need to create a local PostgreSQL database.
In this example, the example database name is **db-name**.

```shell
workspace (branch) $ set_pg
workspace (branch) $ psql

... connection to postgres ...

postgres=# CREATE DATABASE db-name;
CREATE DATABASE
postgres=# \c db-name;
You are now connected to database "db-name" as user "foobar".
db-name=# \q
```

Once that database is created, you must migrate the database changes from your models.py file.
This example uses **app-name** for the name of the primary Flask application.

```shell
workspace (branch) $ python3

... connection to Python CLI ...

>>> from app-name import db
>>> db.create_all()
>>> exit()
```

To confirm that the database table(s) have been created, you can use the following:

```shell
workspace (branch) $ psql -d db-name

... connection to postgres ...

postgres=# \dt

	List of relations
Schema | Name | Type | Owner
-------+------+------+--------
public | blah1 | table | foobar
public | blah2 | table | foobar
public | blah3 | table | foobar

db-name=# \q
```

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps, plus a few extras.

Sample `env.py` file:

```python
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("MONGO_DBNAME", "user's own value")
os.environ.setdefault("MONGO_URI", "user's own value")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DB_URL", "user's own value")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

If using Flask-Migrate, make sure to include the following steps as well.

During the course of development, it became necessary to update the PostgreSQL data models.
In order to do this, [Flask-Migrate](https://flask-migrate.readthedocs.io) was used.

- `pip3 install Flask-Migrate`
- Import the newly installed package on your main `__init__.py` file:
	- `from flask_migrate import Migrate`
- Define **Migrate** in the same file after **app** and **db** are defined:
	- `migrate = Migrate(app, db)`
- Initiate the migration changes in the terminal:

```shell
workspace (branch) $ flask db init

	... generating migrations ...

workspace (branch) $ set_pg
workspace (branch) $ flask db migrate -m "Add a commit message for this migration"

	... migrating changes ...

workspace (branch) $ flask db upgrade

	... updating database ...
```

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/boderg/recipe-base) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/boderg/recipe-base.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/boderg/recipe-base)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/boderg/recipe-base)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Credits

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section you need to reference where you got your content, media, and extra help from.
It is common practice to use code from other repositories and tutorials,
however, it is important to be very specific about these sources to avoid plagiarism.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Content

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to provide attribution links to any borrowed code snippets, elements, or resources.
A few examples have been provided below to give you some ideas.

Ideally, you should provide an actual link to every resource used, not just a generic link to the main site!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to provide attribution to any supports that helped, encouraged, or supported you throughout the development stages of this project.
A few examples have been provided below to give you some ideas.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner (John/Jane), for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.
