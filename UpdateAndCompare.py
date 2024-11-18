import pandas as pd
import json
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from MLModel import get_cross_val_mean_accuracy, best_gb_model  # Import existing functions and model

json_file_path = 'sensors_db.sensors.json'
with open(json_file_path, 'r') as f:
    sensor_data = json.load(f)

sensor_df = pd.DataFrame(sensor_data)

sensor_df.rename(columns={"Light": "Sunlight_Hours"}, inplace=True)

features = sensor_df[['Temperature', 'Humidity', 'Sunlight_Hours']]

sensor_df['Growth_Milestone'] = best_gb_model.predict(features)

csv_file_path = 'plant_growth_data.csv'
existing_data = pd.read_csv(csv_file_path)

updated_data = pd.concat([existing_data, sensor_df[['Temperature', 'Humidity', 'Sunlight_Hours', 'Growth_Milestone']]])

updated_csv_path = 'updated_plant_growth_data.csv'
updated_data.to_csv(updated_csv_path, index=False)

updated_data = pd.read_csv(updated_csv_path)

X_updated = updated_data[['Temperature', 'Humidity', 'Sunlight_Hours']]
y_updated = updated_data['Growth_Milestone']

X_train_updated, X_test_updated, y_train_updated, y_test_updated = train_test_split(
    X_updated, y_updated, test_size=0.3, random_state=42
)

model_updated = GradientBoostingClassifier(
    n_estimators=200, learning_rate=0.01, max_depth=10, random_state=42
)
model_updated.fit(X_train_updated, y_train_updated)

y_test_pred_updated = model_updated.predict(X_test_updated)
accuracy_updated = accuracy_score(y_test_updated, y_test_pred_updated)

print("Old Accuracy (Cross-Validation):", get_cross_val_mean_accuracy())
print("New Accuracy (Test Set):", accuracy_updated)
