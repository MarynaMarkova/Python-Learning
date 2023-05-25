from translate import Translator

translator = Translator(to_lang="fr")
translation = translator.translate("hello, I love you")
print(translation)
