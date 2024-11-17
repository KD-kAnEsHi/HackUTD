import pandas as pd
import json
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from MLModel import get_cross_val_mean_accuracy, best_gb_model  # Import existing functions and model

# Load JSON sensor data
json_file_path = '/Users/kazangue/CS-Files/HackUTD/AI/sensors_db.sensors.json'
with open(json_file_path, 'r') as f:
    sensor_data = json.load(f)

# Convert JSON to DataFrame
sensor_df = pd.DataFrame(sensor_data)

# Rename columns to match the model's expected input
sensor_df.rename(columns={"Light": "Sunlight_Hours"}, inplace=True)

# Select relevant features for the model
features = sensor_df[['Temperature', 'Humidity', 'Sunlight_Hours']]

# Classify conditions (Good/Bad)
sensor_df['Growth_Milestone'] = best_gb_model.predict(features)

# Load existing CSV
csv_file_path = '/Users/kazangue/CS-Files/HackUTD/AI/plant_growth_data.csv'
existing_data = pd.read_csv(csv_file_path)

# Append new data to the CSV
updated_data = pd.concat([existing_data, sensor_df[['Temperature', 'Humidity', 'Sunlight_Hours', 'Growth_Milestone']]])

# Save updated CSV
updated_csv_path = 'updated_plant_growth_data.csv'
updated_data.to_csv(updated_csv_path, index=False)

# Reload the updated dataset to retrain the model
updated_data = pd.read_csv(updated_csv_path)

# Define features and target with the updated data
X_updated = updated_data[['Temperature', 'Humidity', 'Sunlight_Hours']]
y_updated = updated_data['Growth_Milestone']

# Train-test split for the updated dataset
X_train_updated, X_test_updated, y_train_updated, y_test_updated = train_test_split(
    X_updated, y_updated, test_size=0.3, random_state=42
)

# Train the Gradient Boosting model with the updated data
model_updated = GradientBoostingClassifier(
    n_estimators=200, learning_rate=0.01, max_depth=10, random_state=42
)
model_updated.fit(X_train_updated, y_train_updated)

# Calculate accuracy on the updated test set
y_test_pred_updated = model_updated.predict(X_test_updated)
accuracy_updated = accuracy_score(y_test_updated, y_test_pred_updated)

# Output the old and new accuracies
print("Old Accuracy (Cross-Validation):", get_cross_val_mean_accuracy())
print("New Accuracy (Test Set):", accuracy_updated)