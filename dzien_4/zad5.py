# mamy plansze do gry w kolko i krzyzyk
#
# 1: x|o|x
# ...............
# 2. | |
# ..............
#3.o| |
# A B C

# board = [
#     ["x","0","x"],
#     [" "," "," "],
#     ["0"," "," "]
# ]
#
# Naisz fuknkcje get_row_col
#
# ktora przyjmie napis odpowiadajacy polozeniu na planszy np.A1, C2 i zwroci koordynaty
# get_row_col("A3")->(2,0)

# def get_row_col(napis):
    #   for litera in napis:
    #     if litera =="A":
    #         a=2
    #     if litera =="B":
    #         a=1
    #     else:
    #         a=0
    # for cyfra in napis:
    #     if cyfra =="1":
    #         b=0
    #     if cyfra ==2:
    #         b=1
    #     else:
    #         b=2
    #  return result=(a,b)


def get_row_col(position):
    columns="ABC"
    rows="123"
    col_n, row_n=list(position)
    try:
        return rows.index(row_n), columns.index(col_n)
    except:
        return "kordynata spoza planszy"

def test_get_row_col():
    assert get_row_col("A3")==(2,0)
    assert get_row_col("C3")==(2,2)
    assert get_row_col("D4")=="kordynata spoza planszy"

