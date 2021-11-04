// console.log("Javascript is loaded")

function addToCart(e) {
    e.remove()
}

function message() {
    alert('You just added this item to your cart')
}

let accept = document.querySelector('#cookies')

function acceptCookies() {
    accept.remove()
}

let numCount = 0;
let num = document.querySelector('.fav')

function addFav() {
    numCount += 1
    num.innerText = numCount
}