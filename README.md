# DataLoadAndTransformation

**Software requirements:** 

    Pycharm 
    Python
    pip
    pandas

**Setup :** 

    Clone Repository "https://github.com/muneendravipparthi/DataLoadAndTransformation"
    Install libraries from requirements.txt

**Input Files** 
“/app/in”
     
 **InstrumentDetails.csv**

        ID
        Name
        ISIN
        Unit Price
     
**PositionDetails.csv**

        ID
        InstrumentID
        Quantity
      
**Output File** 
“/app/out”

**PositionReport.csv
DestinationFile = Pandas script df of(Input1 +Input2)**

        ID
        PositionID
        ISIN 
        Quantity
        Total Price

**Script Execution** 
_pythonProject/FileTransferamtion/FileTransfermation.py_

# Data Validation

    SourceFile = PositionReport.csv
    DestinationFile = Pandas script df of(Input1 +Input2)
    Data validation report = SourceFile <> DestinationFile

**To find the data difference between Source and Destination**
PositionReport_validationreport.csv  / PositionReport_validationreport.xlsx

Note: wantedly entered wrong data in source file to show the failed record in reports (PositionId P008) 

