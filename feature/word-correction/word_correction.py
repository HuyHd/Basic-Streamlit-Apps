import streamlit as st
from levenshtein_distance import levenshtein_distance


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word:")

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        vocabs = load_vocab(file_path="./source/vocab.txt")
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distences = dict(
            sorted(leven_distances.items(), key=lambda item: item[1])
        )
        correct_word = list(sorted_distences.keys())[0]
        st.write("Correct word:", correct_word)

        col1, col2 = st.columns(2)
        col1.write("Vocabulary:")
        col1.write(vocabs)
        col2.write("Distances:")
        col2.write(sorted_distences)


def load_vocab(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        words = sorted(set([line.strip().lower() for line in lines]))
    return words


if __name__ == "__main__":
    main()
