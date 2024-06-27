from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    """
    Encrypts an image by modifying its pixel values based on the key.
    """
    # Open the image
    image = Image.open(image_path)
    pixels = np.array(image)

    # Encrypt the image by adding the key value to each pixel
    encrypted_pixels = (pixels + key) % 256

    # Create and save the encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    """
    Decrypts an image by reversing the encryption operation.
    """
    # Open the image
    image = Image.open(image_path)
    pixels = np.array(image)

    # Decrypt the image by subtracting the key value from each pixel
    decrypted_pixels = (pixels - key) % 256

    # Create and save the decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    """
    Main function to run the image encryption and decryption tool.
    """
    print("Image Encryption and Decryption Tool")
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return

    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the path to save the output image: ")
    try:
        key = int(input("Enter the key value (integer): "))
    except ValueError:
        print("Invalid key value. Please enter an integer.")
        return

    if choice == 'e':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
