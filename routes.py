from fastapi import APIRouter, HTTPException, status
from db import post_collection, comment_collection
from models import BlogPost, Comment
from bson import ObjectId

router = APIRouter()

#create a blog post
@router.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: BlogPost):
    post_dict = post.dict()
    result = await post_collection.insert_one(post_dict)
    return {"id": str(result.inserted_id)}

#get post by id
@router.get("/posts/{post_id}")
async def get_post(post_id: str):
    post = await post_collection.find_one({"_id": ObjectId(post_id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {**post, "_id": str(post["_id"])}

#update post's title n content
@router.put("/posts/{post_id}")
async def update_post(post_id: str, update_data: dict):
    # Only allow updating `title` and `content`
    update_fields = {key: value for key, value in update_data.items() if key in ["title", "content"]}
    
    if not update_fields:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    result = await post_collection.update_one(
        {"_id": ObjectId(post_id)}, {"$set": update_fields}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return {"message": "Post updated successfully"}

#delete post by id
@router.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    result = await post_collection.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}

#create comment for post
@router.post("/comments/", status_code=status.HTTP_201_CREATED)
async def create_comment(comment: Comment):
    comment_dict = comment.dict()
    result = await comment_collection.insert_one(comment_dict)
    return {"id": str(result.inserted_id)}

#read comment by id
@router.get("/comments/{comment_id}")
async def get_comment(comment_id: str):
    comment = await comment_collection.find_one({"_id": ObjectId(comment_id)})
    
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    comment["_id"] = str(comment["_id"])
    return comment

#update comment's text
@router.put("/comments/{comment_id}")
async def update_comment(comment_id: str, update_data: dict):
    if "text" not in update_data:
        raise HTTPException(status_code=400, detail="Only 'text' field can be updated")

    result = await comment_collection.update_one(
        {"_id": ObjectId(comment_id)}, {"$set": {"text": update_data["text"]}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")

    return {"message": "Comment updated successfully"}

#delete comment by id
@router.delete("/comments/{comment_id}")
async def delete_comment(comment_id: str):
    result = await comment_collection.delete_one({"_id": ObjectId(comment_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted"}

