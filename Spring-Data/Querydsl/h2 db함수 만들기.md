## h2 db함수 만들기 

## H2CustomAlias.class

    package com.bs.krxstockservice.repository;

    public class H2CustomAlias {
        public static String YEARWEEK(String date){
            if (date.length() < 8) return "";
            DateTimeFormatter yyyyMMdd = DateTimeFormatter.ofPattern("yyyyMMdd");
            LocalDate locDate = LocalDate.parse(date, yyyyMMdd);
    
            TemporalField weekOfWeekBasedYear = WeekFields.of(Locale.KOREAN).weekOfWeekBasedYear();
            //get monday from arg
            LocalDate startOfWeek = locDate.with(DayOfWeek.MONDAY);
            //get week count
            int weekCount = startOfWeek.get(weekOfWeekBasedYear);
            // generate  'year of monday' + 'weekCount'
            return String.format("%02d", startOfWeek.getYear()).concat(String.valueOf(weekCount));
        }
    }


## 세팅

    package com.bs.krxstockservice.repository
    
    @BeforeEach
        fun setUp() {
            queryFactory = JPAQueryFactory(entityManager)
            entityManager!!
                .createNativeQuery("CREATE ALIAS IF NOT EXISTS YEARWEEK FOR \"com.bs.krxstockservice.repository.H2CustomAlias.YEARWEEK\"")
                .executeUpdate()

            
        }

## 사용법

    // -------------------------------------------------------------------------
    //  Expressions.stringTemplate("YEARWEEK({0})", QStock.stock.stockId.date)
    // -------------------------------------------------------------------------

    @Test
    fun yearWeekH2CustomFunctionTest(){
        //given
        val day = "20230101"
        val expect = "202253"
        //when
        val result = H2CustomAlias.YEARWEEK(day)
        //then
        assertEquals(expect,result)
    }

    @Test
    @Rollback
    fun getStockHLVOfWeekTest(){
        //given
        for (data:Stock in stocks){
            entityManager.persist(data)
        }
        //when
        var stockHLVOfWeeks = queryFactory
            .select(
                QStockHLV(
                    QStock.stock.stockId.ticker.`as`("ticker"),
                    QStock.stock.stockId.date.min().`as`("firstDayOfWeek"),
                    QStock.stock.highPrice.max().`as`("maxHighOfWeek"),
                    QStock.stock.lowPrice.min().`as`("minLowOfWeek"),
                    QStock.stock.volume.castToNum(Long::class.java).sum().stringValue().`as`("volume"),
                )
            )
            .from(QStock.stock)
            .where(QStock.stock.stockId.ticker.eq("000001"))
            .groupBy(
                QStock.stock.stockId.ticker,
                Expressions.stringTemplate("YEARWEEK({0})", QStock.stock.stockId.date)
            )
            .orderBy(OrderSpecifier(Order.DESC,QStock.stock.stockId.date.min()))
            .fetch()
        //then
        assertEquals(2, stockHLVOfWeeks.size)
    }

    
