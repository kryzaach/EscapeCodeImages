# EscapeCodeImages
Converts images to ascii escape codes for more interesting MOTD Banners

Couple of things going on here:
  -Foreground characters are ` .-+*#%@$` to simulate luminance
  -Foreground colours are selected by sampling the upper half of a vertical pxel "doublet"
  -Background colours are selected by sampling the bottom half of the same

That's about it.
Simple images will give more usable results depending on the system hosting.

(Cisco switches will crap out about halfway through a decent image because of the sheer amount of characters required to write an escape code. A partial workaround for these platforms is to split the banenr between "Login" and "MOTD", which doubles the available character space)

Usage terminal3.py image_path [width]

