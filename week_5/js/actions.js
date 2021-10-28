console.log("This has been connected");

// Line 38 - ALERT MESSAGE

function message() {
    alert("You just made a message appear")
}

// Line 43 - SHOW TEXT

function showText(e) {
    alert(e.innerText)
}

// Line 50 - REMOVE ITEM

function removeButton(e) {
    e.remove()
}

// Line 84 - COOKIES POLICY

let accept = document.querySelector("#cookie-policy")
function acceptCookies() {
    accept.remove()
}

// Line 33 - COUNT

let numCount = 0
let num = document.querySelector("#num")

function add() {
    numCount++
    num.innerText = numCount
}