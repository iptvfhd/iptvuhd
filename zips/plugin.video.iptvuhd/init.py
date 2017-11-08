# -*- coding: utf-8 -*-
######################
#IPTV UHD
#####################



import os
import sys
import urllib
import urllib2
import shutil
import base64

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

import plugintools


art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.iptvuhd/art', ''))
MEN = "http://158.69.126.51:8000/WHDkodi/cuenta5.png"
tv = "http://158.69.126.51:8000/WHDkodi/live5.png"
estatideportes0lat = "http://158.69.126.51:8000/WHDkodi/deportes6.png"
estatisports0eng2 = "http://158.69.126.51:8000/WHDkodi/sports6.png"
estatinflgamepass2 = "http://158.69.126.51:8000/WHDkodi/nflgmpss6.png"
estatifsmlbpk2 = "http://158.69.126.51:8000/WHDkodi/fsmlbpk6.png"
estatinbapk2 = "http://158.69.126.51:8000/WHDkodi/nbapk6.png"
estatilatinofhd = "http://158.69.126.51:8000/WHDkodi/latinosfhd6.png"
estatiespanafhd = "http://158.69.126.51:8000/WHDkodi/espanafhd6.png"
estati24hrspk = "http://158.69.126.51:8000/WHDkodi/24hrsprm6.png"
estatitvabiertamx = "http://158.69.126.51:8000/WHDkodi/tvabierta6.png"
estatinoticias = "http://158.69.126.51:8000/WHDkodi/noticias6.png"
estatimundoycultura = "http://158.69.126.51:8000/WHDkodi/mundoycultura6.png"
estatiinfantil = "http://158.69.126.51:8000/WHDkodi/infantil6.png"
estatimusica = "http://158.69.126.51:8000/WHDkodi/musica6.png"
estatientretenimiento = "http://158.69.126.51:8000/WHDkodi/entretenimiento6.png"
estaticine = "http://158.69.126.51:8000/WHDkodi/cine6.png"
estatiusahd60fps = "http://158.69.126.51:8000/WHDkodi/usahd6.png"
estatiinternacionales = "http://158.69.126.51:8000/WHDkodi/internacionales6.png"
estatipr = "http://158.69.126.51:8000/WHDkodi/puertorico6.png"
estatiespana = "http://158.69.126.51:8000/WHDkodi/espana6.png"
estaticolombia = "http://158.69.126.51:8000/WHDkodi/colombia6.png"
estatiargentina = "http://158.69.126.51:8000/WHDkodi/argentina6.png"
estatiecuador = "http://158.69.126.51:8000/WHDkodi/ecuador6.png"
estatiperu = "http://158.69.126.51:8000/WHDkodi/peru6.png"
estatichile = "http://158.69.126.51:8000/WHDkodi/chile6.png"
estatihonduras = "http://158.69.126.51:8000/WHDkodi/honduras6.png"
estatiparaguay = "http://158.69.126.51:8000/WHDkodi/paraguay6.png"
can = "http://158.69.126.51:8000/addonlogos/cuenta8.jpg"
estati = "http://158.69.126.51:8000/addonlogos/estati.jpg"
estatitv = "http://158.69.126.51:8000/addonlogos/LiveTV8.jpg"
estativod = "http://158.69.126.51:8000/addonlogos/vodtvshow8.jpg"
estatimusic = "http://158.69.126.51:8000/addonlogos/estatimusic.jpg"
estatixxx = "http://158.69.126.51:8000/addonlogos/adults8.jpg"
referer = 'http://www.seriesflv.com/'
thumbnail = 'http://aldocarranza.hol.es/wp-content/uploads/2014/07/iTunes-icon-150x150.png'
lista = 'http://icon-icons.com/icons2/159/PNG/256/list_tasks_22372.png'
music = "http://158.69.126.51:8000/addonlogos/music.png"
pel = "http://158.69.126.51:8000/WHDkodi/vod5.png"
nopor = "http://158.69.126.51:8000/WHDkodi/adults5.png"
eve = "http://jvinsidercircle.com/members/images/calendar.png"
THUMBNAIL = "thumbnail"
TV_SHOWS = "tvshows"
wachusername = plugintools.get_setting("wachusername")
wachpass = plugintools.get_setting("wachpass")
morros = plugintools.get_setting("morros")
url = "http://wachtv.org:8000/enigma2.php?username=" + wachusername + "&password=" + wachpass + "&type=get_live_categories"
yea = "http://wachtv.org:8000/enigma2.php?username=" + wachusername + "&password=" + wachpass 
chifu = "&type=get_vod_streams&cat_id="
wallpaperwhddeportes7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhddeportes7.jpg"
wallpaperwhdsports7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdsports7.jpg"
wallpaperwhdnflgamepass7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdnflgamepass7.jpg"
wallpaperwhdfsmlbpack7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdfsmlbpack7.jpg"
wallpaperwhdnbapack7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdnbapack7.jpg"
wallpaperwhdlatinos7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdlatinos7.jpg"
espanoles7 = "http://158.69.126.51:8000/WHDkodi/espanoles7.jpg"
wallpaperwhd24hrspremium7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhd24hrspremium7.jpg"
usahd7 = "http://158.69.126.51:8000/WHDkodi/usahd7.jpg"
wallpaperwhdinternacionales7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdinternacionales7.jpg"
puertorico7 = "http://158.69.126.51:8000/WHDkodi/puertorico7.jpg"
wallpaperwhdcolombia7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdcolombia7.jpg"
wallpaperwhdargentina7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdargentina7.jpg"
wallpaperwhdecuador7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdecuador7.jpg"
wallpaperwhdperu7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdperu7.jpg"
chile7 = "http://158.69.126.51:8000/WHDkodi/chile7.jpg"
wallpaperwhdhonduras7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdhonduras7.jpg"
wallpaperwhdparaguay7 = "http://158.69.126.51:8000/WHDkodi/wallpaperwhdparaguay7.jpg"



