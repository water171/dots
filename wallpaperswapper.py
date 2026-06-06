import subprocess
from simple_term_menu import TerminalMenu

WALLPAPER_DIR = "/home/sam/wallpapers"

def select_wallpaper():
    wallpapers = subprocess.check_output(["ls", WALLPAPER_DIR]).decode().splitlines()
    selector = TerminalMenu(wallpapers)
    select_wallpaper = selector.show()
    if select_wallpaper is not None:
        selected_wallpaper = wallpapers[select_wallpaper]
        subprocess.call(["matugen", "image", selected_wallpaper], cwd=WALLPAPER_DIR)
        subprocess.call(["swww", "img", selected_wallpaper], cwd=WALLPAPER_DIR)

def show_help():
    print("\n1 - change wallpaper")
    print("2 - preview a wallpaper")
    print("help - print this")

def preview_wallpaper():
    wallpapers = subprocess.check_output(["ls", WALLPAPER_DIR]).decode().splitlines()
    seletor = TerminalMenu(wallpapers)
    select_wallpaper = seletor.show()
    if select_wallpaper is not None:
        subprocess.call(["feh", "--fullscreen", wallpapers[select_wallpaper]], cwd=WALLPAPER_DIR)        

if __name__ == "__main__":
    number = input("what to do? ").lower()
    if number == "1":
        select_wallpaper()
    elif number == "2":
        preview_wallpaper()
    elif number == "help":
        show_help()
    else:
        print("invalid input")
