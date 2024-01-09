function openModal(imageUrl, altText) {
    var modal = document.getElementById('myModal');
    var modalImage = document.getElementById('modalImage');

    modalImage.src = imageUrl;
    modalImage.alt = altText;

    modal.style.display = 'flex';
}

function closeModal() {
    var modal = document.getElementById('myModal');
    modal.style.display = 'none';
}

/* show more artwork on homepage */

document.addEventListener('DOMContentLoaded', function () {
    var artworksContainer = document.getElementById('artworksContainer');
    var artworks = document.querySelectorAll('.artwork');
    var showMoreButton = document.getElementById('showMoreButton');
    var artworksToShow = 8;
    var currentIndex = 0;

    function showNextArtworks() {
        for (var i = currentIndex; i < currentIndex + artworksToShow; i++) {
            if (artworks[i]) {
                artworks[i].style.display = 'block';
            }
        }
        currentIndex += artworksToShow;

        // Hide "Show More" button if all artworks are shown
        if (currentIndex >= artworks.length) {
            showMoreButton.style.display = 'none';
        }
    }

    // Show initial artworks
    showNextArtworks();

    // Attach click event to the "Show More" button
    showMoreButton.addEventListener('click', showNextArtworks);
});