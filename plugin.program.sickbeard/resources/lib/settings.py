import xbmcaddon
import os
import urllib

# Hackish... not sure if there is a better way to get the API key
# Parses the HTML of the General page and pulls the API key
def GetAPIKey(ip, port):
    # Get API key from Sickbeard
    html=urllib.urlopen('http://'+ip+':'+port+'/config/general/')
    result=html.readlines()
    html.close()
    api_line = ""
    for line in result:
      if "id=\"api_key\"" in str(line):
        api_line = line
    api_index = api_line.index("value=\"")+7
    APIKey = api_line[api_index:api_index+32]
    return APIKey

# Set constants
__addon__ = xbmcaddon.Addon(id='plugin.program.sickbeard')
__ip__ = __addon__.getSetting('Sickbeard IP')
__port__= __addon__.getSetting('Sickbeard Port')
__APIKey__ = GetAPIKey(__ip__, __port__)
__url__='http://'+__ip__+':'+__port__+'/api/'+__APIKey__+'/'
