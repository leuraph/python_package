from awesome_package import module_B
from dev_tools import utils


def main():
    a = 2
    b = 4

    print()
    print("manual test for module_B...")
    print("---------------------------")
    print("module_B.multiply :")
    print(f"expected value: {a*b}, got: {module_B.multiply(a, b)}")

    print("testing something with utils needed")
    utils.say_hello_to(name="Pino")


if __name__ == '__main__':
    main()
