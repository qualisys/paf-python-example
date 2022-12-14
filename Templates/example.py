<?php
$temp_dir = str_replace('\\','\\\\', $template_directory);
$work_dir = str_replace('\\','\\\\', $working_directory);
?> 

from ezc3d import c3d
from lxml import etree
from pathlib import Path
from typing import List, Dict

# Some directory paths that we get from qtm through using php
templateDirectory = "<?=$temp_dir;?>"
workingDirectory = "<?=$work_dir;?>"

class SessionXml:
    def __init__(self, path):
        self._path = path
        self._xml = etree.parse(path)
        self._root = self._xml.getroot()

    @property
    def _measurements(self) -> Dict:
        out = {}
        for measurement in self._xml.getroot().findall(".//Measurement"):
            measurement_name = measurement.attrib["Filename"].split(".qtm")[0]
            out[measurement_name] = measurement
        return out

    def is_selected(self, measurement_name) -> bool:
        measurement = self._measurements[measurement_name]
        used_field = measurement.find("Fields/Used").text
        selected = True if used_field == "True" else False
        return selected

    @property
    def selected_measurement_names(self) -> List:
        out = []
        for measurement_name in self._measurements.keys():
            if self.is_selected(measurement_name):
                out.append(measurement_name)
        return out

def load_session_xml(path: Path) -> SessionXml:
    session_xml = SessionXml(path)
    return session_xml

# Load session.xml file to know the selected measurements for the analysis
session_xml = load_session_xml("session.xml")

# Read the c3d files and parse data into an output xml file
page = etree.Element('xml')
doc = etree.ElementTree(page)
for filename in session_xml.selected_measurement_names:
    if 'Static' not in filename:# Ignore static file if exists
        c3dFile = filename + ".c3d"
        xmlc3dFile = c3dFile.replace(' ','_')
        reader = c3d(c3dFile)
        captureFq = reader['parameters']['POINT']['RATE']['value']
        frames = reader['parameters']['POINT']['FRAMES']['value']

        filename = etree.SubElement(page, xmlc3dFile)
        headElt = etree.SubElement(filename, 'Metrics')
        out = etree.SubElement(headElt, 'Capture_Frequency')
        out.text = str(captureFq[0])
        out = etree.SubElement(headElt, 'Frames')
        out.text = str(frames[0])

with open('output.xml', 'wb') as f:
    f.write(etree.tostring(doc, pretty_print=True))