# Encoding: utf-8
"""
    written by:     Lawrence McDaniel
                    https://lawrencemcdaniel.com

    date:           jun-2023

    usage:          minimalist implementation of Logistic Regression model.
"""
import os

# Libraries to help with reading and manipulating data
import pandas as pd

# Libraries to help with data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the Machine Learning models we require from Scikit-Learn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# Code to ignore warnings from function usage
import warnings

warnings.filterwarnings("ignore")

# module variables
sns.set()
HERE = os.path.abspath(os.path.dirname(__file__))
hotel = pd.read_csv(os.path.join(HERE, "data", "reservations-db.csv"))
data = hotel.copy()
data = data.drop(["Booking_ID"], axis=1)
data["booking_status"] = data["booking_status"].apply(
    lambda x: 1 if x == "Canceled" else 0
)


# Creating metric function
def metrics_score(actual, predicted):
    print("Metrics Score.")
    print(classification_report(actual, predicted))

    cm = confusion_matrix(actual, predicted)
    plt.figure(figsize=(8, 5))

    sns.heatmap(
        cm,
        annot=True,
        fmt=".2f",
        xticklabels=["Not Cancelled", "Cancelled"],
        yticklabels=["Not Cancelled", "Cancelled"],
    )
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    plt.show()


def main():
    # hive off the dependent variable, "booking_status"
    X = data.drop(["booking_status"], axis=1)
    Y = data["booking_status"]

    # clean up our data.
    X = pd.get_dummies(X, drop_first=True)  # Encoding the Categorical features

    # Split data in train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.30, stratify=Y, random_state=1
    )

    # Fit a logistic regression model
    lg = LogisticRegression()
    lg.fit(X_train, y_train)

    # Set the optimal threshold (refer to the Jupyter Notebook to see how we arrived at 42)
    optimal_threshold = 0.42

    # Create a confusion matrix for the training data
    y_pred_train = lg.predict_proba(X_train)
    metrics_score(y_train, y_pred_train[:, 1] > optimal_threshold)

    # Create a confusion matrix for the test data
    y_pred_test = lg.predict_proba(X_test)
    metrics_score(y_test, y_pred_test[:, 1] > optimal_threshold)


if __name__ == "__main__":
    main()
