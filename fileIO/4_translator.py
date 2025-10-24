# Exercise: Translator

from translate import Translator

translator = Translator(to_lang="zh")
try:
    with open("app/translator.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)

        with open("app/translator-ja.txt", mode="w") as my_file2:
            my_file2.write(translation)

except FileNotFoundError as err:
    print("check your file path silly!!")
