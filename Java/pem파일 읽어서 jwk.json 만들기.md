# pem파일 읽어서 jwk.json 만들기

openssl private키 생성 후 자바에서 pem파일을 읽어올 경우 pcks8인코딩이 아니여서 에러가 발생한다. 이럴 경우 pem파일을 pkcs8방식으로 인코딩해서 해당 경로에 넣어준다.


        openssl pkcs8 -in private.pem -inform pem -out pri8.pem -outform PEM -topk8 -nocrypt


code


        public class JWKEX {

            private final static String PATH = "src/main/resources/key/";
            private final static String PUBLIC_FILE_NAME = "public.pem";
            private final static String PRIVATE_FILE_NAME = "pri8.pem";



            private RSAPublicKey getRSAPulicKey() throws IOException, NoSuchAlgorithmException, InvalidKeySpecException {
                File file = getRSAFile(PUBLIC_FILE_NAME);
                String key = new String(Files.readAllBytes(file.toPath()), Charset.defaultCharset());

                String publicKeyPEM = getReplacedPublicKey(key);
                byte[] bytes = Base64.decodeBase64(publicKeyPEM);
                KeyFactory keyFactory = KeyFactory.getInstance("RSA");
                X509EncodedKeySpec keySpec = new X509EncodedKeySpec(bytes);
                return (RSAPublicKey) keyFactory.generatePublic(keySpec);
            }

            private RSAPrivateKey getRSAPrivateKey() throws IOException, NoSuchAlgorithmException, InvalidKeySpecException {
                File file = getRSAFile(PRIVATE_FILE_NAME);
                String key = new String(Files.readAllBytes(file.toPath()), Charset.defaultCharset());
                String privateKeyPEM = getReplacedPrivateKey(key);
                byte[] bytes = Base64.decodeBase64(privateKeyPEM);
                KeyFactory kf = KeyFactory.getInstance("RSA");
                PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(bytes);
                return (RSAPrivateKey) kf.generatePrivate(keySpec);
            }

            private File getRSAFile(String fileName){
                return new File(PATH,fileName);
            }

            private String getReplacedPublicKey(String key){
                return key.replace("-----BEGIN PUBLIC KEY-----", "")
                        .replaceAll(System.lineSeparator(), "")
                        .replace("-----END PUBLIC KEY-----", "");

            }
            private String getReplacedPrivateKey(String key){
                return key.replace("-----BEGIN PRIVATE KEY-----", "")
                        .replaceAll(System.lineSeparator(), "")
                        .replace("-----END PRIVATE KEY-----", "");

            }
            
            public String createJwt() throws IOException, NoSuchAlgorithmException, InvalidKeySpecException{
            
                RSAPublicKey pubKey = getRSAPulicKey();
                RSAPrivateKey privateKey = getRSAPrivateKey();

                Algorithm algorithm = Algorithm.RSA256(pubKey,privateKey);
                return JWT.create().withSubject("test").withClaim("name", "park").withIssuer("ISSUER").sign(algorithm);
            
            }
            
            public String getJwk() throws IOException, NoSuchAlgorithmException, InvalidKeySpecException {
                
        
                //String sign = JWT.create().sign(Algorithm.RSA256(rsaPublicKey));
        //        JWK jwk = new RSAKey.Builder(rsaPublicKey)
        //                .privateKey(privKey)
        //                .keyUse(KeyUse.SIGNATURE)
        //                .keyID(UUID.randomUUID().toString()).
        //                build();
        //        System.out.println(jwk);
        //        List<Object> test = new ArrayList<>();
        //        test.add(jwk.getRequiredParams());
                RSAPublicKey pubKey = getRSAPulicKey();

                JWKDto jwkDto = JWKDto.builder()
                        .e(java.util.Base64.getUrlEncoder().encodeToString(pubKey.getPublicExponent().toByteArray()))
                        .kty(pubKey.getAlgorithm())
                        .n(java.util.Base64.getUrlEncoder().encodeToString(pubKey.getModulus().toByteArray()))
                        .build();

             
                return JWKRetFormat.builder().jwkDto(jwkDto).build();;
            }
            
            @Getter
            public static class JWKRetFormat{
                private List<JWKDto> key = new ArrayList();
                @Builder
                public JWKRetFormat(JWKDto jwkDto){
                    this.key = Collections.singletonList(jwkDto);
                }
            }
            @Getter
            public static class JWKDto{
                private String e;
                private String kty;
                private String n;
                
                @Builder
                public JWKDto(String e, String kty, String n){
                    this.e = e;
                    this.kty = kty;
                    this.n  = n;
                }
            }
        }
