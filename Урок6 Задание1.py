from time import sleep


class TrafficLight:
    __color = ['\033[31mКрасный', '\033[33mЖелтый', '\033[32mЗеленый', '\033[33mЖелтый']

    def running(self):
        print("Светофор")
        t = 0
        while t <= 2:
            i = 0
            while i < 4:
                print(f'\033[0mЦвет светофора: {TrafficLight.__color[i]}')
                if i == 0:
                    sleep(7)
                elif i == 1:
                    sleep(2)
                elif i == 2:
                    sleep(8)
                elif i == 3:
                    sleep(2)
                i += 1
            t += 1


TrafficLight1 = TrafficLight()
TrafficLight1.running()