from redis.sentinel import Sentinel




def redis_populate():
  """Function to populate keys in Redis Server"""
  # client = redis.StrictRedis(host=configs["redis_host"], port=configs["redis_port"])
  # sentinel = Sentinel(
  #   [
  #     ("redis-cloudflare-node-0.redis-cloudflare-headless.dns-proxy.svc.cluster.local", 26379), 
  #     ("redis-cloudflare-node-1.redis-cloudflare-headless.dns-proxy.svc.cluster.local", 26379), 
  #     ("redis-cloudflare-node-2.redis-cloudflare-headless.dns-proxy.svc.cluster.local", 26379)
  #   ],     
  # socket_timeout=0.1)
 
  from redis.sentinel import Sentinel
 
  sentinel = Sentinel([
      ('redis-cloudflare',26379),
  ],sentinel_kwargs={'password': 'NotImPortAntPassWorD'},password='NotImPortAntPassWorD') 

  sentinel.discover_master('mymaster')

  client = sentinel.master_for('mymaster', socket_timeout=0.5)
  for i in range(1000000):
      key='key'+str(i)
      result=client.get(key)
      if result is not None:
        print(key,result)

if __name__ == "__main__":
  redis_populate()