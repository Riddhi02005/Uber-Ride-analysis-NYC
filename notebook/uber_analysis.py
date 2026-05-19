"""
Uber Ride Analysis for NYC
Analyzing 4.5M+ Uber NYC rides using Python
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import folium
from folium.plugins import HeatMap
import warnings
warnings.filterwarnings('ignore')

# Configure styling
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

class UberAnalysis:
    """Main class for Uber ride data analysis"""
    
    def __init__(self, data_path):
        """Initialize with data file path"""
        self.data_path = data_path
        self.df = None
        
    def load_data(self):
        """Load and preprocess Uber ride data"""
        print("Loading Uber ride data...")
        self.df = pd.read_csv(self.data_path)
        self._preprocess_data()
        return self.df
    
    def _preprocess_data(self):
        """Clean and preprocess the data"""
        print(f"Dataset shape: {self.df.shape}")
        print(f"Columns: {self.df.columns.tolist()}")
        
        # Convert datetime columns
        if 'tpep_pickup_datetime' in self.df.columns:
            self.df['tpep_pickup_datetime'] = pd.to_datetime(self.df['tpep_pickup_datetime'])
            self.df['tpep_dropoff_datetime'] = pd.to_datetime(self.df['tpep_dropoff_datetime'])
        
        # Remove outliers
        self.df = self.df[(self.df['trip_distance'] > 0) & 
                          (self.df['total_amount'] > 0)]
        
    def analyze_trips(self):
        """Analyze trip statistics"""
        stats = {
            'total_trips': len(self.df),
            'avg_distance': self.df['trip_distance'].mean(),
            'avg_fare': self.df['total_amount'].mean(),
            'avg_duration': self.df['trip_duration'].mean() if 'trip_duration' in self.df.columns else 0
        }
        return stats
    
    def plot_distance_distribution(self):
        """Plot trip distance distribution"""
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x='trip_distance', bins=50, kde=True)
        plt.title('Distribution of Trip Distances in NYC')
        plt.xlabel('Distance (miles)')
        plt.ylabel('Frequency')
        plt.tight_layout()
        return plt
    
    def plot_fare_vs_distance(self):
        """Plot fare vs distance relationship"""
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df.sample(5000), x='trip_distance', y='total_amount', alpha=0.5)
        plt.title('Fare Amount vs Trip Distance')
        plt.xlabel('Distance (miles)')
        plt.ylabel('Fare Amount ($)')
        plt.tight_layout()
        return plt
    
    def create_heatmap(self, output_path='uber_heatmap.html'):
        """Create heatmap visualization of pickup locations"""
        if 'pickup_latitude' not in self.df.columns:
            print("Latitude/Longitude columns not found")
            return None
        
        # Create base map centered on NYC
        m = folium.Map(
            location=[40.7128, -74.0060],
            zoom_start=11,
            tiles='OpenStreetMap'
        )
        
        # Add heatmap layer
        heat_data = [[row['pickup_latitude'], row['pickup_longitude']] 
                     for idx, row in self.df.iterrows()]
        HeatMap(heat_data).add_to(m)
        
        m.save(output_path)
        print(f"Heatmap saved to {output_path}")
        return m
    
    def summary_report(self):
        """Generate summary statistics report"""
        print("\n" + "="*50)
        print("UBER RIDE ANALYSIS SUMMARY")
        print("="*50)
        
        stats = self.analyze_trips()
        print(f"Total Trips Analyzed: {stats['total_trips']:,}")
        print(f"Average Trip Distance: {stats['avg_distance']:.2f} miles")
        print(f"Average Fare: ${stats['avg_fare']:.2f}")
        print(f"Average Trip Duration: {stats['avg_duration']:.2f} minutes")
        print("="*50 + "\n")

if __name__ == "__main__":
    # Example usage
    analysis = UberAnalysis('data/uber_rides.csv')
    # Uncomment to run analysis
    # df = analysis.load_data()
    # analysis.summary_report()
