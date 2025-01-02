from astrapy import Collection
from app.models.schema import ApiResponse
from app.database.database_connection import get_database_client

def get_all_posts():
    try:
        db = get_database_client()
        collection_name = "posts"  
   
        my_collection: Collection[dict] = db.get_collection(
            collection_name
        )

        posts = list(my_collection.find())

        return ApiResponse(
            status_code=200,
            message="Fetched all posts successfully.",
            data=posts
        )

    except Exception as e:
        return ApiResponse(
            status_code=500,
            message="Failed to fetch posts.",
            data={
                "error": str(e)
            }
        )
