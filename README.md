# Creation Date Merger
A simple python script to merge creation and last modification date of any type of file with the associated information contained in a json file.
This can be useful to merge timestamp of photos and videos fetched with Google takeout, which, normally, split the multimedia file and its information in two different files.

# INSTRUCTIONS
In the first rows of the script, you can edit the value of these three variables:
-media_path: Path where multimedia files are placed
-meta_path: Path where json files are placed (note that media_path and meta_path can assume the same value)
-processed_path: Path where images with creation date updated will be saved. This path must be different from media_path.

#File name
"my.photo.jpg" creation date must be contained in file "my.photo.jpg.json"

#JSON Examples
Minimum JSON file:

{
  "title": "myTitle.jpg",
  "photoTakenTime": {
    "timestamp": "1512663569"
  }
}
