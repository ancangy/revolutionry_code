from PIL import Image
import numpy as np

baseline = 'C:/results/'
def message_to_binary(message):
    """Convert a string message to its binary representation."""
    return ''.join(format(ord(char), '08b') for char in message)

def binary_to_message(binary_data):
    """Convert binary string back to the original message."""
    binary_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(b, 2)) for b in binary_data)

def hide_message_in_image(image, message):
    """Hide a binary message within the LSB of image pixels."""
    binary_message = message_to_binary(message) + '1111111111111110'  # Add a stopping delimiter

    image_data = np.array(image)
    flat_image_data = image_data.flatten()

    for i in range(len(binary_message)):
        flat_image_data[i] = (flat_image_data[i] & ~1) | int(binary_message[i])

    new_image_data = flat_image_data.reshape(image_data.shape)
    return Image.fromarray(new_image_data.astype('uint8'))

def extract_message_from_image(image):
    """Extract a hidden message from the LSB of image pixels."""
    image_data = np.array(image)
    flat_image_data = image_data.flatten()

    binary_message = ''
    for i in range(len(flat_image_data)):
        binary_message += str(flat_image_data[i] & 1)

    # Find the stopping delimiter and extract the message
    delimiter_index = binary_message.find('1111111111111110')
    if delimiter_index != -1:
        binary_message = binary_message[:delimiter_index]
    else:
        return "No hidden message found."

    return binary_to_message(binary_message)

# Load a sample image (make sure you have a grayscale image available)
image = Image.open(baseline+'sample_grayscale_image.png').convert('L')

# Message to hide
message = "Hello Team!"

# Hide the message in the image
hidden_image = hide_message_in_image(image, message)
hidden_image.save(baseline+'hidden_message_image.png')

# Extract the hidden message from the image
extracted_message = extract_message_from_image(hidden_image)
print("Extracted Message:", extracted_message)
