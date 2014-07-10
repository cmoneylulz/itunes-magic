import xml.etree.ElementTree as ET

class ITunesParser():
  def __init__(self):
    self.file_path = "/Users/cwilson/Music/iTunes/iTunes Music Library copy.xml"

    print "Loading iTunes XML Library..."
    self.etree = ET.parse(self.file_path)
    self.root = self.etree.getroot()
    print "Successfully Loaded XML Tree Root."

    print "XML ROOT TAG: " + self.root.tag
    print "XML ROOT ATTRIBUTES: "
    print self.root.attrib

    keys = self.root.find('dict')

    tracklist = keys.find('dict')

    count = 0
    for track in tracklist:
        print track.text
    

parser = ITunesParser()