def run():
    plugintools.log("wachtv.run")
    params = plugintools.get_params()
    if params.get("action") is None:
        xtv(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()
	
	
def xtv(params):
  xtvmaster = plugintools.get_setting("xtvmaster")
  

  if xtvmaster == 'false':
   plugintools.message("IPTV UHD","Ingresar Usuario/Contraseña")
   plugintools.open_settings_dialog()
  else:
        data = plugintools.read(url + "0")
        if "<items>" in data:
           main_list(params)
        elif "" in data:
           xbmc.executebuiltin("Notification(%s,%s,%s,%s)" % ('IPTV UHD', "Usuario o Contraseña Incorrecta......", 10 , art+'b.png')) 
           plugintools.open_settings_dialog()

def main_list(params):
    plugintools.log("wachtv.main_list "+repr(params))
    plugintools.set_view(THUMBNAIL)
    plugintools.add_item( 
        action = "cuenta", 
        title = "Cuenta / Account",
        thumbnail = MEN,
        fanart = can,
        folder = False )
    plugintools.add_item( 
        action = "perro2", 
        title = "TV en Vivo / Live TV",
        thumbnail = tv,
        fanart = estatitv,
        url = url,
        folder = True )
    plugintools.add_item( 
        action = "perro3", 
        title = "Peliculas Y Series / VOD",
        thumbnail = pel,
        fanart = estativod,
        url = yea + "&type=get_vod_categories",
        folder = True )


    if morros == "true" :
	plugintools.add_item( 
        action = "perro", 
        title = "Solo Adultos / Adults Only",
        url = "http://wachtv.org:8000/enigma2.php?username=" + wachusername + "&password=" + wachpass + "&type=get_live_streams&cat_id=" + "41",
        thumbnail = nopor,
        fanart = estatixxx,
        folder = True )
	
	
def parse3(params):
    plugintools.log("parse "+repr(params))
    plugintools.set_view(THUMBNAIL)
    plugintools.add_item( 
        action = "perro", 
        title = "SERIES",
        url = yea + chifu + "33",
        thumbnail = music,
        folder = True )
    plugintools.add_item(
        action = "search5",
        title = "PELICULAS",
        thumbnail = music,
        folder = True )
		
#http://usa.01.cdnstreams.in:6034/viewsa/ch20q1.stream/playlist.m3u8?
		
		
def perro(params):
    plugintools.set_view(TV_SHOWS)
    url = params.get("url")
    data = plugintools.read(url)
    
    SongLists = plugintools.find_multiple_matches(data, '<channel>(.*?)</channel>')
    for entry in SongLists:
            ima = plugintools.find_single_match(entry, '<desc_image>([^"]+)</desc_image>')
            ima = ima.replace("<![CDATA[", "")
            ima = ima.replace("]]>", "")
            titulo = plugintools.find_single_match(entry, '<title>([^"]+)</title>')
            titulo = base64.b64decode(titulo)
            titulo = titulo.upper()
            titulo = titulo.replace("PARENT-CODE=\"6666\"","")
            description = plugintools.find_single_match(entry, '<description>([^"]+)</description>')
            description = base64.b64decode(description)
            playstation = plugintools.find_single_match(entry, '<stream_url>([^"]+)</stream_url>')
            playstation = playstation.replace("<![CDATA[", "")
            playstation = playstation.replace("]]>", "")
            #playstation = playstation.replace(".ts", ".m3u8")
            plugintools.add_item(action="play", title = titulo , plot = description , url = playstation , thumbnail = ima , fanart = ima , info_labels = None , folder = False, isPlayable = True)


def perro2(params):
    plugintools.set_view(THUMBNAIL)
    url = params.get("url")
    data = plugintools.read(url)
    
    SongLists = plugintools.find_multiple_matches(data, '<channel>(.*?)</channel>')
    for entry in SongLists:
     ima = plugintools.find_single_match(entry, '<desc_image>([^"]+)</desc_image>')
     ima = ima.replace("<![CDATA[", "")
     ima = ima.replace("]]>", "")
     playstation = plugintools.find_single_match(entry, '<playlist_url>([^"]+)</playlist_url>')
     playstation = playstation.replace("<![CDATA[", "")
     playstation = playstation.replace("]]>", "")
     titulo = plugintools.find_single_match(entry, '<title>([^"]+)</title>')
     titulo = base64.b64decode(titulo)
     titulo = titulo.upper()
     if titulo.find("DEPORTES") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatideportes0lat , fanart = wallpaperwhddeportes7 , folder = True)
     if titulo.find("SPORTS") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatisports0eng2 , fanart = wallpaperwhdsports7 , folder = True)
     if titulo.find("NFL GAME PASS") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatinflgamepass2 , fanart = wallpaperwhdnflgamepass7 , folder = True)
     if titulo.find("FS / MLB PACK") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatifsmlbpk2 , fanart = wallpaperwhdfsmlbpack7 , folder = True)
     if titulo.find("NBA PACK") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatinbapk2 , fanart = wallpaperwhdnbapack7 , folder = True)
     if titulo.find("LATINOS FHD") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatilatinofhd , fanart = wallpaperwhdlatinos7 , folder = True)
     if titulo.find("ESPAÑA FHD") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatiespanafhd , fanart = espanoles7 , folder = True)
     if titulo.find("24/7 PREMIUM") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estati24hrspk , fanart = wallpaperwhd24hrspremium7 , folder = True)
     if titulo.find("TV ABIERTA") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatitvabiertamx , fanart = wallpaperwhdlatinos7 , folder = True)
     if titulo.find("NOTICIAS") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatinoticias , fanart = wallpaperwhdlatinos7 , folder = True)
     if titulo.find("MUNDO Y CULTURA") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatimundoycultura , fanart = wallpaperwhdlatinos7 , folder = True)
     if titulo.find("INFANTIL") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatiinfantil , fanart = wallpaperwhdlatinos7 , folder = True)
     if titulo.find("MUSICA") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatimusica , fanart = wallpaperwhdlatinos7 , folder = True)
     if titulo.find("ENTRETENIMIENTO") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatientretenimiento , fanart = wallpaperwhdlatinos7 , folder = True)
     if titulo.find("CINE") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estaticine , fanart = wallpaperwhdlatinos7 , folder = True)
     if titulo.find("USA HD") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatiusahd60fps , fanart = usahd7 , folder = True)
     if titulo.find("INTERNACIONALES") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatiinternacionales , fanart = wallpaperwhdinternacionales7 , folder = True)
     if titulo.find("PUERTO RICO") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatipr , fanart = puertorico7 , folder = True)
     if titulo.find("ESPANA") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatiespana , fanart = espanoles7 , folder = True)
     if titulo.find("COLOMBIA") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estaticolombia , fanart = wallpaperwhdcolombia7 , folder = True)
     if titulo.find("ARGENTINA") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatiargentina , fanart = wallpaperwhdargentina7 , folder = True)
     if titulo.find("ECUADOR") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatiecuador , fanart = wallpaperwhdecuador7 , folder = True)
     if titulo.find("PERU") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatiperu , fanart = wallpaperwhdperu7 , folder = True)
     if titulo.find("CHILE") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatichile , fanart = chile7 , folder = True)
     if titulo.find("HONDURAS") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatihonduras , fanart = wallpaperwhdhonduras7 , folder = True)		
     if titulo.find("PARAGUAY") >= 0:
        plugintools.add_item(action="perro", title = titulo , url = playstation , thumbnail = estatiparaguay , fanart = wallpaperwhdparaguay7 , folder = True)
	 	
