import java.io.*;
import java.math.BigInteger;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.crypto.NoSuchPaddingException;
import java.security.InvalidKeyException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.BadPaddingException;

public class AliceDecrypt {
    public static void main(String[] args) throws NoSuchAlgorithmException, IOException, NoSuchPaddingException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException {

        BigInteger oBIP = new BigInteger(args[1]);  // Número primo extremamente grande;
        BigInteger oBIsk = new BigInteger(args[2]);  // Chave privada;
        BigInteger oBIpkB = new BigInteger(args[3]); // Chave efémera;

        // Gerar a chave comum ao dois
        // K = Y ^ x mod P
        BigInteger OPBIK = oBIpkB.modPow(oBIsk, oBIP);

        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte keyHash[] = md.digest(OPBIK.toByteArray());
        byte bKey[] = new byte[16];
        byte bIV[] = new byte[16];
        for(int i = 0; i < 16; i++) {
            bKey[i] = keyHash[i];
            bIV[i] = keyHash[i+16];
        }

        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(bKey, "AES"), new IvParameterSpec(bIV));

        File inputFile = new File(args[0]);
        byte[] cipherText = new byte[(int) inputFile.length()];
        try(FileInputStream fis = new FileInputStream(inputFile)) {
            fis.read(cipherText);
        } catch (IOException e) {
            e.printStackTrace();
        }

        byte[] plainText = cipher.doFinal(cipherText);
        System.out.println(new String(plainText));
    }
}
