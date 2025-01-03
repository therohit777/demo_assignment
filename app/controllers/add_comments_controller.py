from astrapy import Collection
from fastapi import HTTPException
from app.database.database_connection import get_database_client
from app.models.schema import ApiResponse, CommentSchema


def add_comment_controller(post_id: str, comment: CommentSchema):
    try:
        # Get database client and collection
        db = get_database_client()
        collection_name = "posts"
        my_collection: Collection = db.get_collection(collection_name)

        # Ensure the post exists
        post = my_collection.find_one({"_id": post_id})
        if not post:
            raise HTTPException(
                status_code=404,
                detail=f"Post with ID {post_id} not found."
            )

        # Prepare the new comment
        new_comment = {
            "username": comment.username,
            "content": comment.content
        }
        if not new_comment["content"]:
            raise HTTPException(
                status_code=400,
                detail="Comment content cannot be empty."
            )

        # Ensure comments follow expected structure
        comments = post.get("comments", [])
        if not isinstance(comments, list):
            comments = []
        comments.append(new_comment)

        # Update only the comments field in the database
        my_collection.update_one(
            {"_id": post_id},
            {"$set": {"comments": comments}}
        )

        return ApiResponse(
            status_code=200,
            message="Comment added successfully.",
            data={"post_id": post_id, "new_comment": new_comment}
        )

    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to add comment: {str(e)}"
        )