import json
import os
import re
import select
from tkinter import *
import argparse
import logging
from pprint import pprint
from PIL import Image, ImageDraw, ImageTk
import pyglet


PAGER_SCREEN_WIDTH = 480
PAGER_SCREEN_HEIGHT = 222

BATTERY = "charged"
VOLUME = "medium"
BRIGHTNESS = "100"
VIBRATE = "on"

# TODO: add buttons for: navigation, reloading theme, exiting tool, toggling debug output
# TODO: add gui for selecting theme path if not provided as argument



# Set up logging
logger = logging.getLogger("theme_test")

def main():
    global menu_target, selected_menu_item, selected_page, button_map, canvas_screen, menu, menu_items, pages, palette, a_button, b_button, up_button, down_button, left_button, right_button, menus, menu_path, status_bars, menu
    
    pyglet.font.add_file("tests/fonts/DejaVuSans.ttf")
    
    menu_target = "dashboard_path"
    menu_path = [menu_target]
    
    parser = argparse.ArgumentParser(description="Test Theme Tool")
    
    # Argument that need to be provided
    parser.add_argument("--theme", type=str, required=True, help="Location of the base directory of the theme to test")
    
    # Argument that can be provided but have defaults
    parser.add_argument("--menu-target", "-i", type=str, default=menu_target, help="Target of the menu to load initially (default: dashboard_path)")
    
    # Debug argument
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output for debugging")
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug mode")
    
    
    args = parser.parse_args()
    
    menu_target = args.menu_target
    if menu_target not in menu_path:
        menu_path.append(menu_target)
    menu_items = []
    pages = []
    
    selected_menu_item = 0
    selected_page = 0
    
    button_map = {}
    
    # Configure logging
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        logger.debug("Debug mode enabled")
    elif args.verbose:
        logging.basicConfig(level=logging.INFO)
        logger.info("Verbose mode enabled")
    else:
        logging.basicConfig(level=logging.WARNING)
    
    logger.info(f"Testing theme located at: {args.theme}")
    
    # Initialize Tkinter root
    logger.debug("Initializing Tkinter root window")
    root = Tk()
    root.title("Theme Test Tool")
    root.geometry(f"{PAGER_SCREEN_WIDTH}x{PAGER_SCREEN_HEIGHT+85}")  # Extra space for buttons below the screen
    
    # Bind Ctrl+C to exit
    def on_ctrl_c(event):
        logger.info("Ctrl+C pressed, exiting...")
        root.quit()
    
    root.bind('<Control-c>', on_ctrl_c)
    
    canvas_screen = Canvas(root, width=PAGER_SCREEN_WIDTH, height=PAGER_SCREEN_HEIGHT, bg="black")
    canvas_screen.pack()
    canvas_screen.create_rectangle(0, 0, PAGER_SCREEN_WIDTH, PAGER_SCREEN_HEIGHT, fill="blue")
    
    
    # Pager navigation buttons
    a_button = Button(root, text="A")           # Accept/Select
    b_button = Button(root, text="B")           # Back/Cancel
    up_button = Button(root, text="Up")         # Up
    down_button = Button(root, text="Down")     # Down
    left_button = Button(root, text="Left")     # Left
    right_button = Button(root, text="Right")   # Right
    
    b_button.place(x=50, y=32.5+PAGER_SCREEN_HEIGHT, width=50, height=20)
    a_button.place(x=110, y=32.5+PAGER_SCREEN_HEIGHT, width=50, height=20)
    
    left_button.place(x=210, y=20+PAGER_SCREEN_HEIGHT, width=50, height=45)
    up_button.place(x=265, y=20+PAGER_SCREEN_HEIGHT, width=50, height=20)
    right_button.place(x=320, y=20+PAGER_SCREEN_HEIGHT, width=50, height=45)
    down_button.place(x=265, y=45+PAGER_SCREEN_HEIGHT, width=50, height=20)
    
    
    # functions for buttons
    def on_a_button():
        logger.info("A button pressed. \t It is mapped to: " + button_map['a'])
        use_button_map('a')
    
    def on_b_button():
        logger.info("B button pressed. \t It is mapped to: " + button_map['b'])
        use_button_map('b')

    
    def on_up_button():
        logger.info("Up button pressed. \t It is mapped to: " + button_map['up'])
        use_button_map('up')
    
    def on_down_button():
        logger.info("Down button pressed. \t It is mapped to: " + button_map['down'])
        use_button_map('down')
    
    def on_left_button():
        logger.info("Left button pressed. \t It is mapped to: " + button_map['left'])
        use_button_map('left')
    
    def on_right_button():
        logger.info("Right button pressed. \t It is mapped to: " + button_map['right'])
        use_button_map('right')
    
    # assign functions to buttons
    a_button.config(command=on_a_button)
    b_button.config(command=on_b_button)
    up_button.config(command=on_up_button)
    down_button.config(command=on_down_button)
    left_button.config(command=on_left_button)
    right_button.config(command=on_right_button)

    # reload button
    reload_button = Button(root, text="Reload Theme")
    reload_button.place(x=400, y=32.5+PAGER_SCREEN_HEIGHT, width=75, height=20)
    def on_reload():
        logger.info("Reloading theme...")
        try:
            theme_data = load_theme(args.theme)
            menus = create_menus(theme_data, args.theme)
            status_bars = create_status_bars(theme_data, args.theme)
            if menus:
                load_menu()
                logger.info("Theme reloaded and menu rendered.")
            else:
                logger.warning("No menus found in theme data after reload.")
        except Exception as e:
            logger.error(f"Failed to reload theme: {e}")
    reload_button.config(command=on_reload)
    


    # Load theme
    logger.debug("Loading theme")
    try:
        logger.debug(f"Loading theme from path: {args.theme}")
        theme_data = load_theme(args.theme)
        logger.debug("Theme data:")
        #pprint(theme_data)
        logger.info(f"Theme '{args.theme}' loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to load theme: {e}")
        return
    
    # Create menus from theme data
    menus = create_menus(theme_data, args.theme)
    status_bars = create_status_bars(theme_data, args.theme)
    logger.info(f"Created {len(menus)} menus from theme data.")
    logger.info(f"Created menus: {list(menus.keys())}")
    
    if menus:
        if menu_target in list(menus.keys()):
            logger.info(f"Loading menu {menus[menu_target].menu_data['screen_name']}")
            menu = menus[menu_target]
        elif f'{menu_target}_path' in list(menus.keys()):
            menu_target = menu_target + '_path'
            menu = menus[menu_target]
            logger.info(f"Loading menu {menus[menu_target].menu_data['screen_name']}")
        else:
            logger.error(f"Couldn't find menu target '{menu_target}' in menus.")
            logger.error(f"Available menus: {list(menus.keys())}")
            return
            
        load_menu()
        print(button_map) # TODO: remove
    else:
        logger.warning("No menus found in theme data to render")
    
    logger.info("Starting the Theme Test Tool GUI")
    root.mainloop()
    logger.info("Exiting the Theme Test Tool")
    

