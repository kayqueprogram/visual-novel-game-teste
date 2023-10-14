# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.










image bg snow = "images/op_snowywoods.jpg"
image bg parque = "bg (1).png"
image bg school = 'images/bgschool.jpg'
image bg frontSchool = 'images/school.png'
image bg artroom = "images/sala_arte.png"
image bg corredor = 'images/bgcorredor.png'
image bg bosque1 = "images/bosque1.png"
image bg bosque2 = "images/bosque2.png"
image bg city = "images/city2.png"
image bg casa = "images/Casa_1.png"

image bg nigthRoom = "images/dorm_prota_night.jpg"
image bg nightRoomBlurred = "images/dorm_prota_night_blurred_ni .jpg"

image snow = SnowBlossom("images/snowflake.png", count=10, border=50, xspeed=(20, 50), yspeed=(100, 200), start=0, fast=False, horizontal=False)
   




image splash = "images/Intro.png"

image vid_a = Movie(play="opening.webm", channel="movie", loop=False)




transform walk:
    xalign 1.0
    ease 3.0 xalign 0.5

transform breathe:
    ease 2.0 yalign 0.0
    ease 2.0 yalign 0.04 #sobe e desce


# usar hide com fade para personagens não é boa ideia kkk


label splashscreen: 
    scene splash
    with Pause(1)

    show text "Sirius Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    scene bg school with dissolve
    $ player = renpy.input ("Digite seu nome: ")
    if player == "":
        $ player = "Yuno"

    $ snow_counter = 0
   
    play music "audio/bgm/piano/Piano 1.ogg"

    scene bg snow with dissolve
    show snow with dissolve
  

    mc "Ei, o que você está fazendo por aqui?"
    show mk normal at truecenter with hpunch:
        zoom 0.5
        yalign 0.19
   
    mk "Ah, [player]? Não esperava te encontrar por aqui."
    mc "Pois é, nem eu. Mas o que faz por aqui?"
    mk "Ah, nada demais, só estou... dando um passeio"
    mc "Você não me parece bem... o que aconteceu?"
    hide mk normal
    show mk happy at truecenter:
        zoom 0.5
        yalign 0.19
    mk "Eu já disse, não é nada."
    "Regra número um sobre as mulheres, que todo homem precisa saber..."
    "Quando elas dizem que não é nada, é porque realmente tem algo a incomodando."
    mc "Unhum, sei"
    mc "Mas, falando sério mocinha, você pode me contar!"

    hide mk happy
    show mk normal at truecenter:
        zoom 0.5
        yalign 0.19
    mc "Pode confiar em mim Miki, eu sou seu amigo, afinal"
    mk "Eu sei [player], é só que... tive uma briga feia com meu irmão hoje."
    mc "Ah, entendo. Família, né? Às vezes as coisas ficam um pouco complicadas."
    hide mk normal
    show mk angry at truecenter:
        zoom 0.5
        yalign 0.19
    mk "Exatamente. Como ele pode ser tão teimoso?!"
    "Eu não me lembro da Miki ter um irmão..."
    "Bem.. deixa pra lá"
    hide mk angry
    show mk happy at truecenter:
        zoom 0.5
        yalign 0.19
    mk "Enfim.. vai passar, não se preocupe."
    "... Será que eu realmente conheço a Miki?"
    "Ela sempre foi tão reservada, mas é minha melhor amiga desde a infância."
    "Eu me pergunto o que ela esconde por trás desse sorriso."
    "Talvez eu nunca tenha prestado atenção o suficiente."
    "Será que a gente realmente se conhece, ou será que só sabemos o que queremos mostrar?"
    "Esses pensamentos sempre passaram pela minha cabeça, mas agora... estão ficando mais fortes."
    "Acho que... talvez eu só esteja pensando demais nisso."
    "Nós nos conhecemos desde pequenos, se algo a incomodasse, ela me contaria, não?"
    "Acho que sim."
    hide mk happy
    show mk surprise at truecenter:
        zoom 0.5
        yalign 0.19
    mc "Hey Miki! Vamos! Se ficarmos por aqui, vamos acabar nos atrasando."
    mk "Oh! É mesmo, quase que me esqueço vamos!"
    "A nerd da turma esquecendo que tem aula? Estranho.."
    stop music
    scene black
    
    show vid_a
    pause

    play sound "audio/alarme.webm"
    scene bg artroom with fade
   
    "Lá vem o Sr.Yasahiro..."
    stop sound
    play music "audio/bgm/beanfeast.ogg"
    mc "Ô bicho chato!"
    show teacher normal at truecenter with dissolve:
        zoom 0.27
        yalign 0.9
    teacher "O que disse [player]?"
    mc "Ah... n-não foi nada senhor..."
    hide teacher normal
    show teacher disagree at truecenter:
        zoom 0.27
        yalign 0.9
    teacher "Acho bom mesmo."
    teacher "Vamos começar a aula pessoal!"
    hide teacher disagree
   
    show ms normal at right with fade: 
        zoom 0.27
        yalign 0.9
    ms "E aí [player]!."
    ms "Como foram suas férias?"
    "Masamune... representante de classe e o aluno mais inteligente e social da classe..."
    "Ele é... tudo o que eu não posso ser."
    "No fim, isso é culpa minha, não é?"
    mc "E aí Cara!"
    show teacher normal at left with dissolve: 
        zoom 0.27
        yalign 0.9
    "Yasahiro olha para trás desconfiado. Nós tratamos logo de disfarçar, enquanto ele voltava aos seus infindáveis textos na lousa."
    hide teacher normal
    mc "Era pra ser uma aula de arte né?"
    ms "Acho que sim, mas não mude de assunto [player] !"
    mc "A mesma coisa de sempre."
    hide ms normal
    show ms stranger at right: 
        zoom 0.27
        yalign 0.9
    ms "O quê?"
    mc "As férias, bestão"
    ms "Ah... você quer dizer, jogando e lendo?"
    mc "Sim, isso mesmo, mas por quê sinto que você ta me desprezando ein?"
    hide ms stranger
    show ms smirk at right: 
        zoom 0.27
        yalign 0.9
    ms "Hahaha"
    ms "Deve ser coisa da sua cabeça"
    "Yasahiro olha novamente para trás, a risada exagerada de Masamune deve ter lhe chamado a atenção."
    "Por um instante, finjo que não o conheço."
    "O Professor se volta para a lousa, e eu, me volto para a criatura ao meu lado."
    mc "O que você quer, ein?"
    hide ms smirk
    show ms stranger at right:
        zoom 0.27
        yalign 0.9
    ms "Huh?!"
    mc "Desenbucha"
    hide ms stranger
    show ms smirk at right: 
        zoom 0.27
        yalign 0.9
    ms "É, parece que não posso te enganar."
    mc "Não mesmo."
    ms "Então [player], eu e um pessoal da sala combinamos de sair depois da escola hoje, que tal?"
    mc "Huh?"
    ms "Você não quer vir junto?"
    "Estranho..."
    "Ele nunca me convidou para nada antes."
    "Acho que..."

    menu:
        "Acho que não vai fazer mal...":
            jump sair_com_amigos
        "Definitivamente não":
            jump nao_sair
        
    
    "Fim da rota, por enquanto"

