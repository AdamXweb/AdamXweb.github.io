---
title: 'Awesome Aussie, an awesome list automated with Airtable'
date: 2022-09-15T17:48:23.000+10:00
slug: awesome-aussie
description: Automating a build of an Awesome List on Github. Using Airtable to manage the data to build a README.md and update a website.
image: "/uploads/awesomeaussie.png"
keywords:
- awesome aussie
- aussie apps
- github automation
- airtable
- awesome list
- airtasker diy
- blog
author: Adam Kostarelas
tags:
- tech
math: false
toc: false

---

![Awesome Aussie](/uploads/awesomeaussie.png "Awesome Aussie")


Awesome lists are handy. They allow a community or individual to manage a simple list in a Readme in a Git repository. That means all the benefits of revision history, merging changes from different versions and other advantages of git are included.

Where I feel they can often come short is when the lists get a bit too long. Typically data is to the point and a list usually to provides a URL and a brief description of that resource.

In the case of Awesome Aussie, I felt that aussie businesses could have so much more information that could be captured, and that it could be shared and managed in a more efficient way.

My last project, HuTasker was a great learning exercise to play with Airtable's API, and to automate workflows.

## Awesome Aussie
Awesome Aussie provides great a great resource for users looking for aussie apps, software, tools or popular services.
Check out the list on [Github](https://github.com/AdamXweb/awesome-aussie) or at [awesome-aussie.com](https://awesome-aussie.com)

The data is as open as possible, with the ability to download a CSV from AirTable or sync it to your own base. If someone syncs the data to their own base, they can use their own API keys with AirTable to support their own site.
Of course, the data is also available from the README.md on Github.

The current implementation consists of a few javascript based scripts to connect to AirTable's API and Github's API to manage data.

Data is managed in a few ways which will need future refinements.
### Additions
A user is free to submit new items to the list either directly via an AirTable form, or as a pull request from their own repo or can submit a new Github issue.
When a user submits an addition through AirTable, AirTable's own automations connect to Github and create a new issue with the data.
If a user creates a pull request, it can be merged, however the details would need to be manually added to AirTable.
When a user creates a new issue, the Github Issues workflow adds the data to a sheet in AirTable.

### Amendment
At this stage, amendments are only via raising an issue or via pull request. Only authorised users will have permissions to change the data in Airtable.


A breakdown of the technical details:

### Readme
`readme/app.js` connects to Airtable's API to build the Readme.

It checks for data filtered by Airtable that are active in the 'Awesome Aussie' view that are relevant to the list.

The script also ensures that only the categories with an entry are added to the list
Extended list

`readme/extended.js` connects to Airtable's API to build the extended list.

It works similarly to the above, and filters data by the 'Extended' view

### Issues

`issues/app.js` connects to Github's API and Airtable's API. It syncs recent Github Issues to Airtable. This allows the Airtable automations to quickly see if a new submission is a duplicate.
Pull Requests


## Github Workflows

    Issues: Runs the issues script on schedule
    Readme: Builds both normal Readme and Extended list and creates a pull request to update main branch.
    Sync Mirror: Syncs commits to Codeberg
    Sync Website: Syncs commits to the gh-pages branch which hosts awesome-aussie.com


There are still some bugs to figure out and workflows to tweak, but it is available all in the [Airtable branch](https://github.com/AdamXweb/awesome-aussie/tree/airtable) in Awesome Aussie.

