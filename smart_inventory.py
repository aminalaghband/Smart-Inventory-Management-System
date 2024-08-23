import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class SmartInventory:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.model = LinearRegression()

    def train_model(self):
        X = self.data[['day']].values
        y = self.data['sales'].values
        self.model.fit(X, y)

    def predict_sales(self, future_days):
        future_days = np.array(future_days).reshape(-1, 1)
        return self.model.predict(future_days)

    def optimize_inventory(self, safety_stock=10):
        predictions = self.predict_sales(range(1, 31))
        optimal_stock = predictions.mean() + safety_stock
        return optimal_stock

# Example usage
data = {
    'day': range(1, 31),
    'sales': np.random.randint(20, 100, size=30)
}

inventory_system = SmartInventory(data)
inventory_system.train_model()
print("Predicted sales for the next 30 days:", inventory_system.predict_sales(range(31, 61)))
print("Optimal stock level:", inventory_system.optimize_inventory())
