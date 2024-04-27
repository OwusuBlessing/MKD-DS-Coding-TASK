
from src.product_recommender.data_preparation.Data_preprocessing import DataPreprocessing
#from src.product_recommender.data_preparation.vector_db_setup import VectorDB 
from src.product_recommender.endpoints.natural_query import query
from sentence_transformers import SentenceTransformer
from src.product_recommender.OCR.extract_text import extract_text
from src.product_recommender.Webscraper.scraper import scrape


print("Running data preparation pipeline..................")
print("****************************************************")
data_path = "Artifacts/data_preparation/dataset.csv"
location =  "Artifacts/data_preparation"
save_file_name = "Clean_data.CSV"
data_preprocessor = DataPreprocessing(data_path=data_path,
                                      location=location,
                                      save_name=save_file_name)

""""
data_preprocessor.clean_data()

vectordb = VectorDB(data_path="Artifacts/data_preparation/Cleaned_data.csv")
vectordb.setup_vectordb()

result = query(
    "VORY DINER WALL CLOCK"
)

"""
#print(result)

#"WHITE HANGING HEART T-LIGHT HOLDER":"https://www.google.com/search?sca_esv=5d5b8bda91a2629d&rlz=1C1KNTJ_enNG1063NG1063&sxsrf=ACQVn0-LFtKZJMOHIwgIYggmKc33-HgCxQ:1714199679400&q=WHITE+HANGING+HEART+T-LIGHT+HOLDER&uds=AMwkrPueUEb7dRubD0hu0-5vnR-1M_1yL8dGsY7FHyLWM3oJuxTHNXtWw3s0G3PPqbS9xC7ixhk8eVt9oFDW9qvGE9R1DGcjabSte3qqdEpkoPLJHXh2avLQH2DPHREqyu66f2HCJCuUxvoJKaqmpDvH3WZBcX5hrSmZ1ZabGORv3IIQK1TmeMK0qCeI5mTPvueX9chiD0Gzj_TKp2sqH59I9sSe5DKQHoBCwMewKQR535a2ZwQOypcSyVj0R45D4kEZL11kJSJkBALSAafQRVYcX75N_pksmE6hRM4tB3JArRljWF3u72bijpKwflMFsuwPswQBTey9&udm=2&prmd=isvnmbz&sa=X&ved=2ahUKEwiMwNu34-GFAxXNVUEAHRkpCl0QtKgLegQIDxAB&biw=1536&bih=738&dpr=1.25",


result = query(
    "VORY DINER WALL CLOCK"
)


print(result)



