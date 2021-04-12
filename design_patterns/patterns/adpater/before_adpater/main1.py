from mock_customer import MOCKCUSTOMER


def main():
    for customer in MOCKCUSTOMER:
        print(f"Nazwa: {customer.name}; Adres: {customer.address}")


if __name__=="__main__":
    main()
