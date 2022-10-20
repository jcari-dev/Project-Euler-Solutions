
import java.util.ArrayList;
import java.util.List;

public class Solution {

    public static int multiplesOfFiveAndThree(int number) {
        List<Integer> listOfMultiples = new ArrayList<>();

        for (int x = 1; x < number; x++) {
            if (x % 3 == 0 || x % 5 == 0) {
                listOfMultiples.add(x);
            }
        }

        return listOfMultiples.stream()
                .reduce(0, (a, b) -> a + b);

    }

    public static void main(String[] args) {

        System.out.println(multiplesOfFiveAndThree(1000));
    }
}