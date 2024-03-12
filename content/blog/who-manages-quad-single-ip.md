
---
title: 'Quad single IP addresses'
date: 2024-03-01T17:20:23.000+10:00
slug: quad-single-ip-addresses
description: Who manages the rare quad single ip address like 1.1.1.1, and what are they typically used for. I investigated their public use as of early 2024.
image: "/uploads/quadips.png"
keywords:
- Who owns quad single ip addresses
- quad ip address
- quad single ip addresses
- blog
author: Adam Kostarelas
tags:
- tech
math: false
toc: true
---

Quad single IP addresses - think 1.1.1.1, ... 8.8.8.8, 9.9.9.9 
Who owns them, and what are they used for?

Anyone who has tinkered around with DNS settings are familiar with a few like 1.1.1.1, 8.8.8.8 and 9.9.9.9 (Cloudflare, Google and Quad9).
I'll be including links and readouts of whois if you're interested to find out more.

It is interesting to learn about IP addressing, and having recently completed FIT5037 at Monash, understanding [BGP](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) (Border Gateway Protocol) routing with [ASN (Autonomous system numbers)](https://www.iana.org/assignments/as-numbers/as-numbers.xhtmlß) 

Spoiler, if you try to visit any of the below IPs, Cloudflare is the only one that will provide a webpage at [1.1.1.1](https://1.1.1.1)


## 1.1.1.1

####    IP Net: 
    1.1.1.0/24 -> 1.1.1.0 - 1.1.1.255
####  Registered to [APNIC](https://www.apnic.net/)
Run by CloudFlare as a DNS resolver


``` ts
╭────────────────────────╮
│ ASN lookup for 1.1.1.1 │
╰────────────────────────╯

 1.1.1.1 ┌PTR one.one.one.one
         ├ASN 13335 (CLOUDFLARENET, US)
         ├RNK #78  TOP 100 AS
         ├ORG APNIC and Cloudflare DNS Resolver project
         ├NET 1.1.1.0/24 (APNIC-LABS)
         ├ABU helpdesk@apnic.net
         ├ROA ✓ VALID (1 ROA found)
         ├TYP  Anycast IP   Hosting/DC
         ├GEO Hamburg, Hamburg (DE)
         ├POR Open ports: 53, 80, 443, 2083, 2086, 2087, 8080, 8443, 8880
         └REP ✓  KNOWN GOOD as "Cloudflare Public DNS"
```
Ports that are open suggest 53 for DNS, 80 for HTTP, 443 for HTTPS, 2083 for radsec (Authorisation protocol), 

Links:
- [BGP.tools for 1.1.1.1](https://bgp.tools/prefix/1.1.1.0/24)
- [Wikipedia for 1.1.1.1](https://en.wikipedia.org/wiki/1.1.1.1)
- [ipinfo for 1.1.1.1](https://ipinfo.io/1.1.1.1)
- [reachability issues of 1.1.1.1](https://blog.cloudflare.com/fixing-reachability-to-1-1-1-1-globally/)

## 2.2.2.2

####    IP Net: 

    2.2.0.0/16 -> 2.2.0.0 - 2.15.255.255

#### Assigned to: [Orange](https://en.wikipedia.org/wiki/Orange_S.A.).
Assigned to a french telecom, Orange.
Not used for any obvious public facing services.

 

``` ts
╭────────────────────────╮
│ ASN lookup for 2.2.2.2 │
╰────────────────────────╯

 2.2.2.2 ┌PTR -
         ├ASN 3215 (France Telecom - Orange, FR)
         ├RNK #204  TOP 500 AS
         ├ORG AS3215
         ├NET 2.2.0.0/16 (FR-TELECOM-20100712)
         ├ABU gestionip.ft@orange.com
         ├ROA ✓ VALID (1 ROA found)
         ├GEO San Jose, California (US)
         ├POR Open ports: 161
         └REP ✓ NONE
```

The port active on 2.2.2.2 suggests it could be SNMP (Simple Network Management Protocol) which typically is used to communicate logging and management information.

- [BGP.tools for 2.2.2.2](https://bgp.tools/prefix/2.2.0.0/16)
- [ipinfo for 2.2.2.2](https://ipinfo.io/2.2.2.2)

## 3.3.3.3

####    IP Net: 

    3.3.3.0/24 -> 3.3.3.0 - 3.3.3.255

#### Registered by Amazon.

Looks like the IP range is reserved and possibly used by [AWS](https://aws.amazon.com/ec2) for EC2 instances. [AWS is a subsidiary of Amazon.](https://en.wikipedia.org/wiki/Amazon_Web_Services)
RPKI suggests it could be for US East cost AWS.

``` ts
╭────────────────────────╮
│ ASN lookup for 3.3.3.3 │
╰────────────────────────╯

 3.3.3.3 ┌PTR -
         ├ASN 14618 (AMAZON-AES, US)
         ├RNK #7169
         ├ORG Amazon Technologies Inc.
         ├NET 3.3.3.0/24 (AT-88-Z)
         ├ABU abuse@amazonaws.com
         ├ROA ✓ VALID (4 ROAs found)
         ├TYP  Hosting/DC
         ├GEO Ashburn, Virginia (US)
         └REP ✓ NONE
```

- [BGP.tools for 3.3.3.3](https://bgp.tools/prefix/3.3.3.0/24)
- [ipinfo for 3.3.3.3](https://ipinfo.io/3.3.3.3)

## 4.4.4.4

####    IP Net: 

    4.0.0.0/9 -> 4.0.0.0 - 4.127.255.255
Registered to Level 3, which has rebranded to [Lumen](https://www.lumen.com).

[They are a communications provider](https://en.wikipedia.org/wiki/Lumen_Technologies).
This is one of the largest ranges which includes a theoretical 8388606 hosts!

4.4.4.4 doesn't look like it is reserved for any public facing services from Lumen, but may be assigned to one of their clients.

```ts
╭────────────────────────╮
│ ASN lookup for 4.4.4.4 │
╰────────────────────────╯

 4.4.4.4 ┌PTR -
         ├ASN 3356 (LEVEL3, US)
         ├RNK #1  TOP 10 AS
         ├ORG Level 3 Parent, LLC
         ├NET 4.0.0.0/9 (LVLT-ORG-4-8)
         ├ABU abuse@level3.com
         ├ROA ✓ UNKNOWN (no ROAs found)
         ├TYP  Proxy host
         ├GEO Honolulu, Hawaii (US)
         └REP ✓ NONE
```
- [BGP.tools for 4.4.4.4](https://bgp.tools/prefix/4.0.0.0/9)
- [ipinfo for 4.4.4.4](https://ipinfo.io/4.4.4.4)


## 5.5.5.5

####    IP Net: 
    5.4.0.0/14 ->  5.4.0.0 - 5.7.255.255

Allocated to [Telefonica Germany](https://www.telefonica.de), [a German telecommunications provider](https://en.wikipedia.org/wiki/Telef%C3%B3nica_Germany).

Looks like the 5.5.5.5 IP is reserved for private use, with no obvious public services.

``` ts
╭────────────────────────╮
│ ASN lookup for 5.5.5.5 │
╰────────────────────────╯

 5.5.5.5 ┌PTR dynamic-005-005-005-005.5.5.pool.telefonica.de
         ├ASN 6805 (TDDE-ASN1, DE)
         ├RNK #1917
         ├ORG TDDE-ASN1
         ├NET 5.4.0.0/14 (DE-MEDIAWAYS-20120425)
         ├ABU abuse.de@telefonica.com
         ├ROA ✓ VALID (1 ROA found)
         ├GEO Frankfurt am Main, Hesse (DE)
         └REP ✓ NONE
```
- [BGP.tools for 5.5.5.5](https://bgp.tools/prefix/5.4.0.0/14)
- [ipinfo for 5.5.5.5](https://ipinfo.io/5.5.5.5)


## 6.6.6.6

#### IP Net:
    6.0.0.0/8 -> 6.0.0.0 - 6.255.255.255

A Whois Result shows this as part of the US AISC.

There are no obvious public facing services for 6.6.6.6


``` ts
╭────────────────────────╮
│ ASN lookup for 6.6.6.6 │
╰────────────────────────╯
 6.6.6.6 ┌PTR -
         ├ASN N/A (address not announced)
         ├ORG Headquarters, USAISC
         ├NET N/A (CONUS-YPG-NET)
         ├GEO Sierra Vista, Arizona (US)
         └REP ✓ NONE
```

- [BGP.tools for 6.6.6.6](https://bgp.tools/prefix/6.0.0.0/8)
- [ipinfo for 6.6.6.6](https://ipinfo.io/6.6.6.6)

## 7.7.7.7

#### IP Net: 
    7.0.0.0/8 -> 7.0.0.0 - 7.255.255.255

This range is part of the US DoD.

There are no obvious public facing services for 7.7.7.7


``` ts
╭────────────────────────╮
│ ASN lookup for 7.7.7.7 │
╰────────────────────────╯

 7.7.7.7 ┌PTR -
         ├ASN 749 (DNIC-AS-00749, US)
         ├ORG DoD Network Information Center
         ├NET 7.7.7.0/24 (DISANET7)
         ├GEO Whitehall, Ohio (US)
         └REP ✓ NONE
```

- [BGP.tools for 7.7.7.7](https://bgp.tools/prefix/7.0.0.0/8)
- [ipinfo for 7.7.7.7](https://ipinfo.io/7.7.7.7)

## 8.8.8.8

#### IP Net:
     8.8.8.0/24 -> 8.8.8.0 - 8.8.8.255

This range is allocated to Google by ARIN - Canada and USA.
Google runs a public DNS resolver on 8.8.8.8

``` ts
╭────────────────────────╮
│ ASN lookup for 8.8.8.8 │
╰────────────────────────╯

 8.8.8.8 ┌PTR dns.google
         ├ASN 15169 (GOOGLE, US)
         ├RNK #1818
         ├ORG Google LLC
         ├NET 8.8.8.0/24 (GOGL)
         ├ABU network-abuse@google.com
         ├ROA ✓ VALID (1 ROA found)
         ├TYP  Anycast IP   DC  Google LLC
         ├GEO London, Westminster (GB)
         ├POR Open ports: 53, 443
         └REP ✓  KNOWN GOOD as "Google Public DNS"
```

Interestingly the open ports are 53 for DNS and 443 which i'm assuming is for DoH but also resolves dns.google


- [BGP.tools for 8.8.8.8](https://bgp.tools/prefix/8.8.8.0/24)
- [ipinfo for 8.8.8.8](https://ipinfo.io/8.8.8.8)

## 9.9.9.9

#### IP Net:
    9.9.9.0/24 -> 9.9.9.0- 9.9.9.255

Quad 9. Based out of Swizerland, Quad 9 runs a DNS resolver that aims to offer better privacy. 

Administered by ARIN - Canada and USA


``` ts
╭────────────────────────╮
│ ASN lookup for 9.9.9.9 │
╰────────────────────────╯

 9.9.9.9 ┌PTR dns9.quad9.net
         ├ASN 19281 (QUAD9-AS-1, CH)
         ├RNK #33644
         ├ORG Quad9
         ├NET 9.9.9.0/24 (CLEAN-97)
         ├ABU abuse@quad9.net
         ├ROA ✓ VALID (1 ROA found)
         ├TYP  Anycast IP
         ├GEO Tokyo, Tokyo (JP)
         ├POR Open ports: 53, 443
         └REP ✓  KNOWN GOOD as "IBM Quad9 Public DNS"
```
Whilst 9.9.9.9 has port 443 open, it is exclusively used for DNS.
Interestingly, the DNS record for quad9.net resolves to 216.21.3.77 (Feb 2024) which is part of the prefix 216.21.2.0/23 allocated to AS715 - WoodyNet, Inc https://woodynet.net/ 

- [BGP.tools for 9.9.9.9](https://bgp.tools/prefix/9.9.9.0/24)
- [ipinfo for 9.9.9.9](https://ipinfo.io/9.9.9.9)

## Extras


### 0.0.0.0
#### IP Net:
    0.0.0.0/8 -> 0.0.0.0 - 0.255.255.255

0.0.0.0 [is reserved](https://en.wikipedia.org/wiki/Reserved_IP_addresses) as a current or local network.


This along with the 10.0.0.0/8 subnet are addresses allocated for private internet as [outlined in RFC1918](https://datatracker.ietf.org/doc/html/rfc1918).

### 10.10.10.10
#### IP Net:
    10.0.0.0/8 -> 10.0.0.0 - 10.255.255.255

Reserved private network space as outlined above. It is also commonly refered to as a [Bogon address](https://en.wikipedia.org/wiki/Bogon_filtering)


### 20.20.20.20
#### IP Net:
    20.0.0.0/11 -> 20.0.0.0 - 20.31.255.255

Registered to [Microsoft](https://www.microsoft.com/en-au), an [American technology company](https://en.wikipedia.org/wiki/Microsoft)

No obvious public services.

### 30.30.30.30
#### IP Net:
    30.0.0.0/8 -> 30.0.0.0 - 30.255.255.255

Registered to **DoD**

No obvious public services.


### 40.40.40.40
#### IP Net:
    40.40.40.0/24 -> 40.40.40.0 - 40.40.40.255
    
Registered to [Telefonica de Argentina](https://www.telefonica.com.ar/), an [Argentinian communications company](https://es.wikipedia.org/wiki/Telef%C3%B3nica_Argentina)

No obvious public services.


### 50.50.50.50
#### IP Net:
    50.50.0.0/16 -> 50.50.0.1 - 50.50.255.254

Possibly registered to [Frontier communications of America](https://en.wikipedia.org/wiki/Frontier_Communications)

Whois has frontiernet.net which loads frontier.yahoo

No obvious public services.


### 60.60.60.60
#### IP Net:
    60.60.0.0/17 -> 60.60.0.1 - 60.60.127.254

Registered to [JCOM co ltd](https://www.jcom.co.jp/en/corporate/). More infor can be found on their [Japanese Wikipedia page](https://ja.wikipedia.org/wiki/JCOM)

No obvious public services.


### 70.70.70.70
#### IP Net:
    70.68.0.0/14 -> 70.68.0.1 - 70.71.255.254

Registed to [Shaw communicatons](https://shawcable.net), a Canadian telecom company.

No obvious public services.

### 80.80.80.80
#### IP Net:
    80.80.80.0/24 -> 80.80.80.0 - 80.80.80.255

Registered to [Freedom Registry BV](https://it.wikipedia.org/wiki/Freenom)

Which changed its name from opentld.com -> freenom.com

No obvious public services.


### 90.90.90.90
#### IP Net:
    90.90.0.0/16 -> 90.90.0.1 - 90.90.255.254

Registered to [Orange](https://en.wikipedia.org/wiki/Orange_S.A.).


No obvious public services.


### 100.100.100.100
Bogon IP address.

Popular usage includes with [Tailscale](https://tailscale.com/)

### OPTE
A cool project that visualises BGP and networks is called [OPTE](https://www.opte.org/about)
![OPTE visualisation](/uploads/opte.jpg "OPTE Preview")
<img alt="Creative Commons License" style="border-width:0;max-width:80px" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png">

OPTE visualises network topology and connections that exist between them that make up the internet.
Networks are often clusters of IP ranges that connect to each other, and OPTE does a good job visualising this.


This was a fun exercise to learn about IP addresses and to also brush up on subnetting.


Have I missed anything, or are there any corrections? Please leave a comment below.