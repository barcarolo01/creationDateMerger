# metadataMerger
A python script to merge JPG images with metadata contained in a json file
This can be useful to merge metadata with photos fetched from Google takeout.

# INSTRUCTIONS
By default, the script will look for JPG images and for JSON files in two directories respectively called "Images" and "Metadata", bothplaced in the same folder.
Results (Photos containing metadata) will be placed in a folder called "Processed" (that will be automatically created if it does not exists)

You can change this location of input images, metadata and output images by editing the variables "img_path", "meta_path" and "processed_path" in the firsts raws of the script.
Variables "img_path" and "meta_path" can assume the same value, instead "img_path" and "processed path" must have different values.

Launch the script and wait all the images to be merged with their metadata.

IMPORTANT: This script works only with JPEG (".jpg" or ".jpeg") files. Any other type of file inside the input images folder will be ignored.
