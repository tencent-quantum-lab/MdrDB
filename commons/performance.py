from sklearn.metrics import r2_score, make_scorer, roc_auc_score, precision_recall_curve, auc
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
import numpy as np
from scipy.stats import pearsonr
from .utils import load_obj
import pandas as pd

def get_rmse(y_test, y_pred):
    rmse = math.sqrt(mean_squared_error(y_test, y_pred))
    return rmse

def get_pearson(y_test,y_pred):
    corr, p_value = pearsonr(y_test, y_pred)
    return corr

def get_auc_roc(y_test, y_pred):
    auc_roc = roc_auc_score(y_test, y_pred)
    return auc_roc

def get_R2(y_test, y_pred):
    r2 = r2_score(y_test, y_pred)
    return r2

def get_mae(y_test, y_pred):
    mae = mean_absolute_error(y_test, y_pred)
    return mae

def get_auc_prc(y_test, y_pred):
    true_bool = np.array([i > 1.36 for i in y_test])   # identify resistant mutations (ddG > 1.36 kcal/mol)
    pred_bool = np.array(y_pred)                       # the scores are the calc ddg (higher ddg = higher probability of resistance)
    precision, recall, thresholds = precision_recall_curve(true_bool, pred_bool)
    auc_pr = auc(recall, precision)
    return auc_pr

def cal_performance_groupcv(models_list, save_path, save_ddg, n_fold=5):
    result_ddg = load_obj(save_filename=save_ddg, save_path=save_path)
    result_ddg = pd.DataFrame(result_ddg)
    
    rmse_dict = {}
    pears_dict = {}
    auprc_dict = {}
    
    n_iter = int(len(result_ddg[models_list[0]].iloc[0])/n_fold)
    
    for method in models_list:
        rmse_dict[method] = []
        pears_dict[method] = []
        auprc_dict[method] = []
    
    for method in models_list:
        Y_exp = result_ddg[method].iloc[0]
        Y_pred = result_ddg[method].iloc[1]
        
        for i in range(n_fold):
            if i != n_fold:
                y_exp = result_ddg[method].iloc[0][n_iter*i : n_iter*(i+1)]
                y_pred = result_ddg[method].iloc[1][n_iter*i : n_iter*(i+1)]
            else:
                y_exp = result_ddg[method].iloc[0][n_iter*i : ]
                y_pred = result_ddg[method].iloc[1][n_iter*i : ]

            rmse = get_rmse(y_exp, y_pred)
            pears = get_pearson(y_exp, y_pred)
            auprc = get_auc_prc(y_exp, y_pred)
            
            rmse_dict[method].append(rmse)
            pears_dict[method].append(pears)
            auprc_dict[method].append(auprc)
    
    # statistic the results
    results = pd.DataFrame(columns=['Methods', 'RMSE_avg', 'RMSE_std', 'Pearson_avg', 'Pearson_std', 'AUPRC_avg', 'AUPRC_std'])
    
    for row_idx, model in enumerate(models_list):
        results.loc[row_idx] = [model, 
                                np.mean(rmse_dict[model]), np.std(rmse_dict[model]), 
                                np.mean(pears_dict[model]), np.std(pears_dict[model]), 
                                np.mean(auprc_dict[model]), np.std(auprc_dict[model])]
    results = results.round(3)
    results = results.sort_values(by="RMSE_avg", ascending=False).reset_index(drop=True)
    return results