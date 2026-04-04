---
title: mini nas
date: 2026-03-27
feature_image: /img/posts/mini_nas/mini_nas.jpg
feature_alt: a mini nas with 3HDDs and a rasperri in a messi of cables
description: the setup of my first (real) mini nas
tags: 
    - nas
    - mini
    - tech
    - homelab
    - zfs
    - eng
---

## *premise:*

Im am not english native and i dont have a proof reader so, sorry for any mistakes.
Also this is a blog where i yap, this IS NOT, I ANY WAY a tutorial I AM NOT RESPONSABLE for related incidents.

---

## the problem
As of now the mini nas solves to probles, alleviate my 4TB main HDD and create a
way for my mother for:
1. still have a sort of cloud migrating from Mac to Linux ( congratulations to her ). 
2. have a location where to make backups of her files

## the how

My mother posses two 2TB HDDs and a friend gifted us a bunch of usb HDDs. This
plus a raspberri 3, i had laying around made the perfect opportunity.
Also both i and my mom have FTTH gigabit connections. So we can transfer data 
pretty quickly. The main bottleneck are the usb interfaces.

## the process

first i opened two of the two enclosures to swtch the original 2TB and 3TB with
the newer 2TB WDredNas HDDs of my mother. Form my data i formatted another without
changing anything.
aftrer switching around the data on the 2HDDs on my HDD i formatted them with a mirrored zsa pool.

---

### ~~!!! WORK IN PROGRESS !!!~~

here i don't have a good keyboard so i cannot write comfortably, but i will uptate
this article. Also as of now there is more to do.

---

<a>============ </a>
</br>
edit: 2026-03-30 
</br>
<a>============</a>

I figured out how to set colemack on the shitty keyboard so writing is less painfull.

## so, unexpected things from life

my grandpa gifted me a 2 bay nas. So the raspberry would be turned to a smart tv.
The new nas wold also manage my support hdd.
But for now i installed jellyfin on the pi and modified samba settings to make it 

compatible with ios. When the arrive i will swap all to it if i can flash a decent
os on it.

---

<a>============ </a>
</br>
edit: 2026-04-04 
</br>
<a>============</a>

_idk if this is the right way to write a blog or if i should add a new post for
every update but for now i will write like this_

so, anyways i started installing some services on my mom nas. 

The first one was <a href="https://stashapp.cc/">stash</a> with podman and then 
i tried jellyfin but the raspberry 3 couldn't sustain the load so i made the 
decision of renouncing to it. 

After that i tried unsuccessfully to install paperless-ngx on podman but i gave up. 
After some digging around i found <a href="https://papra.app/en/">papra</a> an
alternative to paperless. But after trying unsuccessfully to install it via podman i
resigned myself to use docker as i didn't want to have the double headache of using
podman on arm.