def load_theme(theme_path):
    global palette
    # first get the theme.json file form the root of the theme path
    theme_file = os.path.join(theme_path, "theme.json")
    # check if the file exists
    if not os.path.isfile(theme_file):
        raise FileNotFoundError(f"Theme file not found: {theme_file}")
    # load the theme file and convert it to a dictionary
    import json
    with open(theme_file, 'r', encoding='utf-8') as f:
        theme_data_raw = json.load(f)
    
    # Expand paths relative to the theme root so values like "assets/..." work
    theme_data = expand_dict(theme_data_raw, base_path=theme_path)
    '''if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Expanded theme data:")
        pprint(theme_data)'''
    
    palette = theme_data.get('color_palette', {})
    logger.debug(f"Loaded color palette: {palette}")
    
    return theme_data

# Expand dictionaries recursively
def expand_dict(d: dict, base_path: str):
    """Recursively expand dict values that point to files/dirs relative to base_path."""
    logger.debug(f"Expanding dictionary: {d}")
    for key, value in d.items():
        logger.debug(f"Processing key: {key}, value: {value}")

        # Try to resolve strings as paths relative to the theme root
        if isinstance(value, str):
            candidate = value if os.path.isabs(value) else os.path.normpath(os.path.join(base_path, value))

            logger.debug(f"Resolved candidate path for key '{key}': {candidate}")
            
            if os.path.isfile(candidate):
                logger.debug(f"Resolved file for key '{key}': {candidate}")
                if candidate.endswith('.json'):
                    logger.debug(f"Loading JSON file for key '{key}': {candidate}")
                    with open(candidate, 'r', encoding='utf-8') as f:
                        loaded = json.load(f)
                    d[key] = expand_dict(loaded, base_path)
                else:
                    logger.debug(f"Assigning file path for key '{key}': {candidate}")
                    d[key] = candidate
                continue
            
            if os.path.isdir(candidate):
                logger.debug(f"Resolved directory for key '{key}': {candidate}")
                d[key] = candidate
                continue
            
            logger.debug(f"No file or directory found for key '{key}', keeping original value")

        if isinstance(value, dict):
            logger.debug(f"Expanding dictionary for key: {key}")
            d[key] = expand_dict(value, base_path)
        elif isinstance(value, list):
            logger.debug(f"\u001b[41mEntering list for key: {key}\u001b[0m")
            d[key] = enter_lists(value, base_path)
        else:
            logger.debug(f"Did nothing for key: {key}, value: {value}")
            d[key] = d[key]
    return d

