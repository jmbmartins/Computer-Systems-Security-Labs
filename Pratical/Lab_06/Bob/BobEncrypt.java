import java.io.*;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.NoSuchPaddingException;
import java.security.InvalidKeyException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.BadPaddingException;

public class BobEncrypt {
    public static void main(String[] args) throws NoSuchAlgorithmException, IOException, NoSuchPaddingException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException {

        BigInteger oBIP = new BigInteger(args[1]);  // Número primo extremamente grande;
        BigInteger oBIg = new BigInteger(args[2]);  // g, um gerador para o grupo;
        BigInteger oBIokA = new BigInteger(args[3]); // pk, a chave pública;

        BufferedReader br = new BufferedReader(new FileReader(args[0]));
        StringBuilder stringBuilder = new StringBuilder();
        char[] buffer = new char[10];
        while (br.read(buffer) != -1) {
            stringBuilder.append(new String(buffer));
            buffer = new char[10];
        }
        br.close();

        String data = stringBuilder.toString();
        byte[] plainText = data.getBytes();

        // Chave Privada Bob
        SecureRandom prng = SecureRandom.getInstance("SHA1PRNG");
        BigInteger oBIy = new BigInteger(prng.generateSeed(128));
        oBIy = oBIy.abs();

        // Chave Pública Bob
        BigInteger oBIpkB = oBIg.modPow(oBIy, oBIP);
        System.out.println("-- Bob pk --");
        System.ou.println(oBIpkB.toString());

        // Gerar a chave comum ao dois
        // K = Y ^ x mod P
        // K = X ^ y mod P
        BigInteger OPBIK = oBIokA.modPow(oBIy, oBIP);

        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte keyHash[] = md.digest(OPBIK.toByteArray());
        byte bKey[] = new byte[16];
        byte bIV[] = new byte[16];
        for(int i = 0; i < 16; i++) {
            bKey[i] = keyHash[i];
            bIV[i] = keyHash[i+16];
        }

        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, new SecretKeySpec(bKey, "AES"), new IvParameterSpec(bIV));
        byte[] cipherText = cipher.doFinal(plainText);              

        File outputFile = new File("cyphertext.egm");
        try(FileOutputStream fos = new FileOutputStream(outputFile)) {
            fos.write(cipherText);
        } catch (IOException e) {
            e.printStackTrace();                           

        }
    }
}
