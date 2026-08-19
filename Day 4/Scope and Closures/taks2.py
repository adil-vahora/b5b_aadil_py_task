def make_greeting(language):

    def greet(name):
        if language == "hindi":
            print("Namaste,", name)
        else:
            print("Hello,", name)

    return greet


english_greeting = make_greeting("english")
hindi_greeting = make_greeting("hindi")

english_greeting("Adil")
hindi_greeting("Rahim")