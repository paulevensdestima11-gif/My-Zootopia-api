import os
import webbrowser
import data_fetcher


def serialize_animal(animal):
    """Convert one animal into required text format"""

    characteristics = animal.get("characteristics", {})

    name = animal.get("name")
    diet = characteristics.get("diet")
    locations = animal.get("locations")
    animal_type = characteristics.get("type")

    output = ""

    if name:
        output += f"{name}\n"

    if diet:
        output += f"Diet: {diet}\n"

    if locations:
        output += f"Location: {' and '.join(locations)}\n"

    if animal_type:
        output += f"Type: {animal_type}\n"

    output += "\n"

    return output


def build_output(data):
    """Build full output for all animals"""
    return "".join(serialize_animal(animal) for animal in data)


def main():
    animal_name = input("Enter an animal name: ")

    base_dir = os.path.dirname(os.path.abspath(__file__))

    template_path = os.path.join(base_dir, "animals_template.html")
    output_path = os.path.join(base_dir, "animals.html")

    # DATA COMES FROM SEPARATE MODULE
    data = data_fetcher.fetch_data(animal_name)

    # Milestone 3: handle missing animals
    if not data:
        animals_text = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        animals_text = build_output(data)

    # Load template
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    # Replace placeholder
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_text)

    # Write file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(final_html)

    print("Generated:", output_path)

    webbrowser.open(f"file://{output_path}")


if __name__ == "__main__":
    main()