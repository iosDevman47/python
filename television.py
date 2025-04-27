class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a Television instance with default settings.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle the mute status if the television is on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel by one, wrapping to MIN_CHANNEL if over MAX_CHANNEL.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the channel by one, wrapping to MAX_CHANNEL if below MIN_CHANNEL.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume by one if below MAX_VOLUME and unmute the television.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by one if above MIN_VOLUME and unmute the television.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the television's current state.
        """
        display_volume = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"