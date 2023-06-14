import redis


def load(counts, redis_url, collection_name):
    """Load count data from redis into `counts`."""
    result = redis.Redis.from_url(redis_url).hgetall(collection_name)
    if result:
        redis_counts = {k.decode("utf-8"): v.decode("utf-8") for k, v in result.items()}

        # Update all fields in counts that appear in both counts and redis_counts.
        for key in redis_counts:
            if key in counts:
                counts[key] = redis_counts[key]


def save(counts, redis_url, collection_name):
    """Save count data from `counts` to redis."""
    redis.Redis.from_url(redis_url).hset(collection_name, mapping=counts)
