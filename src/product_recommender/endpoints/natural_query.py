from sentence_transformers import SentenceTransformer
import torch
from pinecone import Pinecone
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()




def query(query):
                       
        api_key=os.getenv('PINECONE_API_KEY')

        pc = Pinecone(api_key=api_key)

        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device=device)
       
        
        index = pc.Index('semantic-search-product')


        # create the query vector
        xq = model.encode(query).tolist()

        # now query
        res = index.query(vector=xq, top_k=5, include_metadata=True)

        items = [match['metadata']['text'] for match in res['matches']]

        parsed_items = []
        for item in items:
                # Remove any dollar signs from the item
                item = item.replace('$', '')
                # Split the item by "Price:"
                parts = item.split("Price:")
                # The first part is the product name
                product = parts[0].strip()
                # The second part is the price
                price = parts[1].strip()
                # Append the parsed product and price to the list
                parsed_items.append({'product': product, 'price': price})

        return parsed_items
        

        return text_list




client = OpenAI()

def llm_response(res):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a sale assistant that takes in recommended products for a user as input and their respective price and say tell it to user in natural language and nice way."},
        
        {"role": "user", "content":f"{res}"}
    ]
    )

    ans = response.choices[0].message.content

    return ans
