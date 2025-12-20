1.class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.title} | {self.due_date} | {status}"
2.class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def list_all_tasks(self):
        for i, task in enumerate(self.tasks):
            print(i, task)

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if not task.completed:
                print(task)
3.todo = ToDoList()

while True:
    print("\n1. Add Task\n2. Complete Task\n3. List All Tasks\n4. Incomplete Tasks\n5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        desc = input("Description: ")
        due = input("Due date: ")
        todo.add_task(Task(title, desc, due))

    elif choice == "2":
        todo.list_all_tasks()
        index = int(input("Enter task index: "))
        todo.mark_task_complete(index)

    elif choice == "3":
        todo.list_all_tasks()

    elif choice == "4":
        todo.list_incomplete_tasks()

    elif choice == "5":
        break

Homework 2: Simple Blog System
1.class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
2.class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for i, post in enumerate(self.posts):
            print(i, post)

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            self.posts.pop(index)

    def edit_post(self, index, title, content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = title
            self.posts[index].content = content

    def latest_posts(self, n=3):
        for post in self.posts[-n:]:
            print(post)
3.blog = Blog()

while True:
    print("\n1. Add Post\n2. List Posts\n3. By Author\n4. Delete\n5. Edit\n6. Latest\n7. Exit")
    choice = input("Choose: ")

    if choice == "1":
        t = input("Title: ")
        c = input("Content: ")
        a = input("Author: ")
        blog.add_post(Post(t, c, a))

    elif choice == "2":
        blog.list_posts()

    elif choice == "3":
        author = input("Author name: ")
        blog.posts_by_author(author)

    elif choice == "4":
        blog.list_posts()
        i = int(input("Index: "))
        blog.delete_post(i)

    elif choice == "5":
        blog.list_posts()
        i = int(input("Index: "))
        t = input("New title: ")
        c = input("New content: ")
        blog.edit_post(i, t, c)

    elif choice == "6":
        blog.latest_posts()

    elif choice == "7":
        break

Homework 3: Simple Banking System
1.class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.acc_no} | {self.name} | Balance: {self.balance}"
2.class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_no] = account

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def deposit(self, acc_no, amount):
        acc = self.get_account(acc_no)
        if acc:
            acc.balance += amount

    def withdraw(self, acc_no, amount):
        acc = self.get_account(acc_no)
        if acc:
            if acc.balance >= amount:
                acc.balance -= amount
            else:
                print("Insufficient funds")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver and sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
3.bank = Bank()

while True:
    print("\n1. Add Account\n2. Balance\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Details\n7. Exit")
    choice = input("Choose: ")

    if choice == "1":
        acc = input("Account No: ")
        name = input("Name: ")
        bank.add_account(Account(acc, name))

    elif choice == "2":
        acc = input("Account No: ")
        print(bank.get_account(acc).balance)

    elif choice == "3":
        acc = input("Account No: ")
        amt = float(input("Amount: "))
        bank.deposit(acc, amt)

    elif choice == "4":
        acc = input("Account No: ")
        amt = float(input("Amount: "))
        bank.withdraw(acc, amt)

    elif choice == "5":
        a1 = input("From: ")
        a2 = input("To: ")
        amt = float(input("Amount: "))
        bank.transfer(a1, a2, amt)

    elif choice == "6":
        acc = input("Account No: ")
        print(bank.get_account(acc))

    elif choice == "7":
        break
