class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError('Температура может быть только числом!!')
        self._celsius=float(value)

    @property
    def fahrenheit(self):
        return self.celsius*9/5+32

    @fahrenheit.setter
    def fahrenheit(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError('Температура может быть только числом!!')
        self.celsius=(value-32)*5/9


if __name__=='__main__':
    t=Temperature(36.6)
    print(f"36.6°C={t.fahrenheit:.1f}°F")
    t.fahrenheit=123
    print(f"123°F={t.celsius:.1f}°C")
    try:
        t.celsius='tfugvh'
    except TypeError as e:
        print(e)