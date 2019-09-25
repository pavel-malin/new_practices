from stevedore.driver import DriverManager
import time


def main(name):
    seconds_passed = 0
    seconds, callable = DriverManager(
                                      'pytimed',
                                      name,
                                      invoke_on_load=True).driver
    while True:
        if seconds_passed % seconds == 0:
            callable()
        time.sleep(1)
        seconds_passed += 1


main("hello")
