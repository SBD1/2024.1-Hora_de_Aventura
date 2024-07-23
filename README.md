# 2024.1-Hora_de_Aventura

<div align="center"> <img src="docs/Imagens/HoraDeAventura.jpg" height="230" width="auto"/> </div>

## Sobre o projeto

Repositório dedicado a realização do trabalho sobre a série Hora de Aventura com os conceitos aprendidos na matéria de Bancos de Dados - 2024.1 ministrada na UnB-FGA pelo professor Maurício Serrano.

## Alunos

| Nome                                                     | Matrícula |
| :------------------------------------------------------- | :-------: |
| [Ciro Costa de Araujo](https://github.com/)              | 190011611 |
| [Luana de Lima Medeiros](https://github.com/LuaMedeiros) | 190091444 |
| [Lucas Macedo Barboza](https://github.com/Luckx98)       | 190091720 |

<div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
    <tbody>
        <tr>
               <td align="center"><a href="https://github.com/ciro-c">
               <img onmouseover="opaqImg(this)" onmouseout="normalImg(this)" style="border-radius: 50%; opacity: 1;" src="https://avatars.githubusercontent.com/ciro-c" alt="" width="100px;"><br><sub><b>Ciro Costa</b></sub></a><br><a href="https://github.com/ciro-c"></a>
               </td> 
                      <td align="center"><a href="https://github.com/LuaMedeiros">
                      <img onmouseover="opaqImg(this)" onmouseout="normalImg(this)" style="border-radius: 50%; opacity: 1;" src="https://avatars.githubusercontent.com/LuaMedeiros" alt="" width="100px;"><br><sub><b>Luana Medeiros</b></sub></a><br><a href="https://github.com/LuaMedeiros"></a>
                      </td>  
        <td align="center"><a href="https://github.com/Luckx98"><img onmouseover="opaqImg(this)" onmouseout="normalImg(this)" style="border-radius: 50%; opacity: 1;" src="https://avatars.githubusercontent.com/Luckx98" alt="" width="100px;"><br><sub><b>Lucas Macedo</b></sub></a><br><a href="https://github.com/Luckx98"></a></td> 
    </tr> 
</tbody></table></div></div>

## Sobre o Desenho

### Personagens Principais:

- Finn: Um jovem corajoso e aventureiro que veste um chapéu branco com orelhas. Ele é o último humano conhecido e sonha em ser um grande herói.
- Jake: Um cão mágico que é o melhor amigo e irmão adotivo de Finn. Ele tem a habilidade de esticar e mudar sua forma de várias maneiras.
- Princesa Jujuba: A governante do Reino Doce, uma cientista e criadora de muitos dos habitantes do seu reino.
- Rei Gelado: Um vilão trágico que usa uma coroa mágica que lhe dá poder, mas também o deixa mentalmente instável. Ele sequestra princesas na esperança de encontrar o amor.

### Resumo

"Hora de Aventura" é uma série de animação que segue as aventuras de Finn, um garoto humano, e seu melhor amigo Jake, um cachorro com poderes mágicos que pode mudar de forma e tamanho à vontade. Juntos, eles vivem na Terra de Ooo, um mundo pós-apocalíptico cheio de criaturas fantásticas e bizarras. Finn é um jovem corajoso e aventureiro que sonha em ser um grande herói, enquanto Jake é seu melhor amigo e irmão adotivo, com habilidades mágicas que os ajudam em suas jornadas. Eles são acompanhados por outros personagens memoráveis, como a Princesa Jujuba, a governante do Reino Doce e cientista criadora de muitos dos habitantes do seu reino, e o Rei Gelado, um vilão trágico que usa uma coroa mágica que lhe dá poder, mas também o deixa mentalmente instável.

A série aborda temas de aventura e amizade, destacando a importância da lealdade, ao mesmo tempo em que explora um mundo cheio de fantasia e magia. A Terra de Ooo está repleta de seres mágicos, reinos exóticos e mistérios que Finn e Jake desvendam ao longo de suas missões. Além das aventuras, a série também trata do crescimento e maturidade de Finn, que passa por várias experiências que o ajudam a entender mais sobre si mesmo e o mundo ao seu redor.

"Hora de Aventura" é conhecida por seu estilo de animação vibrante e colorido, com personagens e cenários criativos. A série combina humor leve e absurdo com temas profundos como identidade, perda e moralidade. Com uma narrativa serializada, a história evolui ao longo das temporadas, apresentando arcos de personagens complexos e desenvolvimento de trama contínuo. A série se tornou um fenômeno cultural, influenciando outras obras de animação e ganhando uma base de fãs dedicada, além de ser amplamente aclamada pela crítica por sua originalidade e criatividade. "Hora de Aventura" é uma mistura encantadora de aventuras épicas, comédia e momentos emocionantes, ambientada em um mundo mágico e peculiar que atrai tanto crianças quanto adultos, oferecendo algo único para cada espectador.

## Sobre o Jogo

### Como o jogo funciona?

### Como jogar?

#### Intalação
O projeto pode ser rodado com docker ou sem docker. Basta instalar o docker ou python 3 e Postgres.

#### Rodando o projeto
No docker:
Rodar os commandos
```console
# Rodando postgress no background
docker-compose up -d postgres
# Rodando a aplicação em python
docker-compose up app
```
Sem docker:
Subir o seu Postgres e depois mandar o python instalar os requisitos
```console

pip install -r requirements.txt

```
Em seguida mandar o python rodar a main do projeto

```console
python3 ./main.py

```

#### Parando o projeto
no Docker:
```console
docker-compose down
```
Sem docker:
Fechar o terminal ou dar ctrl+c


## Apresentações

| Módulo | Link da gravação          | Data       |
| ------ | ------------------------- | ---------- |
| 1      | [Apresentação Módulo 1](https://www.youtube.com/watch?v=gWyj5AUVdbY) | 22/07/2024 |

## Histórico de Versão

| Versão |    Data    | Descrição         | Autor                                            | Revisão                 |
| :----: | :--------: | ----------------- | ------------------------------------------------ | ----------------------- |
|  1.0   | 19/07/2024 | Criação do README | [Luana Medeiros](https://github.com/LuaMedeiros) | [Ciro Costa](https://github.com/ciro-c) |