# Enter Lists in dictionaries
def enter_lists(d: list, base_path: str):
    for i in range(len(d)):
        value = d[i]
        if isinstance(value, dict):
            d[i] = expand_dict(value, base_path)
        elif isinstance(value, list):
            d[i] = enter_lists(value, base_path)
        elif isinstance(value, str):
            candidate = value if os.path.isabs(value) else os.path.normpath(os.path.join(base_path, value))
            if os.path.isfile(candidate):
                d[i] = candidate
            elif os.path.isdir(candidate):
                d[i] = candidate
            else:
                d[i] = value
        else:
            d[i] = value

    return d

# Renders the menu on the screen in the frame
def render_menu(menu_data):
    global canvas_screen,selected_page, menu_items, pages
    logger.debug(f"Rendering menu: {menu_data.get('screen_name', 'Unnamed')}")
    
    # For now, just clear the screen and write the menu title
    canvas_screen.delete("all")
    
    # Initialize image list to keep references
    canvas_screen.images = []
    
    background = menu_data['background']
    if 'background_color' in background.keys():
        background_color = background['background_color'] # returns a dict with r,g,b keys 
        # convert to hex color
        background_color = f"#{background_color['r']:02x}{background_color['g']:02x}{background_color['b']:02x}"
        logger.debug(f"Using background color: {background_color}")
        canvas_screen.create_rectangle(0, 0, PAGER_SCREEN_WIDTH, PAGER_SCREEN_HEIGHT, fill=background_color)

    if 'layers' in background.keys():
        layers: list = background['layers']
        for layer in layers:
            if 'image_path' in layer.keys():
                image_path = layer['image_path']
                if os.path.isfile(image_path):
                    logger.debug(f"Loading background layer image from path: {image_path}")
                    image = PhotoImage(file=image_path)
                    canvas_screen.create_image(layer['x'], layer['y'], anchor=NW, image=image)
                    # Keep a reference to all images to prevent garbage collection
                    canvas_screen.images.append(image)
                else:
                    logger.warning(f"Background layer image file not found: {image_path}")
    if 'title' in menu_data:
        canvas_screen.create_text(PAGER_SCREEN_WIDTH//2, 20, text=menu_data['title'], fill="white", font=("Arial", 16))
    # Render menu items
    if 'items' in menu_data:
        for index, item in enumerate(menu_data['items']):
            y_position = 50 + index * 30
            canvas_screen.create_text(20, y_position, text=item.get('label', 'Unnamed'), anchor='w', fill="white", font=("Arial", 12))

# create menus based on theme data and returns a list of generic_menu objects
def create_menus(theme_data, theme_path) -> list:
    menus = {}
    #pprint(list(theme_data.keys()))
    #pprint(theme_data)
    for key, value in theme_data.items():
        if key == "color_palette":
            continue  # skip color_palette key
        if key == "status_bars":
            continue  # skip status_bars key
        # Check if the value is already a loaded menu dictionary (has screen_name)
        if isinstance(value, dict) and 'screen_name' in value:
            menu = generic_menu(value, theme_path)
            menus[key] = menu
            '''if 'screen_name' in menu.menu_data:
                menus[menu.menu_data['screen_name']] = menu
            else:
                menus[key] = menu'''
            logger.debug(f"Created menu from key: {key}")
        
        # if the value is a dictionary, check if it has nested menu dictionaries
        elif isinstance(value, dict):
            if key.endswith('_path'):
                menu = generic_menu(value, theme_path)
                menus[key] = menu
                logger.debug(f"Created menu from path in key: {key}")
            else:
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, dict) and 'screen_name' in sub_value:
                        menu = generic_menu(sub_value, theme_path)
                        menus[sub_key] = menu
                        logger.debug(f"Created menu from sub-key: {sub_key} in key: {key}")
        elif isinstance(value, str):
            logger.info(f"Processing string value for key: {key} with value: {value}")
            # check if the value is a path to a menu json file
            if not key.endswith('_path'):
                continue
            if value.endswith('.png'):
                continue  # skip image files
            menu = generic_menu(value, theme_path)
            menus[key] = menu
            logger.debug(f"Created menu from path in key: {key}")
    
    logger.debug(f"Created {len(menus)} menus total")
    
    '''if 'generic_menus' in theme_data:
        for menu_name, menu_path in theme_data['generic_menus'].items():
            menu = generic_menu(menu_path, theme_path)
            menus[menu.menu_data['screen_name']] = menu
            logger.debug(f"Created generic menu: {menu_name}")'''
    return menus

