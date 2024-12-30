from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# # Set environment variables
# os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
# os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
# os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# Initialize the FastAPI app with title and description
app = FastAPI(
    title="demo-Levelmind",
    description="""This API provides various endpoints for managing and searching in an Elasticsearch database.
    
    - **GET /health-check**: Check the health status of the API.
    - **POST /create_index**: Create an index in Elasticsearch.
    - **POST /generate_embeddings**: Generate and store embeddings from a specified file.
    - **POST /vector_search**: Perform a vector search based on the provided query.
    - **POST /textual_search**: Perform a textual search based on the provided query.
    - **POST /auto_suggestions**: Get auto-suggestions based on the provided query.
    - **POST /facetting**: Perform faceting based on the provided filter query.
    - **POST /pagination**: Paginate results based on the provided index name, query, score, and data ID.
    """
)
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

from app.routes import user_routes