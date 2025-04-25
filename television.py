class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        self._status = not self._status

    def mute(self) -> None:
        if self._status:
            self._muted = not self._muted

    def channel_up(self) -> None:
        if self._status:
            self._channel += 1
            if self._channel > self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        if self._status:
            self._channel -= 1
            if self._channel < self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        if self._status:
            self._muted = False
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        if self._status:
            self._muted = False
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:

        display_volume = 0 if self._muted else self._volume

        return f"Power = {self._status}, Channel = {self._channel}, Volume = {display_volume}"