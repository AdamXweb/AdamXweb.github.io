---
title: 'Arc Browser, how private is it?'
date: 2023-07-30T11:20:23.000+10:00
slug: arc-browser-privacy-check
description: Arc Browser is the latest flavour of Chromium that requires an account to use. How much data is shared and why?
image: "/uploads/arc.png"
keywords:
- privacy check
- arc browser
- chromium
- adam kostarelas
- blog
author: Adam Kostarelas
tags:
- tech
math: false
toc: false

---

![Arc Browser](/uploads/arc.png "Arc Browser Privacy")

**This writeup looks into how Arc phones home to log analytics without giving users a good way to opt-out.**


Arc browser is one of the many [Browsers to run Chromium](https://en.wikipedia.org/wiki/List_of_web_browsers#Blink-based) (Blink) which includes browsers like Microsoft Edge, Brave and Opera.

It however is unique, being one of the only browsers that requires you log in before using it.
### Mandatory login
![User Login](/uploads/arc/00-userlogin.png "Login prompt")

*Their argument: "Sync data, provide support"* - 
Its a tough ask, no matter how you spin it to require your users to be logged in to a service before using it. No matter if a user's actions are anonymised, the [way you use your browser is still logged](#data-being-collected). A scary fact is just like Google's Chrome browser and Google, policies change over time. At this stage data may not be collected or synced, but the convenience of having tabs on your phone, or to remember that website you were searching for earlier on in the day on another device will be the downfall of privacy for Arc.

![Welcome page](/uploads/arc/01-welcome.png "Welcome after logging in")

After logging in, you're greeted by a ['personalised' Card](/uploads/arc/02-card.png "Arc downloadable identifier card") with your name/alias.


Below is the first tab you'll see using Arc (at V1.0.1). There are tabs open on the side with a Wikipedia page, and two other websites.

![First Tab](/uploads/arc/03-firsttab.png "First page you'll see")
### Phoning home

These sites are all loaded in the system by the process Arc Helper, which is nice to be seperate from Arc itself, however the pages chosen starts to develop a unique fingerprint.

![First websites domains loaded](/uploads/arc/05-helpersites.png "First website domains loaded")

From the domains Arc loads on first launch, its evident the Arc team is very product-focused. With three major tools collecting user data: Segment, Sentry and Launchdarkly.
As upfront as their [Privacy Policy](https://thebrowser.company/privacy/) is, they are incredibly vague as to which platform, or how many they use in the browser. As you will see later on, its disappointing that there is a lack of opting out of sharing of any usage.

![Browser load phone home](/uploads/arc/04-phonehome.png "Browser load domains")


### Preferences
It was good to see some level above the standard [chrome settings](/uploads/arc/14-chromesettings.png) giving customisation to the browser. On the flip side, for a browser that talks a lot about privacy, mandating that users be signed in, and not providing an option to opt-out of providing device analytics (unless you block them at the DNS level) is disappointing. 

![User preferences](/uploads/arc/08-preferences.png "Browser preferences")
![User preferences grid](/uploads/arc/23-pref.png "Browser preferences pages")
![User preferences other](/uploads/arc/13-pref5.png "Browser preferences pages")

Notice the absence of an option to log out of an account to continue using the browser, or opting out of sending analytics to the browser company.

## Data being collected

The following is an extract of a sample being logged and sent to Sentry in accordance with the Browser Company's [personal data collection policy](https://thebrowser.company/privacy/#what-personal-data-do-we-collect-and-how-do-we-collect-it).

### Captured log - Sentry.io
![Sample log for sentry](/uploads/arc/16-logsidentifiers.png "Identifiers phoning home")

A few things to note here: 
* Every user has an 'anonymous id' as well as a ['user id'](https://docs.sentry.io/platforms/python/guides/logging/enriching-events/identify-user/) which could be speculated as being linked to your e-mail address to 'provide support' or understand how you prefer to use the browser.
* Events are logged, as per their privacy policy. This means it sends an update to Sentry when you Command Tab to another app, and another log sent when you go back. Other events include things like viewing preferences, creating a space among many other features I didn't test.
* The identifier of your Mac is sent. My one; Mac14,9 shows my model - MacBook Pro M2 2023 14in, with RAM config.
* Locale (Keyboard) and timezone are shared
* Interestingly, window dimensions are shared
* The network shows current connection, in my case WiFi, and although Bluetooth shows 'false' this refers to the network connection as Bluetooth was on.
* IP isn't logged (at this build)

An example of another event being logged
![Event sample](/uploads/arc/18-logsactivitypreferences.png "Event sample of action in Arc")

Interestingly, there were some interesting bits of data captured. One of which included a variable to check if the user logged in was internal (I wonder what that was for)
![Internal email](/uploads/arc/17-internalemail.png "internal email")


### Captured log - Launchdarkly
There wasn't much to decode from the Launchdarkly, with everything being encoded

![Launch darkly sample](/uploads/arc/15-darkly.png "Darkly sample")


### Permissions
Arc browser requests to see files on a few too many areas of you PC. Expect to get prompted if you plan on taking it for a spin.

![permission request](/uploads/arc/19-unnessesarypermission.png "Arc wants to view files in a lot of folders")


## Arc's Privacy Policy, and the problem with trying to 'sell' privacy
Arc's [Privacy Policy](https://thebrowser.company/privacy/) is upfront, being transparent that they are product-centric, wanting to understand their users behaviour.

>"What we do care about when it comes to data is building the best, most reliable product we can. For instance, understanding which features our members are digging most (and which features they hate, oof). Keep reading to check out our full privacy policy."

### A few days later.. the true purpose of needing an account

As with most products, the most valuable thing to an investor is measuring traction and growth. Having users sign up creates an asset of user details, which makes me wonder how The Browser Company is planning on monetising Arc or their future projects..

![Newsletter tracking](/uploads/arc/22-email.png "Newsletter sent with Mailchimp tracking stats")

## Result

I guess Arc browser isn't a privacy oriented browser. It has a unique take on developing an 'all-in-one' app to extend a web browser, heavily focused on user experience. Although, being Gecko based (Firefox) would have been a nice to see, the hype around Arc and Chromium isn't going away any time soon, and is typically viewed as the more performant on the web.

It would be nice if Arc, or rather the browser company provided more options to control what data is being logged, or provided a simple opt-out of everything option. Its understandable that they only recently went V1.0 and ditched the invite only system, however to build trust with users, I believe that along with using it without an account are the main barriers to recommend jumping on the Arc wagon. 

![Uninstalling Arc](/uploads/arc/21-removing.png "Arc files left on system")
Arc ended up in the trash on my test machine.

👍 Comes with uBlock pre-installed

👎 Account is mandatory

👎 No way to opt-out of sending analytics

🤷 A bit over the top permissions needed to access folders / files for the average user

🤷 Based on Chromium


*<b>Disclosure:</b> I work on an [open-source theme of Firefox browser to make it look like Safari](https://github.com/AdamXweb/WhiteSurFirefoxThemeMacOS)*



**Tools used in this writeup:**
- Little snitch
- Proxyman
- AppCleaner


Let me know in the comments below your thoughts on Arc