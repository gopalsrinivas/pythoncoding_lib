from PIL import Image, ImageDraw, ImageFont


def add_diagonal_text_to_image(
    image_path, text, font_path, output_path, font_size=130, text_opacity=200
):
    # Load the image
    img = Image.open(image_path).convert("RGBA")

    # Create a new blank image with the same size and RGBA mode
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))

    # Initialize ImageDraw for the text layer
    draw = ImageDraw.Draw(txt_layer)

    # Load the font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        raise Exception("Font file not found. Please check the font path.")

    # Get the size of the text
    text_bbox = font.getbbox(text)
    textwidth = text_bbox[2] - text_bbox[0]
    textheight = text_bbox[3] - text_bbox[1]

    # Get image dimensions
    img_width, img_height = img.size

    # Start from the bottom-left corner (0, img_height) and go diagonally to the top-right (img_width, 0)
    for i, char in enumerate(text):
        # Calculate the position for each character
        # x position increases as we go across the image
        x_pos = (img_width / len(text)) * i
        # y position decreases as we move diagonally
        y_pos = img_height - ((img_height / len(text)) * i) - textheight

        # Draw the text with some opacity (semi-transparent white)
        draw.text((x_pos, y_pos), char, font=font, fill=(255, 255, 255, text_opacity))

    # Composite the original image and the text layer
    watermarked = Image.alpha_composite(img, txt_layer)

    # Save the image
    watermarked.convert("RGB").save(output_path)

    # Open the saved image to view
    watermarked.show()


# Example usage:
image_path = r"Game_changer.jpg"
text = "Gopalcoding.com"
font_path = r"arial.ttf"
output_path = r"Game_changer_with_watermark.jpg"
add_diagonal_text_to_image(image_path, text, font_path, output_path)
