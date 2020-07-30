+++
author = "Adam Kostarelas"
date = 2020-07-30T05:03:00Z
description = "My journey of selling my PC to become a remote cloud gamer"
draft = true
image = ""
keywords = ["parsec gaming with aws", "ec2 gaming in aus", "playing warzone on aws", "aws gaming aus", "amazon aws gaming"]
math = false
slug = "aws-ec2-gaming"
tags = []
title = "Becoming a cloud gamer in Aus"
toc = false

+++
## Why I sold my PC and decided to become a cloud gamer

Over the past few years, i've wound back the amount that I play online. Full disclosure, I grew up as a playstation kid, not really touching nintendo since the 64, with the only attempts at 'cloud' gaming i'd ever attempted is using remote play with my PS4 over mobile data, which was choppy at best.

I was sceptical about trying out gaming over the internet,

<VIDEO>

### Guide

#### Step 1

Create your AWS account, and open a customer support request to have access to a G EC2 instance limit increase (the G instances are the ones with GPUs which makes this all possible)

#### Step 2

Once you're approved, launch this AMI instance

[https://aws.amazon.com/marketplace/pp/B07STLTHM8](https://aws.amazon.com/marketplace/pp/B07STLTHM8 "NVIDIA 2019 Server")

#### Step 3

Download Parsec, and create an account.

To realise low latency gaming remotely, RDP won't do, and with Parsec, it allows the GPU to transcode and send the video at a low latency that's playable.

#### Issues

Unfortunately Valorant by Riot doesn't work due to the limitation of installing on a Virtual Machine.

Every so often the system may lag momentaraly