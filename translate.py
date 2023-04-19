from mtranslate import translate

def main():
    # Inicjalizacja obiektu Translator
    translator = translate

    while True:
        # Wejściowe słowo do tłumaczenia
        slowo = input("Podaj słowo lub zdanie do przetłumaczenia (lub wpisz samo 'q' aby wyjść z programu): ")
        if slowo.lower() == 'q':
            # Wyjście z pętli przy wprowadzeniu 'q'
            print("Wyszedłeś z programu.")
            break
        else:
            try:
                # Tłumaczenie na język angielski
                tlumaczenie_en = translator(slowo, "en")
                print("Tłumaczenie na angielski: ", tlumaczenie_en)

                # Tłumaczenie na język niemiecki
                tlumaczenie_de = translator(slowo, "de")
                print("Tłumaczenie na niemiecki: ", tlumaczenie_de)

            except Exception as e:
                print(f"Wystąpił nieoczekiwany błąd: {str(e)}")

if __name__ == '__main__':
    main()
