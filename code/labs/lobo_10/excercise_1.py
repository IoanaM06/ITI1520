# Student name: Ioana Marinescu
# Student number: 300242429



class Temps:
    def __init__(self, hh=12, mm=0, s=0):
        self.setTemps(hh, mm, s)

    # ajoute dans la classe Temps
    def setTemps(self, hh=12, mm=0, s=0):
        '''(Temps)-> None'''

        # seconds
        if s >= 60:
            mm += s // 60
            s %= 60

        elif s < 0:
            mm += s // 60 - 1
            s += 60 + s % 60

        # minutes
        if mm >= 60:
            hh += mm // 60
            mm %= 60
        elif mm < 0:
            hh += mm // 60 - 1
            mm = 60 + mm % 60

        # heures
        if hh >= 24:
            hh %= 24
        elif hh < 0:
            hh = 24 + hh % 24

        self.heure = hh
        self.minute = mm
        self.seconde = s


    def estAvant(self, t2):
        return (
            (self.heure, self.minute, self.seconde) < (t2.heure, t2.minute, t2.seconde)
        )

    def duree(self, t2):
        # convertir en seconds
        t1_total_secs = self.heure * 3600 + self.minute * 60 + self.seconde
        t2_total_secs = t2.heure * 3600 + t2.minute * 60 + t2.seconde

        # difference
        diff_secs = abs(t1_total_secs - t2_total_secs)

        # convertir en original
        hh = diff_secs // 3600
        diff_secs %= 3600
        mm = diff_secs // 60
        ss = diff_secs % 60

        return Temps(hh, mm, ss)

    def __str__(self):
        return f"{self.heure}:{self.minute}:{self.seconde}"

t1 = Temps(12,4,0)
t2 = Temps(10,2,1)

print(t1.estAvant(t2)) # False
print(t2.estAvant(t1)) # True

t2.setTemps(12,45,2)
print(t1.estAvant(t2)) # True
print(t1.duree(t2)) # 0:41:2