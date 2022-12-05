# pem파일 읽어서 jwk.json 만들기

    public Map<String, Object> getJwk() throws IOException, NoSuchAlgorithmException, InvalidKeySpecException {
            String path = "src/main/resources/key/";
            String fileNm = "public.pem";
            File file = new File(path+fileNm);

            String key = new String(Files.readAllBytes(file.toPath()), Charset.defaultCharset());

            String publicKeyPEM = key
                    .replace("-----BEGIN PUBLIC KEY-----", "")
                    .replaceAll(System.lineSeparator(), "")
                    .replace("-----END PUBLIC KEY-----", "");

            System.out.println(publicKeyPEM);
           // byte[] encoded = Base64.getDecoder().decode(publicKeyPEM.getBytes());
            byte[] bytes = Base64.decodeBase64(publicKeyPEM);
            KeyFactory keyFactory = KeyFactory.getInstance("RSA");
            X509EncodedKeySpec keySpec = new X509EncodedKeySpec(bytes);
            RSAPublicKey rsaPublicKey = (RSAPublicKey) keyFactory.generatePublic(keySpec);

            System.out.println(rsaPublicKey.toString());
            Map<String, Object> values = new HashMap<>();
            values.put("kty", rsaPublicKey.getAlgorithm()); // getAlgorithm() returns kty not algorithm
            values.put("kid", "someuniqueid");
            values.put("n", java.util.Base64.getUrlEncoder().encodeToString(rsaPublicKey.getModulus().toByteArray()));
            values.put("e", java.util.Base64.getUrlEncoder().encodeToString(rsaPublicKey.getPublicExponent().toByteArray()));
            values.put("alg", "RS256");
            values.put("use", "sig");
            return values;
        }
