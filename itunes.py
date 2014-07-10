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

    self.keys = self.root[0].findall('key')
    for key in self.keys:
      if key.text == 'Tracks':
        self.tracks = key

    print self.tracks.text

parser = ITunesParser()