# create status bars based on theme data and returns a list of status bar objects
def create_status_bars(theme_data, theme_path) -> list:
    status_bars = {}
    if 'status_bars' in theme_data:
        for status_bar_name, status_bar_path in theme_data['status_bars'].items():
            status_bar = generic_menu(status_bar_path, theme_path)
            status_bars[status_bar_name] = status_bar
            logger.debug(f"Created status bar: {status_bar_name}")
    return status_bars

# make paths absolute in dictionary only if it exists
def make_paths_absolute(d: dict, base_path: str) -> dict:
    for key, value in d.items():
        if isinstance(value, str):
            if not os.path.isabs(value):
                candidate = os.path.abspath(os.path.join(base_path, value))
                if os.path.exists(candidate):
                    d[key] = candidate
        elif isinstance(value, dict):
            d[key] = make_paths_absolute(value, base_path)
        elif isinstance(value, list):
            d[key] = make_list_paths_absolute(value, base_path)
    return d

# make paths absolute in list
def make_list_paths_absolute(lst: list, base_path: str) -> list:
    for i in range(len(lst)):
        logger.debug(f"Making paths absolute in list {lst}")
        logger.debug(f"Processing list index {i} with value: {lst[i]}")
        value = lst[i]
        if isinstance(value, str):
            if not os.path.isabs(value):
                candidate = os.path.abspath(os.path.join(base_path, value))
                if os.path.exists(candidate):
                    lst[i] = candidate
        elif isinstance(value, dict):
            lst[i] = make_paths_absolute(value, base_path)
        elif isinstance(value, list):
            lst[i] = make_list_paths_absolute(value, base_path)
    return lst

