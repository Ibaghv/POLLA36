import pygame
import time

pygame.init()

# --------------------------------------------------
# CONFIGURACIÓN DE LA VENTANA Y DEL JUEGO
# --------------------------------------------------

ANCHO = 1500
ALTO = 750

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Project_NorthZ")

reloj = pygame.time.Clock()

# Variables del jugador y del mapa (prototipo inicial)
jugador_x = 100
jugador_y = 600
velocidad = 5
velocidad_salto = 0
gravedad = 0.6
suelo_y = 650

ancho_mundo = 4500
camara_x = 0


# --------------------------------------------------
# CARGA DE IMÁGENES DEL MENÚ
# --------------------------------------------------

def imagen_Mp():
    Menu_carga = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Menu_carga_prueba.jpeg"
    )
    Menu_Principal = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Menú_principal.png"
    )
    Enpezar_Menu = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Enpezar_Menu_carga.png"
    )
    Nueva_partida = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Nueva_partida_MP.png"
    )
    Controles = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Controles_MP.png"
    )
    Tutorial = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Turotial_MP.png"
    )
    Creditos = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Créditos_MP.png"
    )
    Salir = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Salir_MP.png"
    )

    ControlesA = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Controles negro.png"
    )
    TutorialA = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Tutorial negro.png"
    )
    CreditosA = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Créditos negro.png"
    )
    SalirA = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/SalirA.jpg"
    )

    Nueva_partida_rojo = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Nueva_partida_MP_rojo.png"
    )
    Controles_rojo = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Controles_MP_rojo.png"
    )
    Tutorial_rojo = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Tutorial_rojo.png"
    )
    Creditos_rojo = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Créditos_MP_rojo.png"
    )
    Salir_rojo = pygame.image.load(
        "Project_NorthZ/Imágenes/Menu Carga/Salir_MP_rojo.png"
    )

    Menu_carga = pygame.transform.scale(Menu_carga, (ANCHO, ALTO))
    Menu_Principal = pygame.transform.scale(Menu_Principal, (ANCHO, ALTO))
    Enpezar_Menu = pygame.transform.scale(Enpezar_Menu, (723, 110))

    Nueva_partida = pygame.transform.scale(Nueva_partida, (258, 60))
    Controles = pygame.transform.scale(Controles, (180, 50))
    Tutorial = pygame.transform.scale(Tutorial, (190, 55))
    Creditos = pygame.transform.scale(Creditos, (165, 50))
