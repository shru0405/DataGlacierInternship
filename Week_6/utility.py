#VALIDATING
import logging
import os
import subprocess
import yaml
import pandas as pd
import datetime 
import gc
import re
import configparser

def read_config_file(filepath='store.yaml'):
    with open(filepath, 'r') as stream:
        try:
            return yaml.load(stream, Loader=yaml.Loader)
        except yaml.YAMLError as exc:
            logging.error(exc)


def replacer(string, char):
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string) 
    return string

def col_header_val(df2,table_config):
    '''
    replace whitespaces in the column
    and standardized column names
    '''
    df2.columns = df2.columns.str.lower()
    df2.columns = df2.columns.str.replace('[^\w]','_',regex=True)
    df2.columns = list(map(lambda x: x.strip('_'), list(df2.columns)))
    df2.columns = list(map(lambda x: replacer(x,'_'), list(df2.columns)))
    expected_col = list(map(lambda x: x.lower(),  table_config['columns']))
    expected_col.sort()
    df2.columns =list(map(lambda x: x.lower(), list(df2.columns)))
    df2 = df2.reindex(sorted(df2.columns), axis=1)
    if len(df2.columns) == len(expected_col) and list(expected_col)  == list(df2.columns):
        print("column name and column length validation passed")
        return 1
    else:
        print("column name and column length validation failed")
        mismatched_columns_file = list(set(df2.columns).difference(expected_col))
        print("Following File columns are not in the YAML file",mismatched_columns_file)
        missing_YAML_file = list(set(expected_col).difference(df2.columns))
        print("Following YAML columns are not in the file uploaded",missing_YAML_file)
        logging.info(f'df2 columns: {df2.columns}')
        logging.info(f'expected columns: {expected_col}')
        return 0
