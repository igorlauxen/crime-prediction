from os.path import exists

PATH_TO_FILE = "./map/map_pickup.html"

class FileCreator:

  def createEmptyFile(self):
    # https://www.delftstack.com/howto/python/python-clear-file/
    with open(PATH_TO_FILE,'w') as f:
      pass
    print("File created =)")
  
  def getPathForFile(self):
    return PATH_TO_FILE