from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os, random, string
from datetime import datetime, timedelta

# -----------------------------
# Setup
# -----------------------------
load_dotenv()
app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URI"))
db = client.spmb_cat

# -----------------------------
# Helper: generate token
# -----------------------------
def generate_token(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# -----------------------------
# Endpoint pengawas: generate token session
# -----------------------------
@app.route("/api/admin/create_session", methods=["POST"])
def create_session():
    data = request.json
    exam_id = data.get("exam_id")
    if not exam_id:
        return jsonify({"error": "exam_id wajib diisi"}), 400

    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=30)  # token berlaku 30 menit
    token = generate_token()

    db.sessions.insert_one({
        "_id": token,
        "exam_id": exam_id,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "participants": []
    })

    return jsonify({
        "token": token,
        "exam_id": exam_id,
        "valid_until": end_time.isoformat(),
        "message": "Session created, token berlaku 30 menit"
    }), 200

# -----------------------------
# Endpoint peserta: join exam
# -----------------------------
@app.route("/api/exam/join", methods=["POST"])
def join_exam():
    data = request.json
    token = data.get("token")
    user_id = data.get("user_id")

    if not token or not user_id:
        return jsonify({"error": "token dan user_id wajib diisi"}), 400

    session = db.sessions.find_one({"_id": token})
    if not session:
        return jsonify({"error": "Token invalid atau expired"}), 400

    now = datetime.now()
    start_time = datetime.fromisoformat(session["start_time"])
    end_time = datetime.fromisoformat(session["end_time"])
    if not (start_time <= now <= end_time):
        return jsonify({"error": "Token sudah expired"}), 400

    # Tambahkan peserta ke session jika belum ada
    if user_id not in session.get("participants", []):
        db.sessions.update_one({"_id": token}, {"$push": {"participants": user_id}})

    # Ambil participant
    participant = db.participants.find_one({"_id": user_id})
    if not participant:
        return jsonify({"error": "Participant not found"}), 400

    # Dummy questions
    questions_list = [
        {"text": "Soal dummy 1?", "options": {"a": "1","b":"2","c":"3","d":"4"}},
        {"text": "Soal dummy 2?", "options": {"a": "A","b":"B","c":"C","d":"D"}}
    ]

    return jsonify({
        "exam_id": session["exam_id"],
        "questions": questions_list,
        "message": f"{participant['name']} joined exam"
    }), 200

# -----------------------------
# Jalankan server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
