#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
from pprint import pprint as pp


channels = {
    'UCp6993wxpyDPHUpavwDFqgg': 'Tokino Sora',
    'UC0TXe_LYZ4scaW2XMyi5_kw': 'AZKi',
    'UCDqI2jOz0weumE8s7paEk6g': 'Roboco San',
    'UC-hM6YJuNYVAmUWxeIr9FeA': 'Sakura Miko',
    'UCdn5BQ06XqgXoAxIhbqw5Rg': 'Shirakami Fubuki',
    'UCQ0UDLQCjY0rmuxCDE38FGg': 'Natsuiro Matsuri',
    'UCD8HOxPs4Xvsm8H0ZxXGiBw': 'Yozora Mel',
    'UC1CfXB_kRs3C-zaeTG3oGyg': 'Akai Haato',
    'UCFTLzh12_nrtzqBPsTCqenA': 'Aki Rosenthal',
    'UC1opHUrw8rvnsadT-iGp7Cg': 'Minato Aqua',
    'UC1suqwovbL1kzsoaZgFZLKg': 'Yuzuki Choco',
    'UC7fk0CB07ly8oSl0aqKkqFg': 'Nakiri Ayame',
    'UCXTpFs_3PqI41qX2d9tL2Rw': 'Murasaki Shion',
    'UCvzGlP9oQwU--Y0r9id_jnA': 'Oozora Subaru',
    'UCp-5t9SrOQwXMU7iIjQfARg': 'Ookami Mio',
    'UCvaTdHTWBGv3MKj3KVqJVCw': 'Nekomata Okayu',
    'UChAnqc_AY5_I3Px5dig3X1Q': 'Inugami Korone',
    'UCvInZx9h3jC2JzsIzoOebWg': 'Shiranui Flare',
    'UCdyqAaZDKHXg4Ahi7VENThQ': 'Shirogane Noel',
    'UCCzUftO8KOVkV4wQG1vkUvg': 'Houshou Marine',
    'UC1DCedRgGHBdm81E1llLhOQ': 'Usada Pekora',
    'UCl_gCybOJRIgOXw6Qb4qJzQ': 'Uruha Rushia',
    'UC5CwaMl1eIgY8h02uZw7u8A': 'Hoshimachi Suisei',
    'UCZlDXzGoo7d44bwdNObFacg': 'Amane Kanata',
    'UCS9uQI-jC3DE0L4IpXyvr6w': 'Kiryu Coco',
    'UCqm3BQLlJfvkTsX_hvm0UmA': 'Tsunomaki Watame',
    'UC1uv2Oq6kNxgATlCiez59hw': 'Tokoyami Towa',
    'UCa9Y57gfeY0Zro_noHRVrnw': 'Himemori Luna',
    'UC6t3-_N8A6ME1JShZHHqOMw': 'Hanasaki Miyabi',
    'UCZgOv3YDEs-ZnZWDYVwJdmA': 'Kanade Izuru',
}

parts = [
    # 'snippet',
    'statistics',
]

key = 'AIzaSyBb2geihz612g_0SxfaP0JCSTfkg6vtPAY'
url = 'https://www.googleapis.com/youtube/v3/channels?part={parts}&id={channels}&key={key}'

data = requests.get(url.format(
    parts=','.join(parts),
    channels=','.join(channels.keys()),
    key=key
)).json()

if 'error' in data:
    pp(data)
    sys.exit(1)

for channel in data['items']:

    print('{}: {}'.format(
        channels[channel['id']],
        channel['statistics']['subscriberCount'],
    ))