def load_menu():
    global button_map, menu_index, selected_menu_item, selected_page, menu, canvas_screen, menu_items, pages, a_button, b_button, up_button, down_button, left_button, right_button
    menu_data = menu.menu_data
    logger.debug(f"Loading menu: {menu.menu_data.get('screen_name', 'Unnamed')}")
    
    # button_map
    if 'button_map' in menu_data:
        button_map = menu_data['button_map']
    else:
        button_map = {
            'a': 'select',
            'b': 'back',
            'up': 'previous',
            'down': 'next',
            'left': 'previous_page',
            'right': 'next_page'
        }
    
    if button_map['a'] == "noop":
        a_button.config(state=DISABLED)
    else:
        a_button.config(state=NORMAL)
    if button_map['b'] == "noop":
        b_button.config(state=DISABLED)
    else:
        b_button.config(state=NORMAL)
    
    a_button.config(text=button_map['a'].upper())
    b_button.config(text=button_map['b'].upper())
    
    if button_map['up'] == "noop":
        up_button.config(state=DISABLED)
    else:
        up_button.config(state=NORMAL)
    
    if button_map['down'] == "noop":
        down_button.config(state=DISABLED)
    else:
        down_button.config(state=NORMAL)
    
    if button_map['left'] == "noop":
        left_button.config(state=DISABLED)
    else:
        left_button.config(state=NORMAL)
    
    if button_map['right'] == "noop":
        right_button.config(state=DISABLED)
    else:
        right_button.config(state=NORMAL)
    
    up_button.config(text=button_map['up'].upper())
    down_button.config(text=button_map['down'].upper())
    left_button.config(text=button_map['left'].upper())
    right_button.config(text=button_map['right'].upper())

    logger.debug("Button states and labels configured. Button map: " + str(button_map))
    
    
    menu_items = menu.menu_items
    pages = menu.pages
    logger.debug(f"Loaded menu items({len(menu_items)}): " + str(menu_items))
    logger.debug(f"Loaded menu pages({len(pages)}): " + str(pages))
    
    # when pages contains data and menu_items is empty, load menu_items from the selected page
    if pages and not menu_items:
        page_data = pages[selected_page]
        if 'menu_items' in page_data:
            menu_items = page_data['menu_items']
            logger.debug(f"Loaded menu items from selected page {selected_page}: " + str(menu_items))
            if 'button_map' in menu_items[selected_menu_item]:
                button_map = menu_items[selected_menu_item]['button_map']
                logger.debug(f"Loaded button map from selected menu item {selected_menu_item}: " + str(button_map))
    
    if button_map['a'] == "noop":
        a_button.config(state=DISABLED)
    else:
        a_button.config(state=NORMAL)
    if button_map['b'] == "noop":
        b_button.config(state=DISABLED)
    else:
        b_button.config(state=NORMAL)
    
    a_button.config(text=button_map['a'].upper())
    b_button.config(text=button_map['b'].upper())
    
    if button_map['up'] == "noop":
        up_button.config(state=DISABLED)
    else:
        up_button.config(state=NORMAL)
    
    if button_map['down'] == "noop":
        down_button.config(state=DISABLED)
    else:
        down_button.config(state=NORMAL)
    
    if button_map['left'] == "noop":
        left_button.config(state=DISABLED)
    else:
        left_button.config(state=NORMAL)
    
    if button_map['right'] == "noop":
        right_button.config(state=DISABLED)
    else:
        right_button.config(state=NORMAL)
    
    up_button.config(text=button_map['up'].upper())
    down_button.config(text=button_map['down'].upper())
    left_button.config(text=button_map['left'].upper())
    right_button.config(text=button_map['right'].upper())

    logger.debug("Rendering the menu: " + menu_data['screen_name'])
    render_menu(menu_data)
    draw_menu_items()
    draw_status_bar()
    #pprint(menu_data)
# generic_menu class which contains the information from generic_menus key in theme.json for one menu 

# update menu
def update_menu():
    global menu, menu_target, menus
    logger.info(f"Updating menu to target: {menu_target}")
    if menu_target in menus:
        menu = menus[menu_target]
    elif  f'{menu_target}_path' in menus.keys():
        menu_target = menu_target + '_path'
        menu = menus[menu_target]
    else:
        logger.warning(f"Menu target '{menu_target}' not found in menus.")
        logger.warning("Available menus: " + str(list(menus.keys())))
        return
    
    if 'template' in menu.menu_data:
        menu.menu_data = menu.menu_data['template']
    
    load_menu()


# update currently loaded page
def update_page():
    global selected_page, pages, menu_items, selected_menu_item, button_map, a_button, b_button, up_button, down_button, left_button, right_button
    logger.info(f"Updating to page index: {selected_page}")
    pages = menu.pages
    logger.debug(f"Loaded menu items({len(menu_items)}): " + str(menu_items))
    logger.debug(f"Loaded menu pages({len(pages)}): " + str(pages))
    
    # when pages contains data and menu_items is empty, load menu_items from the selected page
    
    page_data = pages[selected_page]
    if 'menu_items' in page_data:
        menu_items = page_data['menu_items']
        logger.debug(f"Loaded menu items from selected page {selected_page}: " + str(menu_items))
        if 'button_map' in menu_items[selected_menu_item]:
            button_map = menu_items[selected_menu_item]['button_map']
            logger.debug(f"Loaded button map from selected menu item {selected_menu_item}: " + str(button_map))
    
    if button_map['a'] == "noop":
        a_button.config(state=DISABLED)
    else:
        a_button.config(state=NORMAL)
    if button_map['b'] == "noop":
        b_button.config(state=DISABLED)
    else:
        b_button.config(state=NORMAL)
    
    a_button.config(text=button_map['a'].upper())
    b_button.config(text=button_map['b'].upper())
    
    if button_map['up'] == "noop":
        up_button.config(state=DISABLED)
    else:
        up_button.config(state=NORMAL)
    
    if button_map['down'] == "noop":
        down_button.config(state=DISABLED)
    else:
        down_button.config(state=NORMAL)
    
    if button_map['left'] == "noop":
        left_button.config(state=DISABLED)
    else:
        left_button.config(state=NORMAL)
    
    if button_map['right'] == "noop":
        right_button.config(state=DISABLED)
    else:
        right_button.config(state=NORMAL)
    
    up_button.config(text=button_map['up'].upper())
    down_button.config(text=button_map['down'].upper())
    left_button.config(text=button_map['left'].upper())
    right_button.config(text=button_map['right'].upper())