label sair_com_amigos:
    hide ms smirk
    show ms confiant at right: 
        zoom 0.27
        yalign 0.9
    ms "É assim que se fala cara!"
    ms "Me encontre na saída quando as aulas acabarem."
    mc "Okay"
    "Masamune volta sua atenção para a lousa á sua frente"
    hide ms confiant with dissolve
    "Vejo Miki nos encarando, de relance"
    show mk normal at right with dissolve:
        zoom 0.3
        yalign 0.19
    "Ela parece não ter gostado do que ouviu"
    "Mas fazer o quê?"
    "Não posso ficar no pé dela para sempre."
    hide mk normal
    "Será que estou fazendo a coisa certa?"
    stop music
    scene bg corredor with dissolve
    play sound 'audio/alarme.webm'
    mc "Aqui estou."
    show ms confiant at right with dissolve: 
        zoom 0.27
        yalign 0.9
    stop sound
    play music 'audio/bgm/calmandgentle.webm'
    ms "Finalmente cara! Achei que você não viria mais."
    d "Sim! Eu já estava achando que você tinha nos deixado!"
    mc "Wow!"
    show yz descontent at left with dissolve: 
        zoom 0.7
        yalign - 2.9
    "O que a representante da classe 2A ta fazendo  aqui??"
    hide yz
    show yz smile at left: 
        zoom 0.7
        yalign - 2.9
    yz "E aí [player]!"
    "Eu vou acabar com aquele cara..."
    "Por que ele não me avisou que ela estaria aqui?"
    "Estou cara a cara com o diabo em pessoa."
    "Dizem que essa garota é um demônio disfarçado de anjo."
    "Acho que estou em apuros."
    mc "Vejo que me conhece Yuzuru. Mas ... de onde?"
    yz "Não conheço, é só que... o Masamune fala muito de você."
    hide ms confiant
    show ms stranger at right: 
        zoom 0.27
        yalign 0.9
    ms "Sei disso não."
    yz "Sabe sim senhor. Não lembra? 'Aquele cara só sabe jogar e se isolar'."
    mc "É esse o tipo de coisa que o senhor tem espalhado sobre mim, caro {b}amigo?{/b}"
    hide ms stranger
    show ms normal at right:
        zoom 0.27
        yalign 0.9
    ms " Ah cara, sabe como é."
    ms "As pessoas falam uma das outras, quando elas não estão perto."
    mc "Ou seja, você não é exceção."
    ms "Porque seria?"
    hide ms normal
    show ms confident at right:
        zoom 0.27
        yalign 0.9
    ms "É o que eu mais gosto de fazer, cara."
    "Não acredito que estou ouvindo isso."
    yz "Que coisa, não?"
    hide ms confident
    show ms normal at right:
        zoom 0.27
        yalign 0.9
    ms "Faz parte, faz parte."
    "Eu não to conseguindo mais digerir essa conversa."
    mc "E então? Onde vamos?"
    ms "Ah, isso."
    ms "Acredita que eu não pensei nisso?"
    "Sem palavras"
    "Esse cara é um desastre, hahaha"
    yz "Vamos "
    mc "Pra onde?"
    hide yz smile
    show yz OpenSmile at left: 
        zoom 0.7
        yalign - 2.9

    yz "Tenho um  lugar em mente, mas só vão saber quando chegarmos lá"
    hide ms normal
    show ms stranger at right:
        zoom 0.27
        yalign 0.9
    hide yz OpenSmile
    show yz OpenSmile with moveoutleft:
        zoom 0.7
        yalign 0.3
        xpos 0  # Alterado: Define a posição inicial do personagem dentro da tela.
        ypos 300
        linear 3.0 xpos 1920  # Move o personagem para fora da tela à direita (largura da tela) ao longo de 3 segundos.
        linear 1.0 alpha 0.0  # Faz o personagem desaparecer gradualmente.

    ms "Lá vai ela..."
    "Um capeta ambulante"
    "Meu Deus..."
    "Onde vou parar?..."
    "Bem... acho que nada mais pode dar errado agora"
    scene bg frontSchool with fade
    play audio "audio/alarme.webm"
    "É... acabou nosso dia letivo"
    "Concordei em sair com esses malucos.... o que eu tava pensando?"
    stop sound
    "Bem... acho que desta vez , não fará mal..."
    show mk normal at right with dissolve:
        zoom 0.3
        yalign 0.19
    "Espero que Miki entenda...."
    hide mk normal
    "Afinal, esta é a primeira vez que saio com amigos, assim"
    "Espera..."
    "Amigos?"
    show yz OpenSmile at left: 
        zoom 0.7
        yalign - 2.9
    yz "[player]!! Vamos, não fique parado aí!"
    mc "É... talvez sejam..."
    hide yz OpenSmile  with dissolve
    show ms stranger at right: 
        zoom 0.27
        yalign 0.9
    ms "Ein?"
    ms "Como é?"
    mc "Nada não, tava só viajando aqui"
    hide ms stranger
    show ms confiant at right: 
        zoom 0.27
        yalign 0.9
    ms "Ara"
    ms "Novidade"
    mc "Corno"
    ms "Hahahahahhaahha"
    hide ms confiant 
    with dissolve
    "Começamos a seguir Yuzuru, pra onde será que ela vai nos levar?"
    show yz OpenSmile at left with dissolve: 
        zoom 0.7
        yalign - 2.9
    "Olhando assim, de perto, ela não parece ser o demônio que todos dizem..."
    "Será que falam isso por inveja?"
    "Ela não parece ser uma pessoa ruim..."
    hide yz OpenSmile with dissolve 
    show ms confiant at right with dissolve: 
        zoom 0.27
        yalign 0.9
    "E nem o Masamune."
    "Essa beleza dele é muito exagerada"
    "Tomara que bata a cabeça no poste"
    "Seria merecido"
    show yz OpenSmile at left with dissolve:
        zoom 0.7
        yalign - 2.9
    yz "Estão falando de mim?"
    mc "Ah, claro que não, Yuzuru. Estávamos só..."
    yz "Só o quê?"
    ms "Só elogios, pode acreditar!"
    hide yz OpenSmile with dissolve
    "Yuzuru faz que não se importa, Masamune, me dá uma piscada, com seu sorriso tosco."
    hide ms confiant with dissolve
    "Continuamos seguindo Yuzuru, ansiosos para descobrir onde ela nos levaria."
    stop music
    scene bg bosque1 with fade
    play music "audio/bgm/Floresta.mp3"
    "Depois de muito tempo andando, chegamos a um bosque"
    "Por que será que ela nos trouxe aqui?"

    "O lugar é incrivelmente tranquilo e a natureza ao redor é de uma beleza indescritível. As árvores altas e frondosas criam um teto natural, filtrando a luz do sol e criando um ambiente mágico."
    show yz OpenSmile at left with dissolve:
        zoom 0.7
        yalign - 2.9
    yz "Aqui é um dos meus lugares favoritos da cidade. É tão relaxante, não acham?"
    mc "Meio inesperado"
    hide yz OpenSmile
    show yz smile at left:
        zoom 0.7
        yalign - 2.9
    yz "O que foi?"
    mc "Só... não esperava por isso..."
    show ms confiant at right with dissolve: 
        zoom 0.27
        yalign 0.9
    ms "Realmente. Com sua fama de 'mini-diabo', ninguém esperaria um convite para um lugar tão tranquilo como este."
    hide yz smile
    show yz descontent at left:
        zoom 0.7
        yalign - 2.9
    yz "Ah, entendi. Às vezes as pessoas têm ideias erradas sobre os outros, não é mesmo?"
    mc "Parece que sim. Este lugar é incrível, obrigado por compartilhar  seu esconderijo conosco, hahaha."
    ms "Besta"
    mc "Por quê você não vai ver se estou na esquina?"
    ms "Hahahaha"
    scene bg bosque2 with fade
    "Aproveitamos o tempo explorando o bosque, descobrindo cantos escondidos e apreciando a beleza da natureza ao nosso redor."
    "Paramos quando chegamos próximo ao que parecia ser uma ponte"
    show ms stranger at right with dissolve: 
        zoom 0.27
        yalign 0.9
    show yz descontent at left with dissolve:
        zoom 0.7
        yalign - 2.9
    "Bem, se isso algum dia foi uma ponte, não é mais e nem parece que um dia foi uma"
    "O tempo ameaça mudar, nós trocamos olhares de mútua compreensão;"
    "Bem... hora de voltar"
    stop music
    scene bg city with fade
    play music "audio/bgm/cidade-exterior-20201031.mp3"
    "A cidade está bem movimentada hoje..."
    "Acho que é agora que cada um vai por um caminho"
    show yz OpenSmile at left with dissolve:
        zoom 0.7
        yalign - 2.9
    yz "Então pessoas, vou ficar por aqui, meu pai vai vir me buscar"
    show ms confiant at right with dissolve: 
        zoom 0.27
        yalign 0.9
    ms "UHHHHHH, O pai dela vai vir buscar elaaaa"
    hide yz OpenSmile
    show yz CloseSmile at left:
        zoom 0.7
        yalign -2.9
    yz "E você vai voltar como?"
    yz "No seu cavalo encantado?"
    ms "Talvez eu vá"
    yz "Não sabia que cobravam passagem pra usar cavalos encantados"
    "Essa doeu"
    "Mas vou admitir, ele mereceu hhahahah"
    hide ms confiant
    show ms normal at right: 
        zoom 0.27
        yalign 0.9
    ms "Poxa, deixa meu cavalo em paz"
    mc "Hahhaha"
    mc "Faz parte"
    mc "Bem, vou indo pessoal"
    mc "Muito obrigado por hoje!"
    yz "Thau [player]!!"
    ms "Vai tarde"
    stop music
    scene bg casa with fade

    "Chego em casa no fim da tarde, lembrei das tarefas que meu {b}querido{/b} professor passou..."
    mc "Eu to lascado"
    mc "Hoje o Yasahiro lascou comigo"
    "Melhor eu fazer isso logo, não quero parar nas mãos daquele maníaco"
    "Ele pode ser assustador ás vezes..."
    scene bg nigthRoom with dissolve
    play audio "audio/bgm/grilo.mp3"
    "Ufff"
    "Finalmente cara"
    "Por que diabos temos que estudar sobre arte abstrata?"
    mc "Eu não entendo nada daquilo, poxa..."
    mc "Quer dizer... tudo o que eu vejo é um monte de borrão e pinceladas em lugares aleatórios"
    mc "Isso deveria significar algo?"
    scene bg nightRoomBlurred
    "Melhor eu ir dormir, amanhã é um novo dia."
    stop sound
    scene bg corredor with fade
    play sound "audio/alarme.webm"
    "E lá vou eu mais uma vez"
    "Fazer o que?"
    stop sound
    play sound "audio/corredor.mp3"
    "Se eu não vier, o conselho tutelar vai até mim."
    "Triste."
    show ms normal at right with dissolve:
        zoom 0.27
        yalign 0.9
    ms "E aí [player]!"
    mc "E aí?"
    ms "Ta tão animado hoje..."
    mc "Hoje tem prova de matemática cara..."
    ms "Ah... isso, mas isso é moleza!"
    "Esse cara não se toca não?"
    "Uff... já vi que vai ser um longo dia..."
    ms "A propósito..."
    ms "Falei com Yuzuru hoje"
    "Aquela baixinha enérgica me vem a cabeça, por um momento"
    mc "E?"
    ms "Combinamos de sair hoje, no final do dia, ela quer que você vá também"
    ms "O que me diz?"
    menu:
        "Acho que quero ir sim":
            ms "Combinado então, boa sorte na prova!"
            hide ms normal with dissolve
            "Masamune correu em direção a sala, isso tudo é pressa pra fazer a prova?"
            "Deus me livre..."
        "Então quer dizer que, se dependesse de você, eu não iria?":
            hide ms normal
            show ms confiant at right: 
                zoom 0.27
                yalign 0.9
            ms "Isso mesmo, meu caro!"
            mc "Olha que filha da ....."
            ms "hehe"
            mc "vou só de raiva"
            mc "Me aguarde"
            ms "Certo, não garanto que eu vá te esperar"
            hide ms confiant with dissolve
            "Masamune correu em direção a sala, isso tudo é pressa pra fazer a prova?"
            "Deus me livre..."
        "To a fim não":
            hide ms normal
            show ms stranger at right:
                zoom 0.27
                yalign 0.9
            ms "Não tem essa não cara"
            mc "Ein?"
            ms "Se a Yuzuru te chamou, você vai, querendo ou não."
            mc "O que é essa agressividade?"
            ms "..."
            mc "Isso tudo é só pra que eu vá?"
            mc "Não sabia que você tinha essa consideração por mim."
            ms "Não mesmo"
            mc "Bom... já que você {b}INSISTE{/b}, eu irei"
            ms "Não insisti."
            hide ms stranger
            show ms confiant at right: 
                zoom 0.27
                yalign 0.9
            ms "Mas, de qualquer forma... nos vemos na saída! Até"
            hide ms confiant
            "Masamune correu em direção a sala, isso tudo é pressa pra fazer a prova?"
            "Deus me livre..."

    scene bg corredor with fade
    "Procuro Masamune e Yuzuru no corredor, será que eles já foram?"
    mc "Aqui estoy"
    yz "[player]! Aqui!"
    "Aquelas criaturas já estão do lado de fora, me esperando. Masamune está de cara feia, e parece que tem mais alguém com eles."
    scene bg frontSchool with dissolve
    stop audio
    play music "audio/bgm/calmandgentle.webm"
    "A pessoa, uma garota, que aparentemente estava perturbando Masamune e Yuzuru, vem alegremente em minha direção."
    d "Olá [player]!!"
    mc "E-ein?"
    show ak smile at center with dissolve:
        zoom 0.6
        yalign 2.5
    ak "Acho que você ainda não me conhece, né?"
    mc "E-er... não"
    ak "Akemi, muito prazer!"
    mc "[player]..."
    ak "Eu sei, já te vi algumas vezes por aí."
    ak "Fiquei sabendo que você se deu bem com a {i}devil-girl{/i}"
    ak "Meus parabéns, ninguém, além do Masamune, conseguiu dar conta daquele capetinha."
    mc "Ah..."
    mc "Mas... por quê vocês a chamam assim?"
    ak "É simples"
    ak "ELa é um demônio"
    ak "Vai por mim"
    ak "Não queira saber como ela é em sala"
    hide ak smile
    show ak normal at center:
        zoom 0.6
        align 2.5
    ak "uma tirana"
    ak "Sò porque é representante de sala, acha que tem que descontar suas frustrações em nós."
    mc "Frustrações?..."
    "Sinceramente, tenho medo do rumo que essa conversa pode tomar, não sei se deveria continuar com isso."
    ak "Sim"
    ak "Aquela garota mimada..."
    ak "Ouvi que tem algo de errado com a saúde dela."
    ak "Deve ser por isso que... enfim, já falei demais"
    "Olho para frente, e vejo Masamune, deonde está, nos encarando feio."
    ak "Já estou de saída, mas ouça o conselho que te dei."
    ak "Fique longe dela."
    hide ak normal with dissolve
    "E assim se foi ela, tão rapidamente como quando ela chegou."


"fim do game teste"


return
