---
title: 'HuTasker, Hugo X Airtable'
date: 2022-08-15T17:48:23.000+10:00
slug: hutasker-hugo-x-airtable
description: Integrating Hugo, a Static Site Generator with Airtable in a sample app, HuTasker. Read my insights on connecting to Airtable's APIs and making the site build on a schedule. Find out how quick and easy you can follow along at home to set up this theme with your data.
image: "/uploads/hutasker.png"
keywords:
- hugo
- hutasker
- airtable
- hugo x airtable
- airtasker diy
- blog
author: Adam Kostarelas
tags:
- tech
math: false
toc: false

---

![HuTasker Preview](/uploads/hutasker-preview.gif "HuTasker Preview")

### HuTasker
HuTasker integrates Hugo, a Static Site Generator (SSG) with Airtable in a sample app. The end product was to create a mock marketplace for tasks, drawing inspiration from my previous startup Trunked and Airtasker. The technical goal was to use Hugo with a 'back end' that can act as a content management system (CMS) through an API that can fill and manage data on its pages. I started the project making the assumption that my 'client' wanted to manage their data in a spreadsheet that can control the front end. This made up 'client' was developing a MVP (this) for their presentation to validate early in the product development cycle.
To ensure that it was clear that this was a mock site and usable as a theme, call to action (CTA) links to Github were placed.
My personal goal was to solve a problem with Hugo, one that I feel limits the adoption of the technology to tech-savvy users, the lack of a 'good' CMS.

### Trying to find the right CMS
I've been obsessed with trying to find the best CMS for Hugo.
The options available have restrictions that can limit the realistic outputs passing as a solution to a customer.
Users want a system that is straightforward, easy to manage content and make changes at any point in time without relying on a technical person.

A traditional CMS like Wordpress is great as an 'all in one solution' for a non tech-savvy user. The server manages content, renders pages, and has a user interface to edit the site.
Unfortunately in my time working with platforms like Wordpress, Joomla and Drupal the amount of servers that aren't managed is worrying. A large chunk of users don't receive security updates on a platform that has more features than what someone would use for a landing page or something simple.
Aside from being great at managing content for blogs, I feel there are many superior options that have better speed, mobile optimisations and SEO out of the box without enabling plugins. YMMV

### Intro Airtable
I wanted to build a new integration with Airtable, to connect their spreadsheet 'database' like interface with that of a fully separate front end. 
Airtable presents a user with a friendly interface - a spreadsheet, or a kanban board, or a calendar (among others).
Being very versatile and familiar to users, Airtable presented itself as an appropriate solution that could also act like a relative database with rows linking to each other.
Designing the structure for the database, along with different 'Views' that can filter, sort, hide and restrict data was a perfect way to create 'server' like functionality without any programming. An example used is the 'open tasks' view which filters tasks

![Screenshot of Airtable schema](/uploads/hutasker-database-schema.png "Airtable Database Schema")

Being able to effectively build a case that a free platform can replace most people's need for a server is encouraging.
Although HuTasker presents itself as an Airtasker clone, it is missing functionality such as user account creation, and purposely omits the ability to post a task to ensure the quality of data of the template. Although it could be argued that the ability should be enabled for a sample data only site. I'd be afraid in terms of what kind of spam could accumulate if left unmoderated, or if a workflow (or Airtable Automation) to delete data on a schedule wasn't set up.

### Typical SSG uses

Typical common uses for Static Generation include:

    Marketing websites
    Blogs
    E-commerce product listings
    Help and documentation sites

Usually the data is pre-rendered.
Static sites often render files with the help of content pages, often in markdown format at build, generating static pages that can be hosted nearly anywhere. Often these solutions are tied into hosting with a provider that acts as a CDN (Content Delivery Network). In our case, that is Netlify. Static sites often benefit from being hosted on a CDN, as being compiled static files, they can be delivered from anywhere for the fastest load time.

As efficient as managing content in an IDE is for a developer, the user experience isn't the same. Any of the CMS solutions listed above are often the preference for a non technical user that wants to manage content. If they were to make a change with a SSG they'd have to understand the content folder structure, editing a markdown file, version control with Git and then building the pages with the SSG tool.
The technical literacy could obstruct most users from managing content in this way.

Moving all that functionality to a front end that most users are familiar with is essential. Managing data in a database is ideal, and Airtable is one of the closest consumer options that is very user friendly.

### Building the integration
![Screenshot of Airtable Task sheet](/uploads/hutasker-airtable-screenshot.png "Airtable screenshot")

Building the integration, I wanted to focus on ensuring everything was available for free.
That means, free hosting, free 'backend' and of course a free template / data integration available as an open source project.

When integrating with Airtable, there were a few considerations that had to be made clear;
1. Where will people using the theme edit data?
2. Is it easy for users to adapt the functionality for their own data?
3. Security considerations in the repo to protect API keys.


