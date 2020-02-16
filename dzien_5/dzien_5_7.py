board =[
    ["x","0","X"],
    ["","",""],
    ["0","",""]
]
def get_row_col(position):
    rows="123"
    cols="ABC"
    co, row = list(position)
    return rows.index(row), cols.index(col)

assert get_row_col('A3')==(2,0)