# draw menu items on the screen
def draw_menu_items():
    global selected_menu_item, menu_items, canvas_screen
    logger.info("Drawing menu items")
    for index, item in enumerate(menu_items):
        is_selected = (index == selected_menu_item)
        if is_selected:
            layer = item['selected_layers']
        else:
            if 'layers' in item:
                layer = item['layers']
            else:
                layer = []
        
        base_x = item.get('x', 0)
        base_y = item.get('y', 0)
        # draw the layer on the screen
        for i in range(len(layer)):
            layer_item = layer[i]
            if 'image_path' in layer_item:
                image_path = layer_item['image_path']
                if os.path.isfile(image_path):
                    logger.debug(f"Loading menu item image from path: {image_path}")
                    x = layer_item['x']+base_x
                    y = layer_item['y']+base_y
                    if 'recolor_palette' in layer_item.keys():
                        # recolor the image based on the palette
                        pil_image = Image.open(image_path).convert('RGBA')
                        recolored_image = recolor_image(pil_image, layer_item['recolor_palette'])
                        image = ImageTk.PhotoImage(recolored_image)
                    else:
                        image = PhotoImage(file=image_path)
                    canvas_screen.create_image(x, y, anchor=NW, image=image)
                    
                    logger.debug(f"Position of menu item image: x={x}, y={y}")
                    # Keep a reference to all images to prevent garbage collection
                    canvas_screen.images.append(image)
                else:
                    logger.warning(f"Menu item image file not found: {image_path}")
            if 'text' in layer_item:
                text = layer_item['text']
                x = layer_item['x']+base_x
                y = layer_item['y']+base_y
                fill_color = "white"
                if 'text_color_palette' in layer_item:
                    color = layer_item['text_color_palette']
                    color = palette.get(color, {'r': 255, 'g': 255, 'b': 255})
                    fill_color = f"#{color['r']:02x}{color['g']:02x}{color['b']:02x}"
                match layer_item.get('text_size', 'medium'):
                    case "small":
                        font_size = 6
                    case "large":
                        font_size = 16
                    case _:
                        font_size = 12
                canvas_screen.create_text(x, y, text=text, anchor=NW, fill=fill_color, font=("DejaVu Sans", font_size))
                logger.debug(f"Position of menu item text: x={x}, y={y}, text='{text}', color='{fill_color}'")

