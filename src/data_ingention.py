import pandas as pd
import os
import logging
from sklearn.model_selection import train_test_split

logs_dir = "logs"
os.makedirs(logs_dir,exist_ok=True)

logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

log_file_path = os.path.join(logs_dir, 'data_ingestion.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def load_data(data_file_path:str) -> pd.DataFrame:
    """This function use to load data.
    """
    try:
        df = pd.read_csv(data_file_path,on_bad_lines='skip')
        logger.debug("File load successfully")
        return df
    except FileExistsError as e:
        logger("File not found")
    except Exception as e:
        logger.debug("Unexpected exception occured",e)
        print(e)

if __name__ == "__main__":
    load_data("/media/minato/Local Disk/My Stuff/Data Science/MLOPS/MLOPS-proj-basic/notebooks/Credit Card Defaulter Prediction.csv")