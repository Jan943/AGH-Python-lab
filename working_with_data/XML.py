from xml.dom import minidom
import xml.sax

#DOM
docDOM = minidom.parse("example_xml.xml")

name = docDOM.getElementsByTagName("name")
lastchild = name[2]
lastchild.setAttribute('is4x4', 'no')
createXML = docDOM.toxml()
save = "example_xml_changed.xml"
with open(save, "w") as f:
    f.write(createXML)

#SAX
class SaxHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current_data = ""
        self.name = ""
        self.year = ""

    def startElement(self, tag, attributes):
        self.current_data = tag
        if self.current_data == "car":
            print(f"Car id: {attributes['id']}")

    def characters(self, attributes):
        if self.current_data == "name":
            self.name = attributes
        elif self.current_data == "year":
            self.year = attributes

    def endElement(self, attributes):
        if self.current_data == "name":
            print(f"Name: {self.name}")
        elif self.current_data == "year":
            print(f"Year: {self.year}")
        self.current_data = ""

parser = xml.sax.make_parser()

parser.setFeature(xml.sax.handler.feature_namespaces, 0)

sax_handler = SaxHandler()
parser.setContentHandler(sax_handler)
parser.parse("example_xml.xml")