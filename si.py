while True:
    try:
        print(5/0)
    except Exception as e:
        print(f'error{e}')
    print("°")