import glob
import pandas as pd

def create_data_df(df_name,data_path):
    
    # Creating dataframe of entire transcriptions
    for f in glob.glob(data_path):
        df_name = df_name.append(pd.read_csv(f,sep=';'),ignore_index=True)
    
    # combine multiple speech, annotation columns to one and drop rest of columns
    if 'Speech' not in df_name.columns:
        df_name['Speech'] = ''    
    if 'speech' in df_name.columns:
        df_name['Speech'] = df_name[['Speech','speech']].fillna('').sum(axis=1)   
    if 'transcription' in df_name.columns:
        df_name['Speech'] = df_name[['Speech','transcription']].fillna('').sum(axis=1)
    
    if 'sentimentAnnotation' not in df_name.columns:
        df_name['sentimentAnnotation'] = 0    
    if 'sentimentAnnotations' in df_name.columns:
        df_name['sentimentAnnotation'] = df_name[['sentimentAnnotation','sentimentAnnotations']].fillna(0).sum(axis=1)
    if 'sentimentannotations' in df_name.columns:
        df_name['sentimentAnnotation'] = df_name[['sentimentAnnotation','sentimentannotations']].fillna(0).sum(axis=1)
    
    # Remove neutral annotations
    df_name = df_name.query('sentimentAnnotation != 0')
    
    df_name = df_name[['Speech','sentimentAnnotation']].reset_index(drop=True)  
    return df_name

'C:\\Users\\Niraj\\Downloads\\MOUD\\MOUD\\VideoReviews\\transcriptions\\'
df = pd.DataFrame()
df = create_data_df(df)