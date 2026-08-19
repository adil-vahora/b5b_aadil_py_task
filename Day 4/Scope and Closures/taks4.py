def update_status():
    status = "pending"

    def complete():
        nonlocal status
        status = "completed"

    complete()

    print("Final status:", status)


update_status()