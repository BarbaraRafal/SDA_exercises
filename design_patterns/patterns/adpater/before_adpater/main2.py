from mock_customer import MOCKCUSTOMER
from mock_vendor import MOCKVENDOR

TYPE = "customers"


def main():
    if TYPE == "customers":
        for customer in MOCKCUSTOMER:
            print(f"Nazwa: {customer.name}; Adres: {customer.address}")
    elif TYPE == "vendors":
        for vendor in MOCKVENDOR:
            print(f"Nazwa: {vendor.name}; Adres: {vendor.street} {vendor.number}")


if __name__ == "__main__":
    main()
