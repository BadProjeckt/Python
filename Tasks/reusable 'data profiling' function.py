#%% Import libraries
#Import libraries
import pandas as pd
import numpy as np
import pprint

#%% Get the data
#Get the data
df = pd.read_csv('C:/Users/Nick/Desktop/Python/Datasets/Electric Vehicle Specs Dataset (2025)/electric_vehicles_spec_2025.csv')
df.name = 'electric_vehicles_spec_2025'
#%% Define the function
def data_profiling(df):
    """    
    A function to perform data profiling on a given DataFrame.
    It takes:
     - df: A pandas DataFrame
    It prints:
     - Basic information about the dataset
    """
    null_cols = df.columns[df.isnull().any()]

    print(f'Data profiling for the dataset: {df.name}:')
    print('~'*128)
    print(f'The basic information:')
    print(f'The shape of the dataset: Rows: {df.shape[0]} Columns: {df.shape[1]}\n')
    print(f'Column name:')
    pprint.pprint(df.columns.tolist(), width=80, compact=True)
    print('\n')
    print(f'Data types:\n{df.dtypes}\n')
    print(f'Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB')
    print('-'*128)

    print(f'Null information:')
    print(f'Combined null amount: {df.isnull().sum().sum()}\n')
    nu = df.agg(['count']).T
    nu['null_cnt'] = len(df) - nu['count'] 
    nu['null_pct'] = nu['null_cnt'] * 100 / len(df)
    nu = nu.sort_values(by='null_cnt', ascending=False)
    print(nu.round(2).to_string())
    print('-'*128)

    print('Uniques information:')
    un = df.agg(['nunique']).T
    un['unique_percentage'] = un['nunique'] * 100 / df.shape[0] 
    un = un.sort_values(by='nunique', ascending=False)

    print(un.round(2).to_string())
    print(f'Combined unique amount: {df.nunique().sum()}\n')
    print('-'*128)

    print('Descriptive statistics:\nFor numerical columns:')

    num = df.select_dtypes(np.number)
    if not num.empty:
        base = num.agg(['min', 'max', 'mean', 'std', 'median', 'skew', 'kurt']).T

        base['zero_count'] = (num == 0).sum()
        base['zero_percentage'] = base['zero_count'] * 100 / len(df)

        base['negative_count']  = (num < 0).sum()
        base['negative_percentage']  = base['negative_count'] * 100 / len(df)
        base = base.rename(columns={'min': 'min_value', 
                                    'max': 'max_value', 
                                    'mean': 'mean_value', 
                                    'std': 'std_value', 
                                    'median': 'median_value', 
                                    'skew': 'skewness', 
                                    'kurt': 'kurtosis'})
        print(base.round(2).to_string())
        print('-'*128)
    else:
        print('\nNo numerical columns found.\n')

    dates = df.select_dtypes('datetime')
    if not dates.empty:
        print('\nFor datetime columns:')
        dates = dates.agg(['min', 'max']).T
        dates['date_range'] = (dates['max'] - dates['min']).dt.days
        dates = dates.rename(columns={'min': 'min_date', 
                                      'max': 'max_date'})
        print(dates.round(2).to_string())
        print('-'*128)
    else:
        print('\nNo datetime columns found.\n')
#%%
data_profiling(df)

# %%
