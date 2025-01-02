from typing import Dict
from fastapi import HTTPException
from app.database.database_connection import get_database_client
from app.models.schema import ApiResponse


def add_comment_controller(post_id: str, comment: Dict[str, str]):
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

        # Add the new comment to the post's comments list
        comment_list = post.get("comments", [])
        comment_list.append(comment)
        my_collection.update_one(
            {"_id": post_id},
            {"$set": {"comments": comment_list}}
        )

        return ApiResponse(
            status_code=200,
            message="Comment added successfully.",
            data={"post_id": post_id, "comments": comment_list}
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to add comment: {str(e)}"
        )
