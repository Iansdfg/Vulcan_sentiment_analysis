from sentiment_functions import get_senti


if __name__ == '__main__':
    documents = [
        {
            "id": "1",
            "language": "en",
            "text": "I had the best day of my life.",
            "time": "12:34:32"
        },
        {
            "id": "2",
            "language": "en",
            "text": "This was a waste of my time. The speaker put me to sleep.",
            "time": "12:34:32"
        },
        {
            "id": "3",
            "language": "es",
            "text": "No tengo dinero ni nada que dar...",
            "time": "12:34:32"
        },
        {
            "id": "4",
            "language": "it",
            "text": "L'hotel veneziano era meraviglioso. È un bellissimo pezzo di architettura.",
            "time": "12:34:32"
        }
    ]

    res = get_senti(documents)

    for ele in res:
        print(ele)