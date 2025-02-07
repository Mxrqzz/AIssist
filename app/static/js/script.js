// Seleciona o botao de mudar o tema da pagina
const themeButton = document.getElementById('theme-toggle');
const body = document.body;
// Função que muda o tema da pagina
function applyTheme(theme) {
  body.className = theme; // Define a classe do body como o tema escolhido
}

// Verifica se há um tema salvo no localStorage
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    applyTheme(currentTheme);
} else {
  // Define o tema claro com padrão se não houver nada no localStorage
    applyTheme('light-mode');
}

// Adiciona um evento de click no botão de mudar o tema
themeButton.addEventListener('click', () => {
    console.log('vasco')
    const newTheme = body.classList.contains('light-mode') ? 'dark-mode' : 'light-mode';
    applyTheme(newTheme);
  localStorage.setItem('theme', newTheme); // Salva o tema escolhido no localStorage
});

