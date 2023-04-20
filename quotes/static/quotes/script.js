let quoteContainer;
let offset = 0;
const limit = 20;

function fetchQuotes() {
    fetch('fetch-quotes/?offset=' + offset + '&limit=' + limit).then(response => {
        if(response.ok) {
            return response.json();
        } else {
            throw Error();
        }
    }).then(quotes => {
        quotes.forEach(quote => {
            const element = document.createElement('div');
            element.classList.add('quote');
            element.innerHTML = `
            <p>${quote.author}</p>
            <hr>
            <p>${quote.content}</p>
            <p>${quote.category}</p>
            <div class="quote-actions"><div class="love"></div><div class="hide"></div></div>
            `
    
            quoteContainer.appendChild(element);
        });

        offset += limit;
    });
}

function userReachedBottom() {
    return window.scrollY + window.innerHeight >= document.body.offsetHeight - 25;
}


document.addEventListener('DOMContentLoaded', function() {
    quoteContainer = document.querySelector('.quote-container');

    document.onclick = function(event) {
        let element = event.target;
        if(element.className === 'hide') {
            let quoteElement = element.parentElement.parentElement;
            quoteElement.style.animationPlayState = 'running';
            quoteElement.addEventListener('animationend', function() {
                quoteElement.remove();
            });
        }
    }

    window.onscroll = function(event) {
        if(userReachedBottom()) {
            fetchQuotes();
        }
    }

    fetchQuotes();
});
