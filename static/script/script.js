
$(document).ready(function() {
    $(".toggle-button").click(function() {
        // Toggle the visibility of the closest ".additional-info"
        $(this).closest(".artwork").find(".additional-info").toggle();

        // Change the arrow icon based on visibility
        $(this).text(function(_, text) {
            return text === "▼ Show More" ? "▲ Show Less" : "▼ Show More";
        });
    });
});

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