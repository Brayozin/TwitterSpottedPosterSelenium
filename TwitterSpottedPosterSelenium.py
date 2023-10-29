# coding: utf-8
# TwitterSpottedPoster
# This file is part of the TwitterSpottedPosterSelenium distribution
# (https://github.com/Brayozin/TwitterSpottedPosterSelenium).
# Copyright (C) 2018 Matheus Horstmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Implements the class SpottedPosterTwitterSelenium, which is responsible for posting the spotted tweets on Twitter.
# This class uses Selenium to automate the process of posting the tweets.


from __future__ import absolute_import, print_function, unicode_literals
import time
import logging
import re
import config
import tweepy
import time
import textwrap
import requests
import sys

from . import twitterbot as tb


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class TwitterSpottedPosterSelenium(object):
    def __init__(self):
        self.TWITTER_USERNAME = None 
        self.TWITTER_PASSWORD = None
        self._TWITTERMAX_SIZE = 270

    def setup(self, username, password):
        self.TWITTER_USERNAME = username
        self.TWITTER_PASSWORD = password

        self.bot = tb.Twitterbot(self.TWITTER_USERNAME, self.TWITTER_PASSWORD)
        self.bot.login()
        logger.info("Logged on twitter using Selenium")
    
    def post_tweet(self, text):
        def post_message(text):
            logger.info("Posting tweet on Twitter using Selenium")
            logger.info("Tweet: " + text)
            self.bot.post_tweet(text)
            logger.info("Posted tweet on Twitter using Selenium")
        post_message(text)

    def search(self, spotted_number):
        logger.info("Searching for spotted number " + str(spotted_number) + " on Twitter")
        logger.info("To be implemented")
        return None
    
    def delete(self, spotted_number):
        logger.info("Deleting spotted number " + str(spotted_number) + " on Twitter")
        logger.info("To be implemented")
        return None
    
def main():
    app = SpottedPosterTwitterSelenium()
    app.setup(config.TWITTER_USERNAME, config.TWITTER_PASSWORD)
    app.post_tweet("Teste de postagem de tweet")


if __name__ == '__main__':
    main()

        
    