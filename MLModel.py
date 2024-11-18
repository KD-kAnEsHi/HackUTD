import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

file_path = 'plant_growth_data.csv'  
data = pd.read_csv(file_path)

X = data[['Temperature', 'Humidity', 'Sunlight_Hours']]
y = data['Growth_Milestone']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

gb_param_grid = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

gb_grid_search = GridSearchCV(
    GradientBoostingClassifier(random_state=42),
    gb_param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
gb_grid_search.fit(X_train, y_train)

gb_best_params = gb_grid_search.best_params_
best_gb_model = GradientBoostingClassifier(
    n_estimators=gb_best_params['n_estimators'],
    learning_rate=gb_best_params['learning_rate'],
    max_depth=gb_best_params['max_depth'],
    min_samples_split=gb_best_params['min_samples_split'],
    min_samples_leaf=gb_best_params['min_samples_leaf'],
    random_state=42
)
best_gb_model.fit(X_train, y_train)

cross_val_scores = cross_val_score(best_gb_model, X_train, y_train, cv=5, scoring='accuracy')
cross_val_mean_accuracy = np.mean(cross_val_scores)

temp_range = np.linspace(X['Temperature'].min(), X['Temperature'].max(), 20)
humidity_range = np.linspace(X['Humidity'].min(), X['Humidity'].max(), 20)
sunlight_range = np.linspace(X['Sunlight_Hours'].min(), X['Sunlight_Hours'].max(), 20)

highest_probability = 0
best_conditions = None

for temp in temp_range:
    for humidity in humidity_range:
        for sunlight in sunlight_range:
            current_conditions = pd.DataFrame([[temp, humidity, sunlight]], columns=X.columns)
            prob_good_growth = best_gb_model.predict_proba(current_conditions)[0, 1]
            if prob_good_growth > highest_probability:
                highest_probability = prob_good_growth
                best_conditions = (temp, humidity, sunlight)

ideal_temperature = round(best_conditions[0])
ideal_humidity = round(best_conditions[1])
ideal_sunlight = round(best_conditions[2])

def get_cross_val_mean_accuracy():
    return cross_val_mean_accuracy

def get_ideal_temperature():
    return ideal_temperature

def get_ideal_humidity():
    return ideal_humidity

def get_ideal_sunlight():
    return ideal_sunlight

if __name__ == "__main__":
    print("Cross-Validation Mean Accuracy:", get_cross_val_mean_accuracy())
    print("Best Parameters:", gb_best_params)
    print("Ideal Temperature:", get_ideal_temperature())
    print("Ideal Humidity:", get_ideal_humidity())
    print("Ideal Sunlight:", get_ideal_sunlight())