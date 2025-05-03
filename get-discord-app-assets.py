from urllib import request, parse
import json, os

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json'}

appid = int(input("Enter the application id: "))
asset_size = int(input("Enter the asset size (default = 1024): ") or "1024")
asset_url = f"https://discordapp.com/api/oauth2/applications/{appid}/assets"
ast = request.Request(asset_url, headers=hdr, method="GET")
with request.urlopen(ast) as f:
    asset_list = json.loads(f.read().decode('utf-8'))

os.mkdir(f"{os.getcwd()}/assets") if not os.path.exists(f"{os.getcwd()}/assets") else None
os.chdir(f"{os.getcwd()}/assets")

if type(asset_list) is list:
    for x in asset_list:
        icons = request.Request(f"https://cdn.discordapp.com/app-assets/{appid}/{x['id']}.png?size={asset_size}", headers=hdr, method="GET")
        with request.urlopen(icons) as f:
            img_bin = f.read()
        with open(f"{x['name']}.png","wb") as asset_img:
            asset_img.write(img_bin)
else:
    print("An error occured")