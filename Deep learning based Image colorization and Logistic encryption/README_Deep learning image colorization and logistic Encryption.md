### Image Encryption for Facial Recognition Systems
## Overview
This project explores the use of image encryption techniques to enhance the security of facial recognition systems. By encrypting images, we aim to protect sensitive data from unauthorized access and tampering.


## Data Preparation:

Loaded a grayscale image of Lena.
Reshaped the grayscale image to a suitable format for processing.
Autoencoder Training:

Utilized a convolutional autoencoder model to compress and reconstruct the grayscale image.
Trained the autoencoder model for a specified number of epochs using mean squared error (MSE) loss and the Adam optimizer.

## Image Encryption:

Implemented a logistic encryption algorithm using logistic maps and a provided key.
Encrypted the Lena image using the logistic encryption algorithm with different keys.

## Image Decryption:

Implemented a corresponding decryption algorithm using logistic maps and the same key used for encryption.
Decrypted the encrypted Lena images to obtain the original images.
Visualization:

Displayed the original grayscale image, encrypted images, and decrypted images using matplotlib.

## Problems Addressed
Security: Protecting sensitive image data from unauthorized access or tampering.
Data Integrity: Ensuring that encrypted images can be accurately decrypted without compromising data integrity.
Regulatory Compliance: Adhering to regulatory requirements regarding the encryption of sensitive data.
Considerations
Key Management: Ensure proper management of encryption keys to maintain security.
Algorithm Selection: Use well-established and cryptographically secure encryption algorithms.
Performance Overhead: Be mindful of computational overhead introduced by encryption and decryption processes, especially in real-time applications.
Data Integrity: Verify that encrypted images can be decrypted accurately to preserve data integrity.
Regulatory Compliance: Ensure compliance with regulatory requirements regarding data encryption.


## Future Work
Explore advanced encryption techniques to enhance security.
Optimize performance for real-time applications.
Conduct further testing and validation to ensure robustness and compliance.


## Dependencies:-
Python 3.x
NumPy
Matplotlib
TensorFlow/Keras (for autoencoder training)

![Capture9](https://github.com/Rustyryan-11/Projects/assets/44802832/3e716ed3-fd8e-45ce-94fe-4090177638e4)

# Encryption output:

![Capture 10](https://github.com/Rustyryan-11/Projects/assets/44802832/65d10968-7289-48b8-830f-1ff396f6928d)

# Decryption output:
![Capture9](https://github.com/Rustyryan-11/Projects/assets/44802832/3e716ed3-fd8e-45ce-94fe-4090177638e4)

![Capture  8](https://github.com/Rustyryan-11/Projects/assets/44802832/42c09de0-7d93-40b2-a9f1-66b36846e322)

# Encryption output:
![Capture 10](https://github.com/Rustyryan-11/Projects/assets/44802832/65d10968-7289-48b8-830f-1ff396f6928d)


# Decryption output:
![Capture  8](https://github.com/Rustyryan-11/Projects/assets/44802832/42c09de0-7d93-40b2-a9f1-66b36846e322)


![Capture 12](https://github.com/Rustyryan-11/Projects/assets/44802832/9abdd0c2-8298-4901-b168-0b41690a7680)


# Encryption output:
![Capture 10](https://github.com/Rustyryan-11/Projects/assets/44802832/65d10968-7289-48b8-830f-1ff396f6928d)


# Decryption output:
![Capture 12](https://github.com/Rustyryan-11/Projects/assets/44802832/9abdd0c2-8298-4901-b168-0b41690a7680)