#SOLO MEXICO		
		 
def perro3(params):
    plugintools.set_view(TV_SHOWS)
    url = params.get("url")
    data = plugintools.read(url)
    
    SongLists = plugintools.find_multiple_matches(data, '<channel>(.*?)</channel>')
    for entry in SongLists:
        ima = plugintools.find_single_match(entry, '<desc_image>([^"]+)</desc_image>')
        ima = ima.replace("<![CDATA[", "")
        ima = ima.replace("]]>", "")
        titulo = plugintools.find_single_match(entry, '<title>([^"]+)</title>')
        titulo = base64.b64decode(titulo)
        titulo = titulo.upper()
        titulo = titulo.replace("PARENT-CODE=\"6666\",","")
        description = plugintools.find_single_match(entry, '<description>([^"]+)</description>')
        description = base64.b64decode(description)
        playstation = plugintools.find_single_match(entry, '<playlist_url>([^"]+)</playlist_url>')
        playstation = playstation.replace("<![CDATA[", "")
        playstation = playstation.replace("]]>", "")
        if playstation.find("get_vod_scategories") >= 0:
            plugintools.add_item(action="perro5", title = titulo + " " + '[COLOR blue][SERIES][/COLOR]', plot = description , url = playstation , thumbnail = ima , fanart = ima , info_labels = None , folder = True, isPlayable = False)
        if playstation.find("get_vod_streams") >= 0:
            plugintools.add_item(action="perro4", title = titulo, plot = description , url = playstation , thumbnail = ima , fanart = ima , info_labels = None , folder = True, isPlayable = False)			
			

