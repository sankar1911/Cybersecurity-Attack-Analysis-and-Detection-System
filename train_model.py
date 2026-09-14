import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("cybersecurity_attacks.csv")

feature_columns = [
    "Source Port",
    "Destination Port",
    "Protocol",
    "Packet Length",
    "Traffic Type",
    "Anomaly Scores",
    "Severity Level"
]

X = df[feature_columns]
y = df["Attack Type"]

categorical_columns = [
    "Protocol",
    "Traffic Type",
    "Severity Level"
]

numeric_columns = [
    "Source Port",
    "Destination Port",
    "Packet Length",
    "Anomaly Scores"
]

preprocessor = ColumnTransformer([
    ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
    ("numeric", "passthrough", numeric_columns)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("random_forest", RandomForestClassifier(n_estimators=100, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "random_forest_model.pkl")

print("New pipeline model created successfully!")