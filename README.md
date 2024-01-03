# SPAM SMS DETECTION



https://github.com/Rahul4112002/CODAOFT---SPAM-SMS-DETECTION/assets/124488758/64341d0f-6cee-422c-acb1-6efef32067e4



## Overview
This project aims to detect spam messages using machine learning techniques, specifically the Support Vector Machine (SVM) classifier. Additionally, a web application is implemented using Flask for user-friendly interaction.

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Running the Web Application](#running-the-web-application)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## About the Project

This project utilizes machine learning techniques, specifically the SVM algorithm, to classify SMS messages as spam or non-spam. The core functionality is implemented in the "SPAM SMS DETECTION.ipynb" Jupyter notebook.

The project also includes a web application built with Flask, providing an interactive interface for users to input text messages and receive predictions on whether they are spam or not.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Flask

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Rahul4112002/CODAOFT---SPAM-SMS-DETECTION.git
cd CODAOFT---SPAM-SMS-DETECTION
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Training the Model

To train the SVM model using the provided notebook:

```
jupyter notebook "SPAM SMS DETECTION.ipynb"
```

Follow the instructions in the notebook to train and save the model.

### Running the Web Application

Start the Flask web application:

```
python app.py
```

Visit `http://localhost:5000` in your web browser to use the web application.

## File Structure

- **SPAM SMS DETECTION.ipynb**: Jupyter notebook containing the machine learning model implementation.
- **app.py**: Flask web application for user interaction.
- **templates/**: HTML templates for the web application.
- **static/**: Static files (CSS, JS) for the web application.

## Contributing

Feel free to contribute by opening issues, providing feedback, or submitting pull requests.

## Acknowledgements

- Special thanks to [contributors](https://github.com/Rahul4112002/CODAOFT---SPAM-SMS-DETECTION/graphs/contributors) of this project.
- Mention any external libraries or resources used.

---
