class jugador:
    def __init__(self, nickname, nombre_real, país, rol, foto):
        self.nickname = nickname
        self.nombre_real = nombre_real
        self.país = país
        self.rol = rol
        self.foto = foto
    def __str__(self):        return f"Nickname: {self.nickname}\nNombre Real: {self.nombre_real}\nPaís: {self.país}\nRol: {self.rol}\nFoto: {self.foto}"



class Equipo:
    def __init__(self, nombre, pais, ranking, jugadores=None):
        self.nombre = nombre
        self.pais = pais
        self.ranking = ranking

        if jugadores is None:
            self.jugadores = []
        else:
            self.jugadores = jugadores
