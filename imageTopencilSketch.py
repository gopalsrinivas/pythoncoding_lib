import cv2


def convert_to_pencil_sketch(image_path, output_path, blur_intensity=35, scale=150.0):
    """
    Converts an image to a pencil sketch.

    Args:
        image_path (str): Path to the input image (e.g., 'harsha.jpg').
        output_path (str): Path to save the output pencil sketch image (e.g., 'sketch_image.png').
        blur_intensity (int): Intensity of the blur effect. Higher value gives a darker sketch.
        scale (float): Scale factor for sketch intensity. Lower value makes the sketch darker.

    Returns:
        str: Success or error message.
    """
    try:
        # Load the input image
        image = cv2.imread(image_path)
        if image is None:
            return f"Error: Could not load the image from {image_path}. Please check the file path."

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Invert the grayscale image
        inverted = 255 - gray_image

        # Apply Gaussian blur to the inverted image
        blur = cv2.GaussianBlur(inverted, (blur_intensity, blur_intensity), 0)

        # Invert the blurred image
        inverted_blur = 255 - blur

        # Create the pencil sketch
        sketch = cv2.divide(gray_image, inverted_blur, scale=scale)

        # Save the sketch to the output file
        cv2.imwrite(output_path, sketch)

        # Display the sketch
        cv2.imshow("Pencil Sketch", sketch)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return f"Pencil sketch saved successfully at {output_path}."
    except Exception as e:
        return f"An error occurred: {e}"


# Example usage
input_image = "harsha.jpg"  # Replace with your input image file
output_image = "sketch_image_dark.png"  # Replace with your desired output file name

# Call the function
result = convert_to_pencil_sketch(
    input_image, output_image, blur_intensity=35, scale=150.0
)
print(result)
