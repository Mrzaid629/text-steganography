import random


sentences = [
    "The students attended their classes in the morning.",
    "They later visited the library to complete their assignments.",
    "The weather was pleasant throughout the afternoon.",
    "Many students discussed their work with their classmates.",
    "The library remained quiet during the study hours.",
    "Everyone returned home after completing their daily activities.",
    "The students prepared notes for their upcoming examination.",
    "Some students spent time reading useful materials.",
    "The afternoon lecture ended earlier than expected.",
    "The students planned to continue their studies the next morning.",
    "The roads were relatively quiet during the evening.",
    "The college campus was peaceful after the classes ended."
]


def generate_text(number_of_sentences=8):

    selected_sentences = random.sample(
        sentences,
        number_of_sentences
    )

    paragraph = " ".join(selected_sentences)

    return paragraph


if __name__ == "__main__":

    generated_text = generate_text(8)

    print("Generated Innocuous Text:")
    print()

    print(generated_text)