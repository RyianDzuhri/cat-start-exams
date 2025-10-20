from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv('MONGO_URI'))
db = client.spmb_cat

print("🔄 Connecting to MongoDB...")

# Clear existing participants (optional)
db.participants.delete_many({})
print("🗑 Cleared old participants")

# Dummy participants
participants = [
    {
        "_id": "101",
        "user_id": "101",
        "exam_id": "test_01",
        "name": "Ryian",
        "password": "",
        "answers": {}
    },
    {
        "_id": "102",
        "user_id": "102",
        "exam_id": "test_01",
        "name": "Alya",
        "password": "",
        "answers": {}
    }
]

# Insert dummy participants
db.participants.insert_many(participants)
print("✅ Participants inserted")

print("\n📊 Data Summary:")
print(f"Participants: {db.participants.count_documents({})}")

client.close()
print("\n✨ Seeding completed!")
