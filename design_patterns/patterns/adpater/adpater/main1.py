from mock_customer import MOCKCUSTOMER
from mock_vendor import MOCKVENDOR


def main():
    for customer in MOCKCUSTOMER+MOCKVENDOR:
        print(f"Nazwa: {customer.name}; Adres: {customer.address}")


if __name__=="__main__":
    main()
