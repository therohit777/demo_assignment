from typing import Dict, List, Optional
from fastapi import Depends, File, HTTPException, UploadFile
from datetime import datetime
import pytz
from app import app
from app.controllers.add_comments_controller import add_comment_controller
from app.controllers.add_likes_controller import increase_likes_controller
from app.controllers.get_post_controllers import get_all_posts
from app.models.schema import ApiResponse,PostSchema
from app.controllers.creat_post_controller import create_post_controller

@app.get("/server-check")
def Server_check():
    try:
        ist = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

        return ApiResponse(
                status_code=200,
                message="Server check successful.",
                data={
                "timestamp": current_time
                }
            )

    except Exception as e:
        return ApiResponse(
                status_code=500,
                message="Server check failed.",
                data={
                "error": str(e)
                }
            )
    
@app.post("/create-post")
def create_post(
    post: PostSchema = Depends(),
    files: List[UploadFile] = File(...)
):
    if not files:
        raise HTTPException(
            status_code=400, 
            detail="At least one file must be uploaded."
        )

    try:
        # Pass the post data and uploaded files to the controller
        result =  create_post_controller(post, files)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to create post: {str(e)}"
        )

@app.get("/getposts")
def fetch_all_posts():
    return get_all_posts()

@app.put("/post/{post_id}/like")
def increase_likes(post_id: str):
    return increase_likes_controller(post_id)

@app.post("/post/{post_id}/comment")
def add_comment(post_id: str, comment: Dict[str, str]):
    return add_comment_controller(post_id, comment)

