import numpy as np
import matplotlib.pyplot as plt

# Simulated traffic rate data
time = np.arange(0, 100, 1)  # Time intervals
traffic_rate = np.random.randint(50, 500, size=len(time))  # Simulated traffic rate

class TrafficAnalyzer:
    def __init__(self):
        self.window_size_fixed = 10  # Fixed window size
        self.window_size_dynamic = 10  # Initial dynamic window size
        self.processing_time_fixed = []
        self.processing_time_dynamic = []

    def monitor_traffic_volume(self):
        # Simulate monitoring traffic volume
        return np.random.randint(50, 500)

    def adjust_window_size(self, current_window_size, traffic_volume):
        # Simulate adjusting window size based on traffic volume
        threshold_high = 400  # Example threshold for high traffic volume
        threshold_low = 100  # Example threshold for low traffic volume

        if traffic_volume > threshold_high:
            return current_window_size * 2  # Increase window size
        elif traffic_volume < threshold_low:
            return max(current_window_size // 2, 1)  # Decrease window size, ensuring it's not less than 1
        else:
            return current_window_size  # Maintain current window size

    def simulate_processing_time(self, window_size):
        # Simulate processing time based on window size
        return np.random.uniform(0.5, 2) * window_size

    def evaluate_window_sizing(self, traffic_volume):
        # Adjust window size for dynamic window sizing
        self.window_size_dynamic = self.adjust_window_size(self.window_size_dynamic, traffic_volume)

        # Simulate processing time for fixed and dynamic window sizes
        processing_time_fixed = self.simulate_processing_time(self.window_size_fixed)
        processing_time_dynamic = self.simulate_processing_time(self.window_size_dynamic)

        # Store processing times
        self.processing_time_fixed.append(processing_time_fixed)
        self.processing_time_dynamic.append(processing_time_dynamic)


def plot_results(time, traffic_rate, processing_time_fixed, processing_time_dynamic):
    plt.figure(figsize=(12, 6))

    # Plot traffic rate
    plt.subplot(2, 1, 1)
    plt.plot(time, traffic_rate, color='blue')
    plt.title('Simulated Traffic Attack Rate')
    plt.xlabel('Time')
    plt.ylabel('Traffic Rate')

    # Plot processing time for fixed and dynamic window sizes
    plt.subplot(2, 1, 2)
    plt.plot(time, processing_time_fixed, label='Fixed Window', color='red')
    plt.plot(time, processing_time_dynamic, label='Dynamic Window', color='green')
    plt.title('Processing Time Comparison')
    plt.xlabel('Time')
    plt.ylabel('Processing Time')
    plt.legend()

    plt.tight_layout()
    plt.show()
def main():
    traffic_analyzer = TrafficAnalyzer()

    # Simulate network traffic monitoring and analysis
    for t in time:
        # Monitor traffic volume
        traffic_volume = traffic_analyzer.monitor_traffic_volume()

        # Evaluate window sizing and simulate processing time
        traffic_analyzer.evaluate_window_sizing(traffic_volume)

    # Plot results
    plot_results(time, traffic_rate, traffic_analyzer.processing_time_fixed, traffic_analyzer.processing_time_dynamic)


if __name__ == "__main__":
    main()
