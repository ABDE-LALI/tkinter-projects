from tkinter import *

sdk = Tk()
sdk.title("SOUDOUKOU")
sdk.iconbitmap("173877_sudoku_icon.ico")
sdk.geometry("400x500")
usage = Label(
    sdk, text="enter numbers and click check if its correct", bg="#cccccc")
usage.grid(row=0, column=1, columnspan=10)

isvalid_soudo = Label(sdk, text="")
isvalid_soudo.grid(row=16, column=0, columnspan=10, pady=5)

# isnotvalid_soudo = Label(sdk, text="", bg="red")
# isnotvalid_soudo.grid(row=16, column=1, columnspan=10, pady=5)

answers = {}


def check_entry(val):
    valid = (val.isdigit() or val == "") and len(val) < 2 and val != "0"
    return valid


check_res = sdk.register(check_entry)


def petit_table(row, col, color):
    for i in range(3):
        for j in range(3):
            fild = Entry(sdk, width=5, bg=color, justify="center",
                         validate="key", validatecommand=(check_res, "%P"))
            fild.grid(row=row + i, column=col + j,
                      sticky="nsew", padx=1, pady=1, ipady=5)
            answers[(row + i, col + j)] = fild


def grand_table():
    color = "#dddddd"
    for big_row in range(1, 10, 3):
        for big_col in range(0, 9, 3):
            petit_table(big_row, big_col, color)
            if color == "#dddddd":
                color = "#aaaaaa"
            else:
                color = "#dddddd"


def clean_soudou():
    isvalid_soudo.configure(text="", bg="#f0f0f0")
    # isnotvalid_soudo.configure(text="")

    for i in range(1, 10):
        for j in range(0, 9):
            soudou_cell = answers[(i, j)]
            soudou_cell.delete(0, 1)


def check_rows(matric):
    ris45 = 0
    for i in range(9):
        rows_som = 0
        for j in range(9):
            rows_som += matric[i][j]
            if rows_som == 45:
                ris45 += 1
        print(rows_som)
    return True if ris45 == 9 else False


def check_cols(matric):
    cis45 = 0
    for i in range(9):
        cols_som = 0
        for j in range(9):
            cols_som += matric[j][i]
            if cols_som == 45:
                cis45 += 1
        print(cols_som)
    return True if cis45 == 9 else False


def check_squar(matric):
    grs_som = 0
    gis45 = 0
    # s = 0
    # ss = 0
    # n = 3
    # ns = 3
    # for group in range(9):
    #     for i in range(s, n):
    #         for j in range(ss, ns):
    #             grs_som += matric[i][j]
    #     if grs_som == 45:
    #         gis45 += 1
    #     if ns == 9:
    #         ns = 3
    #         ss = 0
    #     else:
    #         ns += 3
    #         ss += 3
    #     if group == 3:
    #         n = 6
    #         s = 3
    #     elif group == 6:
    #         n = 9
    #         s = 6
    #     print(grs_som)
    # result_blocks = []
    # for i in range(0, 9, 3):
    #     for j in range(0, 9, 3):
    #         block = [row[j:j+3] for row in matric[i:i+3]]
    #         result_blocks.append(block)
    # print(result_blocks)
    mat_grs = [[matric[0][0], matric[0][1], matric[0][2], matric[1][0], matric[1][1], matric[1][2], matric[2][0], matric[2][1], matric[2][2]],
               [matric[3][0], matric[3][1], matric[3][2], matric[4][0], matric[4][1], matric[4][2], matric[5][0], matric[5][1], matric[5][2]],
               [matric[6][0], matric[6][1], matric[6][2], matric[7][0], matric[7][1], matric[7][2], matric[8][0], matric[8][1], matric[8][2]],
               [matric[0][3], matric[0][4], matric[0][5], matric[1][3], matric[1][4], matric[1][5], matric[2][3], matric[2][4], matric[2][5]],
               [matric[3][3], matric[3][4], matric[3][5], matric[4][3], matric[4][4], matric[4][5], matric[5][3], matric[5][4], matric[5][5]],
               [matric[6][3], matric[6][4], matric[6][5], matric[7][3], matric[7][4], matric[7][5], matric[8][3], matric[8][4], matric[8][5]],
               [matric[0][6], matric[0][7], matric[0][8], matric[1][6], matric[1][7], matric[1][8], matric[2][6], matric[2][7], matric[2][8]],
               [matric[3][6], matric[3][7], matric[3][8], matric[4][6], matric[4][7], matric[4][8], matric[4][6], matric[4][7], matric[4][8]],
               [matric[6][6], matric[6][7], matric[6][7], matric[7][6], matric[7][7], matric[7][8], matric[8][6], matric[8][7], matric[8][8]]]
    for i in mat_grs :
        for j in i:
            grs_som += j
        print(i)
    if grs_som == 45:
        gis45 += 1
    print(grs_som)
    return True if gis45 == 9 else False


def check_win():
    board = []
    isvalid_soudo.configure(text="", bg="#f0f0f0")
    # isnotvalid_soudo.configure(text="")
    for i in range(1, 10):
        valeus_row = []
        for j in range(0, 9):
            cell_val = answers[(i, j)].get()
            if cell_val == "":
                valeus_row.append(0)
            else:
                valeus_row.append(int(cell_val))
        board.append(valeus_row)
    print(board)
    if check_rows(board) or check_cols(board) or check_rows(board):
        isvalid_soudo.configure(
            text="its a valid soudoukou", bg="green", width=30)
    else:
        isvalid_soudo.configure(
            text="its not a valid soudoukou", bg="red", width=30)


check_btn = Button(sdk, text="Check", bg="green", width=30,
                   command=check_win).grid(row=17, column=0, columnspan=10)
clear_btn = Button(sdk, text="Clean", bg="red", width=30,
                   command=clean_soudou).grid(row=18, column=0, columnspan=10)
grand_table()
sdk.mainloop()
