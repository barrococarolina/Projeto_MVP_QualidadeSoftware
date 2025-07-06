from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

class Trainer:
    def __init__(self, X, y, test_size=0.2, random_state=42):
        self.X = X
        self.y = y
        self.test_size = test_size
        self.random_state = random_state

        self.model = RandomForestRegressor(n_estimators=100, random_state=self.random_state)
        self.scaler = StandardScaler()

    def split_and_scale(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=self.test_size, random_state=self.random_state
        )
        self.X_train_scaled = self.scaler.fit_transform(X_train)
        self.X_test_scaled = self.scaler.transform(X_test)
        self.y_train = y_train
        self.y_test = y_test

    def train(self):
        self.model.fit(self.X_train_scaled, self.y_train)

    def evaluate(self):
        y_pred = self.model.predict(self.X_test_scaled)
        score = r2_score(self.y_test, y_pred)
        return score

    def train_and_evaluate(self):
        self.split_and_scale()
        self.train()
        return self.evaluate(), self.model, self.scaler