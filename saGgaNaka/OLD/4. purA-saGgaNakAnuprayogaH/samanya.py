import eel

eel.init("resources")
try:
    eel.start("index.html",port=2345,position=(0,0),size=(1250,700))
except OSError:
    try:
        eel.start("index.html", mode="edge",port=2345,position=(0,0),size=(1250,700))
    except:
        eel.start("index.html", mode="default",port=2345,position=(0,0),size=(1250,700))
