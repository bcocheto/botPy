# -*- coding: utf-8 -*-
from _datetime import datetime


class Controlador:

    def hora_atual():
        now = datetime.now()
        hora = 'são' + str(now.hour) + 'horas e' + str(now.minute) + 'minutos'
        return hora

    def data_atual():
        now = datetime.now()
        dia = 'hoje é dia '
        return dia
