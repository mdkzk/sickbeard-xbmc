import xbmcaddon
import os
import urllib
import urllib2
import xbmcgui

# Hackish... not sure if there is a better way to get the API key
# Parses the HTML of the General page and pulls the API key
def GetAPIKey(ip, port, username, password):
    # Get API key from Sickbeard
    baseurl = "http://" + ip + ":" + port
    if username and password:
        password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        url = "http://" + ip + ":" + port+ '/config/general/'
        password_manager.add_password(None, url, username, password)
        authhandler = urllib2.HTTPBasicAuthHandler(password_manager)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        result = urllib2.urlopen(req)
        result = result.readlines()
    else:    
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
__username__ = __addon__.getSetting('Sickbeard Username')
__password__= __addon__.getSetting('Sickbeard Password')

try:
    __APIKey__ = GetAPIKey(__ip__, __port__, __username__,__password__)
except:
    dialog = xbmcgui.Dialog()
    dialog.ok("Sickbeard Error", "Check Username and Password Settings")
    sys.exit()

__url__='http://'+__ip__+':'+__port__+'/api/'+__APIKey__+'/'
