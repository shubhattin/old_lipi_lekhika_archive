import eel
from pratidarshan import alert

eel.init("assets")
try:
    eel.start("index.html",port=2345,position=(0,0),size=(1250,700))
except OSError:
    alert("Chrome Not Installed,So opening in Another Browser.", lapse=4000,geo=True)
    try:
        eel.start("index.html", mode="edge",port=2345,position=(0,0),size=(1250,700))
    except:
        eel.start("index.html", mode="default",port=2345,position=(0,0),size=(1250,700))
