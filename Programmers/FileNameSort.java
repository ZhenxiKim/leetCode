import java.util.Arrays;
import java.util.Comparator;
import java.util.Locale;

/**
 * @author jhkim
 * @since 2022-06-05
 */
public class FileNameSort {
    public static void main(String[] args) {
        FileNameSort fileNameSort = new FileNameSort();
        FileNameSort.solution(new String[]{"img12.png", "img10.png", "img02.png", "img1.png", "IMG01000000.GIF", "img2.JPG"});
    }

    private static String[] solution(String[] files) {
        Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                String head1 = o1.split("[0-9]")[0].toLowerCase(Locale.ROOT);
                String head2 = o2.split("[0-9]")[0].toLowerCase(Locale.ROOT);

                int compareResult = head1.compareTo(head2);
                if(compareResult == 0) {
                    //같으면 0반환, 0보다 크면 head1>head2
                    //뒤에 숫자 비교
                    compareResult = convertNum(o1,head1) - convertNum(o2,head2);
                }
                return compareResult;
            }
        });
        return files;
    }

    //숫자인지 검사하여 숫자만 추출하는 메서드
    private static int convertNum(String fileName, String head) {
        //head의 길이만큼 잘라서 숫자부터 시작
        fileName = fileName.substring(head.length());
        String numResult = "";
        for(char c : fileName.toCharArray()) {
            if(Character.isDigit(c) && numResult.length() <= 5) {
                numResult += c;
            } else {
                //숫자가 아닌경우 검사할 필요 없음
              break;
            }
        }
        return Integer.parseInt(numResult);
    }
}
