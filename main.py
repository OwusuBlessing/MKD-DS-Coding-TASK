
from src.product_recommender.data_preparation.Data_preprocessing import DataPreprocessing
from src.product_recommender.data_preparation.vector_db_setup import VectorDB 
from src.product_recommender.endpoints.natural_query import query
from sentence_transformers import SentenceTransformer
from src.product_recommender.OCR.extract_text import extract_text
from src.product_recommender.Webscraper.scraper import run_scraper


print("Running data preparation pipeline..................")
print("****************************************************")
data_path = "Artifacts/data_preparation/dataset.csv"
location =  "Artifacts/data_preparation"
save_file_name = "Clean_data.CSV"
data_preprocessor = DataPreprocessing(data_path=data_path,
                                      location=location,
                                      save_name=save_file_name)

#data_preprocessor.clean_data()
print("data preparation pipeline done..................")
print("****************************************************")


print("Vector database setup started ..................")
print("****************************************************")
#vectordb = VectorDB(data_path="Artifacts/data_preparation/Cleaned_data.csv")
#vectordb.setup_vectordb()
print("Vector database setup done ..................")
print("****************************************************")


print("Training data scraping started ..................")
print("****************************************************")
#run_scraper()
print("Training data scraping completed ..................")
print("****************************************************")
                                                                             

from src.product_recommender.image_recognition.predict import data_transform,load_tinyvgg_model,predict


loaded_model = load_tinyvgg_model(input_shape=3,
                                  model_save_path="Artifacts/trained_models/tinyvgg_model_1.pth",
                                  hidden_units=10,
                                  output_shape=3,
                                  device ="cpu"
)

x,y = predict(model=loaded_model,image_path="Uploads/choco-test.jpg",
              transform = data_transform)

print(x,y)

