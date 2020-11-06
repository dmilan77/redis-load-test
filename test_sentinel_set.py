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
      # value='value'+str(i)
      value=str(i)+'::: https://www.google.co.uk/#sclient=psy-ab&hl=en&source=hp&q=ASUSTeK+Computer+INC.+Model+M4A78LT-M+manual&pbx=1&oq=ASUSTeK+Computer+INC.+Model+M4A78LT-M+manual&aq=f&aqi=&aql=&gs_sm=3&gs_upl=52765l57528l0l57848l8l8l0l0l0l0l2413l3989l8-1.1l2l0&bav=on.2,or.r_gc.r_pw.,cf.osb&fp=3d6c1d1d0a5ea45f&biw=1262&bih=879'
      client.set(key,value)
      print(key,value)

if __name__ == "__main__":
  redis_populate()