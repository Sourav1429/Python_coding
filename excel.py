def convexceltodf(file,sheet='Sheet1'):  #'Sheet1' because it is usually by default the first sheet of an Excel file
    from openpyxl import load_workbook
    import pandas as pd
    import itertools as it
    wb= load_workbook(file)
    ws=wb[sheet]
    data = ws.values
    cols = next(data)[1:]
    data = list(data)
    idx = [r[0] for r in data]
    data = (it.islice(r, 1, None) for r in data)
    df = pd.DataFrame(data, index=idx, columns=cols)
    return df
