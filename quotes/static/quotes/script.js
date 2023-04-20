let quoteContainer;

function fetchQuotes() {
    fetch('fetch-quotes').then(response => {
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
            `
    
            quoteContainer.appendChild(element);
        });
    });


}

document.addEventListener('DOMContentLoaded', function() {
    quoteContainer = document.querySelector('.quote-container');
    fetchQuotes();
});
