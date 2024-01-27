# ArtPulse Django Project

![ArtGallery Logo](/media/mockup2.png)

## Introduction

This Django project is an ArtGallery platform that allows users to explore, share, and connect with other artists. The website provides a range of features including artwork search functionality, user account management, artwork publication, and interaction through ratings and comments.

[Live Link](https://artpulse-2c17e5a691a0.herokuapp.com/)

## Features

### Navbar and Footer

- The top of each page includes a simple horizontal navbar.
- The end of each page includes a simple footer.
- Both the navbar and footer are present on all pages as part of the `base.html` template.


### Artwork Search

- Users can search for artworks using various filters such as title, artist name, description keywords, and category.

Here's an excerpt from the `search_artworks` view:

```python
# ... (other imports)
from django.db.models import Q

def search_artworks(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    artworks = Artwork.objects.all()
    
    if query:
        artworks = Artwork.objects.filter(
            Q(title__icontains=query) | 
            Q(artist__username__icontains=query) | 
            Q(description__icontains=query)
        )
    if category:
        artworks = artworks.filter(category=category)

    return render(request, 'index.html', {'artworks': artworks, 'query': query, 'category': category})
```

### Artwork Browsing

- Users can browse artworks published by other users.
- Users can click on the "show more" button to read details about the artwork, leave a rating score, and add comments.

#### Likes and Comments

- Users can like artworks and leave comments.

### Full-Screen Image View

- Clicking on an artwork allows users to view the image in full screen.

### Collaborative Project

- Users can connect with other artists through collaborative projects.

#### CollaborativeProject Model
- Represents a collaborative project initiated by a user.
- Fields:
  - `user`: ForeignKey to the User model, representing the project creator.
  - `title`: CharField for the project title.
  - `description`: TextField for a detailed project description.
  - `interested_users`: ManyToManyField linking to the User model, allowing multiple users to express interest in the project.

### User Profile Management

- Authenticated users can publish artworks, update or delete them from their account profile.
- Users can change their profile photo.
- Users can view their statistics, including total artworks published, average rating, and total comments received.

### Messaging system

- Users can send private messages to each other.
- Users can send messages expressing interest in collaborative projects.

#### Message Model
- Represents a private message between two users.
- Fields:
  - `sender`: ForeignKey to the User model, representing the sender of the message.
  - `receiver`: ForeignKey to the User model, representing the receiver of the message.
  - `content`: TextField for the message content.
  - `timestamp`: DateTimeField for the message timestamp.

### Ethos Section

- The homepage features an "Ethos" section highlighting the benefits of the website, such as connecting with other artists, sharing artworks, and discovering new artworks and people.

## UI Design

![ArtGallery Logo](/media/artpulse.png)

- The wireframe and prototype was created on Figma: [ArtPulse Figma](https://www.figma.com/file/Dz2mJ6i9WQIjLqTSfUqak9/Untitled?type=design&node-id=0%3A4&mode=design&t=rg41oUqYPTEZzblk-1)
- The logo was created by me using Procreate.
- The main Font used is Futura:
```
@import url("https://fonts.googleapis.com/css2?family=Futura&display=swap");

@import url("https://fonts.googleapis.com/css2?family=Futura+Condensed&display=swap");
```

## Technologies Used

- Django (Python)
- JavaScript
- HTML
- CSS
- Bootstrap
- Git (Version Control)
- Visual Studio Code (IDE)
- Heroku (Cloud Deployment)
- GitHub (Code Repository)

## Getting Started

1. Clone the repository from GitHub.
2. Set up a virtual environment and install the required dependencies using `pip3 install -r requirements.txt`.
3. Apply migrations with `python3 manage.py migrate`.
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
