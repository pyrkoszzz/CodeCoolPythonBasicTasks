import datetime
import time


class AlarmClock:
    def __init__(self):
        self.alarm_time = None

    def set_alarm(self, hour, minute) -> None:
        self.alarm_time = datetime.time(hour, minute)

    def run_alarm_clock(self) -> None:
        print("Set the alarm time: ")

        while True:
            try:
                hour = int(input("Enter the hour (0-23): "))
                minute = int(input("Enter the minute (0-59): "))

                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    self.set_alarm(hour, minute)
                    break
                else:
                    print("Invalid input. Enter a valid hour (0-23) and minute (0-59).")
            except ValueError:
                print("Invalid input. Enter valid integers for hour and minute.")

        print(f"Alarm set for {hour:02d}:{minute:02d}.")

        while True:
            current_time = datetime.datetime.now().time()

            if current_time >= self.alarm_time:
                print("Alarm triggered!")
                break

            time.sleep(1)


if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run_alarm_clock()
