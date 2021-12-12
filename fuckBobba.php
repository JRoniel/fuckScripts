/***
* Envie a frase a ser tratada em forma de String, será retornado como no exemplo abaixo.
* Enviada: Você é um viadinho.
* Retornado: Você é um bobba.
*/

<?php

  function receiver(String $text)
  {
    //Lista de palavras ofensivas a serem bloqueadas.
    $badword = ['viado', 'viadinho', 'gay'];
    for($i = 0; $i < count($badword); $i++)
    {
      $text = str_ireplace($badword[$i], 'bobba', $text);
    } return $text;
  }
