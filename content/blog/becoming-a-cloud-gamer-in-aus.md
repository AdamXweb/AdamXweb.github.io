+++
author = "Adam Kostarelas"
date = 2021-05-19T05:03:00Z
description = "My journey of selling my PC to become a remote cloud gamer"
draft = true
image = "/uploads/"
keywords = ["parsec gaming with aws", "ec2 gaming in aus", "playing warzone on aws", "aws gaming aus", "amazon aws gaming"]
math = false
slug = "aws-ec2-gaming"
tags = ["tech"]
title = "Cloud gamer in Australia"
toc = true

+++
## Why I sold my PC and decided to try cloud gaming

Over the past few years, i haven't played many games online. Full disclosure, I grew up as a playstation kid, playing PS3 with friends growing up. The only attempts I'd previously had at 'cloud' gaming was using remote play with my PS4 over mobile data, which was choppy at best.

I was sceptical about trying out gaming over the internet, but seeing as I would only play one or two games casually, I figured I'd give it a go.


### Guide

The tests below were conducted with 100Mb/s download and 40Mb/s upload with NBN. The ping to AWS' server in Sydney was constantly below 20ms.
#### Step 1

Create your AWS account, and open a customer support request to have access to a G EC2 instance. The request will include a limit increase to access G instances. (the G instances are the ones with GPUs which makes this all possible)

#### Step 2

Once you're approved, launch this AMI instance (AWS server template)

[https://aws.amazon.com/marketplace/pp/B07STLTHM8](https://aws.amazon.com/marketplace/pp/B07STLTHM8 "NVIDIA 2019 Server")

#### Step 3

Download Parsec on your PC, and create an account.

To play games with low latency remotely, Microsoft RDP won't do. With Parsec, it allows the GPU to transcode and send the video at a low latency that's playable.


#### Step 4

Now log into the remote server. The easiest way to do this is to find the password associated with the server, and to download the 'RDP' file.

Once connected, you'll be able to install Parsec here also.
#### Step 5

Connect to your new Parsec server, install your games and play!

It's relatively easy to set everything up, however I do recommend keeping in mind that you'll be charged for every minute the server is online, so remember to shutdown to avoid a big bill.

### Conclusion

Although cloud gaming is possible, playing any competitive shooters like Apex Legends, or Call of Duty Warzone with any form of lag is frustrating. Sometimes whilst plaing remotely with Parsec, some stuttering, freezing or frame drops occur naturally over the connection. I'd recommend trying this if someone doesn't want to buy a console, and already has a library of PC games they want to play on demand.


#### Issues

Unfortunately Valorant by Riot doesn't work due to the limitation of installing on a Virtual Machine.


Feel free to contact me on twitter [@AdamXweb](https://twitter.com/adamxweb) if you need help setting anything up.