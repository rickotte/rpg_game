import time, sys


class TimingBar:
    def __init__(self, duration=3, length=30):
        self.duration = duration
        self.length = length

    def get_color(self, ratio):
        if ratio > 0.6:
            return "\033[97m"  # White
        elif ratio > 0.3:
            return "\033[93m"  # Yellow
        else:
            return "\033[91m"  # Red

    def run(self):
        start_time = time.time()
        while True:
            elapsed = time.time() - start_time
            ratio = max(0, 1 - elapsed / self.duration)
            filled = int(self.length * ratio)
            color = self.get_color(ratio)
            bar = "█" * filled + "-" * (self.length - filled)
            sys.stdout.write(
                f"\r{color}[{bar}]\033[0m {self.duration - elapsed:4.1f}s "
            )
            sys.stdout.flush()
            if elapsed >= self.duration:
                break
            time.sleep(0.05)
        print("\n")
