from flask import Flask, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

# Environment variables
db_url = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/mydb")
redis_host = os.getenv("REDIS_HOST", "redis")

# Redis client
cache = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    # Test Redis cache
    visits = cache.incr("visits")
    
    return jsonify({
        "message": "Welcome to the Flask 2 App!",
        "visits": int(visits)
    })

@app.route("/db")
def test_db():
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute("SELECT 'Database connection successful!'")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"db_status": result[0]})
    except Exception as e:
        return jsonify({"db_error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
