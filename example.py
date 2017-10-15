#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.join(sys.path[0], 'src'))

from instabot import InstaBot

username = sys.argv[1]
password = sys.argv[2]
like_per_day = int(sys.argv[3])
follow_per_day = int(sys.argv[4])
unfollow_per_day = int(sys.argv[5])
media_min_like = int(sys.argv[6])
max_like_for_one_tag = int(sys.argv[7])
proxy = sys.argv[8]
tag_list = []
for x in range(9, len(sys.argv)):
    tag_list.append(sys.argv[x])

bot = InstaBot(
    login=username,
    password=password,
    like_per_day=like_per_day,
    tag_list=tag_list,
    max_like_for_one_tag=max_like_for_one_tag,
    follow_per_day=follow_per_day,
    unfollow_per_day=unfollow_per_day,
    proxy=proxy,
    media_min_like=media_min_like)

while True:
    bot.new_auto_mod()

