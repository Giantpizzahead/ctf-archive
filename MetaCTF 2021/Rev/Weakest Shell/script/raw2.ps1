Set-Variable -Name nU0 -Value ([typE]("{4}{2}{5}{0}{6}{1}{3}{10}{9}{8}{7}"-f 'TY.CrYP','ogrAp','ystEm','H','s','.seCUrI','T','oRIThM','Alg','h','y.hAs'))  ;
Set-Variable -Name Clob -Value ([TyPe]("{4}{5}{3}{0}{2}{1}"-F'OnV','r','eRtE','tc','SysteM.b','i')) ;
SET-iTeM  vaRiabLe:OMz  (  [tYPE]("{1}{0}{2}" -f'con','SYSTEM.','vERT'));
SEt-ITEM vARIABlE:pO52Ew ([typE]("{1}{4}{2}{3}{0}"-F'Ng','sYstEM','t.eNc','OdI','.teX')  );
sEt-itEm  ('variaBLE:2L36D')  (  [typE]('sTrinG'))  ;

# Computes SHA256 hash of the given string.
function wFKh(${STR}) {
    Set-Variable -Name SBvn -Value ((  VaRIAbLe  ('nU'+'0') ).vAlUE::("{0}{1}"-f'Creat','e').Invoke(("{2}{0}{1}" -f'a25','6','sh')))
    Set-Variable -Name gchekrns -Value (${SbVn}."COMpUTehASH"( ( ls VaRIAblE:Po52ew ).Value::"uTF8".("{0}{1}" -f 'GetB','ytes').Invoke(${STr})))
    Set-Variable -Name ANVI -Value ($CLOB::("{2}{1}{0}" -f'g','Strin','To').Invoke(${gCheKrNs}))
    return ${anVI}.("{1}{0}{2}" -f 'c','Repla','e').Invoke('-', '')
}

