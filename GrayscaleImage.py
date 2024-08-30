from PIL import Image
import numpy as np

baseline = 'C:/results/'
# Create a 100x100 pixel grayscale image with random pixel values
width, height = 100, 100
image_array = np.random.randint(0, 256, (height, width), dtype=np.uint8)

# Convert the array to an image
image = Image.fromarray(image_array, 'L')

# Save the image
image.save(baseline+'sample_grayscale_image.png')

# Display the image (optional)
#image.show()
