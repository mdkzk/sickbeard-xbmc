import sickbeard
import sys
import urllib
import xbmcplugin
import xbmcgui

Sickbeard = sickbeard.SB()

# Get the tvdbid and show names 
def GetShowInfo():
    show_ids = Sickbeard.GetShowIds()
    show_info = Sickbeard.GetShowInfo(show_ids)

    show_names = []
    for name, tvdbid in sorted(show_info.iteritems()):
      show_names.append([name, str(tvdbid), Sickbeard.GetShowPoster(tvdbid)])
      
    return show_names

# Parse through shows and add dirs for each
def menu():
      show_info = GetShowInfo()
      show_total = len(show_info)
      context_menu_items = [('Add Show', 'XBMC.RunScript(special://home/addons/plugin.program.sickbeard/resources/lib/addshow.py)'),('Refresh Shows', 'xbmc.executebuiltin("Container.Refresh")')]
      for show_name, tvdbid, thumbnail_path in show_info:
        addShowDirectory(show_name, tvdbid, 4, thumbnail_path, show_total, context_menu_items)

# Add directory item
def addShowDirectory(show_name, tvdbid, menu_number, thumbnail_path, show_total, context_menu_items):
    return_url = sys.argv[0]+"?url="+urllib.quote_plus(str(tvdbid))+"&mode="+str(menu_number)+"&name="+urllib.quote_plus(show_name)
    list_item = xbmcgui.ListItem(show_name, thumbnailImage=thumbnail_path)
    list_item.addContextMenuItems(context_menu_items)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=return_url, listitem=list_item, isFolder=True, totalItems=show_total)  
