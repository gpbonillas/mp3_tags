import os, glob
import sys
import music_tag # for editing audio metadata with an interface that does not depend on the underlying file format.

# Print characters with UTF-8 encoding
sys.stdout.reconfigure(encoding="utf-8")

os.chdir("./")
for file in glob.glob("*.m4a"):
  file_name = os.path.basename(file)
   
  f = music_tag.load_file(file)
  
  # dict access returns a MetadataItem
  title_item = f['title']
  
  title_name = str(file_name).split(' - ')[0]
  file_name_with_tags = title_name + ".m4a"
  
  f['title'] = title_name
  f.save()
  new_title_item = f['title']
  print('Title of m4a file: {0}, now is: {1}'.format(title_item, new_title_item))
  
  os.rename(file_name, file_name_with_tags)
  print('Filename of m4a file: {0}, now is: {1}'.format(str(file_name), file_name_with_tags))