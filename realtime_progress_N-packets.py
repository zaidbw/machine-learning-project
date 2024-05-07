import threading
import time
import numpy as np
import matplotlib.pyplot as plt
from scapy.all import sniff

# Global variables for packet count and window size
packet_count = []
fixed_window_size = []
dynamic_window_size = []

def capture_packets(interface, duration, packet_count):
    # Packet capture callback function
    def packet_callback(packet):
        packet_count.append(len(packet))
        update_window_sizes()  # Update window sizes dynamically
    
    # Start packet capture
    sniff(iface=interface, prn=packet_callback, timeout=duration)

def update_window_sizes():
    # Update fixed window size
    fixed_window_size.extend([10] * len(packet_count))
    
    # Update dynamic window size based on packet count
    threshold = 100  # Example threshold for dynamic adjustment
    dynamic_window_size.clear()
    for count in packet_count:
        if count > threshold:
            dynamic_window_size.append(20)  # Increase window size
        else:
            dynamic_window_size.append(10)  # Maintain default window size

def plot_packet_count_and_window_size():
    # Plot packet count and window size over time
    def update_plot():
        plt.clf()  # Clear the previous plot
        plt.plot(packet_count, label='Packet Count')
        plt.plot(fixed_window_size, label='Fixed Window Size', linestyle='--')
        plt.plot(dynamic_window_size, label='Dynamic Window Size')
        plt.xlabel('Time')
        plt.ylabel('Count')
        plt.legend()
        plt.draw()
        plt.pause(1)  # Pause for 1 second

    plt.ion()  # Turn on interactive mode
    while True:
        update_plot()

def main(interface, duration, packet_count):
    # Start packet capture in a separate thread
    capture_thread = threading.Thread(target=capture_packets, args=(interface, duration, packet_count))
    capture_thread.start()
    
    # Plot packet count and window size in the main thread
    plot_packet_count_and_window_size()

if __name__ == "__main__":
    interface = "Wi-Fi 2"  # Default network interface
    duration = 10  # Duration of packet capture in seconds
    packet_count = []  # List to store packet count
    
    # Prompt user to input the number of packets to capture
    num_packets = int(input("Enter the number of packets to capture: "))
    
    # Start capturing packets
    main(interface, duration, packet_count)
