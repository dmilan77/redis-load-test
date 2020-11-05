from redis.sentinel import Sentinel




def redis_populate():
  """Function to populate keys in Redis Server"""
  # client = redis.StrictRedis(host=configs["redis_host"], port=configs["redis_port"])
  sentinel = Sentinel(
    [
      ("redis-cloudflare-node-0.redis-cloudflare-headless.dns-proxy.svc.cluster.local", 26379), 
      ("redis-cloudflare-node-1.redis-cloudflare-headless.dns-proxy.svc.cluster.local", 26379), 
      ("redis-cloudflare-node-2.redis-cloudflare-headless.dns-proxy.svc.cluster.local", 26379)
    ],     
  socket_timeout=0.1)
  # sentinel.discover_master('mymaster')
  client = sentinel.master_for('mymaster', password='NotImPortAntPassWorD', socket_timeout=0.1)
  for i in range(100000):
      key='key'+str(i)
      value='value'+str(i)
      client.set(key,value)
      print(key,value)

if __name__ == "__main__":
  redis_populate()