#### Making it clear.
A decision had to be made in terms of storing data; Is it in Airtable or in the content folder as a markdown.
Effort was made to try and remove redundancies of hard coded data in the layouts pages, however some pages in the content folders include references to Airtable's views and table names that the layout will pull. 
That being said, the aim for the content is to be stored in Airtable, only restricting the content folders for configuration or legal related info.

#### Adapting the theme to use different data
If a user who has cloned the repo makes changes to the Airtable structure, Hugo will throw an error. It needs to know table names, views and of course the names of the columns.
Understanding the data isn't too difficult. Most of the references to a table e.g. tasks has been categorised into the tasks layouts and partials. Care would need to be taken to adjust the Airtable record field names to suit their use case.
A list of common errors have been compiled in the Wiki to help future users modifying the theme.

#### Security
Security considerations will revolve around how the user manages their API keys to Airtable. As Airtable's API supports CRUD (Create, Read, Update and Delete) it is important to note as a vulnerability to the system.

### Theme Features
![HuTasker screenshot of category paget](/uploads/hutasker-tasks.png "HuTasker screenshot of category page")

#### Tasks
The main part of this theme is presenting the tasks. Tasks are things that need to be completed by 'users', where if this were a real site, users would be able to make offers to [complete the tasks](https://hutasker.netlify.app/tasks/#rechQDh0ppM3rVpQA).
This page is managed with [Javascript](https://github.com/AdamXweb/HuTasker/blob/737cbe013d3f3639903c77f38bb0e72638b5d97c/layouts/partials/task/card-summary.html#L50-L79), showing the pages created and populated by Hugo through the help of CSS classes.

![HuTasker screenshot of category page](/uploads/hutasker-categories.png "HuTasker screenshot of category page")

#### Categories
Categories was included as a way to add some SEO functionality and extra pages into the template. With the help of a command, anything listed in categories can have their own Hugo pages created that then populate current data from Airtable's API (on the CRON schedule).

#### Privacy
Privacy is important, and something I advocate for. To try and include the least amount of tracking scripts or collection of data is important.
As a way to stay open and transparent, I've tried to explain all the services that this sit is built upon.
On this page, there is an embed from the Simple Analytics tracking script to show page views to the public.

#### Github schedule
The [Netlify Build](https://github.com/AdamXweb/HuTasker/blob/737cbe013d3f3639903c77f38bb0e72638b5d97c/.github/workflows/schedule-netlify-build.yml) workflow on Github is set up to hit Netlify's build webhook on a CRON schedule. This is configurable to as often as Netlify will allow you with your build credits.
What's cool is if there is an active amount of data being updated on Airtable, then the frequency in the CRON can be increased.
This had to be implemented due to Airtable's limitations with their automations restricting what is possible on the trigger of 'updating a record'. Ideally when updating a record, it could notify a webhook and remove the need for a Github schedule, however this could push some people out of their build limits with Netlify.

#### Netlify
Netlify is the CDN and builder for our site. It clones any changes off Github, offers previews for pending changes to the theme and also pulls the data from Airtable and places the build on its CDN. [HuTasker](https://hutasker.netlify.app) is hosted on Netlify on a free plan. The [Wiki](https://github.com/AdamXweb/HuTasker/wiki) has information about how to set up API keys and other variables to get the theme up and running.

#### Other
There are a few other nice features, including a dark mode switch, linking tasks to the home page, good SEO and a decent lighthouse score.

### Further reading about CMS
Hugo's current options to manage content include Forestry, or Netlify CMS. It can get complex when inserting images, or any other bit of information that needs to use a shortcode as it is next to impossible for a user to perform when the UI isn't designed for these applications. It really feels like it can limit the use case of Hugo for a non-tech savvy user to something that is well, static.

A solution for keeping the best of both worlds is to manage data with a content platform or a headless CMS.
This allows the front end to be separate from the back end, or the code to be separate from the content.
I find this important, as a solution dedicated and managed that handles user authentication, access, images and other aspects may come with a cost, but will most likely be specialised to managing content in a particular way that has user experience in mind.
There are headless CMS options like Contenful or Strapi that manage content, specifically to bring into solutions like this.

I do hope that Forestry's "V2" [Tina](https://tina.io/?utm_source=adamkostarelasblog&utm_medium=endofpagelink) can provide some additional support for Hugo's Shortcodes.


### Getting setup
In the spirit of keeping data organised, the information to setup the theme and get started are all available on [Github](https://github.com/adamxweb/hutasker/wiki)


### What's next?
HuTasker is one of my last projects with Hugo before moving to new frameworks. My last project will be a blog theme, and I'll be aiming to integrate a CMS with the SEO benefits of Hugo.

Who knows, there may be an adaption of this theme open for public submissions coming soon..