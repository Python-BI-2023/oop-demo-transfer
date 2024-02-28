from src.factories import TransferFactory
from src.transfer import Transfer


def main():
    transfer = TransferFactory()
    src = transfer.get_src()
    dest = transfer.get_dest()
    Transfer(src=src, dest=dest).run()


if __name__ == "__main__":
    main()
