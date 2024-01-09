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