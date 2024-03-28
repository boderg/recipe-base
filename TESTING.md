# Testing

Return back to the [README.md](README.md) file.

## Code Validation

This is where the code for the Recipe Base site has been tested by using the appropriate validation tools.

Here are the results of those tests:

### HTML

The recommended [HTML W3C Validator](https://validator.w3.org) was used to validate all of the Recipe Base HTML files.

All non registered user pages were validated by URI and registered user pages were validated by direct code input due to the validator not being to sign in to the site to access user only pages. The results are as follows:

<details>
<summary>Click to view the results</summary>

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2F&__cf_chl_tk=jjLBKKIgrm.vlGx.8N.YKWzzkh4l.surR6kFpalgz0o-1711531247-0.0.1.1-1791) | ![screenshot](documentation/validation/html/home-warning.png) ![screenshot](documentation/validation/html/home-no-warning.png) | 'Section lacks header h2-h6' warning. <br> This error is due to the flash banner section being injected only when needed so the checker can't find the flash banner section. <br> Corrected by changing the flash banner section to a div in the base html. |
| Recipes | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fget_recipes) | ![screenshot](documentation/validation/html/recipes-warnings.png) ![screenshot](documentation/validation/html/recipes-no-errors.png)  | 'Element h4 not allowed as child of element span in this context' error. <br> This was because a h4 element had been placed inside a span on the card-reveal section of the recipe cards. <br> Corrected by removing the h4 element.  |
| Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Frecipe%2F65fe70f93e67079aba088705) | ![screenshot](documentation/validation/html/recipe-error.png) ![screenshot](documentation/validation/html/recipe.png) | Element ul not allowed as child of element h5 in this context. <br> Corrected by moving the closing h5 tag to the title and adding h6 tags into the list element. |
| Add Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fadd_recipe) | ![screenshot](documentation/validation/html/add-recipe-errors.png) ![screenshot](documentation/validation/html/add-recipe.png) | 1. 'Attribute dropdown not allowed on element div at this point'. <br> Corrected by removing erroneous attribute. <br> 2. 'Element option without label attribute must not be empty'. <br> Corrected by adding text in the option field. <br> 3. 'The value of the for attribute of the label element must be the ID of a non-hidden form control'. <br> Corrected by adding an id to the select element. |
| Edit Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fedit_recipe%2F65fe70f93e67079aba088705) | ![screenshot](documentation/validation/html/edit-recipe-duplicate-id-error.png) ![screenshot](documentation/validation/html/edit-recipe-label-error.png) ![screenshot](documentation/validation/html/edit-recipe.png) | 1. 'Duplicate ID error'. <br> Corrected by adding a jinja2 loop ```{{ loop.index }}``` to the id of each pre populated list. <br> This added a and new error. <br> 2. The new error 'The value of the for attribute of the label element must be the ID of a non-hidden form control'. <br> Corrected by removing the 'for' attribute in the label and creating a new for label without text but with a jinja2 loop index inside of the jinja2 for loop with the input field. |
| Categories | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fget_categories) | ![screenshot](documentation/validation/html/categories.png) | Pass: No Errors |
| Category | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fsingle_category%2F65fb08febb5a2091ffa80826) | ![screenshot](documentation/validation/html/category-error.png) ![screenshot](documentation/validation/html/category.png) | 'Element h4 not allowed as child of element span in this context' error. <br> This was because a h4 element had been placed inside a span on the card-reveal section of the recipe cards and copied over to the category cards. <br> Corrected by removing the h4 element. |
| Add Category | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fadd_category) | ![screenshot](documentation/validation/html/add-category.png) | Pass: No Errors  |
| Edit Category | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fedit_category%2F65fb090abb5a2091ffa80827) | ![screenshot](documentation/validation/html/edit-category.png) | Pass: No Errors  |
| Profile | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fprofile%2Fadmin) | ![screenshot](documentation/validation/html/profile.png) | Pass: No Errors  |
| Edit Profile | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fedit_profile%2Fadmin) | ![screenshot](documentation/validation/html/edit-profile.png) | Pass: No Errors  |
| Log In | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Flogin) | ![screenshot](documentation/validation/html/login-no-error.png) | Pass: No Errors  |
| Register | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2Fregister) | ![screenshot](documentation/validation/html/register-no-error.png) | Pass: No Errors  |

