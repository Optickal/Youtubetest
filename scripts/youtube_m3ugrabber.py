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

#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG80573.png"group-title=7 Star Cloud",7Star TV
http://hdserver.7starcloud.com:1935/live/7star2/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG35713.png"group-title=7 Star Cloud",Sana TV
http://hdserver.7starcloud.com:1935/sanatv/sanatv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG43856.png"group-title=7 Star Cloud",3Tamil TV
https://6n3yogbnd9ok-hls-live.5centscdn.com/threetamil/d0dbe915091d400bd8ee7f27f0791303.sdp/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG58756.png"group-title=7 Star Cloud",Sharvesh 7Star TV
http://hdserver.7starcloud.com:1935/sharvesh/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG244.png"group-title=7 Star Cloud",7STAR PLUS
http://hdserver.7starcloud.com:1935/live/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG39297.png"group-title=7 Star Cloud",CTN 
http://hdserver.7starcloud.com:1935/ctn/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG5530.png"group-title=7 Star Cloud",Polimer Channel
http://hdserver.7starcloud.com:1935/polimer/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG99048.png"group-title=7 Star Cloud",SS Varma TV
http://hdserver.7starcloud.com:1935/ssvarmatv/ssvarmatv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG28145.png"group-title=7 Star Cloud",TEN TV
http://51.79.158.179:1935/tentv/tentv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG34271.png"group-title=7 Star Cloud",Jawahar Channel
http://hdserver.7starcloud.com:1935/jawaharchannel/livetv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG40848.png"group-title=7 Star Cloud",Jawahar TV
http://streamingbox.7starcloud.com:1935/jawahartv/streamingbox/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG18653.png"group-title=7 Star Cloud",SS TV
http://hdserver.7starcloud.com:1935/live/ss/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG66942.png"group-title=7 Star Cloud",DEEPAM TV 
http://hdserver.7starcloud.com:1935//live/deepam/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG9905.png"group-title=7 Star Cloud",Sana Plus
http://media.7starcloud.com:1935/live/sanatv2/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG91933.png"group-title=7 Star Cloud",Ashoka Channel
http://hdserver.7starcloud.com:1935/ashoka/channel/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG49043.png"group-title=7 Star Cloud",Ashoka Channel 2
http://hdserver.7starcloud.com:1935/ashoka/channel2/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG32565.png"group-title=7 Star Cloud",Shalini TV
https://gvjygr2jloem-hls-live.5centscdn.com/shalini/live.stream/chunks.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",Vani TV
http://hdserver.7starcloud.com:1935/vanitv/livemedia/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG95865.png"group-title=7 Star Cloud",S TV
http://hdserver.7starcloud.com:1935/stv/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG97465.png"group-title=7 Star Cloud",SAR TV
http://7starcloud.com:1935/live/sartv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG69533.png"group-title=7 Star Cloud",Shree TV
http://hdserver.7starcloud.com:1935/shree/tv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",N TV
http://7starcloud.com:1935/ntv/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG3523.png"group-title=7 Star Cloud",MK Six
http://103.199.160.85/Content/mktv6/Live/Channel(MKTV6)/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",CTN(Connor)
http://bmlive.net:8000/ctn/ctn/bms.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG49462.png"group-title=7 Star Cloud",Polimer TV
http://103.199.160.85/Content/polimer/Live/Channel(Polimer)/Stream(01)/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG90839.png"group-title=7 Star Cloud",AAKHASH TV
http://hdserver.7starcloud.com:1935/live/bmstv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG99767.png"group-title=7 Star Cloud",MADHIMUGAM TV
http://51.79.158.179:1935/madhimugamtv/madhimugamtv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG11646.png"group-title=7 Star Cloud",Prakalya TV
http://7starcloud.com:1935/pragalya/pragalyatv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",ACN TV
https://stream1.playbox.co.in:1936/babatv/babatv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG53656.png"group-title=7 Star Cloud",SR MUSIX
http://hdserver.7starcloud.com:1935/srmusix/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG66916.png"group-title=7 Star Cloud",Isai Saral
http://bmlive.net:8000/srmusix/srmusix/bms.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG26501.png"group-title=7 Star Cloud",SS TV
http://7starcloud.com:1935/live/sstv2/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG76890.png"group-title=7 Star Cloud",VAANAVIL TV
https://6n3yope4d9ok-hls-live.5centscdn.com/vaanavil/TV.stream/chunks.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG47835.png"group-title=7 Star Cloud",Sri Krishna TV
http://media.7starcloud.com:1935/erodekrishnatv/livestream/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG96815.png"group-title=7 Star Cloud",Nila TV
http://hdserver.7starcloud.com:1935/nilatv/livetv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG53779.png"group-title=7 Star Cloud",MSN TV
http://media.7starcloud.com:1935/msntv/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG74398.png"group-title=7 Star Cloud",Sri Krishna TV(T.kode)
http://7starcloud.com:1935/lotustv/lotustv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG85725.png"group-title=7 Star Cloud",Arunai Tv
http://7starcloud.com:1935/live/arunaitv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG81454.png"group-title=7 Star Cloud",News Plus TV
http://hdserver.7starcloud.com:1935/newsplus/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG26347.png"group-title=7 Star Cloud",DD PODHIGAI
https://m-c15-j2apps.s.llnwi.net/hls/0250.DDPodhigai.in.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG18927.png"group-title=7 Star Cloud",RCN TV
https://5c75277727cd1.streamlock.net:443/rcntv/rcntv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG65772.png"group-title=7 Star Cloud",GTA TAMIL TV
http://142.44.213.115:8888/gta_tamil/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG59189.png"group-title=7 Star Cloud",Captain TV
http://103.199.160.85/Content/captain/Live/Channel(Captain)/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG31950.png"group-title=7 Star Cloud",Hari TV
http://media.7starcloud.com:1935/harimedia/haritv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG6334.png"group-title=7 Star Cloud",Vaanavil Plus
http://45.79.203.234:1935/vanavil/myStream/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",Anuman TV
http://media.7starcloud.com:1935/harimedia/anumantv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",Aarya TV
http://7starcloud.com:1935/aarya/aaryatv/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG36575.png"group-title=7 Star Cloud",Udhayam TV
http://media.7starcloud.com:1935/harimedia/live3/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG2227.png"group-title=7 Star Cloud",Bass TV
http://hdserver.7starcloud.com:1935/basstv/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG93380.png"group-title=7 Star Cloud",Surya TV
http://media.7starcloud.com:1935/suryatv/mystream/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG37758.png"group-title=7 Star Cloud",TUNES 6 MUSIC
https://m-c18-j2apps.s.llnwi.net/hls/3731.Tunes6.in.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG93824.png"group-title=7 Star Cloud",Sai TV
https://streaming37.worldbbtv.com/hls/saitv.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG61964.png"group-title=7 Star Cloud",SVBC TAMIUL
https://player.mslivestream.net/tamil/ac206e74d75b285755ee4924df87d951.sdp/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",SIVAN TV
http://sivantv.livebox.co.in/sivantvhls/sivan.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG67366.png"group-title=7 Star Cloud",IBC BAKTHI
https://tx1.ibctamil.tv/CDN_IBC_Bhakthi/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",IBC SILUVAI
https://tx1.ibctamil.tv/CDN_IBC_Siluvai/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG54067.png"group-title=7 Star Cloud",Imayam TV
https://idvd.multitvsolution.com/idvo/imayamtv_540p/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG96716.png"group-title=7 Star Cloud",Chithiram TV
https://m-c049-j2apps.s.llnwi.net/hls/0614.Chithiram.in_480p/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG67748.png"group-title=7 Star Cloud",7sMusic
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG57807.png"group-title=7 Star Cloud",Isai Aruvi
http://103.199.161.254/Content/isaiaruvi/Live/Channel(IsaiAruvi)/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG93564.png"group-title=7 Star Cloud",Moon TV
https://player.mslivestream.net/mslive/e10bb900976df9177b9a080314f26f86.sdp/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG98289.png"group-title=7 Star Cloud",Vendhar TV
https://m-c06-j2apps.s.llnwi.net/hls/7077.VendarTV.in_480p/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG69759.png"group-title=7 Star Cloud",MaalaiMurasu TV
https://malaimurasucdn.purplestream.com/malaimurasu/49992ade0624eda468a31e137996d044.sdp/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG87377.png"group-title=7 Star Cloud",News 7 Tamil
https://versewsa.pc.cdn.bitgravity.com/versewsa/live/tamilnews7.smil/chunklist_b1000000.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG14345.png"group-title=7 Star Cloud",Puthiya  Thalaimurai
http://versewsa.pc.cdn.bitgravity.com/versewsa/live/puthiyathalaimurai.smil/chunklist_b1800000.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG39858.png"group-title=7 Star Cloud",Polimer News
https://versewsa.pc.cdn.bitgravity.com/versewsa/live/polimernews.smil/chunklist_b1800000.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG2121.png"group-title=7 Star Cloud",News J
https://utube.arapurayil.com/stream/UCsfh2Zb7-m4qzT8jLhK_Fzw/master.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG81475.png"group-title=7 Star Cloud",Thanthi TV
https://vidcdn.vidgyor.com/thanthi-origin/liveabr/thanthi-origin/live1/chunks.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG58239.png"group-title=7 Star Cloud",Sathiyam TV
https://utube.arapurayil.com/stream/UC2ziCMHFPWkFHjocUMXT__Q/master.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG23229.png"group-title=7 Star Cloud",Kalaignar Seithigal
https://versewsa.pc.cdn.bitgravity.com/versewsa/live//kalaignar_tv.smil/chunklist_b500000.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG78365.png"group-title=7 Star Cloud",Captain News
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG72513.png"group-title=7 Star Cloud",Jaya Plus
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG51760.png"group-title=7 Star Cloud",IBC CANADA
https://tx1.ibctamil.tv/CDN_IBC_Canada/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG43539.png"group-title=7 Star Cloud",IBC TAMIL
https://tx1.ibctamil.tv/CDN_IBC_Tamil/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG74540.png"group-title=7 Star Cloud",IBC KIDS
https://tx1.ibctamil.tv/CDN_IBC_Kids/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG18482.png"group-title=7 Star Cloud",IBC COMEDY
https://tx1.ibctamil.tv/CDN_IBC_Pakidi/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",DAN COMEDY
https://askmedia.livebox.co.in/DanComodyhls/9.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG39050.png"group-title=7 Star Cloud",IBC MUSIC
https://tx1.ibctamil.tv/CDN_IBC_Isai/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG49141.png"group-title=7 Star Cloud",SHAKTHI TV
http://88.150.197.10:1935/star-live/shakthi/chunklist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG40826.png"group-title=7 Star Cloud",TVI HD
http://live.tamilvision.tv:8081/TVI/HD/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG40000.png"group-title=7 Star Cloud",DAN NEWS
https://askmedia.livebox.co.in/DanNewshls/3.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG70178.png"group-title=7 Star Cloud",DAN TAMILOLI
https://askmedia.livebox.co.in/DANTAMILOLIhls/1.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG71898.png"group-title=7 Star Cloud",Athavan TV
http://45.77.66.224:1935/athavantv/live_360p/chunklist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",D  JEYAM TV
http://198.144.149.82:8080/NOTV/JEYAMTVCOVAI/tracks-v1a1/mono.m3u8?token=GTR
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG3887.png"group-title=7 Star Cloud",Vaigai TV
http://account9.livebox.co.in/vaigaitvhls/live.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",KING TV
http://account26.livebox.co.in/kinghls/live.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",DEEPAM TV 
http://139.99.96.85:1935/stvs/livestream2/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",V TV
http://198.144.149.82:8080/NOTV/VTV/index.m3u8?token=GTR
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",CITY TV
http://streaming.livebox.co.in/citytvhls/live.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",Nanban TV
http://hdserver.7starcloud.com:1935/nanban/live/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG51065.png"group-title=7 Star Cloud",Vaanavil Plus
https://server.iptelevision.in/hls/vanaviltv.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG36010.png"group-title=7 Star Cloud", MK TV
http://14.199.164.20:4001/play/a0lh/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",PC TV
http://pctv.livebox.co.in/pctvhls/live.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",S TV
http://139.99.96.85:1935/stvs/livestream/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG96639.png"group-title=7 Star Cloud",GTA TAMIL TV
http://142.44.213.115:8888/gta_tamil/index.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/"group-title=7 Star Cloud",Santhora Short Film
http://rtmp.santhoratv.zecast.net/santhora/santhorashortfilm/playlist.m3u8
#EXTINF:-1 tvg-id="1" tvg-logo="http://7starcloud.in/tamilcloud/uploads/images/channel_IMG15109.png"group-title=7 Star Cloud",EET TV
https://live.streamjo.com/eetlive/eettv.m3u8
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
            os.system(f'wget {url} -O temp.txt')
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
