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

(optional but recommended)

You can use whatever DNS option you like, however I use Cloudflare.![](/uploads/screen-shot-2020-07-30-at-5-40-00-pm.png)

#### Step 3

Configure e-mail to send as

Feel free to reach out by twitter and start a conversation!

<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>