# Python for AI & Data Science 🚀

Welcome to the **Python for AI** repository! This repository is a structured, hands-on learning roadmap designed to build a solid Python foundation required for **Artificial Intelligence (AI)**, **Data Science**, and **Machine Learning**.

From Python fundamentals and Object-Oriented Programming (OOP) to handling REST APIs and performing real-world data analysis with `pandas` and `matplotlib`, this repository covers the essential building blocks.

---

## 📂 Repository Structure

```plaintext
python-for-ai/
│
├── 📁 data/                           # Weather datasets (CSV)
│   ├── paris_weather.csv
│   └── Sialkot_weather.csv
│
├── 📁 sales-analysis/                 # Mini-project: Sales data processing & analysis
│   ├── 📁 data/                       # Raw input data (sales.csv)
│   ├── 📁 output/                     # Generated reports (JSON, Excel, CSV)
│   ├── analyzer.py                    # Main sales analysis pipeline with pandas
│   └── helpers.py                     # Reusable helper functions
│
├── 📄 hello.py                        # Getting started & environment check
├── 📄 string.py                       # String manipulation & formatting
├── 📄 math.py                         # Arithmetic & numerical operations
├── 📄 bool.py                         # Boolean logic & expressions
│
├── 📄 condition.py                    # If / Else control flow
├── 📄 multiple conditions.py          # Logical operators (and, or, not) & nested conditions
├── 📄 loops.py                        # While and For loops
├── 📄 try except.py                   # Exception & error handling
│
├── 📄 Lists.py                        # List operations, methods & slicing
├── 📄 tuple.py                        # Immutable sequences (Tuples)
├── 📄 set.py                          # Sets & set operations (union, intersection, etc.)
├── 📄 dictionaries.py                 # Key-value mappings & dictionary methods
├── 📄 Data structures.py              # Working with combined data structures
│
├── 📄 Defining functions.py           # Function definition & scope
├── 📄 functions with parameters.py    # Arguments, keyword arguments & defaults
├── 📄 Function with returning values.py # Returning single & multiple values
│
├── 📄 class.py                        # Intro to OOP & Classes
├── 📄 class methods.py                # Class & instance methods
├── 📄 class real world.py             # Practical OOP examples
├── 📄 class inheritance.py            # Parent & child classes
├── 📄 class overriding method.py      # Method overriding & polymorphism
│
├── 📄 Import pakeges.py               # Modules, packages & standard library
├── 📄 request.py                      # Basic HTTP requests
├── 📄 APIs.py                         # Fetching data from REST APIs
├── 📄 APIs2 working with data.py      # Fetching weather API data, processing & plotting
│
├── 📄 weather_chart.png               # Generated sample plot from API data
├── 📄 requirements.txt                # Project dependencies
└── 📄 create virtual envioronment.txt # Guide for virtual environment setup
```

---

## 🛠️ Key Topics Covered

### 1. Python Fundamentals
- **Variables & Data Types:** Strings, numbers, booleans, and type conversions.
- **Control Flow:** `if`, `elif`, `else`, comparison operators, and loop constructs (`for`, `while`).
- **Error Handling:** Graceful exception handling using `try...except` blocks.

### 2. Core Data Structures
- **Lists & Tuples:** Indexing, slicing, appending, and mutating sequences.
- **Dictionaries & Sets:** Hashmaps, keys/values extraction, unique item sets, and set theory operations.

### 3. Modular Programming & Functions
- Writing clean, reusable functions.
- Default arguments, `*args`, `**kwargs`, and return values.

### 4. Object-Oriented Programming (OOP)
- Class creation, `__init__` constructor, and instance attributes.
- Encapsulation, inheritance, and overriding methods for modular architecture.

### 5. APIs & Data Visualization
- Requesting external APIs using `requests`.
- Parsing JSON responses and structuring data into `pandas` DataFrames.
- Visualizing trends and saving charts using `matplotlib`.

### 6. Practical Project: Sales Analysis
- Located in `sales-analysis/`.
- Reads raw CSV transaction data.
- Analyzes metrics, computes totals, and exports multi-format reports (`.json`, `.xlsx`, `.csv`).

---

## ⚡ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/python-for-ai.git
cd python-for-ai
```

### 2. Set Up a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running Examples

Run any individual script to test concepts:

```bash
# Test basic concepts
python hello.py

# Test OOP concepts
python "class inheritance.py"

# Test API fetching and plotting
python "APIs2 working with data.py"

# Run the Sales Analysis project
cd sales-analysis
python analyzer.py
```

---

## 📦 Requirements

Major libraries used:
- [`pandas`](https://pandas.pydata.org/) - High-performance data manipulation and analysis
- [`requests`](https://requests.readthedocs.io/) - HTTP library for API interactions
- [`matplotlib`](https://matplotlib.org/) - Visualization and chart creation
- [`numpy`](https://numpy.org/) - Numerical computing foundation
- [`openpyxl`](https://openpyxl.readthedocs.io/) - Excel report generation

---

## 📈 Learning Path Ahead
- [ ] Exploratory Data Analysis (EDA) with Seaborn & Pandas
- [ ] Machine Learning with Scikit-Learn
- [ ] Deep Learning fundamentals (PyTorch / TensorFlow)
- [ ] Building LLM & Agentic AI applications (LangChain, CrewAI)

---

## 🤝 Contributing
Contributions, suggestions, and improvements are welcome! Feel free to open an issue or submit a pull request.
