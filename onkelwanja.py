import random

subjects = ["Ein grüner Dinosaurier", "Ein frecher Pinguin", "Ein furchtloser Kosmonaut", "Ein einsamer Wanderer", "Ein alter Mann", "Eine abenteurlustige Frau", "Ein berühmter Ritter"]
verbs = ["tanzt", "fliegt", "lacht über","trinkt", "läuft", "schläft", "hüpft ", "kämpft"]
objects = ["eine Banane", "einen Regenbogen", "eine Tasse Kaffee", "ein Regenschauer", "ein Picknick", "mit einem altem Schwert"]
places = ["in einer fernen Galaxie", "im tiefen Ozean", "auf einem fernen Planeten""auf dem Mond", "im Dschungel", "in der Wüste", "auf dem Mars", "in den Ruinen einer Stadt ", "am Wegesrand", "ein Tunier in der Unterstadt"]
actions = ["entdeckte", "erkundete", "rettete", "verwandelte","starb","zauberte", "besiegte"]
highlights = ["einen außerirdischen Freund", "einen geheimen Schatz", "das Universum", "die wahre Bedeutung des Lebens"]
endings = ["und lebte glücklich bis ans Ende seiner Tage.", "und kehrte mit vielen Abenteuern nach Hause zurück.", "und wurde zur Legende."]

def Rasskazchik_Skazok(num_sentences):
    introduction = random.choice(places)
    main_character = random.choice(subjects)
    story = f"{introduction}, dort lebte {main_character}. "

    for _ in range(num_sentences - 2):  # -2 to account for intro and ending
        action = random.choice(actions)
        object = random.choice(objects)
        sentence = f"{main_character} {action} {object}. "
        story += sentence

    climax = random.choice(highlights)
    story += f"Dann {main_character} traf {climax}. "
    
    ending = random.choice(endings)
    story += ending

    return story

def main():
    print("Willkommen bei Onkel Wanja dem Geschichtenerzähler!")
    while True:
        num_sentences = int(input("Wie viel Sätze soll die Geschichte haben? "))
        dyadya_wanja = Rasskazchik_Skazok(num_sentences)
        print("Hier ist deine einzigartige Geschichte:")
        print(dyadya_wanja)
        
        another_story = input("Möchtest du noch eine weitere Geschichte hören? (Ja/Nein): ")
        if another_story.lower() != "ja":
            print("Vielen Dank das du Onkel Wanja zughört hast, до свидания!")
            break

if __name__ == "__main__":
    main()
