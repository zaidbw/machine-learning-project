import numpy as np
import imgaug.augmenters as iaa
from scapy.all import *

# Function to load raw packet capture dataset
def load_raw_data(file_path):
    packets = rdpcap(file_path)
    return packets

# Function to save augmented dataset
def save_augmented_data(augmented_data, save_path):
    wrpcap(save_path, augmented_data)

# Define augmentation sequence with desired transformations
def define_augmentation_seq():
    return iaa.Sequential([
        iaa.AdditiveGaussianNoise(scale=(0, 0.1*255)),  # Add Gaussian noise
        iaa.Multiply((0.5, 1.5)),  # Multiply pixel values (brightness)
        iaa.ContrastNormalization((0.5, 2.0)),  # Adjust contrast
        iaa.Grayscale(alpha=(0.0, 1.0)),  # Convert to grayscale with random intensity
        iaa.SaltAndPepper(p=(0, 0.05)),  # Add salt and pepper noise
        # Add more transformations as needed
    ])

def main():
    # File paths
    raw_data_file = "D:\ML\ML project\DDoS_HTTP\DDoS_HTTP"  # Replace with the path to your pcap file
    augmented_data_file = "D:\ML\ML project\DDoS_HTTP\Augmented"  # Replace with the desired path for saving augmented data

    # Load raw packet capture dataset
    raw_data = load_raw_data(raw_data_file)

    # Define augmentation sequence
    augmentation_seq = define_augmentation_seq()

    # Apply augmentation sequence to generate augmented samples
    augmented_data = augmentation_seq.augment_images(raw_data)

    # Save augmented dataset
    save_augmented_data(augmented_data, augmented_data_file)

if __name__ == "__main__":
    main()
