
// Initialisation de SocketIO
const socket = io();

// // Fonction appelée lorsque le bouton est cliqué
// const sendMessage = () => {
//     console.log("Send : ")
//     // Récupération du texte de l'input
//     const message = document.getElementById("textArea").value;
//     console.log(message)
//     // Envoi du message au serveur
//     socket.emit("message", message);
// };

// Initialisation du bouton
// document.getElementById("sendBtn").addEventListener("click", sendMessage);


socket.on('voices', function (data) {

    data.forEach(element => {
        const ul = voiceUl;
        const li = document.createElement("li");

        const newBtn = document.createElement("btn");
        newBtn.innerText = element;
        newBtn.className = "dropdown-item";

        newBtn.addEventListener("click", function (event) {
            voiceValue = event.target.innerText;
            voiceDropdown.innerText = voiceValue;
            // document.querySelector("#voiceIcon").src = "/static/img/" + voice.toLowerCase() + ".jpg";
        });


        li.appendChild(newBtn);
        ul.appendChild(li);
    });

    voiceDropdown.innerText = voiceUl.children[0].innerText;
    voiceBtn = voiceUl.querySelectorAll("btn");
});

socket.on('results', function (data) {
    console.log("RESULTS")
    data.forEach(element => {
        const parent = document.querySelector("#genResults").children[0];


        const div = document.createElement('div');
        div.classList.add('d-flex');
        div.classList.add('align-items-center');
        div.classList.add('gap-2');
        div.classList.add('mt-2');
        
        const h7 = document.createElement('h7');
        h7.textContent = "";//String(element).reverse()//.split("/")
        div.appendChild(h7);
        
        const audio = document.createElement('audio');
        audio.controls = true;
        audio.controlsList = 'nodownload noplaybackrate';
        
        const source = document.createElement('source');
        url = "/static/"+element; //"{{ url_for('static', filename='"+element+"') }}";
        console.log(element)
        console.log(url)
        source.src = url;
        source.type = 'audio/mpeg';
        audio.appendChild(source);
        
        div.appendChild(audio);
        
        parent.appendChild(div);
    });

})