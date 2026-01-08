from ctypes.wintypes import PLARGE_INTEGER


class icecream:

    def ice_cream_price(self):
        flavours = {
            "Chocolate": {"Large": 100, "Small": 70},
            "Vanilla": {"Large": 90, "Small": 70},
            "ButterScotch": {"Large": 80, "Small": 60}
        }

        print("Welcome to Natural Ice Cream!Enjoy")

        # Keep asking until a valid flavour is entered
        while True:
            flavour = input("Which flavour do you want? ").title()
            if flavour in flavours:
                break
            print("Flavour not available. Please try again.")

        # Keep asking until a valid size is entered
        while True:
            size = input("What size do you want? (Large/Small): ").title()
            if size in flavours[flavour]:
                break
            print("Invalid size. Please try again.")

        price = flavours[flavour][size]
        print(f"Price of {size} {flavour} Ice Cream is ₹{price}")


ice=icecream()
ice.ice_cream_price()


