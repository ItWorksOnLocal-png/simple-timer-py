import time
import os


def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Timer ran out, press any key to exit!')
    os.system('pause >nul')


def main():
    print("===Simple Timer===\n")

    seconds = input("Enter the time in seconds: ")

    os.system('cls')

    print("===Simple Timer===\n")


    countdown(int(seconds))


if __name__ == '__main__':
    main()