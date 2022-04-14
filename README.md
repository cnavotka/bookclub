# BookClub

This Project is the Milestone 3 of the Code Institute Diploma in Software Development.
Aims to provide a place where members of a Bookclub can write a summary of a book and the main insights they got from reading a book. Also, the user will be able to create any list of books they want and share with other users if desired. In case they like any book of another member, a link is supplied to purchase it.

Here you can check the live site:
https://bookclub-manager.herokuapp.com/

![Heroku](https://bookclub-manager.herokuapp.com/)

![Responsive Image](https://github.com/cnavotka/bookclub/blob/main/static/images/responsiveimage2.png)



## Table of Contents

### UX
#### User stories

* As a user, I want to easily understand the main purpose of the site and learn more about the Bookclub.
* As a user, I want to easily understand the main purpose of the site and learn more about the organisation.
* As a user, I want to easily log in on my account.
* As a user, I want to write personal summaries and main insights about the books I'm reading or already read.
* As a user, I want to create a list of books and share it with other users.
* As a user, I want to find list of books from other people and get inspired to read other books.
* As a user, I want to easily find a way to buy the books in the lists.
* As a user, I want to update or delete old book summaries and lists of books.

### Strategy

* Provide a platform where the user can create personal summaries about books they read.
* Provide a platform where user can create a list of books and share it with other users if they want.
* Create an enjoyable, and easy to use platform that makes the user uses it frequently.

### Scope

* Fits in with my current skill-set of HTML, CSS, JavaScript, Python, Flask and MongoDB.
* Easy way to sign up into the website with Sign Up Button for new users.
* Easy way to log in into the website.
* Allow the user to create, read, update and delete their personal reviews.
* Allow the user to create, read, update, delete and share their wish lists.

#### Structure

As the website has two main ideas, create personal book summaries and lists of books, I kept the website as simple as possible and easy to use. Instead of creating a lot of functionality and decide to create a few functionalities that the user can do a lot of fo things.

* A part of the home page, every page has the same structure to keep consistency and to make the navigation easy to assimilate.
* The modals in different pages are very similar to each other to keep consistency.

#### Skeleton

* Wireframes
You can find them here:

![Skeleton](https://github.com/cnavotka/bookclub/tree/main/static/documents)

* Navigation bar - Menu with links pointing to each page
1. Home - A short description letting the user knows what the website is about.
2. Sign Up / Log In - Very similar design to keep consistency and be user friendly.
3. Profile - After users sign up, they are redirected to their profile with a flash message welcoming them and advise to create their first book summary. Also, in the profile page, in large screens, random quotes about reading will be displayed.
4. Books - A very similar design of the profile page. Until users create their first list a message will be display encouraging then to do it.
5. View Books / View Lists - Two similar pages where the user can see books and lists with more details. Also, they can edit and delete it.
6. Discover - Allows the users to see the shared list from other users. The same design from Best Books page used to keep familiarity.

* Database diagram

![DBDiagram](https://github.com/cnavotka/bookclub/blob/main/static/images/QuickDBD-bookclubdb.png)


#### Surface
The overall UX is clean and similar in all pages to keep consistency.

* Colours
The base color was chosen from Materalize. Some different teal were also chosen because that was the colour used in the library of my primary school. 

* Typography

I used Oswald and Azeret Mono from Google Fonts.

* Images

### Features
#### Existing features

* Designed with HTML5, CSS3, JavaScript, Python3, Flask, MongoDB and Materalize.
* Responsive navigation bar.
* Button to create summaries that pops up a modal to fill in with the book's information.
* Button to create a list of books.
* Button to share a list of books.
* Section where user can edit and delete summaries and lists.
* Random quotes that inspire reading on the profile page (only on large screens.
* Footer with social media links.

#### Future features

* Like and dislike functionality for the shared books on the Discover page.
* Add a book API to add books more easily.
* Add lost password functionality.
* Create a mailing list.

### Technologies used
#### Languages

* HTML
* CSS
* JavaScript
* Python

#### Integrations

* Google Fonts - Typography
* Font Awesome - Icons
* Materialize - CSS Framework
* JQuery - JavaScript Library
* Flask - Micro web framework written in Python
* MongoDB - NoSQL database program, using JSON like documents

#### Workspace, Version Control and Repository storage

* Gitpod - IDE (Integrated Development Environment) used to write the code
* GitHub - Repository hosting service to host the deployed website and track previous versions of code
* Git - Version control tool to record changes and updates to my files
* Heroku - Container-based cloud platform for deployment and running of apps

### Resources

* W3School - General resource
* Balsamiq - Wireframing design tool
* Gimp - Efficient compression of images for site
* QuickDBD - Draw your database relationship diagrams and flow quickly using simple DSL language
* RandomKeygen - To generate a password for the Secret Key in env.py

#### Code Validation

* Nu HTML Checker - HTML Markup Validation
* W3C - CSS Validation
* JSHINT - JavaScript code warning & error check
* PEP8 - PEP8 validator.


### Testing

You can find the testing in this document:
![Testing](https://github.com/cnavotka/bookclub/blob/main/static/test.md)

### Bugs

* Page doesn't run properly, the folowing message appeared:

![Bug](https://github.com/cnavotka/bookclub/blob/main/static/images/bug-mistake-home-hmtl-1.png)

Fixed the {% enblock %} and save it.

* Page doesn't run properly, the following message appeared:

![Bug2](https://github.com/cnavotka/bookclub/blob/main/static/images/bug-curly-braces-missing.png)

Added the missing curly brace.

* Getting a 404 error in the console when ispect it, due to a lack of favicon:

![Favicon Error](https://github.com/cnavotka/bookclub/blob/main/static/images/console-404.png)

Added favicon to fix it.

### Deployment

#### Project creation

1. To create this project the CI Gitpod Full Template.
2. I was then directed to the create new repository from template page and entered in my desired repository name, then clicked create repository from template button.
3. Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

#### Deployment to Heroku

* This project is deployed and hosted on Heroku

1. Navigate to Heroku and login
2. On the dashboard, click on the 'New' button and select 'Create new app'
3. Enter the app name and select a region
4. Under the 'Settings' tab, click on 'Config Vars' to add Configuration Variables from the env.py file. This includes the IP, Port, Secret key, MongoDB name and URI, as well as mail settings for Flask Mail.
5. In the menu select the 'Deploy' option
6. Under 'Deployment method' select the GitHub option to connect to your GitHub repository. Ensure GitHub username is selected and use the search function to find the relevant repository
7. Select Automatic deploys from the main branch and click 'Deploy Branch'

#### Cloning

* The code can be run locally through clone or download from the repository on GitHub
* You can do this by opening the repository, clicking on the green 'Code' button and selecting either 'clone or download'
* You can do this by opening the repository, clicking on the green 'Code' button and selecting either 'clone or download'
* The Download ZIP option provides a link to download a ZIP file which can be unzipped on your local machine. The files can then be uploaded to your IDE




### Credits
* Media

The backfround picture for the project was taken by myself.
The favicon was designed by Saoirse Mc Dermott ![Link to Society6](https://society6.com/saoirsesushi)

* Code

Code from ![Github](https://github.com/Henriqueperoni/CI-MS3-Books-World) was used for parts the CSS, JavaScript and HTML.

Used the Mini-Project Putting it all together as a guide.

### Acknowledgments

* To my mentor, Gurjot Singh. My family for the inconditional support and the Slack Channel of the Code Institute.


