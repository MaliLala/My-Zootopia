import json

# Step 1: Load animal data from JSON file
def load_data(file_path):
    """Loads data from a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Step 2: Load the template HTML file
def load_template(file_path):
    """Loads the HTML template."""
    with open(file_path, "r") as template_file:
        return template_file.read()

# Step 3: Generate HTML output for each animal
def generate_animal_html(data):
    """Generates the HTML content for the animals."""
    output = ''  # define an empty string
    for animal_data in data:
        output += '<li class="cards__item">'
        output += f'<div class="card__title">{animal_data["name"]}</div>\n'
        output += f'<p class="card__text">\n'
        output += f'<strong>Diet:</strong> {animal_data["characteristics"]["diet"]}<br/>\n'
        output += f'<strong>Location:</strong> {animal_data["locations"][0]}<br/>\n'
        if "type" in animal_data:
            output += f'<strong>Type:</strong> {animal_data["type"]}<br/>\n'
        output += '</p>\n</li>\n'
    return output

# Step 4: Main function to process everything
def main():
    # Load data from the JSON file
    animals = load_data('animals_data.json')

    # Load the template content
    template_content = load_template('animals_template.html')

    # Generate the HTML for each animal
    animals_html = generate_animal_html(animals)

    # Replace the placeholder in the template with the generated HTML
    final_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_html)

    # Write the updated content back to the template file
    with open('animals_template.html', 'w') as template_file:
        template_file.write(final_html)

    print("Template updated successfully!")

# Run the main function
if __name__ == "__main__":
    main()
