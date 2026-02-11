import xml.etree.ElementTree as ET

root = ET.Element("dvd_rental")

movie1 = ET.SubElement(root, "movie", id="M001")

ET.SubElement(movie1, "title").text = "3 Idiots"
ET.SubElement(movie1, "genre").text = "Comedy-Drama"
ET.SubElement(movie1, "language").text = "Hindi"
ET.SubElement(movie1, "year").text = "2009"
ET.SubElement(movie1, "available").text = "false"

rented = ET.SubElement(movie1, "rented_by")
ET.SubElement(rented, "customer_id").text = "C101"
ET.SubElement(rented, "name").text = "Rahul Sharma"
ET.SubElement(rented, "rental_date").text = "2025-06-15"
ET.SubElement(rented, "return_due").text = "2025-06-22"


movie2 = ET.SubElement(root, "movie", id="M002")

ET.SubElement(movie2, "title").text = "Bahubali: The Beginning"
ET.SubElement(movie2, "genre").text = "Action"
ET.SubElement(movie2, "language").text = "Telugu"
ET.SubElement(movie2, "year").text = "2015"
ET.SubElement(movie2, "available").text = "true"


tree = ET.ElementTree(root)
ET.indent(tree, space="    ")

tree.write("dvd.xml", encoding="utf-8", xml_declaration=True)
#tree.write("dvd.xml")

print("XML file created successfully!")
