# train_model.py
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(df):
    X = df[['feature1', 'feature2']]
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=100)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)

        # MLflow logs
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")

        print("MSE logged to MLflow:", mse)

    return y_test.values, y_pred
