import random


class Sputnuk():
    def __init__(self, name: str, mass, size) -> None:
        assert name.isascii(), "Назва спутник має містити символи ASTE"
        assert mass >= 0 and size >= 0, "Маса та Розмір спутник не може бути меншою за 0!"
        # Так працює але так не роблять
        # if not size > 0:
        #    raise AssertionError("Розмір СПУТНИКА не може бути меншою за 0!")

        self.name = name
        self.mass = mass
        self.size = size

    @property
    def info(self):
        return f"сПУТНИК {self.name} має масу {self.mass} кг та розмір {self.size} м."

    def convert_to_pounds(self):
        return self.mass * 2.20462262

    def convert_to_feet(self):
        return self.size * 3.2808399

    @property
    def info_in_en(self):
        return f"Спутник {self.name} має масу {self.convert_to_pounds()} фунтів та розмір {self.convert_to_feet()} футів."

    def crash_on_start(self):
        c = random.random()
        print(f"Згенерована імовірність = {c}")
        if c >= 0.9:
            print("Невданий запуск Спутник")
            return False
        else:
            print("Спутник успішно полетіла")
            return True


# def test_obj_asterics():
#    r = Sputnuk("Asterics 6", 549054, 70)
#    print(r.info)
#    print(r.info_in_en)
#    r2 = Sputnuk("Asterics V", 546700, 58.3)
#    print(r2.info)
#    assert r.name in r.info, "інфо про спутник не містить її назви"
#    return True
#
# if test_obj_asterics():
#    print("Перевірки виконано")

r = Sputnuk("Asterics 6", 549054, 70)
r.crash_on_start()
