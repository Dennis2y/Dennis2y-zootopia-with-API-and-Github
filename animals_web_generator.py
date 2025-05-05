import data_fetcher

HTML_TEMPLATE = "animals_template.html"

def generate_html(animals, animal_name):
    with open(HTML_TEMPLATE, "r") as f:
        template = f.read()

    if animals:
        animal_html = ""
        for animal in animals:
            animal_html += '<li class="cards__item">'
            animal_html += f'<div class="card__title">{animal["name"]}</div>'
            animal_html += '<div class="card__text"><ul>'

            for key, value in animal["characteristics"].items():
                animal_html += f"<li><strong>{key.capitalize()}</strong>: {value}</li>"

            animal_html += "</ul></div></li>"
        final_html = template.replace("__REPLACE_ANIMALS_INFO__", animal_html)
    else:
        final_html = template.replace(
            "__REPLACE_ANIMALS_INFO__",
            f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
        )

    with open("animals.html", "w") as f:
        f.write(final_html)

    print("Website was successfully generated to the file animals.html.")

def main():
    animal_name = input("Enter a name of an animal: ").strip()
    animals = data_fetcher.fetch_data(animal_name)
    generate_html(animals, animal_name)

if __name__ == "__main__":
    main()
