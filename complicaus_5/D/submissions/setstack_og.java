import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class setstack_og {

	Stack<Set<Integer>> stack = new Stack<Set<Integer>>();
	Map<Set<Integer>,Integer> idmap = new HashMap<Set<Integer>,Integer>();

	void execute(String cmd) {
		if (cmd.equals("DUP")) {
			stack.push(stack.peek());
		} else if (cmd.equals("PUSH")) {
			stack.push(new HashSet<Integer>());
		} else {
			Set<Integer> A = stack.pop();
			Set<Integer> B = stack.pop();
			stack.push(calculate(cmd, A, B));
		}
	}

	Set<Integer> calculate(String cmd, Set<Integer> A, Set<Integer> B) {
		Set<Integer> set = new HashSet<Integer>();
		if (cmd.equals("ADD")) {
			set.add(getId(A));
			set.addAll(B);
		} else if (cmd.equals("UNION")) {
			set.addAll(A);
			set.addAll(B);
		} else {
			assert cmd.equals("INTERSECT");
			set.addAll(A);
			set.retainAll(B);
		}
		return set;
	}

	Integer getId(Set<Integer> set) {
		Integer stored = idmap.get(set);
		if (stored == null) {
			stored = idmap.size();
			idmap.put(set,stored);
		}
		return stored;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());
		for (int t=0; t<T; ++t) {
			setstack_og ss = new setstack_og();
			int N = Integer.parseInt(in.readLine());
			for (int i=0; i<N; ++i) {
				String cmd = in.readLine();
				ss.execute(cmd);
				System.out.println(ss.stack.peek().size());
			}
			System.out.println("***");
		}
	}

}
