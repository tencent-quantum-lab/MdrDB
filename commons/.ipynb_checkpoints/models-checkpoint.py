# Create the model
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import ExtraTreesRegressor, AdaBoostRegressor, RandomForestRegressor
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor
from sklearn.model_selection import KFold, GroupKFold, LeavePGroupsOut
from sklearn.model_selection import cross_val_score, cross_validate, cross_val_predict
from sklearn.metrics import r2_score, make_scorer, roc_auc_score, precision_recall_curve, auc, mean_absolute_error
from sklearn.neural_network import MLPRegressor
from sklearn import svm
from sklearn import linear_model


def InstantiationModel(model_name):
    
    if model_name == 'ElasticNet':
        model = linear_model.ElasticNet(alpha=0.1,l1_ratio=0.5)
    elif model_name == 'Lasso':
        model = linear_model.Lasso(alpha=0.1)
    elif model_name == 'DecisionTree':
        model = DecisionTreeRegressor()
    elif model_name == 'RandomForest':
        model = RandomForestRegressor(n_estimators=500, n_jobs= -1)
    elif model_name == 'ExtraTrees':
        model = ExtraTreesRegressor(n_estimators=500, n_jobs= -1)
    elif model_name == 'Bagging':
        model = BaggingRegressor(n_estimators=500, n_jobs= -1)
    elif model_name == 'AdaBoost':
        model = AdaBoostRegressor(n_estimators=500)
    elif model_name == 'GradientBoost':
        model = GradientBoostingRegressor(n_estimators=500)
    elif model_name == 'SVR':
        model = svm.SVR()
    elif model_name == 'MLP':
        model = MLPRegressor(hidden_layer_sizes=(64, 128, 64, ), activation='relu', solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.001)
    
    return model