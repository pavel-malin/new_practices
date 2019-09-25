import warnings


class Car(object):

    def turn_left(self):
        """Поворот машины налево.

        ... deprecated:: 1.1
        Используйте :func:`turn` вместо этого, с аргументом left (влево)
        """
        warnings.warn("turn_left больше не используется; испольлуйте \
                       вместо этого функцию turn с аргументом left \
                       (влево)", DeprecationWarning)
        self.turn(direction='left')

    def turn(self, direction):
        """Поворачивает машину в заданном направлении.

        :param direction: Параметр, определяющий направление.
        :type direction: str (тип параметра)
        """
        # Здесь код функции
        pass
