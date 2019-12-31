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
            "`Me: Tera Baap Romeo` @Its_Jaani ,`Mere Bhai Se Baat Kra,Prabal Gaming`",
            "`User Authorised.`",
            "`Calling Prabal`  `At +916367796969`",
            "`Private  Call Connected...`",
            "`Me: Are Prabal, Bhai isko Smjhao Expose Kr do LoL.`",    
            "`Pavel: May I Know Who Is This?`",
            "`Me: Are, LoL.`",    
            "`Prabal: Are you Romeo?? RighT `",
            "`Me: Are Beti, I Am` @Its_Jaani ",
            "`Prabal: OMG!!! Long time no see, Wassup Brother...\niska Naam Address photo snd kro Abhi Expose krta hu Within 2Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Prabal: Please Don't Thank Brah, Jaani is Heart of Swarg. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Prabal: Yes Sir, There Is A Bug In PUBG v0.16.5.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App key On My Whatsapp, I Will Fix The Bug & Send You.`",
            "`Prabal: Sure Sir \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
            
