from PIL import Image, ImageDraw, ImageFont

# based on current image with font 20 limit of line should be around 36 chars.


fontPath = None # only TTF supported didn't tried others.
fontSize = None   # I set default as a 20 you can change the size of font
transparency = 128 # I left half opaque you can calculate with 
					# 2.55 * percentage how opaque you want to be.

def renderText(file, image):
	# get an image
	base = Image.open(image).convert("RGBA")
	# make a blank image for the text, initialized to transparent text color
 
	txt = Image.new("RGBA", base.size, (255,255,255,0))
	# get a font
	# global fontPath, fontSize, transparency
	fontP = fontPath if fontPath else "/usr/share/fonts/TTF/FiraCode-Regular.ttf"
	fontS = fontSize if fontSize else 20
	fontT = transparency if transparency else 255

	fnt = ImageFont.truetype(fontP, fontS)
	
	
	# get a drawing context
	d = ImageDraw.Draw(txt)
	count = 0
	xpos = 15
	ypos = 150
	# get a lines
	with open(file, "r") as f:
		for line in f.readlines():
			if len(line) + 2 > 40:
				line1 = line[:39]
				line2 = line[39:]
				d.text((xpos, ypos), "* " + line1, font=fnt, fill=(255,255,255,fontT))
				d.text((xpos, ypos + 31), " " + line2, font=fnt, fill=(255,255,255,fontT))
				ypos += 50
			else:
				d.text((xpos, ypos), "* " + line, font=fnt, fill=(255,255,255,fontT))
				ypos += 25
			count += 1	
 
	# draw text, full opacity
	# d.text((15,180), "* " + text, font=fnt, fill=(255,255,255,255))
	tmp = Image.alpha_composite(base, txt)

	tmp.show()
	tmp.save("updated.png")
	tmp.close()

renderText(image="original.png", file="updates")
