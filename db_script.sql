
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
    'itemId' VARCHAR(50),
    'dCodProd' VARCHAR(50),
    'dDescProd' INTEGER ,
    'cUnidad' VARCHAR(22),
    'dFechaFab' DATETIME,
    'dFechaCad' DATETIME,
    "dPrUnit" DECIMAL(16,4),
    'Taxable' BOOLEAN

);

CREATE TABLE IF NOT EXISTS Company ( 

    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'dNombEm' VARCHAR(100),
    'dSucEm' VARCHAR(4) ,
    'dCoordEm' VARCHAR(22),
    'dDirecEm' VARCHAR(100), 
    'dTfnEm' VARCHAR(12),
    'dCorElectEmi' VARCHAR(50),
    'dRuc' VARCHAR(20),
    'dTipoRuc' VARCHAR(1),
    'dDV' VARCHAR(2),
    'dCodUbi' VARCHAR(8),
    'dCorreg' VARCHAR(50),
    'dDistr' VARCHAR(50),
    'dProv' VARCHAR(50)

);


CREATE TABLE IF NOT EXISTS DocumentHdr ( 

    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'iDoc' VARCHAR(1),
    'dNroDF' VARCHAR(10),
    'dPtoFacDF' VARCHAR(3),
    'dFechaEm' DATETIME,
    'dFechaSalida' DATETIME,
    'iNatOp' VARCHAR(2),
    'iTipoOp' VARCHAR(1),
    'iDest' VARCHAR(1),
    'iTipoTranVenta' VARCHAR(1),
    'dInfEmFE' VARCHAR(5000),
    'customer_id' INTEGER

  

);


CREATE TABLE IF NOT EXISTS DocumentDtls ( 

    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'dSecItem' VARCHAR(4),
    'dDescProd' VARCHAR(500) ,
    'dCodProd' VARCHAR(20),
    'cUnidad' VARCHAR(20), 
    'dCantCodInt' DECIMAL(11,6),
    'dFechaFab' DATETIME,
    'dFechaCad' DATETIME,
    'dCodCPBSabr' VARCHAR(2),
    'dCodCPBScmp' VARCHAR(4),
    'cUnidadCPBS' VARCHAR(30),
    'dInfEmFE' VARCHAR(5000),
    'dPrUnit' DECIMAL(11,6),
    'dPrUnitDesc' DECIMAL(11,6),
    'dPrItem' DECIMAL(11,6),
    'dPrAcarItem' DECIMAL(11,2),   
    'dPrSegItem' DECIMAL(11,2),  
    'dValTotItem' DECIMAL(11,6),  
    'dGTINCom' INTEGER,  
    'dCantGTINCom' DECIMAL(11,6),  
    'dGTINInv' INTEGER,  
    'dCantComInvent' DECIMAL(11,6),  
    'dTasaITBMS' INTEGER ,  
    'dValITBMS'  DECIMAL(11,6),  
    'dTasaISC' DECIMAL(11,4),  
    'dValISC'  DECIMAL(11,6)

);



CREATE TABLE IF NOT EXISTS Settings ( 

    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'key'   VARCHAR(50),
    'count' INTEGER ,
    'val1' VARCHAR(150),
    'val2' VARCHAR(150),
    'val3' VARCHAR(150),
    'val4' VARCHAR(150)
);
