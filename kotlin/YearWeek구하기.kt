internal class YearWeek구하기Test{

    @Test
    fun yearWeekTest(){
        val arg = "20230101"
        val dateFormatter = DateTimeFormatter.ofPattern("yyyyMMdd")
        val date = LocalDate.parse(arg, dateFormatter)

        val temporalField: TemporalField = WeekFields.of(Locale.KOREAN).weekOfWeekBasedYear()
        //get monday from arg
        val startOfWeek = date.with(DayOfWeek.MONDAY)
        //get week count
        val weekCount = startOfWeek.get(temporalField)
        // generate  'year of monday' + 'weekCount'
        val result = startOfWeek.year.toString().plus(weekCount.toString())
        Assertions.assertEquals("202253", result)
    }
}
