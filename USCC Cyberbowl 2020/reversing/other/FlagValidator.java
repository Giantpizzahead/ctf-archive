import java.util.Scanner;

public class FlagValidator {
    public static final String VALID_FLAG = new String(new byte[]{75, 86, 74, 85, 71, 81, 51, 51, 79, 52, 89, 72, 79, 88, 90, 82, 79, 82, 80, 88, 79, 78, 68, 84, 76, 53, 86, 72, 75, 52, 50, 85, 76, 53, 82, 68, 73, 52, 51, 70, 71, 77, 90, 72, 50, 61, 61, 61});
    private static final String alpha = new String(new byte[]{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 50, 51, 52, 53, 54, 55});

    public FlagValidator() {
    }

    public static String encode(byte[] inputFlag) {
        int var2 = 0;
        boolean var3 = false;

        StringBuffer encodedFlag = new StringBuffer((inputFlag.length + 7) * 8 / 5);
        int var7;
        for(int var1 = 0; var1 < inputFlag.length; encodedFlag.append(alpha.charAt(var7))) {
            int var4 = inputFlag[var1];
            if (var2 > 3) {
                int var5;
                if (var1 + 1 < inputFlag.length) {
                    var5 = inputFlag[var1 + 1];
                } else {
                    var5 = 0;
                }

                var7 = var4 & 255 >> var2;
                var2 = (var2 + 5) % 8;
                var7 <<= var2;
                var7 |= var5 >> 8 - var2;
                ++var1;
            } else {
                var7 = var4 >> 8 - (var2 + 5) & 31;
                var2 = (var2 + 5) % 8;
                if (var2 == 0) {
                    ++var1;
                }
            }
        }

        return encodedFlag.toString();
    }

    public static void main(String[] inputFlag) {
        // Each char is influenced by 2 chars
        String validFlag = "USCC";
        for (int i = 4; i < 30; i++) {
            // Brute force next 2 characters
            int bestJ = 0, bestK = 0, bestValid = 0;
            for (int j = 0; j < 128; j++) {
                for (int k = 0; k < 128; k++) {
                    System.out.println(j + ' ' + k);
                    String nextFlag = validFlag + (char) j + (char) k;
                    String encoded = encode(nextFlag.getBytes());
                    // Check length of valid
                    int lastValid = 0;
                    for (int l = 0; l < encoded.length(); l++) {
                        if (encoded.charAt(l) != VALID_FLAG.charAt(l)) {
                            lastValid = l - 1;
                            break;
                        }
                    }
                    if (lastValid > bestValid) {
                        bestJ = j;
                        bestK = k;
                        bestValid = lastValid;
                    }
                }
            }
            validFlag += (char) bestJ;
        }
        System.out.println(validFlag);
    }
}
