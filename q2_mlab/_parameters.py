import numpy as np


class ParameterGrids:
    def get(algorithm):
        grids = {
            "LinearSVC": {
                'penalty': ['l2'],
                'tol': [1e-4, 1e-3, 1e-2, 1e-1],
                'loss': ['hinge', 'squared_hinge'],
                'random_state': [2018]
            },
            "LinearSVR": {
                "C": [1e-4, 1e-2, 1e-1, 1e0, 1e1, 1e2, 1e4],
                "epsilon": [1e-2, 1e-1, 0, 1],
                "loss": ["squared_epsilon_insensitive", "epsilon_insensitive"],
                "random_state": [2018],
            },
            "RidgeClassifier": {
                "alpha": [1e-15, 1e-10, 1e-8, 1e-4],
                "fit_intercept": [True],
                "normalize": [True, False],
                "tol": [1e-1, 1e-2, 1e-3],
                "solver": [
                    "svd",
                    "cholesky",
                    "lsqr",
                    "sparse_cg",
                    "sag",
                    "saga",
                ],
                "random_state": [2018],
            },
            "RidgeRegressor": {
                "alpha": [1e-15, 1e-10, 1e-8, 1e-4],
                "fit_intercept": [True],
                "normalize": [True, False],
                "tol": [1e-1, 1e-2, 1e-3],
                "solver": [
                    "svd",
                    "cholesky",
                    "lsqr",
                    "sparse_cg",
                    "sag",
                    "saga",
                ],
                "random_state": [2018],
            },
            "RandomForestClassifier": {
                "n_estimators": [1000, 5000],
                "criterion": ["gini", "entropy"],
                "max_features": ["sqrt", "log2", None] + list(np.arange(0.01, 1, 0.2)),
                "max_depth": [None],
                "n_jobs": [-1],
                "random_state": [2018],
                "bootstrap": [True, False],
                "min_samples_split": list(np.arange(0.01, 1, 0.2)),
                "min_samples_leaf": list(np.arange(0.01, 0.5, 0.1)) + [1],
            },
            "RandomForestRegressor": {
                'n_estimators': [1000, 5000],
                'criterion': ['mse'],
                'max_features': ['auto', 'sqrt', 'log2'],
                'max_depth': [None],
                'n_jobs': [-1],
                'random_state': [2018],
                'bootstrap': [True, False],
                'min_samples_split': list(np.arange(0.01, 1, 0.2)),
                'min_samples_leaf': list(np.arange(0.01, .5, 0.1)) + [1],
            },
        }
        return grids[algorithm]
