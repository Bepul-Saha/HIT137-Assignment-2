from PIL import Image
import time

# Generate a number based on the current time
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print(f"Generated Number: {generated_number}")

# Open the image from the correct location
image_path = 'C:/Users/bipul/Downloads/Compressed/Assignment 2/chapter1.jpg'
image = Image.open(image_path)
pixels = image.load()  # Get the pixel map

# Apply the generated number to each pixel
n = generated_number  # Use the number generated earlier
width, height = image.size

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        # Update the pixel values by adding n to each channel
        r = min(255, r + n)
        g = min(255, g + n)
        b = min(255, b + n)
        pixels[x, y] = (r, g, b)

# Save the modified image
output_image_path = 'C:/Users/bipul/Downloads/Compressed/Assignment 2/chapter1out.png'
image.save(output_image_path)
print(f"Modified image saved as '{output_image_path}'")

# Calculate the sum of all red pixel values in the new image
new_image = Image.open(output_image_path)
new_pixels = new_image.load()

# Initialize the red pixel sum
red_sum = 0

# Sum all red pixel values
for x in range(width):
    for y in range(height):
        r, g, b = new_pixels[x, y]
        red_sum += r

print(f"Sum of red pixel values: {red_sum}")
