const alert_info = document.getElementById('alert-info');

function closePopup() {
    // alert_info.classList.remove('alter-container');
    alert_info.classList.add('close-alert');
}

function openPopup() {
    alert_info.classList.add('alter-container');
    alert_info.classList.remove('close-alert');
}