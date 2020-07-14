+++
author = "Adam Kostarelas"
date = 2020-07-14T09:00:00Z
description = "I'm new to hugo, and wanted to document my journey creating a blog with Hugo."
draft = true
image = ""
keywords = ["coding", "hugo"]
math = false
slug = "creating-a-hugo-blog"
tags = ["Code"]
title = "Experience creating a Hugo Blog with thumbnails"
toc = true

+++
# Overview

**I'm by no means an expert with Hugo.**

This isn't an official guide, but rather a documentation of my successful migration to hugo for our business website [Topre design](https://topre.design)

Having recently converted my [website](https://adam.kostarelas.com) to a Hugo site, I thought about how it could save costs with Topre, and efficiently host the code securely.

> _TLDR;_  
> The operating environment consists of:
>
> DNS, SSL etc. managed by Cloudflare  
> Page hosted on Github Pages, built with Hugo and CMS maintained by Forestry.

### Step 1 (analyse current site's environment)

Topre was hosted in a S3 container on AWS. We had built the pages as standard HTML