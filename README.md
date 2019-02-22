# DankBot
[![Heroku](https://heroku-badge.herokuapp.com/?app=dankbot-tg&style=flat)](https://telegram.me/TheRealDankBot)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0)
[![Codacy Badge](https://img.shields.io/codacy/grade/bae5054274c7463f98206a684c9e58b5.svg?style=flat-square)](https://www.codacy.com/app/Rippr/DankBot)
[![CodeFactor](https://www.codefactor.io/repository/github/rippr/dankbot/badge)](https://www.codefactor.io/repository/github/rippr/dankbot)
[![Codebeat Badge](https://codebeat.co/badges/34ed37f8-955c-4907-8edb-c902b99f6b78)](https://codebeat.co/projects/github-com-rippr-dankbot-master)
[![Maintainability](https://img.shields.io/codeclimate/maintainability/Rippr/DankBot.svg?style=flat-square)](https://codeclimate.com/github/Rippr/DankBot/maintainability)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg?style=flat-square)](https://saythanks.io/to/Rippr)


DankBot is a Telegram Bot which can send, generate, and fry memes.

# Why DankBot?
DankBot has been an extremely fun project to work on. <br><br>
The idea itself started off as a joke - My friends and I would often reference memes in our conversations and wishfully discuss about a tool that would share memes in response to certain triggers. While the idea of making a bot had occurred to me, the fact that Whatsapp, our primary communications app, didn't have a public API was discouraging. After a lot of deliberation, I began this project on the fourth of September, 2018.

### Major Technologies Used
- Python 3.7
- PIL (Pillow)
- OpenCV
- Numba
- Python Telegram Bot

### Things I've Learnt
- Building stateless, event-driven bots
- Manipulating images with PIL
- Uploading images to Imgur
- Using OpenCV to find eyes and characters in an image
- Extracting frames from a video and making videos from a series of frames using OpenCV + imutils.
- Using Numba JIT and asynchronous processing for improving performance
- Applying binary search on discrete functions (Used to calculating optimum text size in the meme generator)

# Using DankBot

## Basic Commands
Each of these commands trigger a certain response. <br>
For most commands, there are multiple responses from which one is randomly picked.

- Hmmm
- Boom son
- Just do it
- Nein
- E
- Hello there
- I don't think so
- Wut / Wat / Dude what / What even / What the
- Miss me with that gay shit
- Ironic
- F / RIP
- ???

## Advanced Commands

### ABC, not XYZ
Generates a meme using either the Robbie Rotten, Babushka, or Drake template in which ABC is chosen over XYZ.

### Alt: ABC
Converts text that follows the colon to aLt CaSe. It deletes the trigger message if bot has admin rights.

### Vapourize: ABC
Converts text that follows the colon to Vapourwave text. It deletes the trigger message if bot has admin rights.

### 🅱
Replaces the first consonant group of each word with a 🅱. <br>
It doesn't replace those consonants which can (mostly) be pronounced after a B.

### Alexa / Dankbot play Despacito \[x\]
Sends a GIF of the Despacito music video along with an audio file of Despacito. <br>
If a number x is given, certain effects are applied to the audio. <br>
If not, the audio file has a 10% chance of being extremely bass boosted. <br>

### T: ABC B: XYZ
Creates a meme with the provided captions: ABC as the top-text and XYZ as the bottom-text.
By default, the captions are converted to upper case.
Replacing T with Ts and B with Bs prevents auto-capitalization.


## Deep Fryer
The Deep Fryer fries images, GIFs, or videos (Experimental).
Frying includes increasing saturation & contrast, and adding noise, emojis, lazer eyes, and bulges.

The action is triggered by replying to a message containing a media file with one of the following commands:

- Fry: 1 cycle of frying.
- Nuke: 3 cycles of frying.
- Allah hu Akbar: 5 cycles of frying.
- Tsar Bomba: 10 cycles of frying.

#### Additional parameters

**Deep:** High contrast and saturation increase. <br>
**Shallow:** Low contrast and saturation increase. <br><br>

**High-fat:** Emojis are increased. <br>
**Low-fat:** Emojis are reduced. <br>
**No-fat:** Emojis aren't added. <br><br>

**Heavy:** Extra bulges are added. <br>
**Light:** No bulges are added. <br><br>

**Vitamin-B:** (Experimental) Adds the B emoji on text in the image. <br>
**Chilli:** (Experimental) Adds laser eyes.





          ##### ##                             /            ##### ##
       /#####  /##                           #/          ######  /##
     //    /  / ###                          ##         /#   /  / ##                  #
    /     /  /   ###                         ##        /    /  /  ##                 ##
         /  /     ###                        ##            /  /   /                  ##
        ## ##      ##    /###   ###  /###    ##  /##      ## ##  /        /###     ########
        ## ##      ##   / ###  / ###/ #### / ## / ###     ## ## /        / ###  / ########
        ## ##      ##  /   ###/   ##   ###/  ##/   /      ## ##/        /   ###/     ##
        ## ##      ## ##    ##    ##    ##   ##   /       ## ## ###    ##    ##      ##
        ## ##      ## ##    ##    ##    ##   ##  /        ## ##   ###  ##    ##      ##
        #  ##      ## ##    ##    ##    ##   ## ##        #  ##     ## ##    ##      ##
           /       /  ##    ##    ##    ##   ######          /      ## ##    ##      ##
      /###/       /   ##    /#    ##    ##   ##  ###     /##/     ###  ##    ##      ##
     /   ########/     ####/ ##   ###   ###  ##   ### / /  ########     ######       ##
    /       ####        ###   ##   ###   ###  ##   ##/ /     ####        ####         ##
    #                                                  #
     ##                                                 ##
