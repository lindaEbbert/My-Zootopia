# Zootopia 🦁

Zootopia is a small Python application that generates a styled HTML page with
information about animals. You enter the name of an animal, the program fetches
matching data from the [API Ninjas Animals API](https://api-ninjas.com/api/animals),
and it produces a ready-to-open `animals.html` page that lists each result as a card.

## What problem does it solve?

Instead of reading raw JSON from an API, Zootopia turns animal data into a clean,
human-readable web page. For every animal it shows (when available):

- **Name**
- **Diet**
- **Location** (the first location in the list)
- **Type**

If no animal matches your search, the generated page shows a friendly message
instead of an empty result.

## Who is it for?

This is a learning project aimed at beginners who want a practical example of:

- Calling a REST API with `requests`
- Loading secrets from a `.env` file
- Separating data fetching from presentation logic
- Generating HTML from a template

## Requirements

- Python 3.x
- A free API key from [API Ninjas](https://api-ninjas.com/)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd My-Zootopia
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API key:

   ```env
   API_KEY=your_api_ninjas_key_here
   ```

## Usage

Run the generator from the project root:

```bash
python animals_web_generator.py
```

You will be prompted to enter an animal name:

```text
Enter a name of an animal: fox
```

The program writes the result to `animals.html`. Open that file in your browser
to view the generated page.

### Example

Entering `fox` produces a page with one card per matching fox species, each
showing its diet, location, and type.

## Project structure

| File                       | Description                                              |
| -------------------------- | ------------------------------------------------------- |
| `animals_web_generator.py` | Main script: prompts for input and builds the HTML page |
| `data_fetcher.py`          | Fetches animal data from the API                        |
| `animals_template.html`    | HTML template with the `__REPLACE_ANIMALS_INFO__` placeholder |
| `animals.html`             | Generated output page                                   |
| `requirements.txt`         | Python dependencies                                     |

## Contributing

Contributions are welcome! If you would like to improve Zootopia:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m "Add my feature"`).
4. Push to your branch (`git push origin feature/my-feature`).
5. Open a Pull Request describing what you changed and why.

Please keep changes focused and write clear commit messages.
