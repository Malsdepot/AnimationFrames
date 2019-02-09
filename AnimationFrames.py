from gimpfu import *

def animation_frames(x, y, numberOfFrames):
	img = gimp.Image(x, y, RGB)
	for i in range(numberOfFrames):
		layer = gimp.Layer(img, ("Frame"+str(i)), x, y, RGB_IMAGE, 100, NORMAL_MODE)
		img.add_layer(layer, 0)
		pdb.gimp_layer_add_alpha(layer)
		pdb.gimp_drawable_fill(layer, TRANSPARENT_FILL)
	gimp.Display(img)
		
register(
	"python_fu_animation_frames",
	"Add number pf frames",
	"Add number of layers to be frames for animation",
	"Brian Seeley", "Brian Seeley", "2019",
	"Add Animation Frames...",
	"",
	[
	(PF_INT, "x", "Width", None),
	(PF_INT, "y", "Height", None),
	(PF_INT, "numberOfFrames", "Frames:", None)
	],
	[],
	animation_frames, menu="<Image>/File/Create")

main()


