import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<Integer>(10);

        StackFunc stackFunc = new StackFunc();

        stackFunc.isEmpty(list);

        stackFunc.push(list, 100);
        stackFunc.push(list, 200);
        stackFunc.push(list, 300);

        stackFunc.size(list);

        stackFunc.peek(list);

        stackFunc.pop(list);
        stackFunc.pop(list);
    }
}
