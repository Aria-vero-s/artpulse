# ArtPulse Django Project

![ArtGallery Logo](/media/mockup.png)

## Introduction

This Django project is an ArtGallery platform that allows users to explore, share, and connect with other artists. The website provides a range of features including artwork search functionality, user account management, artwork publication, and interaction through ratings and comments.

[Live Link](https://artpulse-2c17e5a691a0.herokuapp.com/)

## Features

### Navbar and Footer

- The top of each page includes a simple horizontal navbar.
- The end of each page includes a simple footer.
- Both the navbar and footer are present on all pages as part of the `base.html` template.


### Artwork Search

- Users can search for artworks using various filters such as title, artist name, description keywords, category, and rating score.

### Artwork Browsing

- Users can browse artworks published by other users.
- Users can click on the "show more" button to read details about the artwork, leave a rating score, and add comments.

### Full-Screen Image View

- Clicking on an artwork allows users to view the image in full screen.

### User Authentication

- Users must create an account to publish artworks, and leave comments.

### Anonymous Ratings

- Anonymous users can rate artworks but cannot leave comments.

### User Profile Management

- Authenticated users can publish artworks, update or delete them from their account profile.
- Users can change their profile photo.
- Users can view their statistics, including total artworks published, average rating, and total comments received.

### Ethos Section

- The homepage features an "Ethos" section highlighting the benefits of the website, such as connecting with other artists, sharing artworks, and discovering new artworks and people.

## UI Design

- The design was created on Figma, inspired by the painting "Icarus" by Henri Matisse. [ArtPulse Figma](https://www.figma.com/file/Dz2mJ6i9WQIjLqTSfUqak9/Untitled?type=design&node-id=0%3A4&mode=design&t=rg41oUqYPTEZzblk-1)
- Colors for the design were based on the chosen painting.

## Technologies Used

- Django (Python)
- JavaScript
- HTML
- CSS
- Git (Version Control)
- Visual Studio Code (IDE)
- Cloudinary (Image Management)
- Heroku (Cloud Deployment)
- GitHub (Code Repository)

## Getting Started

1. Clone the repository from GitHub.
2. Set up a virtual environment and install the required dependencies using `pip3 install -r requirements.txt`.
3. Apply migrations with `python3 manage.py migrate`.
4. Set up Cloudinary credentials for image management.
5. Configure the database settings in `settings.py`.
6. Run the development server using `python3 manage.py runserver`.

## Deployment

The project is designed to be easily deployable on Heroku. Ensure that the necessary environment variables are set, and connect the project to a Heroku app.

## Contribution

If you'd like to contribute to the project, please follow the standard GitHub flow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and submit a pull request.

## Acknowledgments

Feel free to explore, contribute, and enjoy the ArtGallery Django project!
