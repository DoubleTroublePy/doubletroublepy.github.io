---
title: rack
date: 2026-08-16
description: my rack setup
feature_image: /img/posts/rack/rack.jpg
feature_alt: pc case in a pink illuminated rack with two visible hdds
tags: 
    - nas
    - tech
    - homelab
    - zfs
    - rack
    - eng
---
## *premise:*

I'm am not English native and i don't have a proof reader so, sorry for any mistakes.
Also this is a blog where i yap, this IS NOT, I ANY WAY a tutorial IN AM NOT RESPONSIBLE for related incidents.

---

## *story*:
I update the nas build some time ago but, i procastinated an update post until now.
So now the nas has changed 2 times mobo and i have a server case and rack.

The rack is build like this:
```
[      patch panel      ]
[        switch         ]
[ Futro S520 | mini NAS ]
[                       ]
[          NAS          ]
[                       ]
```

## panel panel

Standard patch panel, nothing to see here


## switch 

A cheap mercusys switch (MS116GS) which will be substituted shortly by the Tenda
TEG5312F managed switch. 


## Futro S520

A cheap mini pc, not very powerfull, but it can be a work as a mini router, given
i had to use [openwrt](https://openwrt.org/) and not [opnsense](https://opnsense.org/)
as i wanted. Is running [proxmox](https://www.proxmox.com/en/), on witch i have 
the following machines:
 - [adguard](https://adguard.com/en/adguard-home/overview.html)
 - [haos](https://www.home-assistant.io) (smart home os)
 - [openwrt](https://openwrt.org) 

### [openwrt](https://openwrt.org) 

The S520 as only 1 ethernet port so i must use a router-on-a-stick configuration:
I have two virtual interfaces with different vlans and with a managed switch i route
the wan traffic on one interface and the lan on the other, is not optimal, but it works.


## [mini NAS](https://doubletroublepy.github.io/posts/mini_nas/)

Updates:
 - gigabit usb rj45 dongle 


## [NAS](https://doubletroublepy.github.io/posts/nas/)

I finally changed the case with a proper rack one, and added a caddy tray. 
Luck wants that my grandfather, witch is a hobbyist photographer was retiring two
8TB hdds. He gifted me this hdds, so now i have the same configuration but with
16TB raw and 8TB usable. As right now yesterday a power outage corrupted one of the
drives, but luckily only data was damaged not the drive itself. I'm currently in the
process of resilvering the drive, 12h of agony.

---

# The rack

The rack is not a good one, i bought a package of rackstuds but the rack holes are
under dimensioned, which is fine for cagenuts but not for rack studs.
Is not a big problem as is was cheap 50 euros and i have another one, 90 euros.
I'm not using the other one as is currently in another city where i plan to return.
I will probably swap this for a minirack for my mother and use the better one for
myself.

