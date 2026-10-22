def on_button_pressed_a():
    music.play(music.string_playable("C C C C C5 C5 C5 C5 ", 500),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_leds("""
        # # . # #
        # # . # #
        . . . . .
        . . . . .
        # # # # #
        """)
    basic.show_leds("""
        # # . # #
        # # . # #
        . . . . .
        # . . . #
        . # # # .
        """)
basic.forever(on_forever)
