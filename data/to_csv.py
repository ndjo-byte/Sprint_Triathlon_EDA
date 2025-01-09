import pandas as pd

from pathlib import Path #more modern and pytonic than os for path manipulation and file system operations


def to_df(dir_path='/Users/nathanjones/Downloads/EDA_p2/data/raw_tsv', sep='\t'):
    
    tsv_dict = {}

    dir_path = Path(dir_path) #turns to a path object which has .iterdir, .partent, .name, .suffix, .stem methods

    for file in dir_path.iterdir():
        
        try:
            if file.suffix=='.tsv':
            
                df = pd.read_csv(file, sep=sep)
                if 'Women' in file.stem:
                    df['Gender'] = 'Female'
                else:
                    df['Gender'] = 'Male'
                
                key = file.stem
                tsv_dict[key] = df
    
        except Exception as e:
            print(f'error handling {file.name}: {e}')


    if not tsv_dict:
        print('no .tsv files found in dir')

    final_df = pd.concat(tsv_dict.values(), ignore_index=True)
    print(f"Processed {len(tsv_dict)} files into a DataFrame with {final_df.shape[0]} rows and {final_df.shape[1]} columns.")


    return final_df

all_sprint_results = to_df()

try:
    all_sprint_results.to_csv('/Users/nathanjones/Downloads/EDA_p2/data/wtc_sprint_data/all_wtc_sprint_results.csv', index=False)
    print('Data saved successfully!')
except FileNotFoundError:
    print('Error: Directory does not exist. Please create it first.')
except PermissionError:
    print('Error: No write permissions for the directory.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')



