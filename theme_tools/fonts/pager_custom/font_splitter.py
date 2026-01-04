# Takes in a png file where each character is in a grid and splits it into individual character pngs
# Takes in a optional string wich describes the order of characters in the grid
# Automatically calculates the size of each character based on the grid size
from PIL import Image
import os
import sys
import argparse


standard_char_order = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()+=[]{},;.:-_\\/"



def main():
    parser = argparse.ArgumentParser(
        description="Splits a grid image of characters into individual character images."
    )
    parser.add_argument("input_image", help="Path to the input PNG image.")
    parser.add_argument(
        "output_folder", help="Folder to save the individual character images."
    )
    parser.add_argument(
        "--char_order",
        help="String representing the order of characters in the grid.",
        default=None,
    )

    args = parser.parse_args()

    # Load the image
    img = Image.open(args.input_image)
    img_width, img_height = img.size
    
    char_order = args.char_order if args.char_order else standard_char_order
    num_chars = len(char_order)
    print(f"Number of characters: {num_chars}")
    
    char_width = img_width // num_chars
    char_height = img_height
    
    print(f"Image size: {img_width}x{img_height}")
    print(f"Character size: {char_width}x{char_height}")
    
    for index, char in enumerate(char_order):
        left = index * char_width
        upper = 0
        right = left + char_width
        lower = upper + char_height
        
        char_img = img.crop((left, upper, right, lower))
        
        # Create output folder if it doesn't exist
        os.makedirs(args.output_folder, exist_ok=True)
        
        # Save the character image
        char_filename = os.path.join(args.output_folder, f"{ord(char)}.png")
        char_img.save(char_filename)
        print(f"Saved character '{char}' as {char_filename}")



if __name__ == "__main__":
    main()