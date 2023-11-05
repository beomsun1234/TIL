import (
  "database/sql"

	_ "github.com/go-sql-driver/mysql"
)

var db       *sql.DB

func bulkInsertStocks(data []krx.Stock, businessDay string) {
	tx, err := db.Begin()
	if err != nil {
		fmt.Println(err)
		return
	}
  // insert할 데이터 수만큼 (?, ?, ?, ?) 를 만들어준다. ?의 수는 저장할 컬럼수 만큼 세팅해준다.
	valueStrings := make([]string, 0, len(data))
  // ?에 들어갈 데이터를 넣어준다.
	valueArgs := make([]interface{}, 0, len(data)*15)
  
	for _, stock := range data {
		valueStrings = append(valueStrings, "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
		valueArgs = append(valueArgs, stock.Ticker)
		valueArgs = append(valueArgs, businessDay)
		valueArgs = append(valueArgs, stock.Name)
		valueArgs = append(valueArgs, "KOSPI")
		valueArgs = append(valueArgs, getChangeCode(stock.FluctuationRange))
		valueArgs = append(valueArgs, stock.FluctuationRange)
		valueArgs = append(valueArgs, stock.FluctuationRate)
		valueArgs = append(valueArgs, stock.OpenPrice)
		valueArgs = append(valueArgs, stock.HighestPrice)
		valueArgs = append(valueArgs, stock.LowestPrice)
		valueArgs = append(valueArgs, stock.ClosePrice)
		valueArgs = append(valueArgs, stock.Volume)
		valueArgs = append(valueArgs, stock.TradingValue)
		valueArgs = append(valueArgs, stock.MarketCap)
		valueArgs = append(valueArgs, "STK")
	}

	stmt := fmt.Sprintf("INSERT INTO STOCK( TICKER, DATE, NAME, MARKET, CHANGE_CODE, CHANGES, CHANGES_RATIO, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, CLOSE_PRICE, VOLUME, AMOUNT, MARKET_CAP, MARKET_ID ) VALUES %s", strings.Join(valueStrings, ","))

	_, err = db.Exec(stmt, valueArgs...)

	if err != nil {
		fmt.Println(err)
		tx.Rollback()
		return
	}

	err = tx.Commit()
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("save")
}
