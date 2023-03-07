# Clan_Bot
A Discord bot developed in Python for my clan in naruto-arena.net.

Naruto-Arena.net is a turn-based, tactical online multiplayer browser game played based on the Shounen Anime and Manga series called Naruto. You pick 3 characters to form a team and battle it out against other players. Players battle for different purposes: Ranking up to number 1, unlocking more characters, or having fun against friends by playing private battles. You can make friends by sending requests to players or through the naruto-arena discord server.

A clan is the name given to a community of players who come together for various purposes.
Wars are another aspect of the game where clans face other clans based on certain rules and conditions.

This bot was developed for the purpose of helping I and my clanmates with Wars by making it easier for us to build teams that meet the criteria of various war rules. This bot displays a graphical representation of all available characters in a certain war. With this, the amount of times a player breaks a rule by using an invalid character would be alleviated. 

The graphical representation of the characters was achieved with the use of Pillow. An Imaging library in Python. It adds image processing capabilities to the Python interpreter.


**Disclaimer:** When using this repository you confirm that you have read the [license](LICENSE) and comprehend that I can take down your repository if you do not meet these requirements

---
NARUTOARENA © 2018-2023 WESPRO. All rights reserved.


# Requirements and Dependencies
The following are the requirements needed to acheive the development of this bot:

* A basic understanding of Python programming language is needed for this. If you don't know the basics. [Here's](https://www.w3schools.com/python/default.asp) a link for resources to learn python.
* Must have Python installed on your system. Follow this quick [guide](https://phoenixnap.com/kb/how-to-install-python-3-windows)
* Must have pip installed in your system. Download [Here](https://phoenixnap.com/kb/install-pip-windows) or follow this [guide](https://pip.pypa.io/en/stable/installation/)
* Must have Discord.py installed. Run the following in your terminal
```
python -m pip install -U discord.py
```
* Must have Pillow (Python Imaging Library (PIL)) installed. Run the following in your terminal
```
python -m pip install pillow
```
* Must have a Discord account and a discord server


# How to Set Up
To set up this bot, you should do the following:
* Clone this repository using `git clone` < url >. Unfamiliar with Git? Check [Here](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners). Don't have Git installed? Download Git [Here](https://git-scm.com/downloads). 
* Learn how to create a Discord bot [here](https://www.makeuseof.com/how-to-make-discord-bot/)

   Alternatively:
   * Create a Discord bot [here](https://discord.com/developers/applications).
   * Click **New Application** at the top-left.
   * Provide a name for your application in the given field. Then click **Create**
   * Look to the left sidebar, and select **Bot** and click **Add Bot** at the extreme right
   * Click **Copy** to copy your bot token and save it somewhere
   * Scroll down to **Privileged Gateway Intents** and toggle all the three switches under it
   * Click **OAuth2** on the left bar to add authentication priorities to your Discord bot 
   * Select **URL Generator** to generate a bot invitation URL for your server. Under **Scopes** check **Bot**. Under **Bot Permissions** check the permissions you want the bot to have (Most important for this bot are "Send Messages" and "Attach Files"). Scroll down to **Generated URL** copy the url there and paste it in your browser
   * From the prompt, click **Select a server** and choose the server you want your bot to run in.
   * You'll see a new menu with a list of permissions you set earlier. Select **Authorize**. Solve the CAPTCHA to complete authorizing your Discord bot
   * To make the bot work in only one channel Check [Here](https://unita.co/blog/restrict-bot-to-one-channel/)
* Open the source code **bot.py** found in the cloned repository in an IDE that supports python, preferably [Visual Studio Code](https://code.visualstudio.com/download)
* Replace < your bots token > with the token of your bot you copied earlier
* Run the code. You would see "< Your Bot > has connected to Discord!". Your bot will now appear online in your server


# How to Use
To use this bot, simply go to the server and channel you set the bot to run in and send the name of a character as a message, all characters except the one you sent would be displayed.

To type multiple characters in one message, the user should separate each characters name by a space, a hyphen, and another space " - ".

Characters names in the sent messages must be spelt according to how they are spelt in the "characters" dictionary.


# Contributing
Contributions, feedback, and bug reports are welcome!

Feel free to send me a message to my [Discord](discordapp.com/users/594215301458034714) (AusBee#1945) if you have any issues or questions


# Built With
* Python 3.10.5
* pip 23.0.1
* Pillow 9.4.0


# Credit
The functionality of this bot was heavily inspired by the functionality of a similar project made by Clover. Feel free to send her a message on [Discord](discordapp.com/users/226165431369596928) (Clover#1315)


# Extending this Work
Some ideas to extend this work:
* Allow the user to type a characters name without case sensitive restrictions
* Store the image after a users message to be able to send different messages and produce results from that same image
* If above is implemented, add a restart command that will make the next message the user sends to produce a new image


# Support
Feel free to support the developers of Naruto-arena by joining their discord server and trying out their game
* [Website](https://naruto-arena.net/en)
* [Discord](https://discord.com/invite/yEFaw6f)



