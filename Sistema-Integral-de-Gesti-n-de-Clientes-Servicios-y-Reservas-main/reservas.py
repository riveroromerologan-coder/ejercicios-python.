# ==========================================
# MODULO DE GESTION DE RESERVAS
# Proyecto: Software FJ
# Aporte: Gestion de reservas
# ==========================================

class ReservaInvalidaError(Exception):
    """Error personalizado para reservas incorrectas."""
    pass


class Reserva:
    """Clase encargada de gestionar las reservas."""

    def __init__(self, id_reserva, cliente, servicio, duracion_horas):

        if not id_reserva:
            raise ReservaInvalidaError("El ID de reserva es obligatorio.")

        if cliente is None or servicio is None:
            raise ReservaInvalidaError("Debe existir un cliente y un servicio.")

        if duracion_horas <= 0:
            raise ReservaInvalidaError("La duración debe ser mayor que cero.")

        self.__id_reserva = id_reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion_horas = duracion_horas
        self.__estado = "Pendiente"

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise ReservaInvalidaError("La reserva no se puede confirmar.")

        self.__estado = "Confirmada"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.__estado == "Cancelada":
            raise ReservaInvalidaError("La reserva ya está cancelada.")

        self.__estado = "Cancelada"
        return "Reserva cancelada correctamente."