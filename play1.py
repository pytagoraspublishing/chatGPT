import numpy as np
import heapq
import matplotlib.pyplot as plt

class MM1QueueSimulation:
    def __init__(self, arrival_rate, service_rate, max_events):
        self.lambda_rate = arrival_rate  # Arrival rate (λ)
        self.mu_rate = service_rate      # Service rate (μ)
        self.max_events = max_events     # Number of events to simulate
        
        # Simulation state variables
        self.current_time = 0.0
        self.queue = []
        self.num_in_system = 0
        self.total_wait_time = 0.0
        self.num_served = 0
        
        # Event list as a priority queue
        self.event_list = []
        
        # Statistics for plotting
        self.times = []
        self.num_in_system_list = []

    def exponential(self, rate):
        """Generate an exponential random variable."""
        return np.random.exponential(1.0 / rate)

    def schedule_event(self, event_time, event_type):
        """Add an event to the event list."""
        heapq.heappush(self.event_list, (event_time, event_type))

    def run(self):
        """Run the simulation."""
        # Schedule the first arrival
        arrival_time = self.current_time + self.exponential(self.lambda_rate)
        self.schedule_event(arrival_time, 'arrival')
        
        while self.num_served < self.max_events:
            # Get the next event
            event_time, event_type = heapq.heappop(self.event_list)
            self.current_time = event_time
            self.times.append(self.current_time)
            self.num_in_system_list.append(self.num_in_system)
            
            if event_type == 'arrival':
                self.handle_arrival()
            elif event_type == 'departure':
                self.handle_departure()
        
        # Calculate average number in system and average wait time
        average_num_in_system = np.mean(self.num_in_system_list)
        average_wait_time = self.total_wait_time / self.num_served
        
        # Print results
        print(f"Simulation Results:")
        print(f"Average number of customers in system: {average_num_in_system:.4f}")
        print(f"Average wait time per customer: {average_wait_time:.4f} time units")
        print(f"Total customers served: {self.num_served}")
        
        # Plot results
        self.plot_results()

    def handle_arrival(self):
        """Handle an arrival event."""
        self.num_in_system += 1
        
        # Schedule next arrival
        next_arrival_time = self.current_time + self.exponential(self.lambda_rate)
        self.schedule_event(next_arrival_time, 'arrival')
        
        # If server is idle, start service immediately
        if self.num_in_system == 1:
            service_time = self.exponential(self.mu_rate)
            departure_time = self.current_time + service_time
            self.schedule_event(departure_time, 'departure')

    def handle_departure(self):
        """Handle a departure event."""
        self.num_in_system -= 1
        self.num_served += 1
        
        # Accumulate wait time
        self.total_wait_time += self.current_time
        
        if self.num_in_system > 0:
            # Schedule next departure
            service_time = self.exponential(self.mu_rate)
            departure_time = self.current_time + service_time
            self.schedule_event(departure_time, 'departure')

    def plot_results(self):
        """Plot the number of customers in the system over time."""
        plt.figure(figsize=(10, 6))
        plt.step(self.times, self.num_in_system_list, where='post')
        plt.title('Number of Customers in System Over Time')
        plt.xlabel('Time')
        plt.ylabel('Number of Customers')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    # User-defined parameters
    arrival_rate = float(input("Enter arrival rate (λ): "))
    service_rate = float(input("Enter service rate (μ): "))
    max_events = int(input("Enter number of customers to simulate: "))
    
    # Run simulation
    sim = MM1QueueSimulation(arrival_rate, service_rate, max_events)
    sim.run()
