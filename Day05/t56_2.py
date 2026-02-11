import xml.etree.ElementTree as ET

tree = ET.parse("dvd.xml")
root = tree.getroot()

print("\n========= DVD RENTAL REPORT =========")

for movie in root.findall("movie"):

    print("\n----------- MOVIE -----------")
    print("Movie ID:", movie.get("id"))
    print("Title:", movie.find("title").text)
    print("Genre:", movie.find("genre").text)
    print("Language:", movie.find("language").text)
    print("Year:", movie.find("year").text)
    print("Available:", movie.find("available").text)

    if movie.find("available").text == "false":
        rented = movie.find("rented_by")

        if rented is not None:
            print("Rented By:", rented.find("name").text)
            print("Rental Date:", rented.find("rental_date").text)
            print("Return Due:", rented.find("return_due").text)
