import urllib.request


x = urllib.request.urlopen('https://api.chess.com/pub/player/Busi_jr')

print(x.read())
