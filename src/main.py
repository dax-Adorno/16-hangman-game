import random


PALABRAS = [
    "python",
    "desarrollo",
    "programacion",
    "algoritmo",
    "variable",
    "funcion",
    "backend",
    "frontend",
    "servidor",
    "database"
]


def elegir_palabra() -> str:
    return random.choice(PALABRAS)


def mostrar_estado(palabra: str, letras_adivinadas: set[str]) -> str:
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)


def palabra_completada(palabra: str, letras_adivinadas: set[str]) -> bool:
    return all(letra in letras_adivinadas for letra in palabra)


def solicitar_letra(letras_usadas: set[str]) -> str:
    while True:
        letra = input("\nIngresa una letra: ").strip().lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Debes ingresar una sola letra válida.")
            continue

        if letra in letras_usadas:
            print("Ya usaste esa letra. Intenta con otra.")
            continue

        return letra


def jugar() -> None:
    palabra = elegir_palabra()
    letras_adivinadas: set[str] = set()
    letras_usadas: set[str] = set()
    intentos = 6

    print("\nBienvenido al juego del ahorcado.")

    while intentos > 0:
        print("\n--- ESTADO ACTUAL ---")
        print(mostrar_estado(palabra, letras_adivinadas))
        print(f"Letras usadas: {', '.join(sorted(letras_usadas)) if letras_usadas else 'Ninguna'}")
        print(f"Intentos restantes: {intentos}")

        letra = solicitar_letra(letras_usadas)
        letras_usadas.add(letra)

        if letra in palabra:
            letras_adivinadas.add(letra)
            print("Correcto. La letra está en la palabra.")
        else:
            intentos -= 1
            print("Incorrecto. La letra no está en la palabra.")

        if palabra_completada(palabra, letras_adivinadas):
            print("\nFelicitaciones. Adivinaste la palabra.")
            print(f"La palabra era: {palabra}")
            return

    print("\nPerdiste.")
    print(f"La palabra era: {palabra}")


def jugar_otra_vez() -> bool:
    while True:
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if respuesta in ("s", "n"):
            return respuesta == "s"
        print("Entrada inválida. Escribe 's' para sí o 'n' para no.")


def main() -> None:
    print("=" * 42)
    print("         JUEGO DEL AHORCADO")
    print("=" * 42)

    while True:
        jugar()
        if not jugar_otra_vez():
            break

    print("\nGracias por jugar.")
    print("Portfolio: https://dax-adorno.github.io/")


if __name__ == "__main__":
    main()