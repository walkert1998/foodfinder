--ReadMe.txt--

Project: FoodFinder

Group members: Thomas Walker, Cornelius Smith, Asma Lokhandwala,
				William Wambolt

--Implementation status--
Our project currently has no online working implementation, this is
because we encountered issues with columns in our database not being
deployed to heroku properly. It is possible to run this project on
localhost but it would require installing several pieces of software
related to the django framework, as of this moment we feel it would
be irresponsible of us to try and make people jump through hoops if
we don't have the exact steps mapped out (which is due to mostly a
lack of free time before we had to hand in the implementation).

There are a few missing features which we intended to include but
will likely do so between now and the user study. Including reviews
and a page where you can see all restaurants of a certain category.

We also only included a small number of restaurants as a proof-of-concept
and so that we could focus on the look and navigation of the restaurant
pages rather than the volume. To add a dozen more restaurants could be
easily done in an hour with how our models are set up but we figured it was better
to focus on quality over quantity.

--Files overview--

Since our project is a website, by the time it is deployed (which should
only take about a day after the submission for the implementation) the
user won't have to deal with any files and can simply interact with the
website as they would any other.

But here is a brief overview of the files used to create the website:

Currently our projects directory contains the 'env' folder for the python
virtual environment which is necessary to run the website on localhost and
to alter the database tables.

The 'foodapp' folder contains the html, css, javascript and .py files
for running the bulk of the frontend for our website. It contains the
templates for the homepage and the individual restaurant pages. It also
contains what are called 'models' which are basically the objects
(i.e. restaurants, reviews, etc.) and their attributes.

The files in 'static' include the css, js files and images. The files
in 'templates' in any folder contain the HTML files for their subsection
of the site, for example foodapp hold the HTML files for the restaurant
pages and foodfinder holds the HTML files for the base templates upon
which the restaurant pages are built.

'foodfinder' is the main site folder, it contains most of the backend
work which includes handling which apps are installed, what database
is being used, etc.


The views and urls .py files are used to navigate the site, urls.py
matches a specific url to a view, and the view then renders the HTML
template associated with it. This was quite nice because we only needed
to make a handful of templates for what could potentially be
dozens of pages.

The requirements.txt file is there so that when someone downloads the git
repository they can just install the items listed in the file in one
command.

The runtime.txt file is used for deploying to heroku, same with Procfile.
