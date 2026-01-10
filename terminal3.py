import sys
from PIL import Image

def convert_image_to_dual(image_path, width=80):
    # Open image and ensure RGB mode
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    orig_width, orig_height = img.size
    
    # Calculate dimensions with aspect correction (2:1 character ratio)
    height = int((orig_height / orig_width) * width * 0.5)
    if height < 1:
        height = 1

    # Double vertical resolution for dual mapping
    pixel_rows = height * 2
    
    # Resize image to target dimensions
    resized_img = img.resize((width, pixel_rows))
    pixels = list(resized_img.getdata())
    
    output_lines = []
    grayscale_chars = " .-+*#%@$"  # Enhanced luminance scale

    for row in range(height):
        line_parts = []
        upper_row_idx = row * 2
        lower_row_idx = row * 2 + 1
        
        for col in range(width):
            # Get colors from two vertically adjacent pixels
            top_r, top_g, top_b = pixels[upper_row_idx * width + col]
            
            if lower_row_idx < pixel_rows:
                bot_r, bot_g, bot_b = pixels[lower_row_idx * width + col]
            else:  # Handle last row padding
                bot_r, bot_g, bot_b = (0, 0, 0)
                
            # Calculate luminance for character selection
            top_lum = int(0.299*top_r + 0.587*top_g + 0.114*top_b)
            char_idx = min(int(top_lum / 28), len(grayscale_chars) - 1)
            char = grayscale_chars[char_idx]
            
            # Create escape sequences
            fg_escape = f"\x1b[38;2;{top_r};{top_g};{top_b}m"
            bg_escape = f"\x1b[48;2;{bot_r};{bot_g};{bot_b}m"
            
            line_parts.append(f"{fg_escape}{bg_escape}{char}")
        
        # Add reset at end of each line to prevent color bleeding
        output_lines.append(''.join(line_parts) + "\x1b[0m")
    
    return '\n'.join(output_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} image_path [width]\n")
        print("Options:")
        print("  width     : Output width in characters (default=80)")
        sys.exit(1)
    
    # Get parameters
    image_path = sys.argv[1]
    width = 100 if len(sys.argv) < 3 else int(sys.argv[2])

    try:
        ascii_art = convert_image_to_dual(image_path, width)
        
        # Add final reset to prevent terminal color bleeding
        print(ascii_art + "\x1b[0m")
    
    except Exception as e:
        print(f"Error processing image: {e}")
