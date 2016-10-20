# Title

## Team Name: Team Research Papers

## Team Members:
- Charles Tian
- Eric Erickson
- Ryan Shea
- Addison Juarez
- Lior Vansteenkiste

# Introduction



# Design

## Selecting our subjects
When choosing pillars we ended up making several changes along the way. These changes were driven by three main criteria. First, that our pillar be reachable by a direct database query. Second, that our pillar's characteristics be reachable from a direct database query without requiring a prohibitive amount of work. Third, that our pillars contain characteristics capable of connecting them.

When going in (and posting our topics on piazza) we were planning on using "Authors" as a pillar. However, we quickly discovered that individual authors were not directly reachable as a query. Instead, each piece of information describing a paper contained a string that could have one or more authors, deliniated by inconsistent delimiters! What this would mean, is that to build a database of Authors from the source we had chosen, we would have had to get the information for every single paper, and parsed the author string (in an only arguably valid way) millions of times. So many calls is simply prohibitive, and we instead migrated the pillar to "Countries."

However, countries also did a poor job of meeting our new-found criteria. Many, if not most, papers contained multiple authoring countries, in no guarenteed order. Attempting to match an authoring (or most-authoring) country to a paper, as it would appear in our table, is simply unreliable at best. Furthermore, we considered organizing years by highest contributing country as providing inadequate information. Most years saw the same top contributor. (U.S.A! U.S.A!) With countries bringing less than satisfactory information, we finally settled on "Journals". 

Journals contain conveniently accessed and extremely relevant information when grouped with the other two pillars. Journals vary their rate of publication over time and the "publications by year" list, as pulled from the database, comes sorted by popularity. This means that our connection: Journal->Year is both cheap and relevant. Journals also tend to prefer certain subjects over others and, once again, this list of subjects is sorted by popularity. As such our Journal->Subject connection is also both cheap and relevant.

## Selecting our characteristics
When choosing what characteristics to attach to each pillar, we once again had specific criteria. First, our characteristics must be conveniently reachable from our database. This one is not as bad as it seems, as we are building the database, and can structure it according to the characteristics we choose. Second, for each pillar, for other pillar, at least one characteristic of the former must connect to each of the latter. Third, the information cannot be worthless. (irrelevant in any context)

Paper's Characteristics:
 - Title > Relevant, useful, exactly one per paper.
 - Authors > Relevant, useful. Only one string per paper
 - Journal > Relevant, connects to another pillar, only one string per paper.
 - Year > Relevant, connects to another pillar. One field.
 - Abstract > Extremely relevant, single string.

Journal's Characteristics:
 - Name > Relevant, identifier, only one
 - Number of Publications > Relevant, gives an indication of size
 - Most Popular Subject > Relevant, gives an indication of what the Journal is all about
 - Most Popular Year > Connects to another pillar, changes w/ time. gives an indication of when a journal is/was active
 - Most Contributing Country > Relevant, can be retrieved from a sorted list in original database

Year's Characteristics:
 - Year(name) > Identifier.
 - Number of Publications > Relevant, shows overall activity over time
 - Most Popular Subject > Shows trends over time.
 - Most Popular Keyword > Shows less distinct but more specific trends over time
 - Top Journal > Connects to other pillar

## Web Design
For front end design, we first decided on the general theme of our website which we agreed that we wanted to keep simplistic and clean. Browsing through Bootstrap, we looked at a theme called Yeti which looked very aesthetically pleasing to the user. First we decided to make a header file which was separated from all other pages in order to minimize the number of changes that would be required. If a change is needed in the header, instead of changing all the other pages, we could only change the one file which would be placed into all the other files. We decided to have the standard header which contained a home page link in the far left and other options to take your to the pillar pages. The pillars are ordered from papers, journals, year which seems to be the most logical order that a site like this would use to browse these options from a broad range to a narrow range. The splash page was created using the jumbotron aspect from yeti theme of bootstrap, attempting to summarize the purpose of the site in minimum amount of words. It offers the goal of the site and the different tools that the papers can be sorted in; by paper, journal published, or year published. Giving the user an overview of the site as well as how each pillar is organized.

## Models

Our models were created using flask's version of sqlalchemy, with the diagram showing their multiplicity being created from the YUML website. These models would allow developer's to get trends over the years of different journals and see data about specific papers with their data on them.

### UML

Our data model's UML depiction was very simple to create using the YUML website. Once we figured out the correct multiplicity between the 3 pillars, we were able to create the diagram below. The diagram shows that between journals and papers there is a one to many relationship which makes sense because a journal can have as many papers in it as it wants to publish but a paper can only be published within a year. This relationship is basically the same as the one between years and papers because a paper can only be published within one year but as many papers as people are publishing can be published within a year. There is a one to one relationship both ways between years and journals as each of them has a top of the other.

### Apiary