def perro5(params):
    plugintools.set_view(TV_SHOWS)
    url = params.get("url")
    data = plugintools.read(url)
    
    SongLists = plugintools.find_multiple_matches(data, '<channel>(.*?)</channel>')
    for entry in SongLists:
            ima2 = plugintools.find_single_match(entry, '<desc_image>([^"]+)</desc_image>')
            ima2 = ima2.replace("<![CDATA[", "")
            ima2 = ima2.replace("]]>", "")
            titulo2 = plugintools.find_single_match(entry, '<title>([^"]+)</title>')
            titulo2 = base64.b64decode(titulo2)
            titulo2 = titulo2.upper()
            titulo2 = titulo2.replace("PARENT-CODE=\"6666\",","")
            description2 = plugintools.find_single_match(entry, '<description>([^"]+)</description>')
            description2 = base64.b64decode(description2)
            playstation2 = plugintools.find_single_match(entry, '<playlist_url>([^"]+)</playlist_url>')
            playstation2 = playstation2.replace("<![CDATA[", "")
            playstation2 = playstation2.replace("]]>", "")
            plugintools.add_item(action="perro4", title = titulo2 , plot = description2 , url = playstation2 , thumbnail = ima2 , fanart = ima2 , info_labels = None , folder = True, isPlayable = True)			

	 

	 
	 
	 
