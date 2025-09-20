import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class DroneDataManager:
    """Manages drone fleet data and operations"""
    
    def __init__(self):
        self.drones = self._generate_drone_data()
        self.missions = self._generate_mission_data()
    
    def _generate_drone_data(self):
        """Generate sample drone fleet data"""
        drone_ids = [f"DRONE-{i:03d}" for i in range(1, 21)]
        statuses = ["Active", "Charging", "Maintenance", "Emergency"]
        
        drones = []
        for drone_id in drone_ids:
            drones.append({
                'id': drone_id,
                'status': random.choice(statuses),
                'battery': random.randint(20, 100),
                'mission': f"Mission-{random.randint(100, 999)}" if random.choice([True, False]) else "Standby",
                'location': f"Location-{random.randint(1, 10)}",
                'last_update': datetime.now() - timedelta(minutes=random.randint(1, 30))
            })
        return drones
    
    def _generate_mission_data(self):
        """Generate sample mission data"""
        missions = []
        for i in range(50):
            missions.append({
                'id': f"MISSION-{i+1:03d}",
                'type': random.choice(["Medical Supply", "Emergency Response", "Routine Delivery"]),
                'status': random.choice(["Completed", "In Progress", "Scheduled"]),
                'delivery_time': random.randint(15, 45),
                'success': random.choice([True, True, True, False])  # 75% success rate
            })
        return missions
    
    def get_fleet_overview(self):
        """Get fleet overview statistics"""
        active_drones = len([d for d in self.drones if d['status'] == 'Active'])
        total_drones = len(self.drones)
        
        return {
            'active': active_drones,
            'total': total_drones,
            'change': random.randint(-2, 3)
        }
    
    def get_detailed_fleet_status(self):
        """Get detailed fleet status"""
        return self.drones
    
    def get_mission_stats(self):
        """Get mission statistics"""
        completed_today = len([m for m in self.missions if m['status'] == 'Completed'])
        avg_delivery_time = np.mean([m['delivery_time'] for m in self.missions if m['status'] == 'Completed'])
        
        return {
            'completed_today': completed_today,
            'change_percent': random.uniform(-5, 15),
            'avg_delivery_time': avg_delivery_time,
            'delivery_time_change': random.uniform(-2, 3)
        }
    
    def get_success_rate(self):
        """Get mission success rate"""
        successful_missions = len([m for m in self.missions if m['success']])
        total_missions = len(self.missions)
        return (successful_missions / total_missions) * 100
    
    def get_delivery_trends(self):
        """Get delivery time trends"""
        dates = [datetime.now() - timedelta(days=i) for i in range(7, 0, -1)]
        trends = []
        
        for date in dates:
            trends.append({
                'date': date.strftime('%Y-%m-%d'),
                'avg_delivery_time': random.uniform(20, 35)
            })
        
        return pd.DataFrame(trends)
    
    def get_mission_distribution(self):
        """Get mission type distribution"""
        types = {}
        for mission in self.missions:
            mission_type = mission['type']
            types[mission_type] = types.get(mission_type, 0) + 1
        return types
    
    def get_battery_distribution(self):
        """Get battery level distribution"""
        levels = {"High (80-100%)": 0, "Medium (50-79%)": 0, "Low (20-49%)": 0}
        
        for drone in self.drones:
            battery = drone['battery']
            if battery >= 80:
                levels["High (80-100%)"] += 1
            elif battery >= 50:
                levels["Medium (50-79%)"] += 1
            else:
                levels["Low (20-49%)"] += 1
        
        return levels