The Apiary for our future restful API mode is currently a very basic example of what we want to implement in the future phases of the project. Our restful API design currently is based on previous years on what they implemented but adapted to our pillars. We at first had problems creating it because we were trying to do it on people's account who were not the administrator of the repo and for apiary to be able to integrate into the Github. So far all we have is simple GET requests to be able to get individual pillars by their unique identifiers. This will just return simple jsons which are a list of all the attributes for that specific pillar that you requested. Once our site is implemented more we may create other requests that people can make which will return other data or make it so you can search within the data on our website through the restful API. The restful API should eventually make it easy for developers to come in and pull the data they want or need so that they are able to make their own projects using the data pulled from our website.

## Unit tests

Our unit tests were created to test against a future database which we have not implemented yet. So it was difficult to come up with worthwile unit tests at first because we weren't sure about how exactly the database would be implemented within future phases of the the project. This led to very basic tests against the models which would be able to be run once we got the database running in future projects. The tests currently just make sure that each model can be created properly, we can pull out attributes, their representations are printing properly, and that they keep their attributes when pulled from the database. These tests are designed so that they will be able to check that our database won't mess up any of our models while storing and querying data.

# Hosting

To set up hosting, we used tools that were recommended in the project description, namely DigitalOcean, Flask, and NameCheap. Additionally, the guide provided by brpowell on Github was also very useful as a guide. The following is an outline of the all of the major tools that we used, and our process in how we used those tools.

## DigitalOcean

We started by setting up a Droplet using DigitalOcean. The process of creating the Droplet was relatively straightforward, although it took over an hour just for DigitalOcean to give us access to our account. The [tutorial](https://github.com/brpowell/flask-example/wiki/Hosting-on-Digital-Ocean) and [sample code](https://github.com/brpowell/flask-example/) provided by [brpowell](https://github.com/brpowell/) on Github proved to be very helpful, and we were able to follow the instructions almost step-by-step.

Because the majority of the steps that we followed for setting up DigitalOcean was described in the aforementioned tutorial, we do not feel the need to re-iterate these instructions step by step. However, there were a couple of issues that we ran into that were not covered by the tutorial. These are outlined below:

### Installing psycopg2

First of all, when trying to install `psycopg2`, which was specified in the `requirements.txt` file provided in brpowell's sample project, we got the following error:
~~~
Error: pg_config executable not found.
~~~

After a Google search on the aforementioned issue, we found a [StackOverflow post](http://stackoverflow.com/questions/11618898/pg-config-executable-not-found) to troubleshoot the problem. It turned out that we had to install a package on our Ubuntu droplet called `libpq-dev`. Thus, we were able to solve the issue by executing
~~~
sudo apt-get install libpq-dev
~~~
before installing the required pip packages using
~~~
pip install -r requirements.txt
~~~

### Using virtualvenv

The tutorial also suggested that we install a package called `virtualvenv` and create a virtual environment from which to deploy our web application. However, there was no mention of this being a requirement in the project decription, and we were unable to figure out how to get the app running with the virtualhost from the virtual environment (we kept getting errors saying that the `pip` packages were not found, as they were only installed in the virtual environment and not on the actual server), so in the end we just ended up installing everything directly on the droplet and ignoring the `virutalvenv` part of the tutorial. From there, we were finally able to successfully connect our Flask application to the website domain name, initially using the sample code that was provided by brpowell. 

Note that this is simply an explanation of how we were able to use DigitalOcean to set up the hosting server, with some sample content. The actual front-end web development is described in the Web Design section.

## Domain integration

### NameCheap

Using [NameCheap](https://www.namecheap.com/), we were able to get a free `.me` domain name to host our site. We decided on the domain name `researchpapers.me`, as it was available and quite fitting for the topic that we are covering. After registering the domain name, we had to connect it with our DigitalOcean droplet by changing the DNS settings from the NameCheap dashboard. Specifically, the A record value was set to the IP address provided by the droplet. 

Furthermore, we had to make some changes in DigitalOcean as well. After adding the domain to our DigitalOcean account through the Networking tab, we had to once again associate it with our droplet by linking the appropriate IP address. At this point, our domain name served as an alias for the IP address; from both URLs we could see the Apache2 Ubuntu default page.  

### Updating the VirtualHost

The final step was to update the VirtualHost so that our Flask web application would display properly when accessed through our NameCheap domain name. Once again, brpowell's tutorial provided us with a base template for the virtual host file, as well as instructions on how to activate it and connect with Flask. The most important changes that we had to make were to set the `ServerName` field in the file to `researchpapers.me`, and creating/linking the appropriate `.wsgi` file. These two steps allowed us to serve our Flask application through the domain name that we registered. 

# Tools

We used the following tools to help us throughout our development process throughout the project:
 - Slack: for messaging and communication
 - NameCheap: getting a free domain name
 - DigitalOcean - hosting the server using a Droplet
 - Flask: a python framework for deploying our web server
 - Apiary - documenting the API that we will be implementing to fetch data from the database
 - Bootstrap - CSS/JavaScript library to beautify and standardize the look of our website
 - Bootstrap [Yeti Theme](https://bootswatch.com/yeti/) - a specific Bootstrap theme that we used
