import random
from datetime import datetime, timedelta

class MedicalSupplyManager:
    """Manages medical supplies inventory and tracking"""
    
    def __init__(self):
        self.supplies = self._generate_supply_data()
        self.inventory_log = self._generate_inventory_log()
    
    def _generate_supply_data(self):
        """Generate sample medical supplies data"""
        supply_types = [
            "Blood Bags", "IV Fluids", "Bandages", "Antibiotics", 
            "Pain Medication", "Surgical Tools", "Oxygen Tanks", 
            "Defibrillators", "Stretchers", "First Aid Kits"
        ]
        
        supplies = []
        for supply_type in supply_types:
            supplies.append({
                'type': supply_type,
                'quantity': random.randint(50, 200),
                'min_threshold': random.randint(20, 50),
                'location': f"Storage-{random.randint(1, 5)}",
                'expiry_date': datetime.now() + timedelta(days=random.randint(30, 365)),
                'status': "Available" if random.choice([True, True, False]) else "Low Stock"
            })
        
        return supplies
    
    def _generate_inventory_log(self):
        """Generate inventory movement log"""
        log_entries = []
        for i in range(30):
            log_entries.append({
                'timestamp': datetime.now() - timedelta(hours=random.randint(1, 72)),
                'action': random.choice(["Restocked", "Used", "Transferred", "Expired"]),
                'supply_type': random.choice([s['type'] for s in self.supplies]),
                'quantity': random.randint(1, 20),
                'location': f"Location-{random.randint(1, 10)}"
            })
        
        return sorted(log_entries, key=lambda x: x['timestamp'], reverse=True)
    
    def get_inventory_overview(self):
        """Get inventory overview statistics"""
        total_supplies = sum(s['quantity'] for s in self.supplies)
        low_stock_count = len([s for s in self.supplies if s['status'] == 'Low Stock'])
        
        return {
            'total_items': total_supplies,
            'availability': random.uniform(85, 98),
            'change': random.uniform(-3, 5),
            'low_stock_items': low_stock_count
        }
    
    def get_supply_status(self):
        """Get detailed supply status"""
        return self.supplies
    
    def get_inventory_log(self, limit=10):
        """Get recent inventory activities"""
        return self.inventory_log[:limit]
    
    def check_expiry_alerts(self):
        """Check for supplies nearing expiry"""
        alerts = []
        for supply in self.supplies:
            days_to_expiry = (supply['expiry_date'] - datetime.now()).days
            if days_to_expiry <= 30:
                alerts.append({
                    'supply_type': supply['type'],
                    'days_to_expiry': days_to_expiry,
                    'location': supply['location']
                })
        return alerts
    
    def get_supply_distribution(self):
        """Get supply distribution by location"""
        distribution = {}
        for supply in self.supplies:
            location = supply['location']
            if location not in distribution:
                distribution[location] = 0
            distribution[location] += supply['quantity']
        return distribution
