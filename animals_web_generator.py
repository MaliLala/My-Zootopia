import json


def serialize_animal(animal_obj):
    """
    Serializes a single animal object into an HTML <li> element.

    Args:
    - animal_obj (dict): The animal data.

    Returns:
    - str: The serialized HTML for the animal.
    """
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<p class="card__text">\n'
    output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    output += f'<strong>Location:</strong> {animal_obj["characteristics"].get("location", "Unknown")}<br/>\n'
    output += f'<strong>Type:</strong> {animal_obj["characteristics"].get("type", "Unknown")}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'
    return output


def load_json_data(file_path):
    """
    Loads the animal data from a JSON file.

    Args:
    - file_path (str): The path to the JSON file.

    Returns:
    - list: A list of animal data dictionaries.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} file not found.")
        return []


def load_template(file_path):
    """
    Loads the HTML template from a file.

    Args:
    - file_path (str): The path to the HTML template file.

    Returns:
    - str: The HTML template content.
    """
    try:
        with open(file_path, "r") as template_file:
            return template_file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} file not found.")
        return ""


def generate_html(animals, template_content):
    """
    Generates the final HTML by replacing the placeholder in the template with serialized animal data.

    Args:
    - animals (list): List of animal data dictionaries.
    - template_content (str): The template HTML content.

    Returns:
    - str: The final HTML content with all animals serialized and added.
    """
    animal_data_html = ""
    for animal in animals:
        animal_data_html += serialize_animal(animal)

    final_html = template_content.replace("<!-- __REPLACE_ANIMALS_INFO__ -->", animal_data_html)
    return final_html


def write_to_template(file_path, content):
    """
    Writes the generated HTML content back to the template file, overwriting it.

    Args:
    - file_path (str): The path to the HTML template file.
    - content (str): The HTML content to write.
    """
    with open(file_path, "w") as output_file:
        output_file.write(content)


def main():
    # Step 1: Load the animal data from the JSON file
    animals = load_json_data("animals_data.json")

    # Step 2: Load the template HTML file
    template_content = load_template("animals_template.html")

    if not animals:
        print("No animals to display!")
        return

    # Step 3: Generate the final HTML with animal data
    final_html = generate_html(animals, template_content)

    # Step 4: Overwrite the template file with the final HTML content
    write_to_template("animals_template.html", final_html)
    print("Template file 'animals_template.html' has been updated successfully.")


if __name__ == "__main__":
    main()
