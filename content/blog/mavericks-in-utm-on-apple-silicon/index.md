---
title: Installing MacOS Mavericks 10.9 in a VM on UTM
date: 2026-03-23T19:20:23.000+10:00
slug: mavericks-in-utm-on-silicon
description: Mavericks marks one of the last of the skeuomorphic MacOS designs, and with Liquid Glass, it's worth revisiting it yourself
keywords:
  - blog
  - marchintosh
  - macos Mavericks in UTM
  - Apple Silicon Mavericks
  - adam kostarelas
author: Adam Kostarelas
tags:
  - tech
math: false
toc: false
draft: false
---

TLDR; - Skip straight to the [Instructions](#instructions)
## My love for Mavericks
I have a soft spot for Mavericks. It was one of the first versions of MacOS I used on a daily basis. It was around 2013 when I purchased my first Mac, a MacBook Air 13", which was impossibly thin at the time compared to everything else in the market.

Being an early adopter, I also quickly upgraded to the flat design of Yosemite. I remember it never felt the same, but there often is no going back with security updates and improvements that lock you in with new features like Airdrop..

It's a shame I didn't get to spend more time with the operating systems named after big cats, instead with the operating systems based in beautiful places in California.

<lite-youtube videoid="w87fOAG8fjk" style="background-image: url('./videopreview/productteam.png');" label="The crack product marketing team" params="start=669&end=766&controls=0&cc_load_policy=1">
</lite-youtube>

> The crack product marketing team in their Volkswagen minibus

<lite-youtube videoid="w87fOAG8fjk" style="background-image: url('./videopreview/flatui.png');" label="The crack product marketing team" params="start=811&end=871&controls=0&cc_load_policy=1">
</lite-youtube>

> It was also the last OS before Apple introduced transparency in all their windows, as well as dark mode. 

<lite-youtube videoid="w87fOAG8fjk" style="background-image: url('./videopreview/dock.png');" label="The crack product marketing team" params="start=888&end=944&controls=0&cc_load_policy=1">
</lite-youtube>

> There was also the promise for an additional 2 hours of potential battery life for free

 Diving into [Aqua](https://en.wikipedia.org/wiki/Aqua_(user_interface)) and the UI elements of MacOS is a topic better left to be argued by designers. See short blog post from [Louie Mantia](https://lmnt.me/blog/visual-richness.html) (a prominent designer who made quite a few icons you'd recognise) about the shift in Apple design and the shift to minimalism.

{{< badge >}}
Tangent{{< /badge >}}
Some of the original UI components and apps are based on [NextStep](https://imgur.com/a/nextstep-1996-vs-os-x-2010-8XLsg), which influenced Cocoa which is what Mavericks is based on. If you want to try an alternative implementation of the UI elements, see [GNUstep](https://www.gnustep.org/) which is remarkably similar. If you're looking into the design, you may as well read this [99pi article about Susan Kare](https://99percentinvisible.org/article/designed-with-kare-influential-macintosh-graphics-of-early-apple-computers/), a designer with very recognisable pixel art..

There's also great article from [ArsTechnica](https://arstechnica.com/gadgets/2009/08/mac-os-x-10-6/) that highlights a lot of history of MacOS changes. If you're going down the rabbit hole of Apple Design, it's worth also looking at their [design motifs](https://en.wikipedia.org/wiki/Apple_Inc._design_motifs)
{{< badge >}}
End Tangent{{< /badge >}}


I won't go in depth about the evolution of Apple design, but i'll leave you with this imagery where I think Liquid Glass fits.
![Evolution of the trash](./img/trash.png)





Anyway, that's enough of an intro.



## Instructions



It's Marchintosh, and what better way to spend it on your Apple Silicon device, than to run an operating system your device doesn't natively support!
This guide assumes you're running [UTM](https://mac.getutm.app/), either from Github or the App store, on an Apple Silicon M1+ device.

### Step 1 - obtain installation medium

Mavericks was the first MacOS to download from the App Store, (which was also free). Apple mysteriously doesn't link to 10.9 on their download pages, and the method that doesn't make you go hunting on the internet archive, is to obtaining an iso using the tools on [MavericksForever](https://mavericksforever.com/)

You can do this in a simple command. **I'd recommend inspecting the bash file before executing, as it may change between now and when you're reading this**. This will download an image as .dmg, where you'll then convert to an .iso

`curl mavericksforever.com/get.sh | sh`

Then utilise your inbuilt disk tools to convert the downloaded dmg to iso.

` hdiutil convert InstallMacOSXMavericks.dmg -format UDTO -o mav.iso`

Rename the file to an iso

`mv mav.iso.cdr mav.iso`

Now we've got the install disk, it's time to [download the UTM config](./Mavericks-OSX-10.9-Config.utm.zip). This has a few images prepped that enable easy installation of MacOS.

A technical note about the config. It's based on Tianocore, with [OVMF](https://github.com/tianocore/tianocore.github.io/wiki/How-to-run-OVMF), adding UEFI to VMs. The image included in the utm config is about 5 years old, as troubleshooting getting the latest version running is out of scope, when this one just worked. You can try [building from source](https://github.com/tianocore/edk2/tree/master/OvmfPkg) and letting me know in the comments below how it goes!
Open core images are from [khronokernel](https://github.com/khronokernel/khronokernel.github.io/blob/master/Binaries/OpenCore/README.md). I'd recommend following their [guide](https://khronokernel.com/apple/silicon/2021/01/17/QEMU-AS.html) 

### Step 2 - load vm and first install

Load the Iso into UTM, then start it up and install.

![Install sped up](./img/install.gif)

This is going to take a while.. the above gif is sped up to illustrate what you'd expect to see.
due to the terms, you'll have to download the iso yourself


{{< gallery >}}
  <img src="./img/firstboot.png" class="grid-w33" />
  <img src="./img/termsandconditions.png" class="grid-w33" />
  <img src="./img/selecthdd.png" class="grid-w33" />
  <img src="./img/thewait.png" class="grid-w33" />
  <img src="./img/almostthere.png" class="grid-w33" />
  <img src="./img/countryselect.png" class="grid-w33" />
  <img src="./img/settingup.png" class="grid-w33" />
  <img src="./img/itworked.png" class="grid-w33" />
{{< /gallery >}}

If you're going to connect to the internet, you may run into the same issue I had. Changing the DNS to 1.1.1.1 or your flavour of choice allowed internet access with no issues... well sort of.

### Step 3 - Optional

The next step is optional, but recommended if you're going to use this. Updating the OS to at least patch it with a 2016 security patch from Apple is a good start, but going through the optional additional items are a good way
![Mavericks Forever Post install](./img/postinstallscript.png "Optional Post install script from mavericksforever.com to harden the OS")


### Exploring
![Exploring](./img/exploring.gif "Have some fun, and see how the UI used to look")


I feel rather nostalgic with the original Safari design. It may be worth theming Firefox to bring it back..?
![The original Safari tab view is marvellous](./img/ogtabview.png "The original Safari tab view is marvellous with tab previews")


Talking about Safari, there were other features inbuilt, long forgotten since Mavericks.
{{< youtubeLite id="4FunXnJQxYU" params="start=915&end=922&controls=0" >}}

Trying to browse to my blog is rather unsuccessful.

![The original Safari tab view is marvellous](./img/webisbroken.png "Modern web does not play nicely with Safari")

I would look at the firefox forked browser as an option to tinker with, as well as to install a few of the optional extras to make the experience a bit more friendly.



![Optional Apps](./img/installoptionalapps.png "It may take a while to install all the optional apps and scripts")

The UTM template has 8GB of RAM, which is more than the 2.9GB or so being used when idle.

![Enough system resources](./img/8gbram.png "There are enough system resources")

Trying anything that requires GPU is a bad idea. Chess, Launchpad and videos were essentially slideshows and not pleasant.
Unfortunately I couldn't figure out a way to pass more resources as UTM didn't support the additional parameter (for now).

{{< gallery >}}
  <img src="./img/chess.png" class="grid-w33" />
  <img src="./img/chesslag.png" class="grid-w33" />
  <img src="./img/gpu3mb.png" class="grid-w33" />
  <img src="./img/utmunhappy.png" class="grid-w33" />
  <img src="./img/videoplayback.png" class="grid-w33" />
  <img src="./img/airplay.png" class="grid-w33" />
{{< /gallery >}}


![Airplay](./img/airplaynotification.png "Interestingly it tried to play the audio through my MacBook as a receiver.")
Accepting showed the code as in the gallery above

![Temp](./img/temp.png "Just keep in mind you're emulating everyhing, and may run into some thermal issues")


### Want to try an alternate version of MacOS?

Check out [@adespoton](https://github.com/adespoton/utmconfigs) on Github for a list of configs to get you going.
I'd recommend downloading the installer directly from Apple, using a tool like [Mist](https://github.com/ninxsoft/Mist)
![Mist App](./img/mist.png)

Make sure to select the Application type or Disk Image.
![Mist App](./img/mistapp.png)

If you select Application, you can use the [createinstalliso](https://github.com/BITespresso/createinstalliso#user-content-installer-application-types) tool from BITespresso on Github to create an ISO.

`sudo ~/bin/createinstalliso --isodirectory <path to ISO directory> --applicationpath <path to OS installer application> [--nointeraction]`

Otherwise you can follow the `hdiutil` command from above to convert it to a disk image and rename to ISO. This isn't best practise, however does get the job done.

### Things to do

Due to the graphical limitations, there isn't a whole heap that's possible.
Yes, it's a novelty to jump into any non demanding tasks and do some basic web browsing, but that's about it.
Emulating the penryn processor is impressive enough, and maybe one day there will be better support for emulating older operating systems.. Or who knows, maybe Apple will bring back the plateau dock, giving us a taste of skeumorphism again?
Don't get me wrong, MacOS has improved in stability, performance and quality of life, but it is fun to revisit what once was and tinker around.

It might be fun to restore from a time machine backup on the network to have a literal timecapsule. I know i've got a couple licenses for software I can play around with.

Let me know how you go, and reach out on Github if you run into any issues.
I'll update this post with any optimisations I find along the way.

#### Most underrated photo editing app - Aperture
Sort of makes a comeback, if you're patiend and want to play workarounds. This would be so much simpler on a physical device though
![Mist App](./img/aperture.gif)
The photos import, exifdata is viewable, and adjustments can be made to the photo, and can even be exported!. However the preview doesn't show when editing, and only shows something when the photo is dragged, which is less than ideal.