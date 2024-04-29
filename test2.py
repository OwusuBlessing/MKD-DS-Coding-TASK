from src.product_recommender.endpoints.natural_query import query,llm_response
from dotenv import load_dotenv
import os
load_dotenv()


res = llm_response(query("I want to buy lantern"))

print(res)


