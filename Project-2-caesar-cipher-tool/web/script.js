const inputText =
    document.getElementById("inputText");

const outputText =
    document.getElementById("outputText");

const shiftKey =
    document.getElementById("shiftKey");

const charCount =
    document.getElementById("charCount");


/* =========================
   CHARACTER COUNTER
========================= */

inputText.addEventListener(
    "input",
    function () {

        charCount.textContent =
            inputText.value.length;

    }
);


/* =========================
   CHANGE SHIFT KEY
========================= */

function changeShift(amount) {

    let shift =
        parseInt(shiftKey.value) || 0;

    shift += amount;


    if (shift < 0) {

        shift = 25;

    }


    if (shift > 25) {

        shift = 0;

    }


    shiftKey.value = shift;

}


/* =========================
   GET SHIFT KEY
========================= */

function getShift() {

    let shift =
        parseInt(shiftKey.value);


    if (isNaN(shift)) {

        shift = 0;

    }


    shift =
        shift % 26;


    if (shift < 0) {

        shift += 26;

    }


    return shift;

}


/* =========================
   CAESAR CIPHER
========================= */

function caesarCipher(
    text,
    shift
) {

    let result = "";


    for (
        let i = 0;
        i < text.length;
        i++
    ) {

        const char =
            text[i];


        /*
        Uppercase letters
        */

        if (
            char >= "A" &&
            char <= "Z"
        ) {

            const code =
                char.charCodeAt(0);


            const newCode =
                (
                    (code - 65 + shift)
                    % 26
                ) + 65;


            result +=
                String.fromCharCode(
                    newCode
                );

        }


        /*
        Lowercase letters
        */

        else if (
            char >= "a" &&
            char <= "z"
        ) {

            const code =
                char.charCodeAt(0);


            const newCode =
                (
                    (code - 97 + shift)
                    % 26
                ) + 97;


            result +=
                String.fromCharCode(
                    newCode
                );

        }


        /*
        Numbers,
        spaces and
        special characters
        */

        else {

            result += char;

        }

    }


    return result;

}


/* =========================
   ENCRYPT
========================= */

function encryptText() {

    const text =
        inputText.value;


    if (
        text.trim() === ""
    ) {

        alert(
            "Please enter text to encrypt."
        );

        return;

    }


    const shift =
        getShift();


    const encrypted =
        caesarCipher(
            text,
            shift
        );


    outputText.textContent =
        encrypted;

}


/* =========================
   DECRYPT
========================= */

function decryptText() {

    const text =
        inputText.value;


    if (
        text.trim() === ""
    ) {

        alert(
            "Please enter text to decrypt."
        );

        return;

    }


    const shift =
        getShift();


    const decrypted =
        caesarCipher(
            text,
            -shift
        );


    outputText.textContent =
        decrypted;

}


/* =========================
   COPY RESULT
========================= */

function copyResult() {

    const result =
        outputText.textContent;


    if (
        result ===
        "Your encrypted or decrypted text will appear here."
    ) {

        alert(
            "There is no result to copy."
        );

        return;

    }


    navigator.clipboard
        .writeText(result)
        .then(
            function () {

                alert(
                    "Result copied!"
                );

            }
        );

}


/* =========================
   CLEAR
========================= */

function clearAll() {

    inputText.value =
        "";

    outputText.textContent =
        "Your encrypted or decrypted text will appear here.";

    charCount.textContent =
        "0";

    shiftKey.value =
        "3";

}