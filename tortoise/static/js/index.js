const textArea = document.querySelector("#textArea");
const charactersCount = document.querySelector("#charactersCount");
const genBtn = document.querySelector("#sendBtn");

const voiceDropdown = document.querySelector("#dropdownVoice");
const voiceUl = document.querySelector("#dropdown_voice_ul");
let voiceBtn = voiceUl.querySelectorAll("btn");

const presetDropdown = document.querySelector("#dropdownPreset");
const presetUl = document.querySelector("#dropdown_preset_ul");
const presetBtn = presetUl.querySelectorAll("btn")

const voiceIcon = document.querySelector("#voiceIcon");
const tradSwitch = document.querySelector("#tradSwitch");

let voiceValue;
let presetValue;
let textContent;
let trad = false;
const textSizeLimit = 200;

Object.values(presetBtn).forEach(element => {
    element.addEventListener("click", function (event) {
        presetValue = event.target.innerText;
        presetDropdown.innerText = presetValue;
    });
});

Object.values(voiceBtn).forEach(element => {
    element.addEventListener("click", function (event) {
        console.log(event.target)
        voiceValue = event.target.innerText;
        voiceDropdown.innerText = voiceValue;
        voiceIcon.src = "/static/img/" + voiceValue + ".png";
    });
});

genBtn.addEventListener("click", function (event) {
    let a = [textContent,voiceValue,trad];
    socket.emit("gen",a);
});

textArea.addEventListener("input", function (event) {
    console.log(event.target);
    let text = String(event.target.value);

    if (text.length <= textSizeLimit )
    {
        charactersCount.style.color = "black";
        textContent = text;
    } else {
        charactersCount.style.color = "red";
        textContent = text.slice(0,textSizeLimit);
    }
        charactersCount.innerText = text.length + "/" + textSizeLimit;
});

tradSwitch.addEventListener("change", function(event) {
    if (event.target.checked) {
        textArea.placeholder = "Votre texte";
        trad = true;
    } else {
        textArea.placeholder = "Your text";
        trad = false
    }
});

window.addEventListener("load", (event) => {
    socket.emit("start");
    charactersCount.innerText = 0 + "/" + textSizeLimit;
    presetDropdown.innerText = presetUl.children[0].children[0].innerText;
});