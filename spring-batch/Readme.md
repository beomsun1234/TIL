#spring batch

## 다중 db 연결 시 JobRepository 생성 필요

    @Bean(name = "jobRepo")
    public JobRepository jobRepository(@Qualifier("jobDb")DataSource dataSource,
                                       @Qualifier("jobTr")PlatformTransactionManager platformTransactionManager){
        JobRepositoryFactoryBean bean = new JobRepositoryFactoryBean();
        JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);
    
        bean.setDataSource(dataSource);
        bean.setJdbcOperations(jdbcTemplate);
        bean.setTransactionManager(platformTransactionManager);
        bean.setDatabaseType(DatabaseType.yourDb.name());
        
        return bean.getObject();
    }
                                
