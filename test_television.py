import pytest
from television import Television

def get_tv_state(tv):
    return f"Status: {tv._status}, Muted: {tv._muted}, Volume: {tv._volume}, Channel: {tv._channel}"

def test_init():
    tv = Television()
    assert not tv._status
    assert not tv._muted
    assert tv._volume == tv.MIN_VOLUME
    assert tv._channel == tv.MIN_CHANNEL

def test_power_toggle():
    tv = Television()
    tv.power()
    assert tv._status
    tv.power()
    assert not tv._status

def test_mute_behavior():
    tv = Television()
    tv.volume_up()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv._muted
    tv.mute()
    assert not tv._muted
    tv.power()
    tv.mute()
    assert not tv._muted

def test_channel_up():
    tv = Television()
    tv.channel_up()
    assert tv._channel == tv.MIN_CHANNEL
    tv.power()
    tv.channel_up()
    assert tv._channel == tv.MIN_CHANNEL + 1
    for _ in range(tv.MAX_CHANNEL):
        tv.channel_up()
    assert tv._channel == tv.MIN_CHANNEL

def test_channel_down():
    tv = Television()
    tv.channel_down()
    assert tv._channel == tv.MIN_CHANNEL
    tv.power()
    tv.channel_down()
    assert tv._channel == tv.MAX_CHANNEL


def test_volume_up():
    tv = Television()
    tv.volume_up()
    assert tv._volume == tv.MIN_VOLUME
    tv.power()
    tv.volume_up()
    assert tv._volume == tv.MIN_VOLUME + 1
    tv.mute()
    tv.volume_up()
    assert not tv._muted
    assert tv._volume == tv.MIN_VOLUME + 2
    tv.volume_up()
    tv.volume_up()
    assert tv._volume == tv.MAX_VOLUME


def test_volume_down():
    tv = Television()
    tv.volume_down()
    assert tv._volume == tv.MIN_VOLUME
    tv.power()
   
    while tv._volume < tv.MAX_VOLUME:
        tv.volume_up()
    tv.volume_down()
    assert tv._volume == tv.MAX_VOLUME - 1
    tv.mute()
    tv.volume_down()
    assert not tv._muted
    assert tv._volume == tv.MAX_VOLUME - 2
    tv.volume_down()
    tv.volume_down()
    assert tv._volume == tv.MIN_VOLUME
