import json

class Certification:
    def __init__(
            self,
            title: str,
            description: str,
            image: str,):

        self.title = title
        self.description = description
        self.image = image


with open("assets/data/certificados.json") as file:
    app_data = json.load(file)

Certificado = [
    Certification(
        item["title"],
        item["description"],
        item["image"]
    )
    for item in app_data
]