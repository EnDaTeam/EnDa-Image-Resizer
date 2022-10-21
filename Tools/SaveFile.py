from Tools.Essentials import *

global optionsFileOptions
optionsFileOptions = """
#Please don't edit example options from the list
#There are for you to have the best quality in your photos
#Use custom option and write the size from this list.

#W - width and H - Height
#Sizes are stored in tupple >> (W,H)

Instagram:
    Ads:
        Landscape >> (1080,556)
        Square >> (1080,1080)
        Stories Ads >> (1080,1920)
    Posts:
        Landscape >> (1080,556)
        Portrait >> (1080,1350)
        Square >> (1080,1080)
    Profile:
        Profile Photo >> (320,320)
    Reels:
        Cover Photo >> (420,654)
        Video >> (1080,1920)

Twitter:
    Profile:
        Profile Photo >> (400,400)
        Header Photo >> (1500,500)
        In-stream Photo >> (1600,900)
        Card Image >> (120,120) //Minumum//
    Ads:
        Single or Multi-Photo >> (1200,670) //or larger//
        Website card Photo >> (800,800) or (800,418)
        App card Photo >> (800,800) or (800,418)
        Carousels >> (800,800) or (800,418)
        DM card >> (800,418)
        Conversion Card >> (800,418)
    
Facebook:
    Profile:
        Profile Photo >> (340,340)
        Cover Photo >> (851,315) or (1200,628)
        Post and Timeline Photo >> (1200,630)
        Stories >> (1080,1920)
    Ads:
        Feed Ads >> (1080,1080)
        Right Columns Ads >> (1080,1080)
        Instant Ads >> (1080,1080)
        Marketplace Ads >> (1080,1080)
        Search Ads >> (1080,1080)
        Sponsored Ads >> (1080,1080)
        Messager inbox and stories ads >> (1080,1080)

Linkedln:
    Profile:
        Profile Photo >> (400,400)
        Profile Cover >> (1584,396)
        Blog post Image >> (1200,627)
    Ads:
        Company logo Ads >> (100,100)
        Spotlight ads logo >> (100,100)
        Spotlight background ads >> (300,250)
        Sponsored content Photo >> (1200,627)
        Sponsored content Carousels >> (1080,1080)
    Company:
        Company logo >> (300,300)
        Page Cover >> (1128,191)
        Life tab main image >> (1128,376)
        Life tab custom module >> (502,282)
        Life tab company photo >> (900,600)
        Square logo >> (60,60)

Pinterest:
    Profile:
        Profile Photo >> (165,165)
        Profile cover Photo >> (800,450)
        Pins >> (1000,1000) or (1000,1500)
        Story >> (1080,1920)
        Fleets >> (1080,1920)
    Ads:
        App install ads >> (1000,1500)
        Carousels ads >> (1000,1500) or (1000,1000)
        Shopping ads >> (1000,1500)

Snapchat:
    Geofilter >> (600,600)
    Ads >> (1080,1920)

Youtube:
    Profile Photo >> (800,800)
    Banners >> (4096,2304)
    Video >> (1920,1080)
    Thumbnail >> (1920,1080)

Tiktok:
    Profile Photo >> (600,600)
    Video >> (1080,1920)
"""

def createfileandsave():
    file = open("Options.txt",'a')
    file.write(optionsFileOptions)
    file.close()