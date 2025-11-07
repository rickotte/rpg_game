import time
import sys
import msvcrt


def attack_timing_bar():
    bar_length = 20
    print("\nTiming Bar (Press Enter):")
    pressed = False
    hit_zone = None

    for i in range(bar_length, 0, -1):
        color = "\033[97m"  # white
        if i <= 7:
            color = "\033[91m"  # red

        sys.stdout.write(f"\r{color}{'█' * i:<{bar_length}}\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)

        # Check if Space is pressed in real time
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key in [b"\r"]:
                pressed = True
                hit_zone = "red" if i <= 7 else "white"
                break

    sys.stdout.write("\033[0m\n")  # Reset color
    if not pressed:
        print("You didn’t strike at all. Stop sleeping!")
        return 0.0
    elif hit_zone == "red":
        print("Perfect")
        return 2.0
    else:
        print("Too Early")
        return 1.0


def defend_timing_bar():
    bar_length = 20
    print("\nDefend Timing (Press Space):")
    pressed = False
    result = "fail"
    time.sleep(1)

    for i in range(bar_length, 0, -1):
        if i > 7:
            color = "\033[97m"  # white
        else:
            color = "\033[91m"  # red

        sys.stdout.write(f"\r{color}{'█' * i:<{bar_length}}\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)

        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key in [b"\r"]:
                pressed = True
                if i <= 7:
                    result = "parry"
                else:
                    result = "defend"
                break

    sys.stdout.write("\033[0m\n")

    if not pressed:
        print("Failed to defend — took full damage!")
        return "fail"
    elif result == "parry":
        print("Perfect Parry! Counterattack triggered!")
    else:
        print("Successful Defend! No damage taken.")
    return result
