import json

# Step 1: Load animal data from the JSON file
with open("animals_data.json", "r") as file:
    animals = json.load(file)

# Step 2: Read the template HTML file
with open("animals_template.html", "r") as template_file:
    template_content = template_file.read()

# Step 3: Build the animal data HTML to replace the placeholder
animal_data_html = "<ul class='cards'>"  # Start the unordered list

# Loop through the animals data and serialize it into HTML <li> items
for animal in animals:
    animal_data_html += f"""
    <li class="cards__item">
        <strong>Name:</strong> {animal['name']}<br/>
        <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>
        <strong>Location:</strong> {animal['characteristics'].get('location', 'Unknown')}<br/>
        <strong>Type:</strong> {animal['characteristics'].get('type', 'Unknown')}<br/>
    </li>
    """

animal_data_html += "</ul>"  # Close the unordered list

# Step 4: Replace the placeholder with the animal data in the HTML template
final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_data_html)

# Step 5: Write the final HTML back to the template file (or a new file)
with open("animals_template.html", "w") as output_file:
    output_file.write(final_html)

print("Template file 'animals_template.html' has been updated successfully.")
