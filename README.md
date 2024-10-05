# Laptop Ranking System

This project is designed to rank laptops based on various factors such as price, processor performance, RAM, storage, graphics, and screen size. The system processes a dataset of laptops, scores each laptop on different attributes, and produces a ranked list based on the overall score.

## Features

- Cleans and preprocesses raw laptop data (price, processor type, RAM, etc.)
- Scores laptops based on processor, RAM, storage, graphics, and price
- Generates a ranked list of laptops with normalized scores
- Saves the top-ranked laptops in a CSV file

## Installation

### Requirements

The project requires Python and the following Python libraries:

- `numpy`
- `pandas`

### Setting Up the Project

1. Clone the repository to your local machine:

```bash
git clone https://github.com/IsbatBInHossain/laptop-ranking.git
cd laptop-ranking
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your laptop data in a CSV file (e.g., `all_laptops.csv`).
2. Run the `main.py` script to rank the laptops:

```bash
python main.py
```

3. The ranked list of laptops will be saved in `best_laptops.csv`.

## Example CSV Input

The input CSV file should have the following columns (at a minimum):

- `Name`
- `Price`
- `Processor Type`
- `RAM`
- `Hard Disk`
- `Graphics Card`
- `Screen Size`
- `Disk Type`

## Output

The script will output the top 10 ranked laptops, displaying the following information:

- `Name`, `Price`, `Processor Type`, `ProcessorScore`, `RAM`, `RAMScore`, `Hard Disk`, `StorageScore`, `GraphicsScore`, `Graphics Card`, `Screen Size`, `ScreenScore`, `NormalizedScore`

## License

This project is licensed under the MIT License.
