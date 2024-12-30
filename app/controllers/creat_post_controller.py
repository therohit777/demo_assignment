from astrapy import Collection
from app.database.database_connection import get_database_client
from app.models.schema import ApiResponse, PostSchema


def create_post_controller(post: PostSchema, files):
    try:
        # Use the Astra DB client
        db = get_database_client()

        # Create or get the collection
        collection_name = "posts"  # Replace with your collection name
        namespace = "your_namespace"  # Replace with your namespace

        my_collection: Collection[dict] = db.get_collection(
            collection_name
            # namespace=namespace
        )

        # Prepare files information
        file_names = [file.filename for file in files]

        # Create a document to insert
        post_document = {
            "likes": post.likes,
            "shares": post.shares,
            "postTypes": post.postTypes,
            "comments": post.comments,
            "username": post.username,
            "files": file_names,
        }

        # Insert the document into the collection
        my_collection.insert_one(post_document)

        return ApiResponse(
            status_code=200,
            message="Post created successfully and saved to Astra DB.",
            data=post_document
        )

    except Exception as e:
        return ApiResponse(
            status_code=500,
            message="Failed to create post.",
            data={
                "error": str(e)
            }
        )

