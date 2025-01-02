from astrapy import Collection
from app.database.database_connection import get_database_client
from app.models.schema import ApiResponse, PostSchema

def create_post_controller(post: PostSchema, files):
    try:
        db = get_database_client()

        collection_name = "posts"  

        my_collection: Collection[dict] = db.get_collection(
            collection_name
        )

        file_names = [file.filename for file in files]

        if len(files) == 1:
            if files[0].content_type.startswith("image/"):
                post_type = "static images"
            elif files[0].content_type.startswith("video/"):
                post_type = "reels"
        elif len(files) > 1:
            post_type = "Carousel"
        else:
            post_type = "unknown"

        post_document = {
            "likes": post.likes,
            "shares": post.shares,
            "postTypes": post_type,
            "comments": post.comments,
            "username": post.username,
            "files": file_names,
        }

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
