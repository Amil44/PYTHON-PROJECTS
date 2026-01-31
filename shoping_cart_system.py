print('''__Shopping Center__
1. Add Product
2. Show Product
3. Delete Product
4. Clear Cart
5. Show Your Curt
6. Exit
''')

products = [
    "1984 by George Orwell",
    "To Kill a Mockingbird by Harper Lee",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
    "The Hobbit by J.R.R. Tolkien",
    "Pride and Prejudice by Jane Austen",
    "The Catcher in the Rye by J.D. Salinger",
    "The Lord of the Rings by J.R.R. Tolkien",
    "Brave New World by Aldous Huxley",
    "The Kite Runner by Khaled Hosseini"
]


tf = True
your_cart = []

while tf:
    try:
        op = int(input('Enter the operation(1, 2, 3, 4, 5, 6):'))

        match op:
            case 1:
                print('\n< Add Product >\nOur Products:\n\t-"1984 by George Orwell"\n\t-"To Kill a Mockingbird by Harper Lee"\n\t-"The Great Gatsby by F. Scott Fitzgerald"\n\t-"Harry Potter and the Sorcerer\' Stone by J.K. Rowling"\n\t-"The Hobbit by J.R.R. Tolkien"\n\t-"Pride and Prejudice by Jane Austen"\n\t-"The Catcher in the Rye by J.D. Salinger"\n\t-"The Lord of the Rings by J.R.R. Tolkien"\n\t-"Brave New World by Aldous Huxley"\n\t-"The Kite Runner by Khaled Hosseini"')
                print('Which one attracts you?\n*Select your book*')

                try:
                    book = int(input('the order of the book(1-10):'))

                    if book == 1:
                        if "1984 by George Orwell" in products:
                            your_cart.append("1984 by George Orwell")
                            print('Product Added Succesfuly')
                            products.remove("1984 by George Orwell")

                        else:
                            print('Product sold out!')
                    

                    elif book == 2:
                        if "To Kill a Mockingbird by Harper Lee" in products: 
                            your_cart.append("To Kill a Mockingbird by Harper Lee")
                            print('Product Added Succesfuly')
                            products.remove("To Kill a Mockingbird by Harper Lee")

                        else:
                            print('Product sold out!')

                    elif book == 3:
                        if "The Great Gatsby by F. Scott Fitzgerald" in products:
                            your_cart.append("The Great Gatsby by F. Scott Fitzgerald")
                            print('Product Added Succesfuly')
                            products.remove("The Great Gatsby by F. Scott Fitzgerald")

                        else:
                            print('Product sold out!')

                    elif book == 4:
                        if "Harry Potter and the Sorcerer's Stone by J.K. Rowling" in products:
                            your_cart.append("Harry Potter and the Sorcerer's Stone by J.K. Rowling")
                            print('Product Added Succesfuly')
                            products.remove("Harry Potter and the Sorcerer's Stone by J.K. Rowling")

                        else:
                            print('Product sold out!')

                    elif book == 5:
                        if "The Hobbit by J.R.R. Tolkien" in products:
                            your_cart.append("The Hobbit by J.R.R. Tolkien")
                            print('Product Added Succesfuly')
                            products.remove("The Hobbit by J.R.R. Tolkien")

                        else:
                            print('Product sold out!')

                    elif book == 6:
                        if "Pride and Prejudice by Jane Austen" in products:
                            your_cart.append("Pride and Prejudice by Jane Austen")
                            print('Product Added Succesfuly')
                            products.remove("Pride and Prejudice by Jane Austen")

                        else:
                            print('Product sold out!')

                    elif book == 7:
                        if "The Catcher in the Rye by J.D. Salinger" in products:
                            your_cart.append("The Catcher in the Rye by J.D. Salinger")
                            print('Product Added Succesfuly')
                            products.remove("The Catcher in the Rye by J.D. Salinger")

                        else:
                            print('Product sold out!')

                    elif book == 8:
                        if "The Lord of the Rings by J.R.R. Tolkien" in products:
                            your_cart.append("The Lord of the Rings by J.R.R. Tolkien")
                            print('Product Added Succesfuly')
                            products.remove("The Lord of the Rings by J.R.R. Tolkien")

                        else:
                            print('Product sold out!')

                    elif book == 9:
                        if "Brave New World by Aldous Huxley" in products:
                            your_cart.append("Brave New World by Aldous Huxley")
                            print('Product Added Succesfuly')
                            products.remove("Brave New World by Aldous Huxley")

                        else:
                            print('Product sold out!')

                    elif book == 10:
                        if "The Kite Runner by Khaled Hosseini" in products:
                            your_cart.append("The Kite Runner by Khaled Hosseini")
                            print('Product Added Succesfuly')
                            products.remove("The Kite Runner by Khaled Hosseini")

                        else:
                            print('Product sold out!')

                    else:
                        raise Exception('!Out of range!')
                    
                    
                except ValueError:
                    print('Please enter a number!')

                except Exception as e:
                    print(e)

                finally:
                    print('''\n__Shopping Center__
1. Add Product
2. Show Product
3. Delete Product
4. Clear Cart
5. Show Your Curt
6. Exit
''')

            case 2:
                for i, el in enumerate(products):
                    print(f'{i + 1}.{el}')

                print('''\n__Shopping Center__
1. Add Product
2. Show Product
3. Delete Product
4. Clear Cart
5. Show Your Curt
6. Exit
''')

            case 3:
                try:
                    print('< Section of Delete Product >')

                    for i, el in enumerate(your_cart):
                        print(f'{i + 1}.{el}')

                    print('Which one do you want to remove from the curt?: ')

                    rem = int(input('Order of Book: '))
                    your_cart.pop(rem - 1)

                    print(f'Your Cart: {your_cart}')

                    print('''\n__Shopping Center__
1. Add Product
2. Show Product
3. Delete Product
4. Clear Cart
5. Show Your Curt
6. Exit
''')

                except ValueError:
                    print('Please enter a number!')

                except IndexError:
                    print('Invalid order number!')

            case 4:
                your_cart.clear()

                print('Your Cart has Cleaned')
                print(f'Your Cart: {your_cart}')

                print('''\n__Shopping Center__
1. Add Product
2. Show Product
3. Delete Product
4. Clear Cart
5. Show Your Curt
6. Exit
''')

            case 5:
                print('Your Products')

                for i, el in enumerate(your_cart):
                    print(f'{i + 1}.{el}')

                print(f'Your Product\'s count: {len(your_cart)}')

                print('''\n__Shopping Center__
1. Add Product
2. Show Product
3. Delete Product
4. Clear Cart
5. Show Your Curt
6. Exit
''')

            case 6:
                print('< Exit >')
                print(f'The Final Cart: {your_cart}')
                tf = False

            case _:
                raise Exception('!!Enter Correct Value!!')

    except ValueError:
        print('Please enter a number!')

    except Exception as e:
        print(e)
