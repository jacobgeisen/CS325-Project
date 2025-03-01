# AI Headline Analysis Project

## Overview

This project uses two different language models, TinyLlama and Phi-1.5, to classify the sentiment of news headlines as **positive, negative, or neutral**. The models take in a headline as input and return a single-word sentiment classification.

## Installation and Setup

### 1. **Clone the Repository**

```sh
git clone https://github.com/jacobgeisen/CS325-Project.git
cd P1
```

### 2. **Set Up the Environment**

To ensure consistency, clone the environment using the provided YAML file:

```sh
conda env create -f requirement.yaml
conda activate P1
```

## Running the Program

### 1. **Prepare Input File**

Add headlines to `input.txt` with one on each line.

### 2. **Run the Script**

```sh
python main.py
```

This will:

- Load two language models
- Process each headline
- Output sentiment classifications to `responses.txt`

## Expected Output

Each headline in `responses.txt` will be labeled with a sentiment:

```
Phi-1.5 -------------
Headline: A shocking Chinese AI advancement called DeepSeek is sending US stocks plunging
Response: negative

TinyLlama -------------
Headline: As sales slump, Kohl’s turns to a new CEO to bring back customers
Response: negative
```