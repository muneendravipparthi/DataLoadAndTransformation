import pandas as pd

input_file_1 = "InstrumentDetails.csv"
input_file_2 = "PositionDetails.csv"
output_file = "PositionReport.csv"

InstrumentDetails_df = pd.read_csv(input_file_1)
PositionDetails_df = pd.read_csv(input_file_2)
PositionDetails_df = PositionDetails_df.rename(columns = {'ID':'PositionID'}, inplace = False)
output_df = InstrumentDetails_df.merge(PositionDetails_df, left_on='ID', right_on='PositionID')
output_df['Total Price'] = output_df['Quantity'] * output_df['Unit Price']
outputcolumnslist = ['ID', 'PositionID', 'ISIN', 'Quantity', 'Total Price']
output_df = output_df[outputcolumnslist]
output_df.to_csv(output_file, index=False)