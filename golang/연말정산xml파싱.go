package main

import (
	"encoding/xml"
	"fmt"
	"os"
)

type YesOne struct {
	XMLName xml.Name `xml:"yesone"`
	Forms   []Form   `xml:"form"`
}

type Form struct {
	XMLName xml.Name `xml:"form"`
	FormCd  string   `xml:"form_cd,attr"`
	Man     Man      `xml:"man"`
}

type Man struct {
	XMLName                 xml.Name `xml:"man"`
	Fnm                     string   `xml:"fnm,attr"`
	Tnm                     string   `xml:"tnm,attr"`
	PyrCprTdmrCsicAddDdcAmt string   `xml:"pyrCprTdmrCsicAddDdcAmt,attr"`
  BhClCd                  string   `xml:"bhClCd,attr"`
  /**
    todo 항목 추가
  **/
}

func main() {
  /**
    test.xml 일부
    
      <yesone>
      
         ...........
         
        <form form_cd="C101Y">
      		<man tnm="서동봄전보영초" bsnoEncCntn="1302604155" fnm="한동명" resnoEncCntn="8308162215206" adr="" pfbAdr="" bhClCd="01">
      			<data lsorFnm="" txprDscmNoEncCntn="4811131004399" hsngTypeClCd="아파트" hsngCtrSfl="25.00" mmrLsrnCtrpAdr="대전 삼호아파트" mmrCtrTermStrtDt="20220101" mmrCtrTermEndDt="20230101" useAmt="6600000" mmrDdcAmt="0"></data>
      			<data lsorFnm="창충" txprDscmNoEncCntn="1601073422807" hsngTypeClCd="다가구" hsngCtrSfl="33.00" mmrLsrnCtrpAdr="세종시" mmrCtrTermStrtDt="20221218" mmrCtrTermEndDt="20231230" useAmt="200000" mmrDdcAmt="0"></data>
      			<data lsorFnm="만판신밤" txprDscmNoEncCntn="1271952403" hsngTypeClCd="오피스텔" hsngCtrSfl="22.00" mmrLsrnCtrpAdr="대전" mmrCtrTermStrtDt="20201221" mmrCtrTermEndDt="20221206" useAmt="300000" mmrDdcAmt="0"></data>
      		</man>
      	</form>
      	<form form_cd="D101Y">
      		<man fnm="한동명" resno="8308162215206" tnm="서동봄전보영초" bsnoEncCntn="1302604155" attrYr="2022">
      			<data resnoEncCntn="8308162215206" yn="O" bsnoEncCntn=" " plymNm=" " mdxpsPrfClCd="1" scnt="2" useAmt="2678000" yn3="X" yn2="X"></data>
      			<data resnoEncCntn="8308162215206" yn="O" bsnoEncCntn="2118536318" plymNm="대우너김 충주임오호" mdxpsPrfClCd="2" scnt="1" useAmt="1000000" yn3="X" yn2="O"></data>
      			<data resnoEncCntn="8308162215206" yn="O" bsnoEncCntn="2118536778" plymNm="（안）종차기우상 약주송단 생항말" mdxpsPrfClCd="2" scnt="4" useAmt="400000" yn3="X" yn2="X"></data>
      		</man>
      	</form>
      </yesone>
      
  **/
  
	file, err := os.ReadFile("test.xml")
	if err != nil {
		panic(err)
	}
  
	var yesOne YesOne

	err = xml.Unmarshal(file, &yesOne)
	if err != nil {
		panic(err)
	}
	fmt.Println(yesOne.Forms)
}



