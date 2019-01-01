import os
import redis
from rq import Worker, Queue, Connection
listen = ['default']
redis_path= os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
connect = redis.from_url(redis_path)

if __name__ == '__main__':
    with Connection(connect):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
