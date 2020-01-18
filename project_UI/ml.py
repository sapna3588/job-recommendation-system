import  pandas as pd
import numpy as np
from sklearn import preprocessing

# load the data
def load_data(file):
    df = pd.read_csv(file)
    # split the data into x and y
    x = df.iloc[:, [2,3,7,8,10,11,12]].values
    y = df.iloc[:, 5].values.astype("int")
    standardized_X = preprocessing.scale(y)
    return x, y

def clean_and_split_data(x, y):
    # clean the data
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    # convert the gender into numeric values
    # v=x[:, 2]
    x[:, 0] = encoder.fit_transform(x[:, 0])
    x[:, 1] = x[:, 1].astype(str)
    x[:, 1] = encoder.fit_transform(x[:, 1])
    x[:, 2] = encoder.fit_transform(x[:, 2])
    #THI CODE IS FOR GETTING ALL CATAGORICAL VALUES OF TEXTUAL DATA
    # dgh = encoder.fit_transform(x[:, 2])
    #
    # dict1 = {}
    # for (val, i) in zip(v, dgh):
    #     # print(f"{val}:{i}")
    #     dict1[val] = i
    # print(dict1)

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=1234)
    return x_train, x_test, y_train, y_test


def build_linear_regression_model():
    # build the model
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor = regressor.fit(x_train, y_train)
    # from sklearn.metrics import mean_squared_error
    # value = regressor.predict([[37,29,0,1,1,0]])
    # # print(y_test)
    # print(value)
    # # for (y,p) in
    # mse = (y_test - value) ** 2
    # print(mse)
    #
    # sum = 0;
    #
    # for val in mse:
    #     sum = sum + val;
    #
    # error = sum / len(y_test)
    # print(error)
    # fmse = mean_squared_error(y_test, value)
    # print(fmse)

    return regressor

#IS ONLY USED FOR CLASSIFICATION
# def build_naive_bayes_model(x_train, y_train):
#     from sklearn.naive_bayes import GaussianNB
#     regressor = GaussianNB()
#     regressor = regressor.fit(x_train, y_train)
#     return  regressor
#
#
# def build_svr_model(x_train, y_train):
#     from sklearn.svm import SVR
#     regressor = SVR()
#     regressor = regressor.fit(x_train, y_train)
#     return  regressor

def build_random_forest_model():
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error
    regressor = RandomForestRegressor()
    regressor = regressor.fit(x_train, y_train)
    # value = regressor.predict(x_test)
    #
    # # print(y_test)
    # print(np.round(value))

    # mse=(y_test-value)**2
    # sum=0;count=0
    # for val in mse:
    #     sum=sum+val;
    #     count+=1
    # error=sum/count
    # print(error)
    #
    # fmse=mean_squared_error(y_test,value)
    # print(fmse)
    return regressor

# def build_decision_tree_model(x_train,y_train):
#     from sklearn.tree import DecisionTreeRegressor
#     regressor=DecisionTreeRegressor()
#     regressor=regressor.fit(x_train,y_train)
#     return regressor
#
#
# def build_gradient_boost_model(x_train, y_train):
#     from sklearn.ensemble import GradientBoostingRegressor
#     regressor = GradientBoostingRegressor()
#     regressor = regressor.fit(x_train, y_train)
#     return regressor


# def build_xgboost_model(x_train, y_train):
#     from xgboost import XGBRegressor
#     regressor = XGBRegressor()
#     regressor = regressor.fit(x_train, y_train)
#     return regressor

# def cross_validation(algorithm, regressor, x_test, y_test):
#     # evaluate the model
#     predictions = regressor.predict(x_test)
#     print(f"{algorithm}:{predictions}")
#     from sklearn.metrics import confusion_matrix
#     cm = confusion_matrix(y_test, predictions)
#     accuracy = (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1])
#     print(f"accuracy of {algorithm} is {accuracy * 100}%")
#     return print_accuracy()
#
# def print_accuracy(name, predictions):
#     from sklearn.metrics import confusion_matrix
#     cm = confusion_matrix(predictions, y_test)
#     accuracy = (cm[0][0] + cm[1][1] + cm[2][2]) / (
#                 cm[0][0] + cm[0][1] + cm[0][2] + cm[1][0] + cm[1][1] + cm[1][2] + cm[2][0] + cm[2][1] + cm[2][2])
#     print(f"{name} has accuracy: {accuracy * 100}%")

# predict the output
x,y = load_data('./final_clean_csv.csv')
# clean_and_split_data(x,y)
x_train, x_test, y_train, y_test = clean_and_split_data(x, y)
build_random_forest_model()
# build_linear_regression_model()