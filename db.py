from motor.motor_asyncio import AsyncIOMotorClient

#local connectiopn
MONGO_URI = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URI)

#execute database n collection after successful connection
database = client["blog_db"]
post_collection = database["posts"]
comment_collection = database["comments"]
