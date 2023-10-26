import eel
import pystray, PIL.Image
eel.init("web")
image = PIL.Image.open("logo.png")  
def on_click(icon, item):
    eel.start("main.html", size=(350, 500))
    
icon = pystray.Icon("Vodka vpn", image, menu = pystray.Menu(pystray.MenuItem("Вызвать меню", on_click, default=True)))

