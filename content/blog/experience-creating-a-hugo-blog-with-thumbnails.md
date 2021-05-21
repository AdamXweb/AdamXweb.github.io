+++
author = "Adam Kostarelas"
date = 2020-07-14T09:00:00Z
description = "I'm new to hugo, and wanted to document my journey creating a blog with Hugo."
draft = true
image = ""
keywords = ["coding", "hugo"]
math = false
slug = "creating-a-hugo-blog"
tags = ["tech"]
title = "Experience creating a Hugo Blog with thumbnails"
toc = true

+++
# Overview

**I'm by no means an expert with Hugo.**

This isn't an official guide, but rather a documentation of my successful migration to Hugo for a business website [Topre design](https://design.topre.com.au)

Having recently converted my [website](https://adam.kostarelas.com) to a Hugo site, I thought about how it could save costs with Topre, and efficiently host the code as a static site, securely.

> _TLDR;_  
> The operating environment consists of:
>
> DNS, SSL etc. managed by Cloudflare  
> Page hosted on Github Pages, built with Hugo (with an automated workflow) maintained by Forestry.

### Step 1 (Analyse current site's environment)

Topre was hosted in a S3 container on AWS. We had built the pages as standard HTML, however we wanted to build in a function to be able to create blog posts, without the effort of a fully blown CMS like Wordpress.

After having some experience with Hugo, I thought it'd be relatively easy to