def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # # # # #
                . . . . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_number(Math.sqrt(4656))
    basic.show_number(Math.sqrt(563748))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_string("Hello my name is Jarvis ")
basic.show_string("How can I help you today ")

def on_forever():
    pass
basic.forever(on_forever)
