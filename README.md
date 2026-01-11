# EscapeCodeImages
Converts images to ansi escape codes for more interesting MOTD Banners

Couple of things going on here:

  -Foreground characters are ` .-+*#%@$` to simulate luminance
  
  -Foreground colours are selected by sampling the upper half of a vertical pxel "doublet"
  
  -Background colours are selected by sampling the bottom half of the same

That's about it.
Simple images will give more usable results depending on the system hosting.

This converter produces reams of text looking like this:
```[38;2;99;52;96m[48;2;103;51;102m-[38;2;99;51;97m[48;2;103;50;102m-[38;2;99;51;98m[48;2;104;50;102m-[38;2;99;51;98m[48;2;103;50;102m-[38;2;99;51;98m[48;2;103;50;102m-[38;2;99;51;98m[48;2;102;51;101m-[38;2;99;51;97m[48;2;101;50;100m-[38;2;96;49;95m[48;2;99;48;97m-[38;2;95;47;94m[48;2;98;46;95m-[38;2;94;47;92m[48;2;97;45;92m-[38;2;94;46;90m[48;2;95;43;92m-[38;2;91;43;87m[48;2;94;41;90m-[38;2;91;42;86m[48;2;96;39;86m-[38;2;90;42;85m[48;2;96;39;86m-[38;2;90;41;83m[48;2;94;38;84m-[38;2;90;40;83m[48;2;95;38;85m-[38;2;89;40;82m[48;2;94;38;85m-[38;2;90;40;82m[48;2;94;39;85m-[0m```

^^^that's one line!

(Cisco switches will crap out about halfway through a decent image because of the sheer amount of characters required to write an escape code. A partial workaround for these platforms is to split the banenr between "Login" and "MOTD", which doubles the available character space)

Usage terminal3.py image_path [width]

Converting an image of The Plague:

![Original](./docs/images/god2.png)

Ends up looking like this:

![ASCII converted](./docs/images/terminal3example.png)

The luminance effect is subtle, but really adds a lot of image detail when compared with background block conversion to colour values or even common techniques like splitting the forground in hald using that wierd unicode half blopck thing letting you double the vertical resolution.

 
