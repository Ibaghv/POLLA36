import pygame
import time
pygame.init()

def cargar_jugador():
    parado=pygame.image.load("Project_NorthZ/Imágenes/Personajes/Fran_estatico.png").convert_alpha()
    derecha1=pygame.image.load("Project_NorthZ/Imágenes/Personajes/Fran_derecha1.png").convert_alpha()
    derecha2=pygame.image.load("Project_NorthZ/Imágenes/Personajes/Fran_derecha2.png").convert_alpha()
    izquierda1=pygame.image.load("Project_NorthZ/Imágenes/Personajes/Fran_izquierda1.png").convert_alpha()
    izquierda2=pygame.image.load("Project_NorthZ/Imágenes/Personajes/Fran_izquierda2.png").convert_alpha()
    salto=pygame.image.load("Project_NorthZ/Imágenes/Personajes/Fran_salto.png").convert_alpha()

    parado=pygame.transform.scale(parado,(260,370))
    derecha1=pygame.transform.scale(derecha1,(190,330))
    derecha2=pygame.transform.scale(derecha2,(190,330))
    izquierda1=pygame.transform.scale(izquierda1,(190,330))
    izquierda2=pygame.transform.scale(izquierda2,(190,330))
    salto=pygame.transform.scale(salto,(190,330))

    return parado, derecha1, derecha2, izquierda1, izquierda2, salto

def imagen_Mp():
    Menu_carga=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Menu_carga_prueba.jpeg")#Cargar la imagen dentro del código
    Menu_Principal=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Menú_principal.png")
    Enpezar_Menu=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Enpezar_Menu_carga.png")
    Nueva_partida=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Nueva_partida_MP.png")
    Controles=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Controles_MP.png")
    Tutorial=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Turotial_MP.png")
    Creditos=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Créditos_MP.png")
    Salir=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Salir_MP.png")
    ControlesA=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Controles.jpeg")
    TutorialA=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Tutorial negro.png")
    CreditosA=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Créditos negro.jpeg")
    SalirA=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/SalirA.jpg")
    Nueva_partida_rojo=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Nueva_partida_MP_rojo.png")
    Controles_rojo=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Controles_MP_rojo.png")
    Tutorial_rojo=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Tutorial_rojo.png")
    Creditos_rojo=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Créditos_MP_rojo.png")
    Salir_rojo=pygame.image.load("Project_NorthZ/Imágenes/Menu Carga/Salir_MP_rojo.png")
    fcliki=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/fcliki.png")
    
    Menu_carga=pygame.transform.scale(Menu_carga,(1500, 750))#Transformar la imagen a un tamaño
    Menu_Principal=pygame.transform.scale(Menu_Principal,(1500, 750))
    Enpezar_Menu=pygame.transform.scale(Enpezar_Menu,(723, 110))
    Nueva_partida=pygame.transform.scale(Nueva_partida,(258,60))#Boton para ir a Nueva partida
    Controles=pygame.transform.scale(Controles,(180,50))
    Tutorial=pygame.transform.scale(Tutorial,(190,55))
    Creditos=pygame.transform.scale(Creditos,(165,50))
    Salir=pygame.transform.scale(Salir,(110,50))
    ControlesA=pygame.transform.scale(ControlesA,(1500,750))
    TutorialA=pygame.transform.scale(TutorialA,(1500,750))
    CreditosA=pygame.transform.scale(CreditosA,(1500,750))
    SalirA=pygame.transform.scale(SalirA,(1500,750))
    Nueva_partida_rojo=pygame.transform.scale(Nueva_partida_rojo,(300,60))
    Controles_rojo=pygame.transform.scale(Controles_rojo,(210,50))
    Tutorial_rojo=pygame.transform.scale(Tutorial_rojo,(230,55))
    Creditos_rojo=pygame.transform.scale(Creditos_rojo,(200,45))
    Salir_rojo=pygame.transform.scale(Salir_rojo,(175,45))
    fcliki=pygame.transform.scale(fcliki,(190,80))
        
    return{
    "pantallas": {
        "carga": Menu_carga,
        "principal": Menu_Principal,
        "controles": ControlesA,
        "tutorial": TutorialA,
        "creditos": CreditosA,
        "salir": SalirA},
    "botones": {
        "empezar": Enpezar_Menu,
        "NP": Nueva_partida,
        "C": Controles,
        "T": Tutorial,
        "Cr": Creditos,
        "S": Salir,
        "volver":fcliki},
    "botones_rojo": {
        "NP_rojo": Nueva_partida_rojo,
        "C_rojo": Controles_rojo,
        "T_rojo": Tutorial_rojo,
        "Cr_rojo": Creditos_rojo,
        "S_rojo": Salir_rojo}
    }

def imagen_lore():
    Nueva_partida_1_lore=pygame.image.load("Project_NorthZ/Imágenes/Juego lore/01_el_dia_que_el_mundo_murio.png")
    Nueva_partida_2_lore=pygame.image.load("Project_NorthZ/Imágenes/Juego lore/02_el_metro.png")
    Nueva_partida_3_lore=pygame.image.load("Project_NorthZ/Imágenes/Juego lore/03_la_huida.png")
    Nueva_partida_4_lore=pygame.image.load("Project_NorthZ/Imágenes/Juego lore/04_las_facciones.png")
    Nueva_partida_5_lore=pygame.image.load("Project_NorthZ/Imágenes/Juego lore/05_los_infectados.png")
    Nueva_partida_6_lore=pygame.image.load("Project_NorthZ/Imágenes/Juego lore/06_el_secreto_de_la_bomba.png")
    Nueva_partida_7_lore=pygame.image.load("Project_NorthZ/Imágenes/Juego lore/07_tu_historia_comienza.png")
    Nueva_partida_8_lore=pygame.image.load("Project_NorthZ/Imágenes/Juego lore/08_final.png")
    
    Nueva_partida_1_lore=pygame.transform.scale(Nueva_partida_1_lore,(1500,750))#Página de la Nueva partida
    Nueva_partida_2_lore=pygame.transform.scale(Nueva_partida_2_lore,(1500,750))
    Nueva_partida_3_lore=pygame.transform.scale(Nueva_partida_3_lore,(1500,750))
    Nueva_partida_4_lore=pygame.transform.scale(Nueva_partida_4_lore,(1500,750))
    Nueva_partida_5_lore=pygame.transform.scale(Nueva_partida_5_lore,(1500,750))
    Nueva_partida_6_lore=pygame.transform.scale(Nueva_partida_6_lore,(1500,750))
    Nueva_partida_7_lore=pygame.transform.scale(Nueva_partida_7_lore,(1500,750))
    Nueva_partida_8_lore=pygame.transform.scale(Nueva_partida_8_lore,(1500,750))
    
    return{
        "pantallas_lore":{
            "Lore1":Nueva_partida_1_lore,
            "Lore2":Nueva_partida_2_lore,
            "Lore3":Nueva_partida_3_lore,
            "Lore4":Nueva_partida_4_lore,
            "Lore5":Nueva_partida_5_lore,
            "Lore6":Nueva_partida_6_lore,
            "Lore7":Nueva_partida_7_lore,
            "Lore8":Nueva_partida_8_lore,}
    }

