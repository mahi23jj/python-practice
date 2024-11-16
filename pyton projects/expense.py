class expense:
    def __init__(self, name, catagory, amount) -> None:
        self.name = name
        self.catagory = catagory
        self.amount = amount

    def __repr__(self) -> str:
        return f"Expnese:{self.name},{self.catagory},{self.amount}"


def get_user():
    name = input("Enter the name:")
    amoun = float(input("Enter the amount"))
    elements = ["food", "rent", "work", "Fun"]
    while True:
        for i in range(len(elements)):
            elem = elements[i]
            print(f"{i+1}. {elem}")
        cat = int(input("Enter the catagory:"))
        if cat > 0 and cat <= len(elements):
            cats=elements[cat-1]
            val = expense(name,cats,amoun)
            break
        else:
            print("invalid input")
    return f"Expnese:{val.name},{val.catagory},{val.amount}"
     
def save_data(expense):
    with open("file_name.txt","a") as e:
        e.write(expense)


# def main():
#     print(f"Running Expense Tracker!")

# if __name__=="__main__":
#     main()
expnse=get_user()
save_data(expense=expnse)
