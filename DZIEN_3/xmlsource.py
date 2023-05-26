import xml.etree.ElementTree as ET

try:
    tree = ET.parse("kraj.xml")
    root = tree.getroot()

    for child in root:
        print(f"Dziecko taga root: {child.tag} z atrybutami {child.attrib}")

    print(root[0])
    print(root[0][1])
    print(root[0][1].text)

except:
    print("taki element nie istnieje!")