def cuenta(params):
    url_getlink = 'http://wachtv.org:8000/panel_api.php?username=' + wachusername + "&password=" + wachpass
    request_headers=[]
    request_headers.append(["User-Agent","Kodi plugin by MikkM"])
    body,response_headers = plugintools.read_body_and_headers(url_getlink, headers=request_headers)
    datos = plugintools.find_multiple_matches(body, '"user_info":(.*?)"server_info"')
    for entry in datos:
     ima = plugintools.find_single_match(entry, '"username":"([^"]+)"')
     ma = plugintools.find_single_match(entry, '"password":"([^"]+)"')
     esta = plugintools.find_single_match(entry, '"status":"([^"]+)"')
     ven = plugintools.find_single_match(entry, '"exp_date":"([^"]+)"')
     dialog = xbmcgui.Dialog()
     selector = dialog.select('IPTV UHD', ['# VER USERNAME Y PASSWORD' , '# VERIFICAR STATUS Y FECHA DE VENCIMIENTO' ])
    if selector == 0:
        plugintools.message("IPTV UHD INFORMA" , "USERNAME:" + ima , "PASSWORD:" + ma  )
    if selector == 1:
        plugintools.message("IPTV UHD INFORMA" , "STATUS:" + esta , "FECHA DE VENCIMIENTO:" + ven )

	
def play2(params):
    plugintools.set_view(THUMBNAIL)
    url = params.get("url")
    plugintools.play_resolved_url(url)


def play(params):
    plugintools.set_view(TV_SHOWS)
    url = params.get("url")
    plugintools.play_resolved_url(url)
	
	
	
	
def perro4(params):
    plugintools.set_view(TV_SHOWS)
    url = params.get("url")
    data = plugintools.read(url)
    
    SongLists = plugintools.find_multiple_matches(data, '<channel>(.*?)</channel>')
    for entry in SongLists:
            ima2 = plugintools.find_single_match(entry, '<desc_image>([^"]+)</desc_image>')
            ima2 = ima2.replace("<![CDATA[", "")
            ima2 = ima2.replace("]]>", "")
            titulo2 = plugintools.find_single_match(entry, '<title>([^"]+)</title>')
            titulo2 = base64.b64decode(titulo2)
            titulo2 = titulo2.upper()
            titulo2 = titulo2.replace("PARENT-CODE=\"6666\",","")
            description2 = plugintools.find_single_match(entry, '<description>([^"]+)</description>')
            description2 = base64.b64decode(description2)
            playstation2 = plugintools.find_single_match(entry, '<stream_url>([^"]+)</stream_url>')
            playstation2 = playstation2.replace("<![CDATA[", "")
            playstation2 = playstation2.replace("]]>", "")
            plugintools.add_item(action="play", title = titulo2 , plot = description2 , url = playstation2 , thumbnail = ima2 , fanart = ima2 , info_labels = None , folder = False, isPlayable = True)
	

def gethttp_referer_headers(url,referer):    
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    request_headers.append(["Referer", referer])    
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    return body

def wachexpant(params):
    #plugintools.log('[%s %s].xtvexpant %s' % (addonName, addonVersion, repr(params)))
    url = params.get("url")
    url_getlink = 'http://wheredoesthislinkgo.com'
    plugintools.log("url_getlink= "+url_getlink)
    post = 'ShortenedUri=' + url
    post = post.replace('&', "%26")
    plugintools.log("post= "+post)
    data,response_headers = plugintools.read_body_and_headers(url_getlink, post=post)
    longurl = plugintools.find_single_match(data, 'expands to <a href="(.*?)">')
    plugintools.log("longurl "+longurl)
    plugintools.play_resolved_url(longurl)	

def americanos(params):
    plugintools.set_view(TV_SHOWS)
    url = params.get("url")
    data = plugintools.read(url)
    
    SongLists = plugintools.find_multiple_matches(data, '<channel>(.*?)</channel>')
    for entry in SongLists:
            ima = plugintools.find_single_match(entry, '<desc_image>([^"]+)</desc_image>')
            ima = ima.replace("<![CDATA[", "")
            ima = ima.replace("]]>", "")
            titulo = plugintools.find_single_match(entry, '<title>([^"]+)</title>')
            titulo = base64.b64decode(titulo)
            titulo = titulo.upper()
            titulo = titulo.replace("PARENT-CODE=\"6666\"","")
            description = plugintools.find_single_match(entry, '<description>([^"]+)</description>')
            description = base64.b64decode(description)
            playstation = plugintools.find_single_match(entry, '<stream_url>([^"]+)</stream_url>')
            playstation = playstation.replace("<![CDATA[", "")
            playstation = playstation.replace("]]>", "")
            plugintools.add_item(action="wachexpant", title = titulo , plot = description , url = playstation , thumbnail = ima , fanart = ima , info_labels = None , folder = False, isPlayable = True)	
		
run()