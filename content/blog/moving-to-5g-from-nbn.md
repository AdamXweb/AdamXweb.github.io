+++
author = "Adam Kostarelas"
date = 2022-05-05T04:08:00Z
description = "My initial experience moving from nbn to 5G"
image = "/uploads/5g-nbn-switch.png"
keywords = ["nbn 5g telstra switch", "nbn issues switch to 5g", "telstra 5g speeds", "nbn speeds vs 5g"]
math = false
slug = "from-nbn-to-5g"
tags = ["tech"]
title = "Moving from NBN to 5G"
toc = false

+++
![](/uploads/5g-nbn-switch.png)

I've been waiting a long time for NBN. Back to the original announcement, I remember the first time the address checker provided a date of installation. Delay after delay the day arrived, I'd have regular access to fast broadband.

Since then, so many innovations have changed the way we use technology on a daily basis.
Having gone through a change in OS I was quickly thrust into the world of linux, homelabs and self hosting.

Tinkering around with selfhosted services, I found myself needing to be able to retrieve data from my 'cloud' on a regular basis. However with a consumer nbn connection was difficult. Granted, my connection is a HFC 250/25 plan (Mbps Download/upload), it prioritises traffic in the wrong direction for my needs.

My intrigue to switch to 5g came from wanting higher upload speeds.\
In Australia it can be tough as a consumer to get decent upload speeds at a reasonable price.\
For example, a nbn plan with 100Mbps download and 20Mbps upload is the standard ['Home fast'](https://www.nbnco.com.au/learn/speed#home-fast) plan. To get 40Mbps upload, most providers would charge an extra $10 often costing around $100 AUD/month.

### An Australian ISP, Superloop's internet plans as at May 2022 for comparison.
![](/uploads/nbn-5g/superloop-nbn.png)
![](/uploads/nbn-5g/superloop-fixedwireless.png)


Ironically how I wish I was eligible for fixed wireless at the promised speeds and prices.

The second part of wanting to switch to 5G was the flexibility of month to month billing and cheaper monthly costs.

My only option in my area was Telstra 5G. They promised
![Quoted speeds](/uploads/nbn-5g/quoted-speed.png)
[Critical information summary of plan](https://www.telstra.com.au/help/critical-information-summaries/personal/home-internet/5g-home-internet/5G-home-internet-plan) 


### Modem arrived.
![](/uploads/nbn-5g/modem.png)

**Time to test.**


### First tests (Peak) connected directly to Telstra 5G / Wifi 5 (AC) network Router with an iPhone
![https://www.speedtest.net/result/i/5101216739](/uploads/nbn-5g/5101216739.png)
Above, Superloop NBN connectoin

![https://www.speedtest.net/result/i/5101218699](/uploads/nbn-5g/5101218699.png)
Above, Telstra 5G

### Second tests (Off Peak) connected with Macbook to Telstra 5G / Wifi 5 (AC) network.


![https://www.speedtest.net/result/i/5102939790](/uploads/nbn-5g/5102939790.png)
Above, Superloop NBN connectoin

![https://www.speedtest.net/result/i/5102939079](/uploads/nbn-5g/5102939079.png)
Above, Telstra 5G (gotta love the 100Mbps + Upload)


So far, so good. I've connected the modem into a second WAN port for load balancing until the my current ISP plan ends.\
Gaming is stable, with not a very big difference compared to a fixed line.

Was a good feeling when streaming pictures from a server at full speed to another network.

Will keep posted in the next article if I reach the 1TB bandwidth limit.

First month of this plan has been free. I am not affiliated with Telstra or Superloop in any way.

#### Article coming soon..
Serving web services behind Carrier-Grade NAT (CGNAT) with a VPN tunnel.


