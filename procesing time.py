import numpy as np
import matplotlib.pyplot as plt
import time

def simulated_traffic(num_packets, attack_prob=0, attack_duration=0):
    """
    Simulates network traffic with a configurable attack scenario.

    Parameters:
    - num_packets: Total number of packets to simulate.
    - attack_prob: Probability of an attack occurring in each packet.
    - attack_duration: Duration of the attack in number of packets.

    Returns:
    - List of packets representing network traffic.
    """
    traffic = np.random.rand(num_packets)
    if attack_prob > 0 and attack_duration > 0:
        attack_start = np.random.randint(0, num_packets - attack_duration)
        attack_end = attack_start + attack_duration
        traffic[attack_start:attack_end] += np.random.normal(1, 0.5, attack_duration)
    return traffic

def extract_features(traffic_window):
    """
    Extracts relevant features from a window of traffic data.

    Parameters:
    - traffic_window: Window of traffic data (list of packet values).

    Returns:
    - Dictionary of extracted features.
    """
    mean_packet_size = np.mean(traffic_window)
    std_dev_packet_size = np.std(traffic_window)
    return {"mean_packet_size": mean_packet_size, "std_dev_packet_size": std_dev_packet_size}

def adjust_window_size(current_window_size, current_traffic_volume, threshold):
    """
    Adjusts the window size dynamically based on current traffic volume.

    Parameters:
    - current_window_size: Current window size.
    - current_traffic_volume: Current traffic volume (number of packets).
    - threshold: Threshold for adjusting the window size.

    Returns:
    - Updated window size.
    """
    if current_traffic_volume > threshold:
        return current_window_size + 1
    else:
        return current_window_size

def detect_attack(features, threshold):
    """
    Detects attacks based on extracted features.

    Parameters:
    - features: Dictionary of extracted features.
    - threshold: Threshold for attack detection.

    Returns:
    - Boolean indicating whether an attack is detected.
    """
    mean_packet_size = features["mean_packet_size"]
    if mean_packet_size > threshold:
        return True
    else:
        return False

def evaluate_window_sizing(num_packets, attack_prob, attack_duration, fixed_window_size, dynamic_threshold):
    """
    Evaluates the performance of fixed and dynamic window sizing in attack detection.

    Parameters:
    - num_packets: Total number of packets to simulate.
    - attack_prob: Probability of an attack occurring in each packet.
    - attack_duration: Duration of the attack in number of packets.
    - fixed_window_size: Size of the fixed window for attack detection.
    - dynamic_threshold: Threshold for dynamically adjusting the window size.

    Returns:
    - Processing times for fixed and dynamic window sizing.
    """
    # Simulate traffic
    traffic = simulated_traffic(num_packets, attack_prob, attack_duration)
    
    # Initialize lists to store processing times for fixed and dynamic window sizing
    fixed_processing_times = []
    dynamic_processing_times = []
    
    # Initialize window sizes and traffic volume
    current_fixed_window_size = fixed_window_size
    current_dynamic_window_size = fixed_window_size
    current_traffic_volume = 0
    
    # Process packets
    for i, packet in enumerate(traffic):
        # Update traffic volume
        current_traffic_volume += 1
        
        # Record start time for fixed window sizing
        fixed_start_time = time.time()
        
        # Extract features from current window for fixed window sizing
        window_start = max(0, i - current_fixed_window_size + 1)
        fixed_window = traffic[window_start:i+1]
        fixed_features = extract_features(fixed_window)
        detect_attack(fixed_features, threshold=1.5)  # Placeholder threshold
        
        # Record end time and calculate processing time for fixed window sizing
        fixed_end_time = time.time()
        fixed_processing_times.append(fixed_end_time - fixed_start_time)
        
        # Dynamically adjust window size for dynamic window sizing
        current_dynamic_window_size = adjust_window_size(current_dynamic_window_size, current_traffic_volume, dynamic_threshold)
        dynamic_start_time = time.time()
        dynamic_window = traffic[max(0, i - current_dynamic_window_size + 1):i+1]
        dynamic_features = extract_features(dynamic_window)
        detect_attack(dynamic_features, threshold=1.5)  # Placeholder threshold
        
        # Record end time and calculate processing time for dynamic window sizing
        dynamic_end_time = time.time()
        dynamic_processing_times.append(dynamic_end_time - dynamic_start_time)
    
    return fixed_processing_times, dynamic_processing_times

# Parameters
num_packets = 1000
attack_prob = 0.1
attack_duration = 50
fixed_window_size = 100
dynamic_threshold = 50

# Evaluate performance
fixed_processing_times, dynamic_processing_times = evaluate_window_sizing(
    num_packets, attack_prob, attack_duration, fixed_window_size, dynamic_threshold)

# Plot processing times for both fixed and dynamic window sizing
plt.plot(fixed_processing_times, label='Fixed Window Sizing')
plt.plot(dynamic_processing_times, label='Dynamic Window Sizing')
plt.xlabel('Packet Index')
plt.ylabel('Processing Time (s)')
plt.legend()
plt.title('Processing Times for Fixed and Dynamic Window Sizing')
plt.show()
