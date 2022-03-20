    
    select 
    I.iInvoiceNum,
    I.dInvoiced,
    U.sUnitName,
    S.sLocationCode as LocationCode,
    S.sSiteName as LocationName,
    C.LedgerID,
    L.iLeaseNum,
    C.dCreated AS Date,
    C.ChargeID as ChargeId,
    CD.ChargeDescID as ItemID,
    CASE
        sChgDesc
        WHEN 'Rent' THEN ISNULL(CD.sChgDesc, '') + ' ' + ISNULL(convert(varchar, C.dChgStrt, 103), '') + '  ' + ISNULL(convert(varchar, c.dChgEnd, 103), '')
        ELSE ISNULL(CD.sChgDesc, '')
    END AS ItemDescription,
    C.dcQty as Qty,
    C.dcPrice as Price,

	CASE C.dcTax1  WHEN 0 THEN   C.dcPrice
	
		                  ELSE  Cast(ROUND((C.dcPrice/1.07)  ,2) as decimal(18,2)) 
	
	END as SubTotalPrice,
	CASE C.dcTax1  WHEN 0 THEN  0
	
		                  ELSE  Cast(ROUND(((C.dcPrice/1.07) * 0.07),2) as decimal(18,2))
	
	END as Itbms,
    T.TenantID,
    CASE
        bCompanyIsTenant
        WHEN 'True' THEN T.sCompany
        WHEN 'False' THEN ISNULL(sFName, '') + ' ' + ISNULL(sLName, '')
    END AS CustomerName,
    T.sLicense as RUC,
    ISNULL(T.sAddr1, '') + ' ' + ISNULL(T.sAddr2, '') + ' ' + ISNULL(T.sCity, '') + ' ' + ISNULL(T.sCountry, '') as Address,
    T.sPhone,
    T.sEmail
    
    from Invoices as I 
   
    inner join InvoiceDetails as D on I.InvoiceID = D.InvoiceID  
    inner join Tenants T on T.TenantID = I.TenantID
    inner join Charges C on C.ChargeID = D.ChargeID
    inner join ChargeDesc CD on CD.ChargeDescID = C.ChargeDescID
    inner join Ledgers as L on L.LedgerID = C.LedgerID
    inner join Sites S on S.SiteID = C.SiteID
    inner join Units U on U.UnitID = L.UnitID
    WHERE
    I.dInvoiced >= (
        SELECT
            Convert(
                DATETIME,
                Convert(VARCHAR(8), GetDate() - 30 , 112)
            )
    )