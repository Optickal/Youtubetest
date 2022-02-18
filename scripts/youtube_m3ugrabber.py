#! /usr/bin/python3

banner = r'''
###########################################################################
#      ____ 	____    _____                                             #
#     |  _ \   |       |  _   \                                           #
#     | |_) |  |____   | |_|  |                                           #
#     |  __/        |  |  _   /                                           #
#     |_|       ____|  |_| |__\                                           #
#                                                                         #
#                                  >> https://github.com/naveenland4      #
###########################################################################


#EXTINF:-1 group-title="4K" tvg-logo="https://i.imgur.com/oYYncnc.png" tvg-id="", Loupe 4K
https://d2dw21aq0j0l5c.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/LoupeArt-prod/playlist.m3u8|User-Agent=ExoPlayerLib/2.9.6
#EXTINF:-1 group-title="4K" tvg-logo="https://i.imgur.com/C9UDwli.png" tvg-id="", Clarity 4K
https://d3thiix3tzne5u.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/ClarityTV4K2-prod/playlist.m3u8|User-Agent=ExoPlayerLib/2.9.6
#EXTINF:-1 group-title="4K" tvg-logo="https://i.imgur.com/ufQEuaF.png" tvg-id="", Love Nature 4K
https://d18dyiwu97wm6q.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/LoveNature4K2-prod/playlist.m3u8|User-Agent=ExoPlayerLib/2.9.6
#EXTINF:-1 group-title="4K" tvg-logo="https://i.imgur.com/oTPJYPO.png" tvg-id="", Bloomberg TV+ UHD
https://0984ed0046994029aafaa07692005474.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung_Bloomberg/playlist.m3u8|User-Agent=ExoPlayerLib/2.9.6
#EXTINF:-1 group-title="4K" tvg-logo="https://i.imgur.com/5gkt9DD.png" tvg-id="", Rai 4K (Italy)
https://raievent10-live.akamaized.net/hls/live/619189/raievent10/raievent10/playlist.m3u8
#EXTINF:-1 group-title="Tamil" tvg-logo="https://i.imgur.com/r9ia17h.jpg" tvg-id="", TV9 Tamil
http://14.199.164.20:4001/play/a0tr/index.m3u8
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = s.get(url, timeout=15).text
    if '.m3u8' not in response:
        response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/in/dishtv.in.epg.xml"')
print(banner)
s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
