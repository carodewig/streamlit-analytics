import redis
import json


def load(counts, redis_url, collection_name):
    """Load count data from redis into `counts`."""
    result = redis.Redis.from_url(redis_url).get(collection_name)
    if result:
        redis_counts = json.loads(result.decode("utf-8"))

        # Update all fields in counts that appear in both counts and redis_counts.
        for key in redis_counts:
            if key in counts:
                counts[key] = redis_counts[key]


def save(counts, redis_url, collection_name):
    """Save count data from `counts` to redis."""
    try:
        json.dumps(counts)
    except Exception:
        print(counts)
    redis.Redis.from_url(redis_url).set(collection_name, json.dumps(counts))
