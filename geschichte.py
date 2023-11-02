import random

subjects = ["Ein grüner Dinosaurier", "Ein frecher Pinguin", "Ein furchtloser Kosmonaut", "Ein einsamer Wanderer", "Ein alter Mann", "Eine abenteurlustige Frau", "Ein berühmter Ritter"]
verbs = ["tanzt", "fliegt", "lacht über","trinkt", "läuft", "schläft", "hüpft ", "kämpft"]
objects = ["eine Banane", "einen Regenbogen", "eine Tasse Kaffee", "ein Regenschauer", "ein Picknick", "mit einem altem Schwert"]
places = ["auf dem Mond", "im Dschungel", "in der Wüste", "auf dem Mars", "in den Ruinen einer Stadt ", "am Wegesrand", "ein Tunier in der Unterstadt"]

def Rasskazchik_Skazok(num_sentences):
    story = ""
    for _ in range(num_sentences):
        subject = random.choice(subjects)
        verb = random.choice(verbs)
        obj = random.choice(objects)
        place = random.choice(places)

        sentence = f"{subject} {verb} {obj} {place}."
        story += sentence + " "

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
