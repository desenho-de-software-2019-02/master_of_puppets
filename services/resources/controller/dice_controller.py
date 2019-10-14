import random


# if desespero then strategy
class DiceController:
    def roll(self, dice_pattern):
        """
        Rolls a virtual dice n times and returns it's value. Recieves a dice
        pattern like '2d8'
        """
        times, faces = self.__split(dice_pattern)
        total = 0
        throws = []

        for n in range(times):
            result = random.randint(1, faces)
            total += result
            throws.append(result)

        return {'result': total, 'throws': throws}

    def __split(self, string):
        """
        Recieves a string like '3d4' and transforms into two values:
        a multiplier (ex.: 3) and a maximum number (ex.: 4)
        """
        split = string.split('d')
        return int(split[0]), int(split[1])
