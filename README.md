[![Build Status](https://travis-ci.org/MaxLFarrell/botmom.svg?branch=master)](https://travis-ci.org/MaxLFarrell/botmom)

# Requirements
Yarn <a href='https://yarnpkg.com'><img width='20%' height='20%' src='https://circleci.com/docs/assets/img/logos/yarn-logo.svg'/></a>
Python 3 <a href='https://www.python.org/downloads/'><img src='https://www.python.org/static/img/python-logo.png'/></a>

# Installation
1. Clone the directory `git clone https://github.com/MaxLFarrell/botmom.git`
2. Navigate into the directory
3. Install python requirements `pip install -r build/requirements.txt`
4. Install yarn packages `yarn install --modules-folder ./res/public/libs`
5. Register tumblr app: https://www.tumblr.com/oauth/apps
6. Click "Explore API" under tumblr app
7. Click "Show Keys" at the upper right corner of the screen
8. Copy and paste the first 4 rows into credentials/credentials (remove any existing data in file, including lines)
9. Remove the text at the beginning of each row

# Adding Your First Bot
1. Create a folder in bots with the name of your bot
2. Follow the example bot guidelines to create your first bot, note which parts are required
3. Set the queue on the tumblr this bot will be associated with, remember how many times a day you will post
4. Navigate to directory and run `python run.py` and follow the instructions
5. Sit back and watch your queue fill up (or if need be, troubleshoot)