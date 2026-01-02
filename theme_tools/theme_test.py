import json
import os
import re
from tkinter import *
import argparse
import logging
from pprint import pprint

PAGER_SCREEN_WIDTH = 480
PAGER_SCREEN_HEIGHT = 222

# TODO: add buttons for: navigation, reloading theme, exiting tool, toggling debug output
# TODO: add gui for selecting theme path if not provided as argument

# Set up logging
logger = logging.getLogger("theme_test")

def main():
    parser = argparse.ArgumentParser(description="Test Theme Tool")
    
    # Argument that need to be provided
    parser.add_argument("--theme", type=str, required=True, help="Location of the base directory of the theme to test")
    
    # Debug argument
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output for debugging")
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()
    
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
    logger.info(f"Created {len(menus)} menus from theme data.")
    
    # render the first menu from the menus list
    menu_index = 0  # for testing, render the third menu if it exists
    if menus:
        logger.debug("Rendering the menu: " + menus[menu_index].menu_data['screen_name'])
        render_menu(canvas_screen, menus[menu_index].menu_data)
    else:
        logger.warning("No menus found in theme data to render")
    
    logger.info("Starting the Theme Test Tool GUI")
    root.mainloop()
    logger.info("Exiting the Theme Test Tool")
    

def load_theme(theme_path):
    # first get the theme.json file form the root of the theme path
    theme_file = os.path.join(theme_path, "theme.json")
    # check if the file exists
    if not os.path.isfile(theme_file):
        raise FileNotFoundError(f"Theme file not found: {theme_file}")
    # load the theme file and convert it to a dictionary
    import json
    with open(theme_file, 'r') as f:
        theme_data_raw = json.load(f)
    
    # Expand paths relative to the theme root so values like "assets/..." work
    theme_data = expand_dict(theme_data_raw, base_path=theme_path)
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Expanded theme data:")
        pprint(theme_data)
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
                    with open(candidate, 'r') as f:
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
def render_menu(canvas_screen: Canvas, menu_data):
    logger.debug("Rendering menu data on screen:")
    pprint(menu_data)
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
    menus = []
    if 'generic_menus' in theme_data:
        for menu_name, menu_path in theme_data['generic_menus'].items():
            menu = generic_menu(menu_path, theme_path)
            menus.append(menu)
            logger.debug(f"Created generic menu: {menu_name} from path: {menu_path}")
    return menus

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

# generic_menu class which contains the information from generic_menus key in theme.json for one menu 
class generic_menu:
    def __init__(self, menu_path, theme_path):
        logger.debug(f"Initializing generic_menu with menu_path and theme_path: {theme_path}")
        # Load JSON file if menu_path is a string path
        if isinstance(menu_path, str):
            with open(menu_path, 'r') as f:
                menu_data = json.load(f)
        else:
            menu_data = menu_path
        # menu_data is a dict, so use make_paths_absolute
        self.menu_data = make_paths_absolute(menu_data, theme_path)
        self.theme_path = theme_path
        logger.debug(f"Loaded generic menu: {self.menu_data.get('screen_name', 'Unnamed')} from path: {menu_path}")
    
    def get_property(self, property_name):
        return self.menu_data.get(property_name, None)


# Entry point
if __name__ == "__main__":
    main()