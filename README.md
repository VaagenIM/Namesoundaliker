# Namesoundaliker README

Welcome to **Namesoundaliker**! Inspired by popular daily word and puzzle games like **Wordle** and **Bandle**, this project lets you try to figure out who or what something sounds like. This README provides instructions on how to set up and run the game locally using Docker.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [Adding More Days](#adding-more-days)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Overview

This game presents a fresh puzzle every day, automatically refreshed for daily play. Challenges are organized in a straightforward folder structure, allowing for easy extension and customization.

## Requirements

- **Docker**: Make sure Docker is installed on your system. If you don’t have Docker, you can [download it here](https://www.docker.com/get-started).

## Installation and Setup

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/VaagenIM/gaming-Kliiyu.git
cd gaming-Kliiyu
```

### Step 2: Run the Game with Docker Compose

Use Docker Compose to build and run the game. This will set up the game environment and expose it on localhost:1738.

```bash
docker compose up -d --build
```

After running the command, the game will be accessible at:
```arduino
http://localhost:1738
```
> Note: The first time you run Docker Compose, it may take a few minutes to build the necessary Docker images.

### Usage
Once the application is running, open your browser and navigate to http://localhost:1738. You’ll be greeted with the day’s puzzle, ready to play.
Each day brings a new challenge, but you can also add additional puzzles (see [Adding More Days](#adding-more-days)).

### Adding More Days
To add more daily challenges, follow these steps:

Navigate to the private/days directory: Each puzzle day is stored as a separate folder in this directory.
```arduino
private/
└── days/
    ├── 1/
    ├── 2/
    └── 3/
```
Create a new folder: Add a new folder inside private/days/. Name the folder according to the day number (e.g., 4).

Follow the file structure: Ensure the new folder follows the same file structure as previous days. Copy the template from another day folder if necessary.

Restart the game: After adding a new day, restart the Docker container to refresh the game content.

```bash
docker compose up -d --build
```

### Contributing
If you’d like to contribute to the project by adding features, improving documentation, or submitting bug fixes, please fork the repository and open a pull request.

### License
This project is licensed under the [MIT License](LICENSE).

Made with ❤️ by Kliiyu and PrettyEpicCat
