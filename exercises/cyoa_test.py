
def main() -> None:
    global bob
    bob: str = ""
    global_bob()


def global_bob() -> None:
    
    bob = "tom"
    print(bob)

if __name__ == "__main__":
    main()

