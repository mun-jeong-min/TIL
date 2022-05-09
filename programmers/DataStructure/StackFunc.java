import java.util.List;

public class StackFunc {
    int top = -1;

    public void isEmpty(List<Integer> list) {
        if(list == null) {
            System.out.println("is Empty!");
        } else {
            System.out.println("is Not Empty!");
        }
    }

    public void push(List<Integer> list, int value) {
        top++;
        list.add(value);
    }

    public void pop(List<Integer> list) {
        Integer value = list.get(top);
        if(value != null) {
            System.out.println(value);
            list.remove(top);
            top--;
        } else {
            System.out.println("is Empty!!");
        }
    }

    public void size(List<Integer> list) {
        System.out.println(list.size());
    }

    public void peek(List<Integer> list) {
        int value = list.get(top);
        System.out.println(value);
    }
}
