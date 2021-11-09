
CREATE TABLE IF NOT EXISTS Customers ( 

    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'dNombRec' VARCHAR(50),
    'iTipoRec' INTEGER ,
    'dTipoRuc' INTEGER,
    'dRuc' VARCHAR(22),
    'dDV' INTEGER, 
    'dDirecRec' VARCHAR(50),
    'dCodUbi' VARCHAR(8),
    'dCorreg' VARCHAR(20),
    'dDistr' VARCHAR(20),
    'dProv' VARCHAR(20),
    'dTfnRec' VARCHAR(15),
    'dCorElectRec' VARCHAR(50),
    'cPaisRec' VARCHAR(2)

);


CREATE TABLE IF NOT EXISTS Products ( 

    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'dCodProd' VARCHAR(50),
    'dDescProd' INTEGER ,
    'cUnidad' VARCHAR(22),
    'dFechaFab' DATETIME,
    'dFechaCad' DATETIME,
    "dPrUnit" DECIMAL(16,4),
    'Taxable' BOOLEAN

);