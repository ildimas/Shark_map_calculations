/**Login/Sign up */
function setInputError(inputElement, message) {
    inputElement.classList.add("formInput--error");
    inputElement.parentElement.querySelector(".formInput-error-message").textContent = message;
}

function clearInputError(inputElement) {
    inputElement.classList.remove("formInput--error");
    inputElement.parentElement.querySelector(".formInput-error-message").textContent = "";
}

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");
    const createAccountForm = document.querySelector("#createAccount");

    document.querySelector("#linkCreateAccount").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.add("form--hidden");
        createAccountForm.classList.remove("form--hidden");
    });

    document.querySelector("#linkLogin").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.remove("form--hidden");
        createAccountForm.classList.add("form--hidden");
    });

    loginForm.addEventListener("submit", e => {
        e.preventDefault();

        // Perform your AJAX/Fetch login

        setFormMessage(loginForm, "error", "Invalid username/password combination");
    });

    document.querySelectorAll(".formInput").forEach(inputElement => {
        inputElement.addEventListener("blur", e => {
            if (e.target.id === "signupUsername" && e.target.value.length > 0 && e.target.value.length < 10) {
                setInputError(inputElement, "Username must be at least 10 characters in length");
            }
        });

        inputElement.addEventListener("input", e => {
            clearInputError(inputElement);
        });
    });
});

/**Something */
$('.arrow').on('click', function(e) {
    e.preventDefault;
    $(this).toggleClass('arrow_active');});
$('.navBarActivateBtn').on('click', function(e) {
    e.preventDefault;
    $(this).toggleClass('navBarActivateBtn_active');});
    $('.navBarActivateBtn_active').on('click', function(e) {
        e.preventDefault;
        $(this).toggleClass('navBarActivateBtn');});