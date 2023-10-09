"""
convert_infofile2aframe_tags.py.
This script convert model list from blsosm_exporter to A-Frame tags.
Date: 20231009
"""

import os
from math import *
import bpy

def write_a_assetts_tag(tagsfile_path_a_assets, obj):
	f = open(tagsfile_path_a_assets, "a")
	f.write("<a-asset-item id=\"{0}_asset\" src=\"{{{{ url_for('static', filename='model/{0}.gltf') }}}}\"></a-asset-item>".format(obj['name']) + "\n")
	f.close()

def write_a_entity_tag(tagsfile_path_a_entity, obj):
	f = open(tagsfile_path_a_entity, "a")
	f.write("<a-entity id=\"{0}\" gltf-model=\"#{0}_asset\" position=\"{1} {3} {2}\" scale=\"1 1 1\" physics-object=\"model: #{0}_asset; body: static; shape: box\" geometry=\"primitive: box; width: {7}; height: {8}; depth: {9}\"></a-entity>".format(obj['name'], 
		int(obj['position'][0]*10000)/10000, int((obj['position'][1]*10000)*-1)/10000, int(obj['position'][2]*10000)/10000, 
		int(obj['scale'][0]*10000)/10000, int(obj['scale'][1]*10000)/10000, int(obj['scale'][2]*10000)/10000,
		int(obj['dimensions'][0]*10000)/10000, int(obj['dimensions'][1]*10000)/10000, int(obj['dimensions'][2]*10000)/10000)
		 + "\n"
		 )
	f.close()


infofile_dir = "/Users/username/Downloads/blender/assets/convert_modellist2A-Frame-tag/"

infofile_filename = "modellist.tsv"
infofile_path = infofile_dir + infofile_filename

tags_filename_a_assets = "modeltags_a_assets.txt"
tagsfile_path_a_assets = infofile_dir + tags_filename_a_assets

tags_filename_a_entity = "modeltags_a_entity.txt"
tagsfile_path_a_entity = infofile_dir + tags_filename_a_entity


if os.path.exists(tagsfile_path_a_assets):
	os.remove(tagsfile_path_a_assets)

if os.path.exists(tagsfile_path_a_entity):
	os.remove(tagsfile_path_a_entity)

f = open(infofile_path, "r")
for line in f:
	obj = {}
	prop = line.split('\t')
	obj['name'] = prop[0]
	obj['position'] = [float(prop[1]), float(prop[2]), float(prop[3])]
	obj['rotation'] = [float(prop[4]), float(prop[5]), float(prop[6])]
	obj['scale'] = [float(prop[7]), float(prop[8]), float(prop[9])]
	obj['dimensions'] = [float(prop[10]), float(prop[11]), float(prop[12])]
	write_a_assetts_tag(tagsfile_path_a_assets, obj)
	write_a_entity_tag(tagsfile_path_a_entity, obj)

f.close()
