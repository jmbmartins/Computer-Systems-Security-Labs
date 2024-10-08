import java.io.*;
import java.math.BigInteger;
import java.security.*;

public class AliceGen {
  static public void main(String[] args) throws NoSuchAlgorithmException {

      // Gera um número primo P (extremamente grande)
      BigInteger oBIP = new BigInteger("99494096650139337106186933977618513974146274831566768179581759037259788798151499814653951492724365471316253651463342255785311748602922458795201382445323499931625451272600173180136123245441204133515800495917242011863558721723303661523372572477211620144038809673692512025566673746993593384600667047373692203583");

      // Encontra um gerador do grupo g
      BigInteger oBIg = new BigInteger("44157404837960328768872680677686802650999163226766694797650810379076416463147265401084491113667624054557335394761604876882446924929840681990106974314935015501571333024773172440352475358750668213444607353872754650805031912866692119819377041901642732455911509867728218394542745330014071040326856846990119719675");

      // Chave Privada: Gera um número entre 0 < x < P - 1
      SecureRandom prng = SecureRandom.getInstance("SHA1PRNG");
      BigInteger oBIsk = new BigInteger(prng.generateSeed(128));
      oBIsk = oBIsk.abs();

      System.out.println("-- Private Key --");
      System.out.println(oBIsk.toString());

      // Chave Pública: X = g ^ x mod P
      BigInteger oBIpk = oBIg.modPow(oBIsk,oBIP);

      System.out.println("-- Public key --");      
      System.out.println("-- P --");      
      System.out.println(oBIP.toString());
      System.out.println("-- g --");      
      System.out.println(oBIg.toString());      
  }
}  