def draw_status_bar():
    global canvas_screen, status_bars, menu
    logger.info("Drawing status bar")
    if 'status_bar' not in menu.menu_data:
        logger.debug("No status bar defined for this menu.")
        return
    status_bar = status_bars.get(menu.menu_data['status_bar'], None)
    #pprint(status_bar.menu_data)
    for status_bar_item_name, status_bar_item in status_bar.menu_data["status_bar_items"].items():
        logger.debug(f"Drawing status bar: {status_bar_item_name}")
        if status_bar_item_name == "Time":
            continue  # skip time for now
        elif status_bar_item_name == "Battery":
            # draw battery status bar
            base_x = status_bar_item.get('x', 0)
            base_y = status_bar_item.get('y', 0)
            layers = status_bar_item['layers']
            #pprint(layers)
            layer = layers[BATTERY][0]
            logger.debug(f"Drawing battery layer.")
            #pprint(layer)
            if 'image_path' in layer:
                image_path = layer['image_path']
                if os.path.isfile(image_path):
                    logger.debug(f"Loading status bar image from path: {image_path}")
                    image = PhotoImage(file=image_path)
                    canvas_screen.create_image(layer['x']+base_x, layer['y']+base_y, anchor=NW, image=image)
                    # Keep a reference to all images to prevent garbage collection
                    canvas_screen.images.append(image)
                else:
                    logger.warning(f"Status bar image file not found: {image_path}")
        elif status_bar_item_name == "Volume":
            # draw volume status bar
            base_x = status_bar_item.get('x', 0)
            base_y = status_bar_item.get('y', 0)
            layers = status_bar_item['layers']
            #pprint(layers)
            layer = layers[VOLUME][0]
            logger.debug(f"Drawing volume layer.")
            #pprint(layer)
            if 'image_path' in layer:
                image_path = layer['image_path']
                if os.path.isfile(image_path):
                    logger.debug(f"Loading status bar image from path: {image_path}")
                    image = PhotoImage(file=image_path)
                    canvas_screen.create_image(layer['x']+base_x, layer['y']+base_y, anchor=NW, image=image)
                    # Keep a reference to all images to prevent garbage collection
                    canvas_screen.images.append(image)
                else:
                    logger.warning(f"Status bar image file not found: {image_path}")
        elif status_bar_item_name == "Brightness":
            # draw brightness status bar
            base_x = status_bar_item.get('x', 0)
            base_y = status_bar_item.get('y', 0)
            layers = status_bar_item['layers']
            #pprint(layers)
            layer = layers[BRIGHTNESS][0]
            logger.debug(f"Drawing brightness layer.")
            #pprint(layer)
            if 'image_path' in layer:
                image_path = layer['image_path']
                if os.path.isfile(image_path):
                    logger.debug(f"Loading status bar image from path: {image_path}")
                    image = PhotoImage(file=image_path)
                    canvas_screen.create_image(base_x, base_y, anchor=NW, image=image)
                    # Keep a reference to all images to prevent garbage collection
                    canvas_screen.images.append(image)
                else:
                    logger.warning(f"Status bar image file not found: {image_path}")
        elif status_bar_item_name == "Vibrate":
            # draw vibrate status bar
            base_x = status_bar_item.get('x', 0)
            base_y = status_bar_item.get('y', 0)
            layers = status_bar_item['layers']
            #pprint(layers)
            layer = layers[VIBRATE][0]
            logger.debug(f"Drawing vibrate layer.")
            #pprint(layer)
            if 'image_path' in layer:
                image_path = layer['image_path']
                if os.path.isfile(image_path):
                    logger.debug(f"Loading status bar image from path: {image_path}")
                    image = PhotoImage(file=image_path)
                    canvas_screen.create_image(layer['x']+base_x, layer['y']+base_y, anchor=NW, image=image)
                    # Keep a reference to all images to prevent garbage collection
                    canvas_screen.images.append(image)
                else:
                    logger.warning(f"Status bar image file not found: {image_path}")


