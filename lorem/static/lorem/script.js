
// function to hide all pages, then show the one requested
function showPage(page) {
    document.querySelectorAll('[id^="page"]').forEach(el => {
        el.style.display = 'none';
    });
    document.getElementById(page).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('[id^="page"]').forEach(el => {
        el.style.display = 'none';
    });

    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            showPage(this.dataset.page);
        }
    });
});
