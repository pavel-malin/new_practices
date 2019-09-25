from debtcollector import moves


class Car(object):
    @moves.moved_method('turn', version='1.1')
    def turn_left(self):
        """Поворот машины налево."""

        return self.turn(direction='left')

    def turn(self, direction):
        """Поворачивает машину в заданном направлении.

        :param direction: The direction to turn to.
        :type direction: str
        """
        # Здесь код функции
        pass