# recolor image based on palette and on new_color string. this will look up the new_color and replaces every color in the original image with the new_color
def recolor_image(image: Image.Image, new_color: str) -> Image.Image:
    global palette
    # Create a new image to avoid modifying the original
    recolored_image = image.copy().convert('RGBA')
    pixels = recolored_image.load()
    # recolor based on palette dictionary
    if new_color not in palette:
        logger.warning(f"Palette color '{new_color}' not found. Using original image.")
        return recolored_image
    
    new_r = palette[new_color].get('r', 0)
    new_g = palette[new_color].get('g', 0)
    new_b = palette[new_color].get('b', 0)
    
    for y in range(recolored_image.height):
        for x in range(recolored_image.width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue  # skip transparent pixels
            # set the color of the pixel to the new color from the palette
            pixels[x, y] = (new_r, new_g, new_b, a)
    return recolored_image



class generic_menu:
    def __init__(self, menu_path, theme_path):
        logger.debug(f"Initializing generic_menu with menu_path and theme_path: {theme_path}")
        # Load JSON file if menu_path is a string path
        logger.debug(f"menu_path type: {type(menu_path)}")
        logger.debug(f"menu_path value: {menu_path}")
        if isinstance(menu_path, str):
            with open(menu_path, 'r', encoding='utf-8') as f:
                menu_data = json.load(f)
        else:
            menu_data = menu_path
        # menu_data is a dict, so use make_paths_absolute
        self.menu_data = make_paths_absolute(menu_data, theme_path)
        self.theme_path = theme_path
        
        
        self.menu_items = self.menu_data['menu_items'] if 'menu_items' in self.menu_data else []
        logging.debug(f"Menu items loaded.")
        
        self.pages = self.menu_data['pages'] if 'pages' in self.menu_data else []
        logging.debug(f"Menu pages loaded.")
        
        
        
        logger.debug(f"Loaded generic menu: {self.menu_data.get('screen_name', 'Unnamed')}")
    
    def get_property(self, property_name):
        return self.menu_data.get(property_name, None)

class page:
    def __init__(self, page_data: dict):
        self.page_data = page_data
        logger.debug(f"Initialized page with data: {page_data}")



# look up functions for menu navigation
def use_button_map(key: str):
    global button_map, canvas_screen, menu_items, selected_menu_item, selected_page, pages
    match button_map[key]:
            case "select":
                logger.info("Select action triggered.")
                select_menu_item()
            case "back":
                logger.info("Back action triggered.")
                back_menu()
            case "previous":
                if len(menu_items) > 1:
                    logger.info("Previous item triggered.")
                    previous_menu_item()
                else:
                    logger.info("Previous page triggered.")
                    previous_page()
                
            case "next":
                if len(menu_items) > 1:
                    logger.info("Next item triggered.")
                    next_menu_item()
                else:
                    logger.info("Next page triggered.")
                    next_page()
            case "previous_page":
                logger.info("Previous page triggered.")
                previous_page()
            case "next_page":
                logger.info("Next page triggered.")
                next_page()
            case _:
                logger.info("No action mapped to A button.")
                return
    
    # when pages contains data and menu_items is empty, load menu_items from the selected page
    if pages:
        page_data = pages[selected_page]
        if 'menu_items' in page_data:
            menu_items = page_data['menu_items']
            logger.debug(f"Loaded menu items from selected page {selected_page}: " + str(menu_items))
            if 'button_map' in menu_items[selected_menu_item]:
                button_map = menu_items[selected_menu_item]['button_map']
                logger.debug(f"Loaded button map from selected menu item {selected_menu_item}: " + str(button_map))
    
    update_menu()
    canvas_screen.delete("all")
    if pages:
        update_page()
    render_menu(menu.menu_data)
    draw_menu_items()
    draw_status_bar()


def select_menu_item():
    global selected_menu_item, menu_items, menu_target, menu_path
    if 0 <= selected_menu_item < len(menu_items):
        menu_target = menu_items[selected_menu_item]['target']
        # append the new target to the menu_path
        menu_path.append(menu_target)
        logger.info(f"Menu item selected. Target: {menu_target}")
    else:
        logger.warning(f"Index {selected_menu_item} out of range for menu items.")

def back_menu():
    global menu_target, menu_path
    if len(menu_path) > 1:
        menu_path.pop()  # remove the last target
        menu_target = menu_path[-1]  # set to the previous target
        logger.info(f"Back action triggered. New target: {menu_target}")
    else:
        logger.info("Already at the root menu. Cannot go back further.")

def next_menu_item():
    global selected_menu_item, menu_items
    #print(menu_items)
    selected_menu_item = (selected_menu_item + 1) % len(menu_items)
    logger.debug(f"Selected menu item changed to index: {selected_menu_item}, selected item: {menu_items[selected_menu_item]}")

def previous_menu_item():
    global selected_menu_item, menu_items
    selected_menu_item = (selected_menu_item - 1) if selected_menu_item > 0 else len(menu_items) - 1
    logger.debug(f"Selected menu item changed to index: {selected_menu_item}, selected item: {menu_items[selected_menu_item]}")

def next_page():
    global selected_page, pages
    selected_page = (selected_page + 1) % len(pages)
    logger.debug(f"Selected page changed to index: {selected_page}")

def previous_page():
    global selected_page, pages
    selected_page = (selected_page - 1) if selected_page > 0 else len(pages) - 1
    logger.debug(f"Selected page changed to index: {selected_page}")


# Entry point
if __name__ == "__main__":
    main()