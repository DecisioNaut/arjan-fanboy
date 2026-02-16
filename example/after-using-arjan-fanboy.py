from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class Switchable(Protocol):
    def turn_on(self) -> None: ...

    def turn_off(self) -> None: ...


class LightBulb:
    def turn_on(self) -> None:
        print("LightBulb: turned on...")

    def turn_off(self) -> None:
        print("LightBulb: turned off...")


@dataclass(slots=True)
class ElectricPowerSwitch:
    device: Switchable
    is_on: bool = False

    def press(self) -> None:
        if self.is_on:
            self.device.turn_off()
            self.is_on = False
            return
        self.device.turn_on()
        self.is_on = True


def main() -> None:
    bulb = LightBulb()
    switch = ElectricPowerSwitch(device=bulb)
    switch.press()
    switch.press()


if __name__ == "__main__":
    main()
