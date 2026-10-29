//constants & event listeners which validate the various requests
const submitBtn = document.querySelector("#submit")
const logoutBtn = document.querySelector("#logout")
const content = document.querySelector("#loggedInContent")
submitBtn.addEventListener("click", submit)
logoutBtn.addEventListener("click", logout)
let validAdmin = "Admin"
let validAdminPW = "pw"
let validUser = "User"
let validUserPW = "pw"
let loggedInAdmin = false
let loggedInUser = false

// revokes login - just sets logged in booleans to false in this case & hides displayed message
function logout() {
    if (loggedInAdmin == true || loggedInUser == true) {
        loggedInAdmin = false
        loggedInUser = false
        content.style.display = "none"
        alert("Successful logout!")
    }
}

// displays a phrase on the index page depending on which type of user logged in
function displayContent() {
    if (loggedInAdmin == true || loggedInUser == true) {
        const adminContent = document.createElement("h2")
        adminContent.textContent = "You are logged in as " + username.value + ", and only you can see this."
        content.appendChild(adminContent)
        return
    }
    else {
        return
    }
}

// passes the entered credentials to the constants above to validate & grants access or rejects access
function submit() {
    const username = document.querySelector("#username").value
    const password = document.querySelector("#password").value
    const role = document.querySelector("#role").value
    
    if (role === "Administrator") {
        if (username === validAdmin && password === validAdminPW ){
            alert("Access Granted!")
            loggedInAdmin = true
            displayContent()
            return
        }
        else {
            alert("Incorrect credentials, try again")
        return
        }
    }
    else if (role === "User") {
        if (username === validUser && password === validUserPW ){
            alert("Access Granted!")
            loggedInUser = true
            displayContent()
            return
        }
        else {
            alert("Incorrect credentials, try again")
        return
        }
    }
}