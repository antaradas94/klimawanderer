import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_name, y_var):    
    df = pd.read_csv(file_name)
    y = df[y_var]
    X = df.drop(columns=[y_var])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    return X_train, X_test, y_train, y_test

def lin_reg(X_train, y_train, X_test):
    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    return y_pred