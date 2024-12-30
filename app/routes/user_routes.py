from typing import List, Optional
from fastapi import Depends, File, HTTPException, UploadFile
from datetime import datetime
import pytz
from app import app
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


