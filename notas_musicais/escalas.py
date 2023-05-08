NOTAS = "C C# D D# E F F# G G# A A# B".split()
ESCALAS = {"maior": (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tonica e uma tonalidade

    Args:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala

    Examples:
        >>> escala('C','maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('A','maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    Raises:
        ValueError: Caso a tonica nao seja uma nota valida
        KeyError: Caso a escala nao exista ou nao tenha sido implementada

    Returns:
        Um dicionario com as notas da escala e os graus.
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f"Essa nota nao existe, tente uma dessas {NOTAS}")
    except KeyError:
        raise KeyError(
            "Essa escala nao existe ou nao foi implementada"
            f", tente uma dessas: {list(ESCALAS.keys())}"
        )

    list_temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        list_temp.append(NOTAS[nota])

    return {"notas": list_temp, "graus": ["I", "II", "III", "IV", "V", "VI", "VII"]}
