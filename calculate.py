def calculate():
    print("簡易電卓アプリケーションです。終了時には '=' を入力してください。")
    result = float(input("数値を入力してください： "))

    while True:
        operation = input("操作を選択してください（+, -, *, /, =）: ")

        if operation == '=':
            print(f"計算結果： {result}")
            break
        elif operation in ('+', '-', '*', '/'):
                number = float(input("数値を入力してください： "))
                match operation:
                    case '+':
                        result += number
                    case '-':
                        result -= number
                    case '*':
                        result *= number
                    case '/':
                        if number != 0:
                            result /= number
                        else:
                            print("0で割ることはできません")
                            continue
        else:
            print("無効な操作です。")

calculate()