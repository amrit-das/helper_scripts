# Helper Scripts

Collection of scripts that I frequently use in my Image Processing and Computer Vision Task

## Requirements
 - aug.py - requires <a href =https://github.com/mdbloice/Augmentor>Augmentor</a>
 - batch_resize.py - requires PIL
 - cv-pil.py - requires OpenCV and PIL
 - rename.py - no requirements
 - resize.py - requires OpenCV
 - video2snaps.py - reqires OpenCV
 - wbscrp.py - requires urllib2
 
## Usage
 - aug.py - To augment images in a folder
 ``` 
 python aug.py folder_name
 ```
 - batch_resize.py - To resize all images in a folder
 ```
 python batch_resize.py folder_name height width 
 ```
 - cv-pil.py - OpenCV and PIL conversions
 
 - rename.py - To rename all files in a folder
 ```
 python rename.py folder_name
 ```
 - resize.py - To resize a single image
 ```
 python resize.py image_name height width
 ```
 - video2snaps.py - reqires OpenCV
 ```
 python video2snaps.py video_file_name
 ```
 - wbscrp.py - requires urllib2
 ```
 python wbscrp.py search_keyword
 ```
 
