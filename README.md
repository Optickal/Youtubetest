
<h1 align="center"> YouTube_to_m3u </h1>

[![M3U generator for YouTube](https://github.com/naveenland4/YouTube_to_m3u/actions/workflows/m3u_Generator.yml/badge.svg)](https://github.com/naveenland4/YouTube_to_m3u/actions/workflows/m3u_Generator.yml)

`https://raw.githubusercontent.com/naveenland4/YouTube_to_m3u/main/youtube.m3u`

Updated m3u links of YouTube live channels, **auto-updated every hour**.


### Add more channels
Edit `youtube_channel_info.txt` to add your favourite YouTube livestreams

Create a pull request

### Usage
Paste this URL: `https://raw.githubusercontent.com/naveenland4/YouTube_to_m3u/main/youtube.m3u` to any player which supports M3U playlists

### Run the tool on your local machine
``` bash
git clone https://github.com/naveenland4/YouTube_to_m3u.git
cd YouTube_to_m3u
chmod +x autorun.sh
./autorun.sh
```

Do not forget to add a cron job set for every 4 hours(or 5) if you plan to run the script locally.

Credits: [benmoose39](https://github.com/benmoose39)
