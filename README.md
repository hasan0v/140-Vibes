# 140 Vibes 

## Overview

Welcome to the 140 Vibes! This project is designed to showcase and manage the music, albums, profiles, and products of the 140 Vibes hiphop group. It features various functionalities including viewing tracks, albums, products, and profiles, along with detailed statistics for YouTube video views and likes.

## Features

- **Home Page:** Displays a list of albums.
- **Tracks Page:** Lists all tracks ordered by creation date.
- **Albums Page:** Lists all albums ordered by creation date.
- **Track Detail Page:** Shows detailed information about a specific track, including YouTube statistics.
- **Album Detail Page:** Displays details of a specific album along with track details and aggregated YouTube statistics.
- **Store Page:** Lists all products available for purchase, including their images.
- **Product Detail Page:** Shows detailed information about a specific product, including all associated images.
- **Profile Page:** Displays detailed information about an artist's profile, including their tracks and YouTube statistics.
- **About Page:** General information about the 140 Vibes hiphop group.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/hasan0v/140-vibes-hiphop.git
   cd 140-vibes-hiphop
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Navigate through the website to explore different pages.
- View the details of tracks, albums, and products.
- Check the profiles of artists and their associated tracks.
- View YouTube statistics for tracks and albums.

## Code Structure

- **views.py:** Contains all the views for handling the different pages and their context data.
- **models.py:** Defines the database models for Track, Album, Profile, Product, and ProductImage.
- **templates/:** Contains all the HTML templates for rendering the views.
- **tools.py:** Includes utility functions like `get_video_stats` and `standardizer` for fetching and formatting YouTube statistics.

## Contributing

1. **Fork the Repository:**
   Click on the "Fork" button on the top right corner of this repository's GitHub page.

2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/hasan0v/140-vibes.git
   cd 140-vibes
   ```


3. **Create a Pull Request:**
   Open your fork on GitHub and click on "New Pull Request".

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact me at alihasanov.m@gmail.com.

---

Thank you for contributing to the 140 Vibes! We appreciate your support and effort in making this project better.
