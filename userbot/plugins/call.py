"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Tera baap Romeo` @Its_Vishal ,`Please Connect me to my lil bro,Prabal Gaming`",
            "`User Authorised.`",
            "`Calling Prabal Gaming`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: Hello Bhai,iska Smjha Yrr Mere Se Lad ra h .`",    
            "`Pavel: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @Its_Jaani ",
            "`Prabal: OMG!!! Long time no see, Wassup Brother...\nOye Sorry Bol Romeo ko within 1Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Prabal: Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Prabal: Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`Prabal: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
