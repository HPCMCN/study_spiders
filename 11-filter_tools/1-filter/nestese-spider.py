import requests
import requests
mp = requests.get("http://m8c.music.126.net/20180923223804/0cadaaebca67e3c280b1a921e8ae016d/ymusic/cf01/1c1e/520e/9a7b530eccda635dc482fd5e0737a6bd.mp3", headers={"Host": "m8c.music.126.net", "Accept": "*/*"})
with open("xxx.mp3", "wb") as f:
    f.write(mp.content)
import requests
url = "http://vodkgeyttp8.vod.126.net/cloudmusic/JCAwJCQgMDZkMDIwMCAkMA==/mv/5965411/594d17287e43934d3bb47f15eb414062.mp4?wsSecret=0a5f537802bf1c1d504c862fd2d8dfbd&wsTime=1537713357"
headers = {
"Host": "vodkgeyttp8.vod.126.net",
"Connection": "keep-alive",
"Accept": "*/*",
"Accept-Encoding": "identity;q=1, *;q=0",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.157 Safari/537.36",
"Accept-Language": "en-us,en;q=0.8",
"Range": "bytes=0-"}
avi = requests.get(url, headers=headers)
with open("xxx.mp4", "wb") as f:
    f.write(avi.content)