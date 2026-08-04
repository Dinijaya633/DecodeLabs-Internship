// Get HTML elements

const passwordInput = document.getElementById("password");

const togglePassword =
    document.getElementById("togglePassword");

const checkButton =
    document.getElementById("checkButton");

const strengthText =
    document.getElementById("strengthText");

const strengthBar =
    document.getElementById("strengthBar");

const recommendation =
    document.getElementById("recommendation");


// Requirements

const lengthRequirement =
    document.getElementById("lengthRequirement");

const uppercaseRequirement =
    document.getElementById("uppercaseRequirement");

const numberRequirement =
    document.getElementById("numberRequirement");

const symbolRequirement =
    document.getElementById("symbolRequirement");


// Show / Hide Password

togglePassword.addEventListener("click", function () {

    if (passwordInput.type === "password") {

        passwordInput.type = "text";

        togglePassword.textContent = "Hide";

    } else {

        passwordInput.type = "password";

        togglePassword.textContent = "Show";

    }

});


// Check Password Function

function checkPassword() {

    const password = passwordInput.value;


    // If password is empty

    if (password.length === 0) {

        strengthText.textContent = "Not Checked";

        strengthBar.style.width = "0%";

        recommendation.classList.add("hidden");

        resetRequirements();

        return;

    }


    // Password checks

    const hasMinimumLength =
        password.length >= 8;

    const hasUppercase =
        /[A-Z]/.test(password);

    const hasNumber =
        /[0-9]/.test(password);

    const hasSymbol =
        /[^A-Za-z0-9]/.test(password);


    // Update requirements

    updateRequirement(
        lengthRequirement,
        hasMinimumLength
    );

    updateRequirement(
        uppercaseRequirement,
        hasUppercase
    );

    updateRequirement(
        numberRequirement,
        hasNumber
    );

    updateRequirement(
        symbolRequirement,
        hasSymbol
    );


    // Calculate score

    let score = 0;


    if (hasMinimumLength) {
        score++;
    }

    if (hasUppercase) {
        score++;
    }

    if (hasNumber) {
        score++;
    }

    if (hasSymbol) {
        score++;
    }


    // Display password strength

    if (score <= 1) {

        showStrength(
            "Weak",
            "25%",
            "red"
        );

        showRecommendation(
            "Your password is weak. Try using at least 8 characters, an uppercase letter, a number, and a special symbol."
        );

    } else if (score <= 3) {

        showStrength(
            "Medium",
            "65%",
            "orange"
        );

        showRecommendation(
            "Your password has moderate strength. Add the missing requirements to make it stronger."
        );

    } else {

        showStrength(
            "Strong",
            "100%",
            "green"
        );

        showRecommendation(
            "Excellent! Your password meets all the basic security requirements."
        );

    }

}


// Update requirement

function updateRequirement(
    element,
    isValid
) {

    const check =
        element.querySelector(".check");


    if (isValid) {

        element.classList.add("valid");

        check.textContent = "✓";

    } else {

        element.classList.remove("valid");

        check.textContent = "✕";

    }

}


// Display strength

function showStrength(
    strength,
    width,
    color
) {

    strengthText.textContent = strength;

    strengthBar.style.width = width;


    if (color === "red") {

        strengthBar.style.backgroundColor =
            "#ef4444";

        strengthText.style.color =
            "#dc2626";

    } else if (color === "orange") {

        strengthBar.style.backgroundColor =
            "#f59e0b";

        strengthText.style.color =
            "#d97706";

    } else {

        strengthBar.style.backgroundColor =
            "#22c55e";

        strengthText.style.color =
            "#16a34a";

    }

}


// Show recommendation

function showRecommendation(message) {

    recommendation.innerHTML =
        "<strong>Security Recommendation</strong>" +
        message;

    recommendation.classList.remove("hidden");

}


// Reset requirements

function resetRequirements() {

    const requirements = [
        lengthRequirement,
        uppercaseRequirement,
        numberRequirement,
        symbolRequirement
    ];


    requirements.forEach(
        function (element) {

            element.classList.remove("valid");

            element.querySelector(
                ".check"
            ).textContent = "✕";

        }
    );

}


// Check button

checkButton.addEventListener(
    "click",
    checkPassword
);


// Also check when typing

passwordInput.addEventListener(
    "input",
    checkPassword
);