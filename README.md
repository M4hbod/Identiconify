# Identiconify
Identiconify is a Python library that generates identicons based on a given string input. An identicon is a visual representation of a hash value, often used to create unique avatars or icons for users.

## Installation
You can install the library using pip:

```bash
pip install identiconify
```

## Usage
```python
from identiconify import PilIdenticon

# Create an identicon object
identicon = PilIdenticon()

# Generate an identicon from a string
identicon_image = identicon.generate("example_string")

# Save the identicon to a file
identicon_image.save("identicon.png")
```

## Customization
You can customize the identicon generation by modifying the parameters of the `PilIdenticon` class.

### Example
```python
from identiconify import PilIdenticon

# Create an identicon object with custom parameters
identicon = PilIdenticon(dimensions=6, size=512, padding=False, background_color="#B4DA55", block_color="#FF5733")

# Generate an identicon from a string
identicon_image = identicon.generate("custom_string")

# Save the identicon to a file
identicon_image.save("custom_identicon.png")
```

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.
