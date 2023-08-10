/***
* Envie a frase a ser tratada em forma de String, será retornado como no exemplo abaixo.
* Enviada: Você é um viado.
* Retornado: Você é um bobba.
*/

function receiver(text) {
  // Lista de palavras ofensivas a serem bloqueadas.
  const badWords = ['viado', 'fuder', 'gay'];

  for (let i = 0; i < badWords.length; i++) {
    const regex = new RegExp(badWords[i], 'gi'); // 'gi' para fazer a substituição sem diferenciação de maiúsculas/minúsculas
    text = text.replace(regex, 'bobba');
  }

  return text;
}
