import xml.sax

class DVDHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current_tag = ""
        self.movie = {}
        self.rented = {}
        self.inside_rented = False

    def startElement(self, tag, attrs):
        self.current_tag = tag

        if tag == "movie":
            self.movie = {"id": attrs["id"]}

        elif tag == "rented_by":
            self.inside_rented = True
            self.rented = {}

    def characters(self, content):
        content = content.strip()
        if not content:
            return

        if self.inside_rented:
            self.rented[self.current_tag] = content
        else:
            self.movie[self.current_tag] = content

    def endElement(self, tag):

        if tag == "rented_by":
            self.movie["rented_by"] = self.rented
            self.inside_rented = False

        elif tag == "movie":
            print("\n----------- MOVIE REPORT -----------")
            print("Movie ID:", self.movie.get("id"))
            print("Title:", self.movie.get("title"))
            print("Genre:", self.movie.get("genre"))
            print("Language:", self.movie.get("language"))
            print("Year:", self.movie.get("year"))
            print("Available:", self.movie.get("available"))

            if self.movie.get("available") == "false":
                rented = self.movie.get("rented_by", {})
                print("Rented By:", rented.get("name"))
                print("Rental Date:", rented.get("rental_date"))
                print("Return Due:", rented.get("return_due"))


parser = xml.sax.make_parser()
parser.setContentHandler(DVDHandler())
parser.parse("dvd.xml")
