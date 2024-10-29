import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def load_data_from_folder(folder_path):
    data_frames = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            
            # print(f"Loaded {filename} with columns: {df.columns.tolist()}")
            if 'start' in df.columns and 'status' in df.columns:
                data_frames.append(df)
            else:
                print(f"Warning: {filename} does not contain the required columns.")
    return data_frames


low_dim_data = load_data_from_folder('low_batch')
medium_dim_data = load_data_from_folder('medium_batch')


low_combined = pd.concat(low_dim_data, ignore_index=True)
medium_combined = pd.concat(medium_dim_data, ignore_index=True)


def plot_combined_survival_data(df, title):
    
    df['Survival_Time'] = df['stop'] - df['start']  
    df['Event'] = df['status']

    
    plt.figure(figsize=(12, 6))
    plt.hist(df['Survival_Time'], bins=50, alpha=0.5, color='blue', label='Survival Time', density=True)
    plt.title(title + ' - Survival Time Distribution')
    plt.xlabel('Survival Time')
    plt.ylabel('Density')
    plt.grid()
    plt.legend()
    plt.show()

   
    event_counts = np.bincount(df['Event'])
    plt.figure(figsize=(12, 6))
    plt.bar(['Censored', 'Event'], event_counts, color=['orange', 'green'])
    plt.title(title + ' - Event Rate vs Censor Rate')
    plt.ylabel('Count')
    plt.xticks(ticks=[0, 1], labels=['Censored', 'Event']) 
    plt.grid()
    plt.show()

plot_combined_survival_data(low_combined, 'Combined Low Dimensional Datasets')

plot_combined_survival_data(medium_combined, 'Combined Medium Dimensional Datasets')