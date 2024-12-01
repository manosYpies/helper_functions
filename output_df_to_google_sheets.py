def output_df_to_google_sheets(df, workbook_nm, sheet_nm, paste_cell):
    import gspread
    """
    Description: 
    Pastes a DF to a linked google sheets document
    the proper permissions must be set in order to paste to google

    if this is your first time using this, please watch this video that'll get you the correct sharing set up:
    https://www.youtube.com/watch?v=bu5wXjz2KvU&t=179s
    

    Inputs:
    - df (dataframe): What you want added to a google sheet page
    - workbook_nm (str): name of the workbook you'd like to add your dataframe to
    - sheet_nm (str): name of the sheet you'd like to add your dataframe to
    - paste_cell (str): cell value (A1, B2,...) you'd like your output written to

    Outputs:
    - NONE


    """
    # Convert DataFrame to list of lists
    df_to_paste = df.values.tolist()

    # Include headers if needed
    headers = df.columns.tolist()
    df_to_paste.insert(0, headers)

    sa = gspread.service_account()
    sh = sa.open(workbook_nm)

    # Load to Google Sheets
    sh.values_update(
        range=sheet_nm+'!'+paste_cell,  # Corrected keyword argument
        params={
            'valueInputOption': 'USER_ENTERED'
        },
        body={
            'values': df_to_paste
        }
    )
