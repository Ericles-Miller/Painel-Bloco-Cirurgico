let seletor = 'azul';
let caixa_azul = document.getElementById('caixa_azul');
let caixa_verde = document.getElementById('caixa_verde');

caixa_azul.addEventListener('click', () => {
    seletor = 'azul';
    console.log(seletor)
});

caixa_verde.addEventListener('click', () => {
    seletor = 'verde';
    console.log(seletor)
})
