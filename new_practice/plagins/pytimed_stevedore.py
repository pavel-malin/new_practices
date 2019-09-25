from stevedore.extension import ExtensionManager
import time


def main():
    seconds_passed = 0
    extensions = ExtensionManager('pytimed', invoke_on_load=True)
    while True:
        for extension in extensions:
            try:
                seconds, callable = extension.obj
            except:
                #  Пропустить ошибку.
                pass
            else:
                if seconds_passed % seconds == 0:
                    callable()

        time.sleep(1)
        seconds_passed += 1
