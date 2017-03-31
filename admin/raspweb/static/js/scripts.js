flatpickr(".flatpickr");

modalOpenButton = document.getElementsByClassName("js-modal-open")[0];
modalCloseButton = document.getElementsByClassName("js-modal-close")[0];
modal = document.getElementsByClassName("js-modal")[0];

modalCloseButton.onclick = function() {
    modal.style.display = "none";
}

modalOpenButton.onclick = function() {
    modal.style.display = "block";
}
