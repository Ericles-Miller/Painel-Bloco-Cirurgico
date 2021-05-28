/*
const requestURL= 'https://viacep.com.br/ws/01001000/json/';

let request = new XMLHttpRequest();

request.open('GET', requestURL);

request.responseType = 'json';
request.send();

request.onload = function() {
    var superHeroes = request.response;
    populateHeader(superHeroes);
    showHeroes(superHeroes);
  }


 /*var data = JSON.parse(request.responseText); 
 console.log(data);*/


 function handleFile(files){
    const reader = new FileReader();
    reader.onload = (event) => {
        let data = event.target.result;
        document.querySelector("#texto").value = data; 
    };
    reader.readAsText(files[0]);

    
}
handleFile('teste.txt');