</details>

### CSS

The recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to validate all of the Recipe Base CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fboderg-recipe-base-6a6e035e0009.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/css/css-validation-from-uri.png) | Errors generated by validator trying to check frameworks. |
| style.css | n/a | ![screenshot](documentation/validation/css/direct-css-validation.png) | Pass: No Errors |

### JavaScript

The recommended [JShint Validator](https://jshint.com) was used to validate all of the Recipe Base JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/validation/js/javascript.png) | Unused variables are being used in the html code as onclick events. |

### Python

The recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) was used to validate all of the Recipe Base Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| app.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/recipe-base/main/app.py) | ![screenshot](documentation/validation/python/python-line-to-long.png) ![screenshot](documentation/validation/python/python.png) | ES01 line too long. <br> W293 blank line contains whitespace.. <br> W292 no new line at end of file. <br> This last one (W293) seems to be a quirk of GitHub. Copying the raw faile from GitHub seems to omit the empty line at the end of the file, however when edit is clicked, the newline is showing in the editor.  |

## Browser Compatibility

The Recipe Base site has been tested using the following browsers:

- [Brave](https://brave.com/download)
- [Chrome](https://www.google.com/chrome)
- [Edge](https://www.microsoft.com/edge)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Safari](https://support.apple.com/downloads/safari)

The results of these tests are as follows and listed by browser:

<details>
<summary>Click to view the results</summary>

### Brave

| Page | Screenshot | Notes |
| :---: | :---: | :---: |
| Home | ![screenshot](documentation/browsers/brave/home.png) | Works as expected |
| Recipes | ![screenshot](documentation/browsers/brave/recipes.png) | Works as expected |
| Recipe | ![screenshot](documentation/browsers/brave/recipe.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/browsers/brave/add-recipe.png) | Works as expected |
| Edit Recipe | ![screenshot](documentation/browsers/brave/edit-recipe.png) | Works as expected |
| Categories | ![screenshot](documentation/browsers/brave/categories.png) | Works as expected |
| Category | ![screenshot](documentation/browsers/brave/category.png) | Works as expected |
| Add Category | ![screenshot](documentation/browsers/brave/add-category.png) | Works as expected |
| Edit Category | ![screenshot](documentation/browsers/brave/edit-category.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/brave/profile.png) | Works as expected |
| Edit Profile | ![screenshot](documentation/browsers/brave/edit-profile.png) | Works as expected |
| Log In | ![screenshot](documentation/browsers/brave/log-in.png) | Works as expected |
| Register | ![screenshot](documentation/browsers/brave/sign-up.png) | Works as expected |

### Chrome

| Page | Screenshot | Notes |
| :---: | :---: | :---: |
| Home | ![screenshot](documentation/browsers/chrome/home.png) | Works as expected |
| Recipes | ![screenshot](documentation/browsers/chrome/recipes.png) | Works as expected |
| Recipe | ![screenshot](documentation/browsers/chrome/recipe.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/browsers/chrome/add-recipe.png) | Works as expected |
| Edit Recipe | ![screenshot](documentation/browsers/chrome/edit-recipe.png) | Works as expected |
| Categories | ![screenshot](documentation/browsers/chrome/categories.png) | Works as expected |
| Category | ![screenshot](documentation/browsers/chrome/category.png) | Works as expected |
| Add Category | ![screenshot](documentation/browsers/chrome/add-category.png) | Works as expected |
| Edit Category | ![screenshot](documentation/browsers/chrome/edit-category.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome/profile.png) | Works as expected |
| Edit Profile | ![screenshot](documentation/browsers/chrome/edit-profile.png) | Works as expected |
| Log In | ![screenshot](documentation/browsers/chrome/login.png) | Works as expected |
| Register | ![screenshot](documentation/browsers/chrome/sign-up.png) | Works as expected |

### Edge

| Page | Screenshot | Notes |
| :---: | :---: | :---: |
| Home | ![screenshot](documentation/browsers/edge/home.png) | Works as expected |
| Recipes | ![screenshot](documentation/browsers/edge/recipes.png) | Works as expected |
| Recipe | ![screenshot](documentation/browsers/edge/recipe.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/browsers/edge/add-recipe.png) | Works as expected |
| Edit Recipe | ![screenshot](documentation/browsers/edge/edit-recipe.png) | Works as expected |
| Categories | ![screenshot](documentation/browsers/edge/categories.png) | Works as expected |
| Category | ![screenshot](documentation/browsers/edge/category.png) | Works as expected |
| Add Category | ![screenshot](documentation/browsers/edge/add-category.png) | Works as expected |
| Edit Category | ![screenshot](documentation/browsers/edge/edit-category.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/edge/profile.png) | Works as expected |
| Edit Profile | ![screenshot](documentation/browsers/edge/edit-profile.png) | Works as expected |
| Log In | ![screenshot](documentation/browsers/edge/login.png) | Works as expected |
| Register | ![screenshot](documentation/browsers/edge/sign-up.png) | Works as expected |

### Firefox Developer Edition

| Page | Screenshot | Notes |
| :---: | :---: | :---: |
| Home | ![screenshot](documentation/browsers/firefox-dev/home.png) | Works as expected |
| Recipes | ![screenshot](documentation/browsers/firefox-dev/recipes.png) | Works as expected |
| Recipe | ![screenshot](documentation/browsers/firefox-dev/recipe.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/browsers/firefox-dev/add-recipe.png) | Works as expected |
| Edit Recipe | ![screenshot](documentation/browsers/firefox-dev/edit-recipe.png) | Works as expected |
| Categories | ![screenshot](documentation/browsers/firefox-dev/categories.png) | Works as expected |
| Category | ![screenshot](documentation/browsers/firefox-dev/category.png) | Works as expected |
| Add Category | ![screenshot](documentation/browsers/firefox-dev/add-category.png) | Works as expected |
| Edit Category | ![screenshot](documentation/browsers/firefox-dev/edit-category.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/firefox-dev/profile.png) | Works as expected |
| Edit Profile | ![screenshot](documentation/browsers/firefox-dev/edit-profile.png) | Works as expected |
| Log In | ![screenshot](documentation/browsers/firefox-dev/login.png) | Works as expected |
| Register | ![screenshot](documentation/browsers/firefox-dev/sign-up.png) | Works as expected |

### Safari

| Page | Screenshot | Notes |
| :---: | :---: | :---: |
| Home | ![screenshot](documentation/browsers/safari/home.png) | Works as expected |
| Recipes | ![screenshot](documentation/browsers/safari/recipes.png) | Works as expected |
| Recipe | ![screenshot](documentation/browsers/safari/recipe.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/browsers/safari/add-recipe.png) | Works as expected |
| Edit Recipe | ![screenshot](documentation/browsers/safari/edit-recipe.png) | Works as expected |
| Categories | ![screenshot](documentation/browsers/safari/categories.png) | Works as expected |
| Category | ![screenshot](documentation/browsers/safari/category.png) | Works as expected |
| Add Category | ![screenshot](documentation/browsers/safari/add-category.png) | Works as expected |
| Edit Category | ![screenshot](documentation/browsers/safari/edit-category.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/safari/profile.png) | Works as expected |
| Edit Profile | ![screenshot](documentation/browsers/safari/edit-profile.png) | Works as expected |
| Log In | ![screenshot](documentation/browsers/safari/login.png) | Works as expected |
| Register | ![screenshot](documentation/browsers/safari/sign-up.png) | Works as expected |

</details>

## Responsiveness

The Recipe Base deployed project has been tested on multiple devices to check for responsiveness issues.

The results are as follows:

<details>
<summary>Click to view the results</summary>

### Mobile (Dev Tools - iPhone 12/13 Pro Max)

| Page | Screenshot | Notes |
| :---: | :---: | :---: |
| Home | ![screenshot](documentation/responsive/mobile-dev-tools/home.png) | Works as expected |
| Recipes | ![screenshot](documentation/responsive/mobile-dev-tools/recipes.png) | Works as expected |
| Recipe | ![screenshot](documentation/responsive/mobile-dev-tools/recipe.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/responsive/mobile-dev-tools/add-recipe.png) | Works as expected |
| Edit Recipe | ![screenshot](documentation/responsive/mobile-dev-tools/edit-recipe.png) | Works as expected |
| Categories | ![screenshot](documentation/responsive/mobile-dev-tools/categories.png) | Works as expected |
| Category | ![screenshot](documentation/responsive/mobile-dev-tools/category.png) | Works as expected |
| Add Category | ![screenshot](documentation/responsive/mobile-dev-tools/add-category.png) | Works as expected |
| Edit Category | ![screenshot](documentation/responsive/mobile-dev-tools/edit-category.png) | Works as expected |
| Profile | ![screenshot](documentation/responsive/mobile-dev-tools/profile.png) | Works as expected |
| Edit Profile | ![screenshot](documentation/responsive/mobile-dev-tools/edit-profile.png) | Works as expected |
| Log In | ![screenshot](documentation/responsive/mobile-dev-tools/login.png) | Works as expected |
| Register | ![screenshot](documentation/responsive/mobile-dev-tools/sign-up.png) | Works as expected |
| Sidenav | ![screenshot](documentation/responsive/mobile-dev-tools/sidenav.png) | Works as expected |

### Tablet (Dev Tools - iPad Air)

| Page | Screenshot | Notes |
| :---: | :---: | :---: |
| Home | ![screenshot](documentation/responsive/tablet-dev-tools/home.png) | Works as expected |
| Recipes | ![screenshot](documentation/responsive/tablet-dev-tools/recipes.png) | Works as expected |
| Recipe | ![screenshot](documentation/responsive/tablet-dev-tools/recipe.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/responsive/tablet-dev-tools/add-recipe.png) | Works as expected |
| Edit Recipe | ![screenshot](documentation/responsive/tablet-dev-tools/edit-recipe.png) | Works as expected |
| Categories | ![screenshot](documentation/responsive/tablet-dev-tools/categories.png) | Works as expected |
| Category | ![screenshot](documentation/responsive/tablet-dev-tools/category.png) | Works as expected |
| Add Category | ![screenshot](documentation/responsive/tablet-dev-tools/add-category.png) | Works as expected |
| Edit Category | ![screenshot](documentation/responsive/tablet-dev-tools/edit-category.png) | Works as expected |
| Profile | ![screenshot](documentation/responsive/tablet-dev-tools/profile.png) | Works as expected |
| Edit Profile | ![screenshot](documentation/responsive/tablet-dev-tools/edit-profile.png) | Works as expected |
| Log In | ![screenshot](documentation/responsive/tablet-dev-tools/login.png) | Works as expected |
| Register | ![screenshot](documentation/responsive/tablet-dev-tools/sign-up.png) | Works as expected |
| Sidenav | ![screenshot](documentation/responsive/tablet-dev-tools/sidenav.png) | Works as expected |

### Desktop 27" 1080p

| Page | Screenshot | Notes |
| :---: | :---: | :---: |
| Home | ![screenshot](documentation/responsive/desktop/home.png) | Works as expected |
| Recipes | ![screenshot](documentation/responsive/desktop/recipes.png) | Works as expected |
| Recipe | ![screenshot](documentation/responsive/desktop/recipes.png) | Works as expected |
| Add Recipe | ![screenshot](documentation/responsive/desktop/add-recipe.png) | Works as expected |
| Edit Recipe | ![screenshot](documentation/responsive/desktop/edit-recipe.png) | Works as expected |
| Categories | ![screenshot](documentation/responsive/desktop/categories.png) | Works as expected |
| Category | ![screenshot](documentation/responsive/desktop/category.png) | Works as expected |
| Add Category | ![screenshot](documentation/responsive/desktop/add-category.png) | Works as expected |
| Edit Category | ![screenshot](documentation/responsive/desktop/edit-category.png) | Works as expected |
| Profile | ![screenshot](documentation/responsive/desktop/profile.png) | Works as expected |
| Edit Profile | ![screenshot](documentation/responsive/desktop/edit-profile.png) | Works as expected |
| Log In | ![screenshot](documentation/responsive/desktop/login.png) | Works as expected |
| Register | ![screenshot](documentation/responsive/desktop/sign-up.png) | Works as expected |


## Lighthouse Audit

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

If you don't have Lighthouse in your Developer Tools,
it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Don't just test the home page (unless it's a single-page application).
Make sure to test the Lighthouse Audit results for all of your pages.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

Sample Lighthouse testing documentation:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse-about-desktop.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## User Story Testing

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality.

In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `enter` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work.

Without the following, Jest won't properly run the tests:

- `npm install -D jest-environment-jsdom`

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```

Remember to adjust the `fs.readFileSync()` to the specific file you'd like you test.
The example above is testing the `index.html` file.

Finally, at the bottom of the script file where your primary scripts are written, include the following at the bottom of the file.
Make sure to include the name of all of your functions that are being tested in the `.test.js` file.

```js
if (typeof module !== "undefined") module.exports = {
    function1, function2, function3, etc.
};
```

Now that these steps have been undertaken, further tests can be written, and be expected to fail initially.
Write JS code that can get the tests to pass as part of the Red-Green refactor process.

Once ready, to run the tests, use this command:

- `npm test`

**NOTE**: To obtain a coverage report, use the following command:

- `npm test --coverage`

Below are the results from the tests that I've written for this application:

| Test Suites | Tests | Screenshot |
| --- | --- | --- |
| 1 passed | 16 passed | ![screenshot](documentation/js-test-coverage.png) |
| x | x | repeat for all remaining tests |

#### Jest Test Issues

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this section to list any known issues you ran into while writing your Jest tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Python (Unit Testing)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Bugs

- I created an event listener to add new input fields in the add recipe page. This listener adds a new  input field under ingredients and instructions when the previous field is populated allowing for ingredients and instructions to be added individually. The event listener has a blur function to remove any created field if it is not populated. This removal only works if you tab to the next input field and on sumbission of the form adds empty list items to the recipe. This also occurs on the edit recipe page as it uses the same function.

![screenshot](documentation/bug01.png)

- To fix this, I _____________________.

- When entering the edit recipe page the first item in a list overlaps the label for that list until that list item is selected for editing.

![screenshot](documentation/bug02.png)

- To fix this, I _____________________.

- Jinja2 `'Undefined Error'` while trying to set a delete button with a confirmation modal on my categories page I was getting this error saying that 'category' was not defined. I tried to fix at first by adding a jinja2 for loop to the modal but this resulted in multiple delete buttons as in image 2.

| Error | Failed solution | Solution |
| :---: | :---: | :---: |
| ![screenshot](documentation/bugs/jinja2-undefined-category.png) | ![screenshot](documentation/bugs/failed-solution.png) | ![screenshot](documentation/bugs/modal-inside-jinja-for-loop.png) |

- To fix this, I moved the modal structure inside of the jinja2 for loop and appended the modal id with the category id.

- Werkzeug `Build error` could not build endpoint single_recipe with values [recipe_id].

| Error description | Error code | Solution |
| :---: | :---: | :---: |
| ![screenshot](documentation/bugs/wekzeug-build-error.png) | ![screenshot](documentation/bugs/werkzeug-build-code.png) | ![screenshot](documentation/bugs/adjusted-code.png) |

- To fix this, I renamed all 'single_recipe' entries to 'recipe' in the app routing along with the name of the recipe.html page.

- Python `E501 line too long` (93 > 79 characters)

![screenshot](documentation/bug04.png)

- To fix this, I _____________________.

## Unfixed Bugs

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

  - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

  - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

  - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

There are no remaining bugs that I am aware of.