def imagen_play():
    JP1=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP 1.jpeg")
    JP2=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP2.jpeg")
    JP3=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP3.jpeg")
    JP4=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP4.jpeg")
    JP5=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP5.jpeg")   
    JP6=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP6.png")
    JP7=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP7.png")
    Lucha_PM1=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/lpm1.jpeg")
    Lucha_PM2=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/lpm2.jpeg")
    JP7_puerta=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP7_puerta.png")
    JP6_puerta=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP6_puerta.png")
        
    Zombie1=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Zombi1.jpeg")
       
    Coches1=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Coches1.jpeg")
    Coche2=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Coche2.jpeg")
    Puerta_coche2=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Puerta_coche2.png")
    
    JP1_puerta=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP1_puerta.png")
    JP2_puerta=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP2_puerta.png")
    JP3_puerta=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP3_puerta.png")
    JP4_puerta=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP4_puerta.png")
    JP7_puerta=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/JP7_puerta.png")
    
    Coche1_click=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Coche1_click.png")
    Coche1_clickd=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Coches1_derecha.png")
    Coche1_clicki=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Coches1_izquierda.png")
    
    zombie1clik=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Zombie1clik.png")
    
    bcurar=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/bcurar.png")
    bdefensa=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/bdefensa.png")
    bhuir=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/bhuir.png")
    bluchar=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/bluchar.png")

    # Versiones PM1: se ajustan al tamaño real de los botones ya dibujados en lpm1.jpeg.
    botones_PM1={
        "Luchar":pygame.transform.smoothscale(bluchar,(180,70)),
        "Defensa":pygame.transform.smoothscale(bdefensa,(180,70)),
        "Curar":pygame.transform.smoothscale(bcurar,(180,70)),
        "Huir":pygame.transform.smoothscale(bhuir,(180,70))}
    
    vida_67=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/67-67.png")
    vida_52=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/52-67.png")
    vida_37=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/37-67.png")
    vida_22=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/22-67.png")
    vida_7=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/7-67.png")
    vida_0=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/0-67.png")

    zombie_33=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/33-33zombie1.png")
    zombie_20=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/20-33zombie1.png")
    zombie_5=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/5-33zombie1.png")
    zombie_0=pygame.image.load("Project_NorthZ/Imágenes/Juego principal/0-33zombie1.png")
    
    barras_fran_PM={
        100:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/100-100-1pmf.png").convert_alpha(),
        85:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/85-100-1pmf.png").convert_alpha(),
        70:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/70-100-1pmf.png").convert_alpha(),
        55:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/55-100-1pmf.png").convert_alpha(),
        40:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/40-100-1pmf.png").convert_alpha(),
        25:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/25-100-1pmf.png").convert_alpha(),
        10:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/10-100-1pmf.png").convert_alpha(),
        0:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/0-100-1pmf.png").convert_alpha()}
    barras_pm1={
        100:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/100-100-1pmpm.png").convert_alpha(),
        90:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/90-100-1pmpm.png").convert_alpha(),
        80:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/80-100-1pmpm.png").convert_alpha(),
        70:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/70-100-1pmpm.png").convert_alpha(),
        60:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/60-100-1pmpm.png").convert_alpha(),
        50:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/50-100-1pmpm.png").convert_alpha(),
        40:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/40-100-1pmpm.png").convert_alpha(),
        20:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/20-100-1pmpm.png").convert_alpha(),
        10:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/10-100-1pmpm.png").convert_alpha(),
        0:pygame.image.load("Project_NorthZ/Imágenes/Juego principal/Barras_PM1/0-100-1pmpm.png").convert_alpha()}

    JP1=pygame.transform.scale(JP1,(1500,750))
    JP2=pygame.transform.scale(JP2,(1500,750))
    JP3=pygame.transform.scale(JP3,(1500,750))
    JP4=pygame.transform.scale(JP4,(1500,750))
    JP5=pygame.transform.scale(JP5,(1500,750))
    JP6=pygame.transform.scale(JP6,(1500,750))
    JP7=pygame.transform.scale(JP7,(1500,750))
    Lucha_PM1=pygame.transform.scale(Lucha_PM1,(1500,750))
    Lucha_PM2=pygame.transform.scale(Lucha_PM2,(1500,750))
    Zombie1=pygame.transform.scale(Zombie1,(1500,750))
    Coches1=pygame.transform.scale(Coches1,(1500,750))
    Coche2=pygame.transform.scale(Coche2,(1500,750))
    # Las tres puertas se ajustan a los límites reales que ocupan en sus fondos
    # ya escalados a 1500x750. Se usan estas mismas dimensiones al dibujarlas
    # y al detectar el clic, para que la imagen visible sea el propio botón.
    Puerta_coche2=Puerta_coche2.subsurface((8,0,66,162)).copy()
    Puerta_coche2=pygame.transform.smoothscale(Puerta_coche2,(66,133))

    JP1_puerta=pygame.transform.scale(JP1_puerta,(89,346))
    JP2_puerta=pygame.transform.scale(JP2_puerta,(258,632))
    JP3_puerta=pygame.transform.scale(JP3_puerta,(270,640))
    JP4_puerta=pygame.transform.scale(JP4_puerta,(231,632))
    JP6_puerta=pygame.transform.smoothscale(JP6_puerta,(145,380))
    JP7_puerta=pygame.transform.smoothscale(JP7_puerta,(205,465))
    Coche1_click=pygame.transform.scale(Coche1_click,(598,240))
    Coche1_clickd=pygame.transform.scale(Coche1_clickd,(256,196))
    Coche1_clicki=pygame.transform.scale(Coche1_clicki,(332,237))
    zombie1clik=pygame.transform.scale(zombie1clik,(163,435))
    
    bluchar=pygame.transform.scale(bluchar,(363,82))
    bdefensa=pygame.transform.scale(bdefensa,(369,82))
    bcurar=pygame.transform.scale(bcurar,(363,82))
    bhuir=pygame.transform.scale(bhuir,(369,82))
    
    vida_67=pygame.transform.scale(vida_67,(378,72))
    vida_52=pygame.transform.scale(vida_52,(378,72))
    vida_37=pygame.transform.scale(vida_37,(378,72))
    vida_22=pygame.transform.scale(vida_22,(378,72))
    vida_7=pygame.transform.scale(vida_7,(378,72))
    vida_0=pygame.transform.scale(vida_0,(378,72))

    zombie_33=pygame.transform.scale(zombie_33,(403,72))
    zombie_20=pygame.transform.scale(zombie_20,(403,72))
    zombie_5=pygame.transform.scale(zombie_5,(403,72))
    zombie_0=pygame.transform.scale(zombie_0,(403,72))  
    
    return{
        "JP_principal":{
            "JP1":JP1,
            "JP2":JP2,
            "JP3":JP3,
            "JP4":JP4,
            "JP5":JP5,
            "JP6":JP6,
            "JP7":JP7},
        "Barras_PM1":{
            "Fran":barras_fran_PM,
            "PM1":barras_pm1},
        "Coches":{
            "Coches1":Coches1,
            "Coche2":Coche2,
            "Puerta_coche2":Puerta_coche2,},
        "Coches_click":{
            "Coches1_click":Coche1_click,
            "Coches1_clickd":Coche1_clickd,
            "Coches1_clicki":Coche1_clicki},
        "JP_puertas":{
            "JP1_puerta":JP1_puerta,
            "JP2_puerta":JP2_puerta,
            "JP3_puerta":JP3_puerta,
            "JP4_puerta":JP4_puerta,
            "JP6_puerta":JP6_puerta},
        "Puerta_PM":{
            "JP7_puerta":JP7_puerta},
        "Zombies":{
            "Zombie1":Zombie1,
            "Zombie1clik":zombie1clik,},
        "Luchas_PM":{
            "PM1":Lucha_PM1,
            "PM2":Lucha_PM2},
        "Botones_combate":{
            "Luchar":bluchar,
            "Defensa":bdefensa,
            "Curar":bcurar,
            "Huir":bhuir},
        "Botones_PM1":botones_PM1,
        "Vida_Fran":{
            67:vida_67,
            52:vida_52,
            37:vida_37,
            22:vida_22,
            7:vida_7,
            0:vida_0},
        "Vida_Zombie":{
            33:zombie_33,
            20:zombie_20,
            5:zombie_5,
            0:zombie_0}
           }
    
def musica():
    click_MCarga=pygame.mixer.Sound("Project_NorthZ/Audio_vídeos/Menu_Carga.mp3")
    click_Mprincipal=pygame.mixer.Sound("Project_NorthZ/Audio_vídeos/Menu_principal.mp3")
        
    return click_MCarga, click_Mprincipal
def rect_boton(imagenes_Mp):
    rect_botonEM=imagenes_Mp["botones"]["empezar"].get_rect()#Crear un rectangulo para que se pueda clickear
    rect_botonEM.topleft=(400,592)#Coordenadas de zona que se puede clickear
    rect_botonNP=imagenes_Mp["botones"]["NP"].get_rect()
    rect_botonNP.topleft=(72,351)
    rect_botonC=imagenes_Mp["botones"]["C"].get_rect()
    rect_botonC.topleft=(72,488)   
    rect_botonT=imagenes_Mp["botones"]["T"].get_rect()
    rect_botonT.topleft=(72,426)
    rect_botonCr=imagenes_Mp["botones"]["Cr"].get_rect()
    rect_botonCr.topleft=(68,544)
    rect_botonS=imagenes_Mp["botones"]["S"].get_rect()
    rect_botonS.topleft=(72,604)
    rect_botonvolver=imagenes_Mp["botones"]["volver"].get_rect()
    rect_botonvolver.topleft=(1200,80)
    
    return{
        "clickeable_AL":{
            "Rb_EM":rect_botonEM,
            "Rb_NP":rect_botonNP,
            "Rb_C":rect_botonC,
            "Rb_T":rect_botonT,
            "Rb_Cr":rect_botonCr,
            "Rb_S":rect_botonS,
            "RB_volver":rect_botonvolver}
    }
    
# Coordenadas medidas sobre los fondos de 1500x750.
# Cada rectángulo se obtiene de la imagen ya escalada: no hay áreas de clic aparte.
POS_PUERTA_COCHE2=(414,460)
POS_PUERTA_JP6=(1324,165)
POS_PUERTA_JP7=(253,122)

# Coordenadas de las zonas gráficas originales de PM1, medidas sobre lpm1.jpeg
# escalado a 1500x750. Las imágenes y sus clics comparten estos mismos rectángulos.
POS_BARRA_PM1=(120,110)
TAM_BARRA_PM1=(206,68)
POS_BARRA_FRAN_PM1=(1300,460)
TAM_BARRA_FRAN_PM1=(200,75)
POS_BOTONES_PM1={
    "Luchar":(1135,590),
    "Defensa":(1320,590),
    "Curar":(1135,665),
    "Huir":(1320,665)}


def rect_puertas(imagenes_play):
    rect_puertaJP1=imagenes_play["JP_puertas"]["JP1_puerta"].get_rect()
    rect_puertaJP1.topleft=(1385,307)
    rect_puertaJP2=imagenes_play["JP_puertas"]["JP2_puerta"].get_rect()
    rect_puertaJP2.topleft=(1230,110)
    rect_puertaJP3=imagenes_play["JP_puertas"]["JP3_puerta"].get_rect()
    rect_puertaJP3.topleft=(1224,228)
    rect_puertaJP4=imagenes_play["JP_puertas"]["JP4_puerta"].get_rect()
    rect_puertaJP4.topleft=(1224,224)
    # El rectángulo es exactamente el contorno de la imagen superpuesta.
    rect_puertaJP6=imagenes_play["JP_puertas"]["JP6_puerta"].get_rect(topleft=POS_PUERTA_JP6)
    rect_puertaCoche2=imagenes_play["Coches"]["Puerta_coche2"].get_rect(topleft=POS_PUERTA_COCHE2)
    rect_puertaJP7=imagenes_play["Puerta_PM"]["JP7_puerta"].get_rect(topleft=POS_PUERTA_JP7)
    
    rect_coche1=imagenes_play["Coches_click"]["Coches1_click"].get_rect()    
    rect_coche1.topleft=(522,362)
    rect_coche1d=imagenes_play["Coches_click"]["Coches1_clickd"].get_rect()
    rect_coche1d.topleft=(1240,130)
    rect_coche1i=imagenes_play["Coches_click"]["Coches1_clicki"].get_rect()
    rect_coche1i.topleft=(118,148)    
    
    rect_botonZ1=imagenes_play["Zombies"]["Zombie1clik"].get_rect()
    rect_botonZ1.topleft=(234,252)
    
    rect_luchar=imagenes_play["Botones_combate"]["Luchar"].get_rect()
    rect_luchar.topleft=(747,579)
    rect_defensa=imagenes_play["Botones_combate"]["Defensa"].get_rect()
    rect_defensa.topleft=(1118,579)
    rect_curar=imagenes_play["Botones_combate"]["Curar"].get_rect()
    rect_curar.topleft=(747,668)
    rect_huir=imagenes_play["Botones_combate"]["Huir"].get_rect()
    rect_huir.topleft=(1118,668)
    # El clic de PM1 se obtiene del rectángulo de cada imagen visible.
    rects_botones_PM1={
        nombre:imagen.get_rect(topleft=POS_BOTONES_PM1[nombre])
        for nombre,imagen in imagenes_play["Botones_PM1"].items()}
    
    return{
        "clickeable_puertas":{
            "Rb_JP1":rect_puertaJP1,
            "Rb_JP2":rect_puertaJP2,
            "Rb_JP3":rect_puertaJP3,
            "Rb_JP4":rect_puertaJP4,
            "Rb_JP6":rect_puertaJP6,
            "Rb_JP7":rect_puertaJP7,
            "Rb_Coche2":rect_puertaCoche2},
        "clickeable_coche":{
            "rectC1":rect_coche1,
            "rectC1d":rect_coche1d,
            "rectC1i":rect_coche1i},
        "clickeable_zombie":{
            "Z1":rect_botonZ1},
        "clickeable_combate":{
            "Luchar":rect_luchar,
            "Defensa":rect_defensa,
            "Curar":rect_curar,
            "Huir":rect_huir},
        "clickeable_combate_PM1":rects_botones_PM1,
        "clickeable_combate_PM":{
            "Luchar":rect_luchar,
            "Defensa":rect_defensa,
            "Curar":rect_curar,
            "Huir":rect_huir}
    }

def dibujar_pantalla(pantalla_actual, imagenes_Mp, jugando, rectangulos_click, imagenes_lore):
    
    if pantalla_actual=="carga":
        ventana.blit(imagenes_Mp["pantallas"]["carga"],(0,0))
        ventana.blit(imagenes_Mp["botones"]["empezar"],(400,592))
    elif pantalla_actual=="principal":
        ventana.blit(imagenes_Mp["pantallas"]["principal"],(0,0))
        
        posicion=pygame.mouse.get_pos()#Donde está el ratón
        if rectangulos_click["clickeable_AL"]["Rb_NP"].collidepoint(posicion):
            ventana.blit(imagenes_Mp["botones_rojo"]["NP_rojo"],(55,351))
        else:
            ventana.blit(imagenes_Mp["botones"]["NP"],(72,351))
        if rectangulos_click["clickeable_AL"]["Rb_T"].collidepoint(posicion):
            ventana.blit(imagenes_Mp["botones_rojo"]["T_rojo"],(45,426))
        else:
            ventana.blit(imagenes_Mp["botones"]["T"],(72,426))
        if rectangulos_click["clickeable_AL"]["Rb_C"].collidepoint(posicion):
            ventana.blit(imagenes_Mp["botones_rojo"]["C_rojo"],(50,488))
        else:
            ventana.blit(imagenes_Mp["botones"]["C"],(72,488))
        if rectangulos_click["clickeable_AL"]["Rb_Cr"].collidepoint(posicion):
            ventana.blit(imagenes_Mp["botones_rojo"]["Cr_rojo"],(40,544))
        else:
            ventana.blit(imagenes_Mp["botones"]["Cr"],(68,544))
        if rectangulos_click["clickeable_AL"]["Rb_S"].collidepoint(posicion):
            ventana.blit(imagenes_Mp["botones_rojo"]["S_rojo"],(45,604))
        else:
            ventana.blit(imagenes_Mp["botones"]["S"],(72,604))
        
    elif pantalla_actual=="Comienzo partida":
        ventana.blit(imagenes_lore["pantallas_lore"]["Lore1"],(0,0))
        
        
    elif pantalla_actual=="Controles":
        ventana.blit(imagenes_Mp["pantallas"]["controles"],(0,0))
        ventana.blit(imagenes_Mp["botones"]["volver"],(1200,80))
    elif pantalla_actual=="Tutorial":
        ventana.blit(imagenes_Mp["pantallas"]["tutorial"],(0,0))
        ventana.blit(imagenes_Mp["botones"]["volver"],(1200,80))
    elif pantalla_actual=="Creditos":
        ventana.blit(imagenes_Mp["pantallas"]["creditos"],(0,0))
        ventana.blit(imagenes_Mp["botones"]["volver"],(1200,80))
    elif pantalla_actual=="Salir":
        ventana.blit(imagenes_Mp["pantallas"]["salir"],(0,0))
        pygame.display.update()
        time.sleep(3)
        jugando=False
    elif pantalla_actual=="plore1":
        ventana.blit(imagenes_lore["pantallas_lore"]["Lore2"],(0,0))
    elif pantalla_actual=="plore2":
        ventana.blit(imagenes_lore["pantallas_lore"]["Lore3"],(0,0))
    elif pantalla_actual=="plore3":
        ventana.blit(imagenes_lore["pantallas_lore"]["Lore4"],(0,0))
    elif pantalla_actual=="plore4":
        ventana.blit(imagenes_lore["pantallas_lore"]["Lore5"],(0,0))
    elif pantalla_actual=="plore5":
        ventana.blit(imagenes_lore["pantallas_lore"]["Lore6"],(0,0))
    elif pantalla_actual=="plore6":
        ventana.blit(imagenes_lore["pantallas_lore"]["Lore7"],(0,0)) 
    elif pantalla_actual=="plore7":
        ventana.blit(imagenes_lore["pantallas_lore"]["Lore8"],(0,0))
    return ventana, jugando

def dib_pantalla_juego(pantalla_actual, imagenes_play):
    if pantalla_actual=="JP_1":
        ventana.blit(imagenes_play["JP_principal"]["JP1"],(0,0))
    elif pantalla_actual=="JP_2":
        ventana.blit(imagenes_play["JP_principal"]["JP2"],(0,0))
    elif pantalla_actual=="JP_3":
        ventana.blit(imagenes_play["JP_principal"]["JP3"],(0,0))
    elif pantalla_actual=="JP_4":
        ventana.blit(imagenes_play["JP_principal"]["JP4"],(0,0))
    elif pantalla_actual=="JP_5":
        ventana.blit(imagenes_play["JP_principal"]["JP5"],(0,0))
        ventana.blit(imagenes_play["Zombies"]["Zombie1clik"],(234,252))
        
    elif pantalla_actual=="JP_6":
        ventana.blit(imagenes_play["JP_principal"]["JP6"],(0,0))
        ventana.blit(imagenes_play["JP_puertas"]["JP6_puerta"],POS_PUERTA_JP6)
    elif pantalla_actual=="JP_7":
        ventana.blit(imagenes_play["JP_principal"]["JP7"],(0,0))
        ventana.blit(imagenes_play["Puerta_PM"]["JP7_puerta"],POS_PUERTA_JP7)

    elif pantalla_actual=="Coche1":
        ventana.blit(imagenes_play["Coches"]["Coches1"],(0,0))
    elif pantalla_actual=="Coche2":
        ventana.blit(imagenes_play["Coches"]["Coche2"],(0,0))
        ventana.blit(imagenes_play["Coches"]["Puerta_coche2"],POS_PUERTA_COCHE2)
        
    elif pantalla_actual=="PM1_lucha":
        ventana.blit(imagenes_play["Luchas_PM"]["PM1"],(0,0))

        # Sustituir solo la zona de PS de cada panel, sin duplicar el HUD.
        dibujar_barra_PM(imagenes_play["Barras_PM1"]["PM1"],vida_pm1,POS_BARRA_PM1,TAM_BARRA_PM1)
        dibujar_barra_PM(imagenes_play["Barras_PM1"]["Fran"],vida_fran_pm1,POS_BARRA_FRAN_PM1,TAM_BARRA_FRAN_PM1)

        # Botones PM1 superpuestos exactamente sobre los botones del fondo.
        for nombre,imagen in imagenes_play["Botones_PM1"].items():
            ventana.blit(imagen,POS_BOTONES_PM1[nombre])

        fuente=pygame.font.Font(None,40)
        if vida_pm1==0:
            texto=fuente.render("PM1 DERROTADO",True,(255,255,255))
            ventana.blit(texto,(550,390))
        elif vida_fran_pm1==0:
            texto=fuente.render("FRAN HA PERDIDO",True,(255,255,255))
            ventana.blit(texto,(550,390))
    elif pantalla_actual=="PM2_lucha":
        ventana.blit(imagenes_play["Luchas_PM"]["PM2"],(0,0))
        fuente=pygame.font.Font(None,38)
        texto=fuente.render(str(vida_pm2)+"/150",True,(255,255,255))
        ventana.blit(texto,(130,75))
        if vida_fran_pm2 in imagenes_play["Barras_PM1"]["Fran"]:
            dibujar_barra_PM(imagenes_play["Barras_PM1"]["Fran"],vida_fran_pm2,(1010,420))
        else:
            texto=fuente.render(str(vida_fran_pm2)+"/100",True,(255,255,255))
            ventana.blit(texto,(1350,470))
        if vida_pm2==0:
            texto=fuente.render("PM2 DERROTADO",True,(255,255,255))
            ventana.blit(texto,(600,390))
        elif vida_fran_pm2==0:
            texto=fuente.render("FRAN HA PERDIDO",True,(255,255,255))
            ventana.blit(texto,(600,390))
        
    elif pantalla_actual=="Z1_lucha":
        ventana.blit(imagenes_play["Zombies"]["Zombie1"],(0,0))

        ventana.blit(imagenes_play["Vida_Zombie"][vida_zombie],(205,141))
        ventana.blit(imagenes_play["Vida_Fran"][vida_fran],(1099,454))

        ventana.blit(imagenes_play["Botones_combate"]["Luchar"],(747,579))
        ventana.blit(imagenes_play["Botones_combate"]["Defensa"],(1118,579))
        ventana.blit(imagenes_play["Botones_combate"]["Curar"],(747,668))
        ventana.blit(imagenes_play["Botones_combate"]["Huir"],(1118,668))

        fuente=pygame.font.Font(None,40)
        if vida_zombie==0:
            texto=fuente.render("ZOMBIE DERROTADO",True,(255,255,255))
            ventana.blit(texto,(550,350))
        elif vida_fran==0:
            texto=fuente.render("FRAN HA PERDIDO",True,(255,255,255))
            ventana.blit(texto,(550,350))
    return ventana,jugando

def combate(accion):
    global vida_fran, vida_zombie, defendiendo

    if vida_fran<=0 or vida_zombie<=0:
        return

    if accion=="Luchar":
        if vida_zombie==33:
            vida_zombie=20
        elif vida_zombie==20:
            vida_zombie=5
        elif vida_zombie==5:
            vida_zombie=0
    elif accion=="Defensa":
        defendiendo=True
    elif accion=="Curar":
        if vida_fran==52:
            vida_fran=67
        elif vida_fran==37:
            vida_fran=52
        elif vida_fran==22:
            vida_fran=37
        elif vida_fran==7:
            vida_fran=22
        return
    if vida_zombie>0:
        if defendiendo:
            defendiendo=False
        else:
            vida_fran-=15
            if vida_fran<0:
                vida_fran=0

def combate_PM(accion, enemigo):
    global vida_pm1, vida_pm2, vida_fran_pm1, vida_fran_pm2, defendiendo_PM, golpes_PM

    if enemigo=="PM1":
        vida_enemigo=vida_pm1
        vida_fran_actual=vida_fran_pm1
        daño_enemigo=15
        vida_maxima=100
    else:
        vida_enemigo=vida_pm2
        vida_fran_actual=vida_fran_pm2
        daño_enemigo=20
        vida_maxima=150

    if vida_enemigo<=0 or vida_fran_actual<=0:
        return

    if accion=="Luchar":
        daños=[10,20]
        daño=daños[golpes_PM%2]
        golpes_PM+=1
        vida_enemigo-=daño
        if vida_enemigo<0:
            vida_enemigo=0
    elif accion=="Defensa":
        defendiendo_PM=True
    elif accion=="Curar":
        vida_fran_actual+=15
        if vida_fran_actual>100:
            vida_fran_actual=100
    elif accion=="Huir":
        return

    if vida_enemigo>0:
        if defendiendo_PM:
            defendiendo_PM=False
        else:
            vida_fran_actual-=daño_enemigo
            if vida_fran_actual<0:
                vida_fran_actual=0

    if enemigo=="PM1":
        vida_pm1=vida_enemigo
        vida_fran_pm1=vida_fran_actual
    else:
        vida_pm2=vida_enemigo
        vida_fran_pm2=vida_fran_actual

def dibujar_barra_PM(barras, vida, posicion, tamaño=(300,58)):
    # Si la vida no coincide exactamente con un fotograma disponible, usar el más cercano.
    vida_mostrada=min(barras.keys(), key=lambda valor: abs(valor-vida))
    imagen=pygame.transform.smoothscale(barras[vida_mostrada],tamaño)
    ventana.blit(imagen,posicion)

def eventos(jugando, pantalla_actual, rectangulos_click, rectangulos_click_puertas):
    global vida_fran, vida_zombie, defendiendo, tiempo_final, tiempo_final_PM, vida_pm1, vida_pm2, vida_fran_pm1, vida_fran_pm2, defendiendo_PM, golpes_PM
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:#si da a la X se cierrra
            jugando=False
        if evento.type==pygame.MOUSEBUTTONDOWN and pantalla_actual=="carga":
            posicion=pygame.mouse.get_pos()
            if rectangulos_click["clickeable_AL"]["Rb_EM"].collidepoint(posicion):
                pantalla_actual="principal"
        if evento.type==pygame.MOUSEBUTTONDOWN and pantalla_actual=="principal":#¿Se ha hecho click?
            posicion=pygame.mouse.get_pos()#Donde se ha hecho click?
            if rectangulos_click["clickeable_AL"]["Rb_EM"].collidepoint(posicion):#Click dentro de la zona 
                pantalla_actual="principal"
            elif rectangulos_click["clickeable_AL"]["Rb_NP"].collidepoint(posicion):
                pantalla_actual="Comienzo partida"
            elif rectangulos_click["clickeable_AL"]["Rb_C"].collidepoint(posicion):
                pantalla_actual="Controles"
            elif rectangulos_click["clickeable_AL"]["Rb_T"].collidepoint(posicion):
                pantalla_actual="Tutorial"
            elif rectangulos_click["clickeable_AL"]["Rb_Cr"].collidepoint(posicion):
                pantalla_actual="Creditos"
            elif rectangulos_click["clickeable_AL"]["Rb_S"].collidepoint(posicion):
                pantalla_actual="Salir"
        if evento.type==pygame.MOUSEBUTTONDOWN:
            posicion=pygame.mouse.get_pos()
            if pantalla_actual=="Controles":
                if rectangulos_click["clickeable_AL"]["RB_volver"].collidepoint(posicion):
                    pantalla_actual="principal"
            elif pantalla_actual=="Tutorial":
                if rectangulos_click["clickeable_AL"]["RB_volver"].collidepoint(posicion):
                    pantalla_actual="principal"
            elif pantalla_actual=="Creditos":
                if rectangulos_click["clickeable_AL"]["RB_volver"].collidepoint(posicion):
                    pantalla_actual="principal"
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_RETURN and pantalla_actual=="carga":#K_RETURN es enter
                pantalla_actual="principal"
            elif evento.key==pygame.K_RETURN and pantalla_actual=="Comienzo partida":
                pantalla_actual="plore1"
            elif evento.key==pygame.K_RETURN and pantalla_actual=="plore1":
                pantalla_actual="plore2"
            elif evento.key==pygame.K_RETURN and pantalla_actual=="plore2":
                pantalla_actual="plore3"
            elif evento.key==pygame.K_RETURN and pantalla_actual=="plore3":
                pantalla_actual="plore4"
            elif evento.key==pygame.K_RETURN and pantalla_actual=="plore4":
                pantalla_actual="plore5"
            elif evento.key==pygame.K_RETURN and pantalla_actual=="plore5":
                pantalla_actual="plore6"
            elif evento.key==pygame.K_RETURN and pantalla_actual=="plore6":
                pantalla_actual="plore7"    
            elif evento.key==pygame.K_RETURN and pantalla_actual=="plore7":
                pantalla_actual="JP_1"
#----------------------------------------------------------------------------------------------
        if evento.type==pygame.MOUSEBUTTONDOWN and rectangulos_click_puertas is not None:
            posicion=pygame.mouse.get_pos()
            if pantalla_actual=="JP_1":
                if rectangulos_click_puertas["clickeable_puertas"]["Rb_JP1"].collidepoint(posicion):
                    pantalla_actual="JP_2"
            elif pantalla_actual=="JP_2":
                if rectangulos_click_puertas["clickeable_puertas"]["Rb_JP2"].collidepoint(posicion):
                    pantalla_actual="JP_3"
            elif pantalla_actual=="JP_3":
                if rectangulos_click_puertas["clickeable_puertas"]["Rb_JP3"].collidepoint(posicion):
                    pantalla_actual="JP_4"
            elif pantalla_actual=="JP_4":
                if rectangulos_click_puertas["clickeable_puertas"]["Rb_JP4"].collidepoint(posicion):
                    pantalla_actual="JP_5"
                elif rectangulos_click_puertas["clickeable_coche"]["rectC1"].collidepoint(posicion):
                    pantalla_actual="Coche1"
            elif pantalla_actual=="Coche1":
                if rectangulos_click_puertas["clickeable_coche"]["rectC1d"].collidepoint(posicion):
                    pantalla_actual="Coche2"
                elif rectangulos_click_puertas["clickeable_coche"]["rectC1i"].collidepoint(posicion):
                    pantalla_actual="Coche1i"
            elif pantalla_actual=="Coche2":
                if rectangulos_click_puertas["clickeable_puertas"]["Rb_Coche2"].collidepoint(posicion):
                    pantalla_actual="JP_6"
            elif pantalla_actual=="JP_6":
                # Clic sobre la puerta que ya forma parte del fondo JP6.
                if rectangulos_click_puertas["clickeable_puertas"]["Rb_JP6"].collidepoint(posicion):
                    pantalla_actual="JP_7"
            elif pantalla_actual=="JP_7":
                if rectangulos_click_puertas["clickeable_puertas"]["Rb_JP7"].collidepoint(posicion):
                    pantalla_actual="PM1_lucha"
                    vida_pm1=100
                    vida_fran_pm1=100
                    defendiendo_PM=False
                    golpes_PM=0
                    tiempo_final_PM=None
            elif pantalla_actual=="JP_5":
                if rectangulos_click_puertas["clickeable_zombie"]["Z1"].collidepoint(posicion):
                    pantalla_actual="Z1_lucha"
                    vida_fran=67
                    vida_zombie=33
                    defendiendo=False
                    tiempo_final=None
            elif pantalla_actual=="Z1_lucha" and vida_fran>0 and vida_zombie>0:
                if rectangulos_click_puertas["clickeable_combate"]["Luchar"].collidepoint(posicion):
                    combate("Luchar")
                elif rectangulos_click_puertas["clickeable_combate"]["Defensa"].collidepoint(posicion):
                    combate("Defensa")
                elif rectangulos_click_puertas["clickeable_combate"]["Curar"].collidepoint(posicion):
                    combate("Curar")
                elif rectangulos_click_puertas["clickeable_combate"]["Huir"].collidepoint(posicion):
                    pantalla_actual="JP_4"
            elif pantalla_actual=="PM1_lucha" and vida_pm1>0 and vida_fran_pm1>0:
                rects_PM1=rectangulos_click_puertas["clickeable_combate_PM1"]
                if rects_PM1["Luchar"].collidepoint(posicion):
                    combate_PM("Luchar","PM1")
                elif rects_PM1["Defensa"].collidepoint(posicion):
                    combate_PM("Defensa","PM1")
                elif rects_PM1["Curar"].collidepoint(posicion):
                    combate_PM("Curar","PM1")
                elif rects_PM1["Huir"].collidepoint(posicion):
                    pantalla_actual="JP_6"
            elif pantalla_actual=="PM2_lucha" and vida_pm2>0 and vida_fran_pm2>0:
                if rectangulos_click_puertas["clickeable_combate_PM"]["Luchar"].collidepoint(posicion):
                    combate_PM("Luchar","PM2")
                elif rectangulos_click_puertas["clickeable_combate_PM"]["Defensa"].collidepoint(posicion):
                    combate_PM("Defensa","PM2")
                elif rectangulos_click_puertas["clickeable_combate_PM"]["Curar"].collidepoint(posicion):
                    combate_PM("Curar","PM2")
                elif rectangulos_click_puertas["clickeable_combate_PM"]["Huir"].collidepoint(posicion):
                    pantalla_actual="JP_7"
                 
    return jugando, pantalla_actual

def movimiento_jugador(x,y,velocidad_y,saltando):
    teclas=pygame.key.get_pressed()

    if pantalla_actual=="JP_1":
        suelo=550
    elif pantalla_actual=="JP_2":
        suelo=600
    elif pantalla_actual=="JP_3" or pantalla_actual=="JP_4":
        suelo=620
    elif pantalla_actual=="JP_5":
        suelo=590
    elif pantalla_actual=="Coche2":
        suelo=620
    elif pantalla_actual=="JP_6":
        suelo=590
    elif pantalla_actual=="JP_7":
        suelo=675
    if teclas[pygame.K_SPACE] and not saltando:
        velocidad_y=FUERZA_SALTO
        saltando=True

    y_anterior=y
    velocidad_y+=GRAVEDAD
    y+=velocidad_y

    movimiento_x=0
    if teclas[pygame.K_d]:
        movimiento_x=VELOCIDAD
    if teclas[pygame.K_a]:
        movimiento_x=-VELOCIDAD

    nuevo_x=x+movimiento_x
    nuevo_rect=pygame.Rect(nuevo_x,y,ANCHO_JUGADOR,ALTO_JUGADOR)

    obstaculos_habitacion=[]
    if pantalla_actual=="JP_1":
        obstaculo_futbolin_JP1=pygame.Rect(580,415,310,110)
        obstaculos_habitacion.append(obstaculo_futbolin_JP1)

    elif pantalla_actual=="JP_2":
        obstaculo_mesa_JP2=pygame.Rect(410,442,620,82)
        obstaculos_habitacion.append(obstaculo_mesa_JP2)

    # Colision lateral con los obstaculos
    for obstaculo in obstaculos_habitacion:
        if nuevo_rect.colliderect(obstaculo):
            nuevo_rect.x=x
            break

    x=nuevo_rect.x
    x=max(0,min(x,1500-ANCHO_JUGADOR))

    # Aterrizar encima de los obstaculos
    jugador_abajo=y+ALTO_JUGADOR
    jugador_abajo_anterior=y_anterior+ALTO_JUGADOR

    if velocidad_y>=0:
        for obstaculo in obstaculos_habitacion:
            toca_obstaculo=(x+ANCHO_JUGADOR>obstaculo.left and x<obstaculo.right)
            cae_encima=(jugador_abajo_anterior<=obstaculo.top and jugador_abajo>=obstaculo.top)

            if toca_obstaculo and cae_encima:
                y=obstaculo.top-ALTO_JUGADOR
                velocidad_y=0
                saltando=False
                break

    # Suelo
    if y+ALTO_JUGADOR>=suelo:
        y=suelo-ALTO_JUGADOR
        velocidad_y=0
        saltando=False

    return x,y,velocidad_y,saltando

def animar_jugador(teclas,parado,derecha1,derecha2,izquierda1,izquierda2,salto,fotograma,tiempo,saltando):
    if pygame.time.get_ticks()-tiempo>=100:
        fotograma+=1
        tiempo=pygame.time.get_ticks()

    if saltando:
        imagen=salto
    elif teclas[pygame.K_d]:
        if fotograma%2==0:
            imagen=derecha1
        else:
            imagen=derecha2
    elif teclas[pygame.K_a]:
        if fotograma%2==0:
            imagen=izquierda1
        else:
            imagen=izquierda2
    else:
        imagen=parado

    return imagen,fotograma,tiempo

pygame.init()
ventana=pygame.display.set_mode((1500, 750))#ancho--alto
boton_pulsado=None
tienpo_pulsación=0
jugando=True
pantalla_actual="carga"#Estamos en la pantalla de carga
pantalla_anterior="carga"

imagenes_Mp=imagen_Mp()
rectangulos_click=rect_boton(imagenes_Mp)

imagenes_lore=None
imagenes_play=None
rectangulos_click_puertas=None

#Constantes movimiento
VELOCIDAD=2
FUERZA_SALTO=-13
GRAVEDAD=0.3
ANCHO_JUGADOR=155
ALTO_JUGADOR=270
SUELO=690

# Vida inicial de los personajes
vida_fran=67
vida_zombie=33
defendiendo=False
tiempo_final=None
vida_pm1=100
vida_pm2=150
vida_fran_pm1=100
vida_fran_pm2=100
defendiendo_PM=False
golpes_PM=0
tiempo_final_PM=None

x=200
y=650-ALTO_JUGADOR
velocidad_y=0
saltando=False
fotograma=0
tiempo=pygame.time.get_ticks()

click_MCarga, click_Mprincipal=musica()
reloj=pygame.time.Clock()

while jugando:
    jugando, pantalla_actual=eventos(jugando, pantalla_actual, rectangulos_click, rectangulos_click_puertas)
    if pantalla_actual!=pantalla_anterior:
        if pantalla_actual=="JP_2":
            x=70
        elif pantalla_actual=="JP_3":
            x=70
        elif pantalla_actual=="JP_4":
            x=70
        elif pantalla_actual=="JP_5":
            x=1200
        elif pantalla_actual=="Coche2":
            x=1200
            y=620-ALTO_JUGADOR
            velocidad_y=0
            saltando=False
        elif pantalla_actual=="JP_6":
            x=1200
            y=590-ALTO_JUGADOR
            velocidad_y=0
            saltando=False
        elif pantalla_actual=="JP_7":
            x=70
            y=675-ALTO_JUGADOR
            velocidad_y=0
            saltando=False
    if pantalla_actual!=pantalla_anterior:
        if pantalla_actual=="Comienzo partida":#Si entramos a lore
            imagenes_Mp=None
            rectangulos_click=None
            imagenes_lore=imagen_lore()
            click_MCarga.play()
        elif pantalla_actual=="principal":#Si entramos a menú
            imagenes_lore=None
            imagenes_Mp=imagen_Mp()
            rectangulos_click=rect_boton(imagenes_Mp)
            click_Mprincipal.play()
        elif pantalla_actual=="JP_1":
            imagenes_Mp=None
            imagenes_lore=None
            rectangulos_click=None
            imagenes_play=imagen_play()
            rectangulos_click_puertas=rect_puertas(imagenes_play)
            parado, derecha1, derecha2, izquierda1, izquierda2, salto= cargar_jugador()
        pantalla_anterior=pantalla_actual
    # 3.Dibujar_las_cosas
    # aquí.dibujaremos_imágenes_personajes_fondo...
    ventana, jugando=dibujar_pantalla(pantalla_actual, imagenes_Mp, jugando, rectangulos_click, imagenes_lore)
    ventana, jugando=dib_pantalla_juego(pantalla_actual, imagenes_play)
    if pantalla_actual in ("JP_1", "JP_2", "JP_3", "JP_4", "JP_5", "Coche2", "JP_6", "JP_7"):
        teclas=pygame.key.get_pressed()
        x, y, velocidad_y, saltando=movimiento_jugador(x, y, velocidad_y, saltando)
        imagen, fotograma, tiempo=animar_jugador(teclas, parado, derecha1, derecha2, izquierda1, izquierda2, salto, fotograma, tiempo, saltando)       
        ventana.blit(imagen,(x,y))
    #música
    if pantalla_actual!=pantalla_anterior:
        if pantalla_actual=="principal":
            click_MCarga.stop()
            click_Mprincipal.play()
        elif pantalla_actual=="carga":
            click_Mprincipal.stop()
            click_MCarga.play()
        elif pantalla_actual=="Comienzo partida":
            click_Mprincipal.stop()
        pantalla_anterior=pantalla_actual
    # Si Fran pierde, 
    if pantalla_actual=="Z1_lucha":
        if (vida_zombie==0 or vida_fran==0) and tiempo_final==None:
            tiempo_final=pygame.time.get_ticks()

        if tiempo_final!=None:
            if pygame.time.get_ticks()-tiempo_final>=3000:
                if vida_zombie==0:
                    pantalla_actual="JP_4"
                    tiempo_final=None
                elif vida_fran==0:
                    jugando=False
        if pantalla_actual in ("PM1_lucha","PM2_lucha"):
            if tiempo_final_PM==None and ((pantalla_actual=="PM1_lucha" and (vida_pm1==0 or vida_fran_pm1==0)) or (pantalla_actual=="PM2_lucha" and (vida_pm2==0 or vida_fran_pm2==0))):
                tiempo_final_PM=pygame.time.get_ticks()
            if tiempo_final_PM!=None and pygame.time.get_ticks()-tiempo_final_PM>=5000:
                if pantalla_actual=="PM1_lucha" and vida_pm1==0:
                    pantalla_actual="PM2_lucha"
                    vida_pm2=150
                    vida_fran_pm2=vida_fran_pm1
                    defendiendo_PM=False
                    golpes_PM=0
                    tiempo_final_PM=None
                elif (pantalla_actual=="PM1_lucha" and vida_fran_pm1==0) or (pantalla_actual=="PM2_lucha" and vida_fran_pm2==0):
                    jugando=False
                elif pantalla_actual=="PM2_lucha" and vida_pm2==0:
                    pantalla_actual="JP_7"
                    tiempo_final_PM=None
    # 4. Actualizar la pantalla
    pygame.display.update()
pygame.quit()#final del juego