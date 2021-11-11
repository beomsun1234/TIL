# Springboot - Kafka

Springboot에서 Kafka의 특정 Topic에 메시지를 생산(Produce)하고 해당 Topic을 Listen 한다.
Kafka 서버에 해당 메시지가 전달되고, Springboot에서 이를 소비(Consume)할 준비가 되면 메시지를 pull 한다.

카프카가 설치 되어있다고 가정한다(도커 설치)

springboot 프로젝트를 만들고 카프카연동을 위한 의존성을 추가해준다

	 implementation 'org.springframework.kafka:spring-kafka'
     

### Consumer에 대한 설정을 해준다

    @EnableKafka
    @Configuration
    public class KafkaConsumerConfig {
        @Bean
        public ConsumerFactory<String, String> consumerFactory() { //접속하고자 하는 정보 topic
            Map<String, Object> properties = new HashMap<>();
            properties.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9093");
            properties.put(ConsumerConfig.GROUP_ID_CONFIG, "test"); //컨슈머 그루핑되어있으면 지금은 1개임
            properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
            properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);

            return new DefaultKafkaConsumerFactory<>(properties);
        }

        @Bean //접속 정보를 가지고 리스너 생성
        public ConcurrentKafkaListenerContainerFactory<String, String> kafkaListenerContainerFactory() {
            ConcurrentKafkaListenerContainerFactory<String, String> kafkaListenerContainerFactory
                    = new ConcurrentKafkaListenerContainerFactory<>();
            kafkaListenerContainerFactory.setConsumerFactory(consumerFactory());

            return kafkaListenerContainerFactory;
        }
    }
    
    
### Produce에 대한 설정을 해준다


    @EnableKafka
    @Configuration
    public class KafkaProducerConfig {

        @Bean
        public ProducerFactory<String, String> producerFactory() { //접속하고자 하는 정보 topic
            Map<String, Object> properties = new HashMap<>();
            properties.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9093");
            properties.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
            properties.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);

            return new DefaultKafkaProducerFactory<>(properties);
        }

        @Bean
        public KafkaTemplate<String, String> kafkaTemplate(){
            return new KafkaTemplate<>(producerFactory());
        }
    }
    
### Produce 생성 (KafkaProducer.java)

    @Service
    @Slf4j
    @RequiredArgsConstructor
    public class KafkaProducer {
        private final KafkaTemplate<String, String> kafkaTemplate;
		
        //예제 
        public void sendTestMessage(String message) {
        
        	kafkaTemplate.send("test", message);
    		log.info("Kafka Producer Message : "+ message);
    	}
        
        //댓글 작성시 Board로 메시지를 보냄
        public String send(String topic, ReplyInfo replyInfo){
            ObjectMapper mapper = new ObjectMapper();
            try {
                String jsonInString = mapper.writeValueAsString(replyInfo);
                kafkaTemplate.send(topic, jsonInString);
                log.info("Kafka Producer sent data from the Board microservice: " + replyInfo);
                return "success";
            }
            catch (JsonProcessingException ex){
                log.info("에러발생={}",ex.getMessage());
                return "failure";
            }
        }
    }
    
### Consumer 생성 (KafkaConsumer.java)

    @Slf4j
    @Service
    public class KafkaConsumer {

        @KafkaListener(topics = "test")
        public void consume(String message) throws IOException {
             log.info("Kafka Consumer: " + message);
        }
    }
    
    
### Controller

    @RestController
    @RequiredArgsConstructor
    @RequestMapping(value = "/kafka")
    public class KafkaController {
        private final KafkaProducer producer;

        @PostMapping
        public String sendMessage(@RequestParam("message") String message) {
            producer.sendMessage(message);
            return "success";
        }
    }
    
 POST  - localhost:8080/kafka?message="hello park"
 
	response ->  success
    
로그를 확인해 보면 

Kafka Producer Message : hello park

Kafka Consumer : hello park
