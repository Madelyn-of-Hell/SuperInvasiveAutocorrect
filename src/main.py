from random import choice
import spellchecker
from pynput import keyboard

MODE = "Auto" # UwU or Auto

class Corrector:
    spell_words_good_inator = spellchecker.SpellChecker()
    keyboard_control_inator = keyboard.Controller()
    def __init__(self):
        self.word:list[str] = [""]
    def keystroke(self, key):
        if key == keyboard.Key.esc:
            return False
        if str(key) in ["Key.space", "Key.enter", "'.'", "';'", "':'", "'/'", "','", "'!'"]:
            word = ''.join(self.word)
            if word == " ": return
            correction:str
            match MODE:
                case "Auto":
                    correction = self.spell_words_good_inator.correction(word)
                case "UwU":
                    correction = Corrector.uwuify(word)
            if correction != word:
                print(f"bad girl :( u meant {correction}")
                if str(key) != "Key.space":
                    self.keyboard_control_inator.press(keyboard.Key.backspace)
                    self.keyboard_control_inator.release(keyboard.Key.backspace)
                self.keyboard_control_inator.press(keyboard.Key.alt)
                self.keyboard_control_inator.press(keyboard.Key.backspace)
                self.keyboard_control_inator.release(keyboard.Key.alt)
                self.keyboard_control_inator.release(keyboard.Key.backspace)
                self.keyboard_control_inator.type(correction)
                self.keyboard_control_inator.press(key)
                self.keyboard_control_inator.release(key)
            else:
                print("good girlllll :3 ur such a good typer <3")
            self.word = [""]
        elif str(key) == "Key.backspace":
            if len(self.word) > 1:
                del self.word[-2]
                print(self.word)
        elif type(key) == keyboard.Key:
            pass
        else:
            del self.word[-1]
            self.word.append(str(key)[1])
            self.word.append("")
        print(''.join(self.word))

    # written according to the UwUification specifications at https://gist.github.com/uwoneko/b5d46b8a56f5642ccc302137b86fe850
    def uwuify(text:str) -> str:
        EMOJI = ["<3", ":3", "UwU", "OwO", "^^", ">w<", ">~<", ">.<", ">w<", "^w^", "(◕ᴥ◕)", "ʕ•ᴥ•ʔ", "ʕ￫ᴥ￩ʔ", "(*^ω^)", "(◕‿◕✿)", "(*^.^*)", "(つ✧ω✧)つ", "(/ =ω=)/"]
        PHRASES = ["*snuzzwes*", "*nuzzwes youw chest*", "*wicks uw neck*", "*paws*", "*puwws*", "*meows*", "*snugs cwosew*", "*pounces on u*"]
        # phase one
        text = text.replace("r", "w")
        text = text.replace("l", "w")

        # phase 2
        text = text.replace("wove", "wuv")
        text = text.replace("nice", "nyaice")
        text = text.replace("what", "wut")
        text = text.replace("you", "u")
        text = text.replace("the", "da")
        text = text.replace("hewwo", "hewo") #changed to regular hello because i felt like it
        text = text.replace("cat", "neko")
        text = text.replace("kitty", "neko")
        text = text.replace("cute", "kawaii")
        text = text.replace(" hi", " hii")

        # phase 3
        text = list(text)
        text.append("") #hacky fix to indicate an endofline character
        len_text = len(text) #subtract 1 so it starts at 0 for indexing purposes
        for i in range(len_text):
            if len_text >= (i + 3) and text[i:i+3] == ["a","w","w"] and text[i+3] in [" ", "\n", "", "."]: #added a period
                text[i]     = "u"
                text[i + 1] = "w"
                text[i + 2] = "u"

            if len_text >= (i + 8) and text[i:i+3] == ["a","w","e"] and text[i+3:i+7] == ["s","o","m","e"]:
                text[i]     = "u"
                text[i + 1] = "w"
                text[i + 2] = "u"

            if len_text >= (i + 1) and text[i] == "n" and text[i + 1] in ["a","e","i","o","u"]:
                text[i] = "ny"

            # removed the fourth complex replacement because it doesn't make any sense to me
            # phase 4

            if text[i] == ".":
                text[i] += " " # proper spacing is vital 😌
                text[i] += choice(choice([EMOJI, PHRASES]))
            if text[i] == ",":
                text[i] += choice(PHRASES)
            if text[i] == "!":
                text[i] += "!"
            if text[i] == "?":
                text[i] = choice(["!?", "?!"])
        text = "".join(text)
        return text


corrector = Corrector()
keyboard_listener = keyboard.Listener(on_press=corrector.keystroke)
keyboard_listener.start()
keyboard_listener.join()

# awesomely
