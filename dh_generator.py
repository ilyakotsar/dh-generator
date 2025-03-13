import random
from cryptography.hazmat.primitives.asymmetric import dh


def generate_dh_parameters(key_size=2048) -> str:
    g = random.choice([2, 5])
    parameters = dh.generate_parameters(generator=g, key_size=key_size)
    numbers = parameters.parameter_numbers()
    return f'{numbers.g}_{numbers.p}'


def main() -> None:
    parameters = generate_dh_parameters()
    print(parameters)
    input('\nPress Enter to exit')


if __name__ == '__main__':
    main()
