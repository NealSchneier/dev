import urllib2

url = "http://download.finance.yahoo.com/d/quotes.csv?s="
security = "%40%5EDJI,GOOG,AAPL"
properties = "&f=l1pc8g3a0b2a5a2b0b3b6b4c1c0m7m5k4j5p2k2c6c3c4h0g0m0m2w1w4r1d0y0e0j4e7e9e8q0m3f6l2g4g1g5g6v1v7d1l1k1k3t1l0l3j1j3i0n0n4t8o0i5r5r0r2m8m6k5j6p0p6r6r7p1p5s6s1j2s7x0s0t7d2m4v0k0j0w0"
static = "&e=.csv"

response = urllib2.urlopen(url + security + properties + static)
html = response.read()

f = open("data/quotes/google.csv","w")
f.write(html)

