import requests
import os

appid = int(input("Enter the application id: "))
asset_size = int(input("Enter the asset size (default = 1024): ") or "1024")
asset_url = f"https://discordapp.com/api/oauth2/applications/{appid}/assets"
asset_list = requests.get(asset_url).json()

os.mkdir(f"{os.getcwd()}/assets") if not os.path.exists(f"{os.getcwd()}/assets") else None
os.chdir(f"{os.getcwd()}/assets")

if type(asset_list) is list:
    for x in asset_list:
        img_bin = requests.get(f"https://cdn.discordapp.com/app-assets/{appid}/{x['id']}.png?size={asset_size}").content
        with open(f"{x['name']}.png","wb") as asset_img:
            asset_img.write(img_bin)
    print(f"Files downloaded to {os.getcwd()}")
else:
    print(f"{asset_list['application_id']} This usually means that the application id is invaild.")