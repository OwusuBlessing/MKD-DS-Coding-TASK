from src.product_recommender.utils.common import read_yaml
from src.product_recommender.logging import logger
import pandas as pd
from src.product_recommender.utils.common import read_yaml,save_filecsv,remove_non_numeric
import re

class DataPreprocessing:

    def __init__(self,data_path,location,save_name):
        self.data_path = data_path
        self.location = location
        self.save_name = save_name
    
    def _read_data(self):

        logger.info("Reading rata.........")
        df = pd.read_csv(self.data_path)
        logger.info("Data is done loading.....")
        

        return df

    def _drop_columns(self):
        df = self._read_data()
        cols = ['InvoiceNo', 'CustomerID', 'Quantity', 'InvoiceDate', 'Country']
        df = df.drop(columns=cols,axis=1)
        logger.info(f"irrelevant columns: {cols} dropped")
        return df
    
    def _clean_features(self):
        # Clean the stock codes by removing alphanumeric characters
        df =self._drop_columns()
        stock_codes = list(df["StockCode"])
        cleaned_stock_codes = [code.replace('ö', '').replace('^', '').strip().upper() for code in stock_codes]
        df["StockCode"] = cleaned_stock_codes
        logger.info(f"Cleaned feature Stockcode by removed non-numeric characters")
        
        return df
    
    def _treat_missing_values(self):

        df = self._clean_features()
        stockcode_description_map = df.groupby('StockCode')['Description'].first().to_dict()
        # Iterate over the DataFrame to fill missing Description values
        for index, row in df.iterrows():
            if pd.isnull(row['Description']):  # Check if Description is missing
                stock_code = row['StockCode']
                if stock_code in stockcode_description_map:
                    df.at[index, 'Description'] = stockcode_description_map[stock_code]

        logger.info("Filled missing values in Description column by category")

        return df
    
    def _remove_duplcates(self):

        df = self._treat_missing_values()
        df = df.drop_duplicates(subset=['StockCode'])
        logger.info("Dropped duplicates to get unique stocCode")  #drop remaning missing rows mising rows
        df = df.dropna()
        logger.info("Dropped remaining missing values")

        return df

    
    def _standardize_features(self):
        df = self._remove_duplcates()

        

        logger.info('Standardizig features')

        logger.info("Remove unwanted characters from Description column")
        product_list_no_dollar_sign = [product.replace('$', '') for product in list(df["Description"])]
        df["Description"] == product_list_no_dollar_sign
        df['UnitPrice'] = df['UnitPrice'].apply(remove_non_numeric)
        df["UnitPrice"]  = df["UnitPrice"].astype(float)
        logger.info("Comverted UnitPrice to float")

        return df
    
    def clean_data(self):
        data = self._standardize_features()

        logger.info("Data cleaning done")

        logger.info("Saving cleaned data......")
        
        product_list_no_dollar_sign = [product.replace('$', '') for product in list(data["Description"])]
        data["Description"] == product_list_no_dollar_sign
        
        save_filecsv(
            df = data,file_name=self.save_name,
            location=self.location
        )

        logger.info(f"Cleaned data is successfully save to {self.location}")