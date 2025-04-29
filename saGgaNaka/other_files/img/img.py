from PIL import Image
import shubhlipi as sh

root = sh.env("sthAnam") + "\\saGgaNakAnuprayogaH"
image = {
    "about.png": (25, 25),
    "github.png": (24, 24),
    "lang.png": (26, 24),
    "on1.png": (32, 18),
    "off1.png": (32, 18),
    "on.png": (51, 29),
    "off.png": (51, 29),
    "main.png": (20, 20),
    "convert.png": (24, 24),
    "usage.png": (24, 24),
    "menu.png": (32, 32),
    "add.png": (15, 15),
    "minimize.png": (20, 20),
    "maximize.png": (20, 20),
    "drag.png": (20, 20),
    "down-arrow.png": (20, 20),
    "up-arrow.png": (20, 20),
    "close.png": (20, 20),
    "quit.png": (20, 20),
    "restart.png": (20, 20),
}
for x in image:
    im = Image.open(f"{root}\\other_files\\img\\moolam\\" + x)
    # resized_im = im.resize(image[x])
    # im.save(f"{root}\\other_files\\img\\prayogan\\" + x)
    im.save(f"{root}\\src\\resources\\img\\" + x[:-4] + ".png")
    # file = open(f"{root}\\other_files\\img\\prayogan\\" + x, mode="rb+")
    # data = "data:image/png;base64," + base64.b64encode(file.read()).decode("ascii")
    # file.close()
    # file = open(f"{root}\\other_files\\img\\prayogan\\base64\\" + x + ".txt", mode="w+")
    # file.write(data)
    # file.close()
