let pageContent;

// function to hide all pages, then show the one requested
function showPage(page) {
    pageContent.innerText = '...';

    fetch(page).then(response => {
        if(response.ok) {
            return response.text();
        } else {
            throw Error(response.status + ': ' + response.statusText);
        }
    }).then(text => {
        pageContent.innerText = text;
    }).catch(error => {
        pageContent.innerText = error;
    })
}

window.addEventListener('popstate', event => {
    showPage(event.state.site);
});

document.addEventListener('DOMContentLoaded', function() {
    pageContent = document.getElementById('page');

    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            let site = this.dataset.site;

            showPage(site);
            let parts = site.split('/');
            history.pushState({ site: site }, '', '/lorem/page/' + parts[parts.length - 1]);
        }
    });

    if(page_nr !== 'None') {
        showPage('/lorem/page-text/' + page_nr);
    }
});
