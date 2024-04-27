import os
import time
import pandas as pd
import pinecone
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from tqdm.auto import tqdm
from src.product_recommender.logging import logger
from pinecone import Pinecone, ServerlessSpec
from pinecone_datasets.catalog import DatasetMetadata
from pinecone_datasets import Dataset

# Load environment variables
load_dotenv()

class VectorDB:
    

    def __init__(self, data_path):

    
        self.data_path = data_path

    def setup_vectordb(self,api_key=os.getenv('PINECONE_API_KEY')):


        pc = Pinecone(api_key=api_key)
        cloud = os.getenv('PINECONE_CLOUD')
        region = os.getenv('PINECONE_REGION')
        spec = ServerlessSpec(cloud=cloud, region=region)
        index_name = 'semantic-search-product'

        """Vectorizes the data."""
        df = pd.read_csv(self.data_path)
        df["text"] = df["Description"] + " Price:" + df["UnitPrice"].astype(str)
        
        logger.info("Vectorizing data with all-MiniLM-L6-v2")
        text_model = SentenceTransformer('all-MiniLM-L6-v2')
        df['text_vectors'] = df['text'].apply(lambda x: text_model.encode(x))

        logger.info("Vectorization completed")
    


        """Creates a dataset from the vectorized data."""
        try:
    
            df['id'] = df.reset_index().index.astype(str)
            df["values"] = df["text_vectors"]
            df["metadata"] = [{"text": x} for x in df["text"]]

            logger.info("IDs, values, and metadata prepared")
            
            meta = {
                "name": "product_dataset",
                "created_at": "2024-05-17 14:17:01.481785",
                "documents": len(df),
                "queries": 2,
                "source": "manual",
                "bucket": "LOCAL",
                "task": "unittests",
                "dense_model": {"name": "bert", "dimension": 384},
                "sparse_model": {"name": "bm25"}
            }

            metadata = DatasetMetadata(**meta)
            dataset = Dataset.from_pandas(documents=df, queries=None, metadata=metadata)
            
            logger.info("Dataset creation successful")
            

    

            """Creates a Pinecone index if it does not already exist."""
        
            existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

            if index_name not in existing_indexes:
                pc.create_index(
                    index_name,
                    dimension=384,  # Dimensionality of MiniLM
                    metric='dotproduct',
                    spec=spec
                )

                # Wait for index to be ready
                while not pc.describe_index(index_name).status['ready']:
                    time.sleep(1)

                logger.info(f"Index {index_name} created")

            index = pc.Index(index_name)
            index.describe_index_stats()

            

    
            logger.info("Inserting vectors into index...")
            for batch in tqdm(dataset.iter_documents(batch_size=500), total=8):
                index.upsert(batch)
            
            logger.info("Vector insertion complete")
            
        except Exception as e:
             logger.error("Error creating index: {e}")
    

