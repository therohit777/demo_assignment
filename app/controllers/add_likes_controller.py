from fastapi import HTTPException
from app.models.schema import ApiResponse
from app.database.database_connection import get_database_client


def increase_likes_controller(post_id: str):
    try:
        # Get database client and collection
        db = get_database_client()
        collection_name = "posts"
        my_collection = db.get_collection(collection_name)

        # Ensure the post exists
        post = my_collection.find_one({"_id": post_id})
        if not post:
            raise HTTPException(
                status_code=404,
                detail=f"Post with ID {post_id} not found."
            )

        # Increment the likes count (default to 0 if not present)
        updated_likes = post.get("likes", 0) + 1
        my_collection.update_one(
            {"_id": post_id},
            {"$set": {"likes": updated_likes}}
        )

        return ApiResponse(
            status_code=200,
            message="Post liked successfully.",
            data={"post_id": post_id, "likes": updated_likes}
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to increase likes: {str(e)}"
        )