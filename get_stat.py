#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from twitter import Api
import requests
import time


channels = {
    'AZKi_VDiVA':       ['AZKi',               '#6cbabc',  '#fff',  'UC0TXe_LYZ4scaW2XMyi5_kw'],
    'akaihaato':        ['Akai Haato',         '#eabb98',  '#fff',  'UC1CfXB_kRs3C-zaeTG3oGyg'],
    'akirosenthal':     ['Aki Rosenthal',      '#5deaf9',  '#fff',  'UCFTLzh12_nrtzqBPsTCqenA'],
    'amanekanatach':    ['Amane Kanata',       '#2650d0',  '#fff',  'UCZlDXzGoo7d44bwdNObFacg'],
    'himemoriluna':     ['Himemori Luna',      '#93446d',  '#fff',  'UCa9Y57gfeY0Zro_noHRVrnw'],
    'suisei_hosimati':  ['Hoshimachi Suisei',  '#799acb',  '#fff',  'UC5CwaMl1eIgY8h02uZw7u8A'],
    'houshoumarine':    ['Houshou Marine',     '#dc6e7f',  '#fff',  'UCCzUftO8KOVkV4wQG1vkUvg'],
    'inugamikorone':    ['Inugami Korone',     '#c88382',  '#fff',  'UChAnqc_AY5_I3Px5dig3X1Q'],
    'kiryucoco':        ['Kiryu Coco',         '#db9574',  '#fff',  'UCS9uQI-jC3DE0L4IpXyvr6w'],
    'minatoaqua':       ['Minato Aqua',        '#793559',  '#fff',  'UC1opHUrw8rvnsadT-iGp7Cg'],
    'murasakishionch':  ['Murasaki Shion',     '#4f3756',  '#fff',  'UCXTpFs_3PqI41qX2d9tL2Rw'],
    'nakiriayame':      ['Nakiri Ayame',       '#bf8996',  '#fff',  'UC7fk0CB07ly8oSl0aqKkqFg'],
    'natsuiromatsuri':  ['Natsuiro Matsuri',   '#edad62',  '#fff',  'UCQ0UDLQCjY0rmuxCDE38FGg'],
    'nekomataokayu':    ['Nekomata Okayu',     '#aa8caf',  '#fff',  'UCvaTdHTWBGv3MKj3KVqJVCw'],
    'ookamimio':        ['Ookami Mio',         '#c6535c',  '#fff',  'UCp-5t9SrOQwXMU7iIjQfARg'],
    'oozorasubaru':     ['Oozora Subaru',      '#6db2ce',  '#fff',  'UCvzGlP9oQwU--Y0r9id_jnA'],
    'robocosan':        ['Roboco San',         '#af7425',  '#fff',  'UCDqI2jOz0weumE8s7paEk6g'],
    'sakuramiko35':     ['Sakura Miko',        '#f6a1a8',  '#fff',  'UC-hM6YJuNYVAmUWxeIr9FeA'],
    'shirakamifubuki':  ['Shirakami Fubuki',   '#5eb6d0',  '#fff',  'UCdn5BQ06XqgXoAxIhbqw5Rg'],
    'shiranuiflare':    ['Shiranui Flare',     '#5bb39d',  '#fff',  'UCvInZx9h3jC2JzsIzoOebWg'],
    'shiroganenoel':    ['Shirogane Noel',     '#dccdcd',  '#fff',  'UCdyqAaZDKHXg4Ahi7VENThQ'],
    'tokino_sora':      ['Tokino Sora',        '#be6c5e',  '#fff',  'UCp6993wxpyDPHUpavwDFqgg'],
    'tokoyamitowa':     ['Tokoyami Towa',      '#d197ce',  '#fff',  'UC1uv2Oq6kNxgATlCiez59hw'],
    'tsunomakiwatame':  ['Tsunomaki Watame',   '#e4d3a3',  '#fff',  'UCqm3BQLlJfvkTsX_hvm0UmA'],
    'uruharushia':      ['Uruha Rushia',       '#80d3c3',  '#fff',  'UCl_gCybOJRIgOXw6Qb4qJzQ'],
    'usadapekora':      ['Usada Pekora',       '#acc0ee',  '#fff',  'UC1DCedRgGHBdm81E1llLhOQ'],
    'yozoramel':        ['Yozora Mel',         '#d7a86a',  '#fff',  'UCD8HOxPs4Xvsm8H0ZxXGiBw'],
    'yuzukichococh':    ['Yuzuki Choco',       '#eb9f74',  '#fff',  'UC1suqwovbL1kzsoaZgFZLKg'],
}

# YouTube
parts = ['statistics']
yt_key = 'AIzaSyBb2geihz612g_0SxfaP0JCSTfkg6vtPAY'
yt_url = 'https://www.googleapis.com/youtube/v3/channels?part={parts}&id={channels}&key={key}'

ids = [values[-1] for values in channels.values()]
yt_data = requests.get(yt_url.format(
    parts=','.join(parts),
    channels=','.join(ids),
    key=yt_key,
)).json()

# Twitter
twitter_api = Api(consumer_key='OsD23pataKp2SvoX9V5VYamen',
                  consumer_secret='u9XUokOOLB3opmuvqeJWrms3cfKDxWcK4VG4AoYQjszsZiCeib',
                  access_token_key='4879173371-UGtBxDnTgX3kLONLUW210zSkR7tC94P3zNQPZjd',
                  access_token_secret='TeqEu6WPcUYnvCs6rgQtZElxnpZI6LZGMuc5noVA686us')

t_data = twitter_api.GetListMembersPaged('1275532206446952448')[2]

# Write stats
data_file = Path(__file__).absolute().parent / 'www/stats'
data_file.write_text('')

with data_file.open('a') as file:
    for yt_user_data in sorted(yt_data['items'], key=lambda item: item['statistics']['subscriberCount'], reverse=True):
        screen_name, channel_data = next(filter(lambda channel: channel[1][-1] == yt_user_data['id'], channels.items()))
        t_user_data = next(filter(lambda user: user.screen_name == screen_name, t_data))

        file.write(','.join([
            *channel_data,
            screen_name,
            str(t_user_data.followers_count),
            yt_user_data['statistics']['subscriberCount'],
            t_user_data.profile_image_url_https.replace('_normal', ''),
        ]) + '\n')
print(time.asctime())
