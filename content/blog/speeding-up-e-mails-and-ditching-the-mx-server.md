+++
author = "Adam Kostarelas"
date = 2020-07-30T04:00:00Z
description = "Making it quicker to receive e-mails"
draft = true
image = ""
keywords = ["godaddy faster email delivery", "email forwarding to gmail", "mx forwarding"]
math = false
slug = "cpanel-to-gmail-email-forwarder"
tags = []
title = "Speeding up e-mails and ditching the MX server"
toc = false

+++
## I've had enough with shared hosting.

![ImprovMX website](/uploads/screen-shot-2020-07-30-at-5-03-26-pm.png "ImprovMX")

For years our domain, Kostarelas.com has been on shared hosting provided by Godaddy.

Previously, I was too young to take control of the administration of the domain, but today was the last straw, thanks to two step verification.

I was setting up a service on a new device that of course asked for a 2 step verification code. Usually with platforms like Gmail, Outlook and fast SMTP servers, you'd get a push notification instantly.

Unfortunately today was not this shared server's day. The e-mail was received at 2:24pm, and set up to forward to my G-mail (redundancy) where it arrived at 2:50pm a whole 26 mins later.

For some of my other projects, i've been using a service called [ImprovMX](improvmx.com "ImprovMX Website") that forwards e-mails to my Gmail.  
They offer a free forwarding service that gives great service delivery rates. They also offer a premium SMTP that bypasses my guide's few steps.

Our use case was that most of the users were already fowarding e-mail to Gmail, and with sign off from them all, we decided to pull the plug on Godaddy and Cpanel.

The benefit of ditching shared hosting handling our emails is that incoming emails delivered through the relay are delivered within 5 seconds, which is tolerable compared to the 26 mins. Outgoing e-mails are also going through TLS through Gmail, which adds a layer of security.

### Guide

Things to know:  
\- Our DNS is managed by Cloudflare, which makes switching MX records super easy and quick.  
\- Users who had Mailboxes on Cpanel won't receive mail there anymore, but at the new address  
\- Privacy may be compromised using Google's services (if that's where you're forwarding emails to)  
\- If you've already got forwarding set up and want to know how to use a faster SMTP with gmail, skip to [Step 3]()

#### Step 1

Set up Redundancies

Before making the switch, first it's time to set up ImprovMX, and configure all the e-mail aliases.

![](/uploads/screen-shot-2020-07-30-at-5-09-32-pm.png)

You'll notice that you aren't receiving e-mails yet, and that's ok.  
Once you've matched e-mail to e-mail it's time to make a switch

#### Step 2

(optional to use Cloudflare but recommended)

You can use whatever DNS option you like, however I use Cloudflare for many conveniences.  
![](/uploads/screen-shot-2020-07-30-at-5-40-00-pm.png)

Create or update the records to match ImprovMX's mail servers of mx1 and mx2 (redundancies so if one doesn't work, the second one still relays mail)

This step is going to change who receives the e-mails so keep that in mind.![](/uploads/screen-shot-2020-07-30-at-5-38-17-pm.png)

You'll then be active to receive e-mails

#### Step 3

Let's now configure e-mail to send as the domain, as you won't have a MX server to send the emails from.

##### Create an app password

Go to your Gmail account and click on Security

![](/uploads/screen-shot-2020-07-30-at-4-42-27-pm.png)

Under signing in to Google, click on App passwords. We're going to create an SMTP password used exclusively with Gmail as our forwarder.

![](/uploads/screen-shot-2020-07-30-at-4-42-49-pm.png)

f

![](/uploads/screen-shot-2020-07-30-at-4-37-43-pm.png)

Name it if you like so you don't forget.

![](/uploads/screen-shot-2020-07-30-at-4-42-16-pm.png)

You need to keep this window open or copy the password somewhere to paste into the next step's SMTP password below.

##### Open Gmail

Go to settings and click See all settings

![](/uploads/screen-shot-2020-07-30-at-4-40-31-pm.png)

##### Add a new alias

![](/uploads/screen-shot-2020-07-30-at-4-40-44-pm.png)

We're going to add the e-mail address here which will allow us to send e-mails as the domain you've now forwarded.

##### Verify details

![](/uploads/screen-shot-2020-07-30-at-4-41-10-pm.png)

Add your forwarded email address <example@domain.com> on the first step

![](/uploads/screen-shot-2020-07-30-at-4-41-26-pm.png)

This step is where you'll need the password from before. Paste the password into the box represented by the pink area, and enter your gmail address into the username, not the email you're going to forward. We're logging into Gmail's SMTP here to send e-mails and your <example@domain.com> wouldn't have a login.

![](/uploads/screen-shot-2020-07-30-at-4-38-53-pm.png)

Seeing as you set up the forwarding first, you'll receive the confirmation with a code from google giving authority to send e-mails on your behalf

##### Enjoy!

![](/uploads/screen-shot-2020-07-30-at-4-42-04-pm.png)

That's it! You'll now receive e-mails from your other domain, benefit from spam protection with g-mail and be able to send and receive e-mails within seconds, all for free.

#### Thanks for reading!

Feel free to reach out by twitter and start a conversation! Tweet me directly [@adamxweb](https://twitter.com/intent/tweet?screen_name=adamxweb&ref_src=twsrc%5Etfw "twitter") if you've got any troubleshooting issues.

<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>