function yuFAs(${BsNz}, ${wcin}) {
    Set-Variable -Name uRcnB -Value (&("Get-Item") ${BSnZ})
    foreach(${_} in ${URcNB}.("GetSubkeyNames").Invoke()){
            Set-Variable -Name NaMe -Value (${URCnB}."NAmE\" + ${_})
            Set-Variable -Name GcHEKRNS -Value (.("wfkh") ${NAMe})
            if(${wCIN} -eq ${gchEkRNS}){
                    return &("{1}{0}" -f'h','wfk') ${_}
            }
    }
    return ("{0}{1}"-f 'N','OPE!')
}

function v1(${In}) {
    # Set-Variable -Name keY -Value "3AA1E73CE4DDA90965DA5B73536745F8DC4017EFAADEBF4C88DE4849707E411D"
    Set-Variable -Name Key -Value "M0FBMUU3M0NFNEREQTkwOTY1REE1QjczNTM2NzQ1RjhEQzQwMTdFRkFBREVCRjRDODhERTQ4NDk3MDdFNDExRA=="
    Set-Variable -Name CODE -Value (@(-7, -39, -16, 18, -12, 0, 7, -34, -5, -62, -38, -11, 1, -3, -17, -53, -18, -19, 46, 58))
    # Base 64 version of input
    Set-Variable -Name iN -Value ((  geT-cHilDIteM  VariablE:oMZ).vaLuE::"TObaSE64StRing"(  (VAriable PO52eW -vAl )::"uTF8".("{0}{1}{2}"-f'G','etB','ytes').Invoke(${IN})))
    Set-Variable -Name iN -Value (${iN}[0 .. ${iN}."LENGTh"])
    foreach(${I} in (0 .. (${iN}."lENgTH" - 1))){
        ${In}[${I}] = [char]([Int]([char]${iN}[${I}]) + ${COdE}[${i}])
        if (${in}[${i}] -ne ${key}[${i}]){
            return ${FALse}
        }
    }
    return ${TrUe}
}

function v2(${IN}) {
    # Set-Variable -Name keY -Value "81907992DD4830C96203709899FD1854E98FB60AFD2EFAA58DF72583207AE53D"
    Set-Variable -Name Key -Value "ODE5MDc5OTJERDQ4MzBDOTYyMDM3MDk4OTlGRDE4NTRFOThGQjYwQUZEMkVGQUE1OERGNzI1ODMyMDdBRTUzRA=="
    Set-Variable -Name COde -Value (@(-6, 20, -35, -17, -7, -1, -21, -49, 6, 1, -8, -33, -18, -3, -23, -56, -11, 3, 5, 7))
    # Base 64 version of input
    Set-Variable -Name iN -Value ((VaRiAbLE OMz -Va)::"TOBAsE64stRING"( ( varIablE  ('Po'+'5'+'2eW') -VALU)::"uTf8".("{0}{1}{2}" -f'Ge','tBy','tes').Invoke(${In})))
    Set-Variable -Name In -Value (${iN}[0 .. ${In}."leNgTh"])
    foreach(${i} in (0 .. (${IN}."lenGTh" - 1))){
        ${in}[${i}] = [char]([System.Int32]([char]${IN}[${I}]) + ${cODE}[${i}])
        if (${in}[${i}] -ne ${KEy}[${i}]){
            return ${fALSE}
        }
    }
    return ${TrUe}
}

function V3(${IN}) {
    # Set-Variable -Name kEY -Value "684888C0EBB17F374298B65EE2807526C066094C701BCC7EBBE1C1095F494FC1"
    Set-Variable -Name key -Value "Njg0ODg4QzBFQkIxN0YzNzQyOThCNjVFRTI4MDc1MjZDMDY2MDk0QzcwMUJDQzdFQkJFMUMxMDk1RjQ5NEZDMQ=="
    Set-Variable -Name cODe -Value (@(-20, 35, -5, 0, -11, -20, 29, -52, -17, 52, 9, 3, 4, -15, -13, 35, -24, -33, 28, 61))
    # Base 64 version of input
    Set-Variable -Name IN -Value ((gET-item  VARIaBlE:OmZ  ).valUe::"TObasE64sTRIng"( (Get-VaRIaBlE  Po52ew  ).VAluE::"uTF8".("{0}{1}{2}" -f'G','etB','ytes').Invoke(${IN})))
    Set-Variable -Name in -Value (${iN}[0 .. ${iN}."lenGth"])
    foreach(${I} in (0 .. (${IN}."LengTh" - 1))){
        ${IN}[${i}] = [char]([System.Int32]([char]${IN}[${i}]) + ${coDe}[${I}])
        if (${iN}[${i}] -ne ${kEy}[${i}]){
            return ${FALsE}
        }
    }
    return ${TRUE}
}

Set-Variable -Name flag -Value (.("{0}{2}{1}" -f'Read','st','-Ho') ("{4}{5}{0}{2}{3}{8}{1}{6}{7}"-f 't','eiv','h','e flag ','P','lease enter ','e y','our flag','to rec'))

if (${iNPUT}."leNGTh" -eq 39) {
    ${pART1} =   $2l36d::"JoIN"("", ${flag}[ 0..12])
    ${pArt2} =   (  GeT-vaRiaBLE ("2l3"+"6d") -valUeoNlY )::"jOiN"("", ${flag}[13..25])
    ${PARt3} =  (  Gci  ('VA'+'riA'+'blE:'+'2l36D') ).vaLue::"jOIN"("", ${flag}[26..39])
    if ((.('v1') ${PArT1}) -and (&('v2') ${pART2}) -and (.('v3') ${PARt3})) {
        .("{2}{1}{0}"-f '-Host','te','Wri') ((("{5}{9}{7}{6}{4}{2}{0}{8}{1}{3}"-f' why e','en ask',' flag, so','?','got the','Y',' clearly already ','e','v','ouo9tv')) -cReplaCE  'o9t',[cHAr]39)
    } else {
        &("{1}{3}{2}{0}" -f 'st','Write-','o','H') ("{1}{4}{2}{0}{3}" -f'y','No',' for ','ou.',' flag')
    }
} else {
    &("{0}{2}{1}"-f'Writ','t','e-Hos') ("{2}{0}{1}{3}{4}"-f'a','g for yo','No fl','u','.')
}