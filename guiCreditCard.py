import tkinter as tk

main_window = tk.Tk()

frame1 = tk.Frame(main_window)
frame1.grid(row=0, column=0)

main_window.geometry('500x300')
padd = 50
main_window['padx'] = padd

title_text = tk.Label(frame1, text='Credit card number verifier')
title_text.grid(row=0, column=0)

display_result = tk.Entry(frame1)
display_result.grid(row=1, column=0)
frame = tk.Frame(main_window)
frame.grid(row=0, column=30)


def destroyLabels(frame):
    for wid in frame.winfo_children():
        wid.destroy()


def luhn():
    global frame
    destroyLabels(frame)
    if not (len(display_result.get()) == 16):
        print("Your card number should be 16 digits long.")

        tk.Label(frame, text="Your card number should be 16 digits", fg="red", font=("calibri", 11)).grid(row=0,
                                                                                                            column=30)
        return False
    # we iterate through the number from the LSD
    cardSum = 0
    isSecond = False
    for i in range(15, -1, -1):
        digit = ord(display_result.get()[i]) - ord('0')
        if isSecond:
            digit *= 2
        # these 2 lines deal with both single digit and double-digit cases
        cardSum += digit // 10
        cardSum += digit % 10
        isSecond = not isSecond
    if cardSum % 10 == 0:
        print("Your card number is valid.")
        tk.Label(frame, text="Verification success", fg="green", font=("calibri", 11)).grid(row=0, column=30)
        return True
    else:
        print("Your card number is not valid.")
        tk.Label(frame, text="Verification failure", fg="red", font=("calibri", 11)).grid(row=0, column=30)

        return False


card_verify = tk.Button(frame1, text='Verify', command=luhn)
card_verify.grid(row=2, column=0)
main_window.mainloop()
